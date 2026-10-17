"""Portfolio dashboard and session-based QA test console for the fictitious claim journey."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import pandas as pd
import plotly.express as px
import streamlit as st


ROOT = Path(__file__).resolve().parents[1]
ref = json.loads((ROOT / "data/referentiel.json").read_text(encoding="utf-8"))
pilot = json.loads((ROOT / "data/pilotage.json").read_text(encoding="utf-8"))
backlog = pd.read_csv(ROOT / "docs/pilotage/backlog.csv")
risk = pd.read_csv(ROOT / "docs/pilotage/registre-risques.csv")
stories = backlog[backlog["type"] == "Story"].copy()

st.set_page_config(page_title="DéclaSinistre · Pilotage & QA", page_icon="◈", layout="wide")
st.markdown(
    """
    <style>
    :root { --ink:#193342; --navy:#102c3b; --teal:#087e78; --muted:#687c82; --line:#e3ebe8; }
    .stApp { background:linear-gradient(180deg,#f2f6f5 0,#f7f9f8 340px,#f7f9f8 100%); color:var(--ink); font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; }
    .block-container { max-width:1320px; padding-top:2.3rem; padding-bottom:3.5rem; }
    h1,h2,h3 { font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif!important; letter-spacing:-.5px; color:var(--navy)!important; }
    h1 { font-size:2.1rem!important; font-weight:700!important; margin:.25rem 0 .3rem!important; }
    h2 { font-size:1.22rem!important; font-weight:700!important; margin-top:1.2rem!important; }
    h3 { font-size:1rem!important; font-weight:700!important; }
    .dash-topline { display:flex; align-items:center; justify-content:space-between; gap:16px; margin-bottom:18px; }
    .dash-brand { display:flex; align-items:center; gap:10px; color:#60767c; font-size:13px; font-weight:700; letter-spacing:.02em; }
    .dash-mark { width:31px; height:31px; display:grid; place-items:center; border-radius:10px; background:#102c3b; color:#a9dfd3; font-weight:800; font-size:16px; }
    .demo-pill { border:1px solid #e5d9b8; border-radius:99px; background:#fbf6e9; color:#85662a; font-size:11px; font-weight:700; padding:6px 11px; letter-spacing:.03em; }
    .hero-copy { color:#6a7c80; font-size:14px; margin:0 0 1.35rem; }
    [data-testid="stMetric"] { background:#fff; border:1px solid var(--line); border-radius:13px; padding:17px 18px; box-shadow:0 5px 20px rgba(20,51,61,.035); min-height:105px; }
    [data-testid="stMetricLabel"] p { color:#73858a!important; font-size:12px!important; font-weight:600!important; }
    [data-testid="stMetricValue"] { color:var(--navy)!important; font-size:1.55rem!important; font-weight:700!important; }
    [data-testid="stMetricDelta"] { display:none; }
    div[data-testid="stVerticalBlockBorderWrapper"] { background:#fff; border:1px solid var(--line); border-radius:14px; padding:17px 19px; }
    .section-kicker { color:#72868a; font-size:10px; font-weight:700; letter-spacing:1px; text-transform:uppercase; margin:0 0 5px; }
    .note-box { border:1px solid #dceae5; border-left:3px solid #268b7e; border-radius:8px; background:#f0f7f4; color:#58716e; padding:11px 14px; font-size:12px; line-height:1.55; margin:10px 0; }
    .trace-chip { display:inline-block; border:1px solid #d9e8e3; border-radius:99px; background:#f1f8f5; color:#176b62; padding:4px 9px; margin:3px 4px 3px 0; font-size:11px; font-weight:700; }
    .stDataFrame { border:1px solid var(--line); border-radius:11px; overflow:hidden; }
    div[data-testid="stAlert"] { border-radius:11px; }
    @media (max-width:700px) { .block-container { padding:1.3rem 1rem 2rem; } h1 { font-size:1.65rem!important; } .dash-topline { align-items:flex-start; } }
    </style>
    <div class="dash-topline"><div class="dash-brand"><span class="dash-mark">D</span> DÉCLASINISTRE <span style="color:#a9b7b7;font-weight:500">/ PILOTAGE & QA</span></div><span class="demo-pill">CAS FICTIF · DONNÉES SIMULÉES</span></div>
    <p class="section-kicker">Pilotage produit</p>
    <h1>Suivre le parcours de déclaration</h1>
    <p class="hero-copy">Avancement, risques, exécution des tests et couverture des huit user stories.</p>
    """,
    unsafe_allow_html=True,
)


def load_story_test_links() -> dict[str, list[str]]:
    """Read the explicit TC links in each US, then include journey-wide checks."""
    doc = (ROOT / "docs/ba/user-stories.md").read_text(encoding="utf-8")
    links = {story["id"]: [] for story in ref["stories"]}
    blocks = re.split(r"(?=^## US-\d{3})", doc, flags=re.MULTILINE)
    for block in blocks:
        match_story = re.match(r"## (US-\d{3})", block)
        match_tests = re.search(r"\*\*Tests :\*\*\s*([^\n.]+)", block)
        if not (match_story and match_tests):
            continue
        story_id = match_story.group(1)
        links[story_id] = re.findall(r"TC-\d{3}", match_tests.group(1))
    # These non-functional checks apply to the full declaration journey.
    all_stories = list(links)
    for test_id in ("TC-014", "TC-015"):
        for story_id in all_stories:
            links[story_id].append(test_id)
    return links


STORY_TESTS = load_story_test_links()
TESTS_BY_ID = {test["id"]: test for test in ref["tests"]}
STORIES_BY_ID = {story["id"]: story for story in ref["stories"]}
REQUIREMENTS_BY_ID = {item["id"]: item for item in ref["requirements"]}
RULES_BY_ID = {item["id"]: item for item in ref["rules"]}
FEATURE_FILES = {story_id: ROOT / "tests/features" / f"{story_id.lower()}.feature" for story_id in STORIES_BY_ID}
TEST_STORIES = {test_id: [story_id for story_id, ids in STORY_TESTS.items() if test_id in ids] for test_id in TESTS_BY_ID}
E2E_FILE = ROOT / "tests/e2e/prototype.spec.js"
E2E_SOURCE = E2E_FILE.read_text(encoding="utf-8") if E2E_FILE.exists() else ""
E2E_TEST_IDS = set(re.findall(r"TC-\d{3}", E2E_SOURCE))
E2E_TEST_COUNT = len(re.findall(r"^test\(", E2E_SOURCE, flags=re.MULTILINE))


@st.cache_data(ttl=120, show_spinner=False)
def latest_github_ci_run() -> dict | None:
    """Read the public status of the latest main-branch test workflow."""
    request = Request(
        "https://api.github.com/repos/didouBK/decla-sinistre/actions/runs?per_page=10",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "decla-sinistre-qa-dashboard"},
    )
    try:
        with urlopen(request, timeout=8) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError, TimeoutError, OSError, ValueError):
        return None
    runs = [
        run for run in payload.get("workflow_runs", [])
        if run.get("name") == "quality" and run.get("head_branch") == "main"
    ]
    if not runs:
        return None
    run = max(runs, key=lambda item: item.get("created_at", ""))
    return {
        "status": run.get("status", "unknown"),
        "conclusion": run.get("conclusion"),
        "created_at": run.get("created_at", ""),
        "url": run.get("html_url", "https://github.com/didouBK/decla-sinistre/actions"),
    }

if "qa_results" not in st.session_state:
    st.session_state.qa_results = {}
if "qa_auto_runs" not in st.session_state:
    st.session_state.qa_auto_runs = []
if "qa_history" not in st.session_state:
    st.session_state.qa_history = []

overview_tab, qa_tab = st.tabs(["Pilotage", "QA · Tests et couverture"])

with overview_tab:
    done = int(stories["statut"].str.startswith("Terminé").sum())
    total = len(stories)
    completion = done / total if total else 0
    testable = [item for item in ref["requirements"] if item["testable"]]
    covered = sum(any(item["id"] in test["links"].split(";") for test in ref["tests"]) for item in testable)

    metric_columns = st.columns(4)
    metric_columns[0].metric("Stories terminées", f"{done} / {total}", help="Stories terminées dans le backlog fictif.")
    metric_columns[1].metric("Avancement simulé", f"{completion:.0%}", help="Part des stories marquées terminées.")
    metric_columns[2].metric("Exigences liées", f"{covered} / {len(testable)}", help="Exigences testables ayant un lien vers au moins un cas de test.")
    metric_columns[3].metric("Exécution produit", "Non mesurée", help="Aucun résultat de test navigateur n’est enregistré.")

    st.markdown('<p class="section-kicker" style="margin-top:25px">Progression et capacité</p>', unsafe_allow_html=True)
    left, right = st.columns([1.05, 0.95], gap="large")
    with left:
        st.subheader("Backlog par priorité")
        priority_order = ["Must", "Should", "Could", "Won't", "Must have", "Should have", "Could have", "Won't have"]
        backlog_chart = px.histogram(
            stories, x="priorite", color="statut", barmode="group",
            category_orders={"priorite": priority_order},
            color_discrete_sequence=["#0b7f78", "#d9a64e", "#9baeb0", "#d97e68"],
            labels={"priorite": "Priorité", "statut": "Statut", "count": "Stories"},
        )
        backlog_chart.update_layout(
            template="plotly_white", height=320, margin=dict(l=8, r=10, t=20, b=8),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Arial, sans-serif", color="#61747b", size=11),
            legend=dict(orientation="h", y=-.22, x=0), bargap=.28,
        )
        backlog_chart.update_xaxes(title=None, showgrid=False, linecolor="#e5ece9")
        backlog_chart.update_yaxes(title=None, gridcolor="#edf1ef", zeroline=False)
        st.plotly_chart(backlog_chart, use_container_width=True, config={"displayModeBar": False})
    with right:
        st.subheader("Sprints simulés")
        sprints = pd.DataFrame([
            {"Sprint": sprint["name"], "Points terminés": sprint["done"], "Capacité théorique": sprint["start_capacity"]}
            for sprint in pilot["sprints"]
        ])
        velocity_chart = px.bar(
            sprints, x="Sprint", y="Points terminés", text="Points terminés",
            color_discrete_sequence=["#238b80"], labels={"Sprint": "", "Points terminés": "Story points"},
        )
        velocity_chart.update_traces(textposition="outside", marker_cornerradius=5, cliponaxis=False)
        velocity_chart.update_layout(
            template="plotly_white", height=320, margin=dict(l=8, r=10, t=20, b=8),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Arial, sans-serif", color="#61747b", size=11), showlegend=False,
        )
        velocity_chart.update_xaxes(title=None, showgrid=False, linecolor="#e5ece9")
        velocity_chart.update_yaxes(title=None, gridcolor="#edf1ef", zeroline=False, rangemode="tozero")
        st.plotly_chart(velocity_chart, use_container_width=True, config={"displayModeBar": False})
        st.caption("Story points relatifs, définis pour le scénario. Ils ne mesurent pas une performance individuelle.")

    st.subheader("Burndown illustratif")
    burndown_rows = [
        {"Sprint": sprint["name"], "Jour": day, "Points restants": remaining}
        for sprint in pilot["sprints"] for day, remaining in enumerate(sprint["remaining_daily"])
    ]
    burndown = px.line(
        pd.DataFrame(burndown_rows), x="Jour", y="Points restants", color="Sprint", markers=True,
        color_discrete_sequence=["#087e78", "#d5a04c", "#6b8491"],
        labels={"Jour": "Jour du sprint", "Points restants": "Story points restants"},
    )
    burndown.update_layout(
        template="plotly_white", height=300, margin=dict(l=8, r=10, t=15, b=8),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Arial, sans-serif", color="#61747b", size=11),
        legend=dict(orientation="h", y=1.12, x=0),
    )
    burndown.update_xaxes(title=None, showgrid=False, linecolor="#e5ece9")
    burndown.update_yaxes(title=None, gridcolor="#edf1ef", zeroline=False)
    st.plotly_chart(burndown, use_container_width=True, config={"displayModeBar": False})
    st.caption("Source : data/pilotage.json. Les valeurs de vélocité et de burndown sont des simulations.")

    st.markdown('<p class="section-kicker" style="margin-top:28px">Maîtrise et couverture documentaire</p>', unsafe_allow_html=True)
    risks_column, coverage_column = st.columns([1.15, 0.85], gap="large")
    with risks_column:
        st.subheader("Registre des risques")
        risk["Criticité P × I"] = risk["probabilite_1_5"] * risk["impact_1_5"]
        risk_view = risk.rename(columns={
            "description": "Risque", "probabilite_1_5": "Probabilité / 5", "impact_1_5": "Impact / 5",
            "responsable": "Responsable", "statut": "Statut",
        })[["Risque", "Probabilité / 5", "Impact / 5", "Criticité P × I", "Responsable", "Statut"]]
        st.dataframe(risk_view, use_container_width=True, hide_index=True)
    with coverage_column:
        st.subheader("Traçabilité des exigences")
        st.metric("Exigences testables liées à un cas", f"{covered} / {len(testable)}")
        st.progress(covered / len(testable) if testable else 0, text=f"Couverture documentaire : {covered / len(testable):.0%}" if testable else "Aucune exigence testable")
        st.markdown('<div class="note-box">Un lien documentaire vers un cas de test ne prouve pas que ce cas a été exécuté.</div>', unsafe_allow_html=True)

    st.subheader("Indicateurs métier : cibles à étudier")
    indicators = pd.DataFrame([
        {"Indicateur": "Dossiers incomplets", "Hypothèse initiale": "30 %", "Cible indicative": "≤ 10 %", "Mesure": "Non mesurée"},
        {"Indicateur": "Prise en charge initiale", "Hypothèse initiale": "5 jours", "Cible indicative": "≤ 1 jour ouvré", "Mesure": "Non mesurée"},
        {"Indicateur": "Durée de déclaration", "Hypothèse initiale": "À mesurer", "Cible indicative": "< 5 min", "Mesure": "Non mesurée"},
    ])
    st.dataframe(indicators, use_container_width=True, hide_index=True)
    st.markdown('<div class="note-box"><strong>Important :</strong> toutes les données et cibles sont fictives. Aucun assureur n’est connecté et aucune donnée réelle n’est collectée.</div>', unsafe_allow_html=True)


with qa_tab:
    st.markdown('<p class="section-kicker">Assurance qualité · référentiel de test</p>', unsafe_allow_html=True)
    st.subheader("Exécuter les contrôles automatiques")
    st.markdown(
        "Les contrôles automatiques vérifient la structure du référentiel et les exports du dépôt. "
        "Les tests navigateur Playwright sont lancés par la CI GitHub Actions; "
        "les scénarios métier non automatisés et la mesure de durée restent à jouer manuellement dans le prototype. "
        "[Voir le workflow de tests](https://github.com/didouBK/decla-sinistre/actions/workflows/ci.yml)."
    )
    ci_run = latest_github_ci_run()
    with st.container(border=True):
        ci_columns = st.columns([1, 2])
        ci_time = ci_run.get("created_at", "") if ci_run else ""
        if ci_run and ci_time:
            ci_time = datetime.fromisoformat(ci_time.replace("Z", "+00:00")).strftime("%d/%m/%Y à %H:%M UTC")
        if ci_run and ci_run["status"] == "completed" and ci_run["conclusion"] == "success":
            ci_columns[0].metric("Dernière CI · Playwright", "Réussie")
            ci_columns[1].markdown(f"**{E2E_TEST_COUNT} tests Playwright réussis** · {ci_time}  \n[Consulter le rapport et ses captures]({ci_run['url']})")
        elif ci_run and ci_run["status"] == "completed":
            ci_columns[0].metric("Dernière CI · Playwright", "Échec")
            ci_columns[1].markdown(f"Exécution terminée · {ci_time}  \n[Consulter le rapport et les traces]({ci_run['url']})")
        elif ci_run:
            ci_columns[0].metric("Dernière CI · Playwright", "En cours")
            ci_columns[1].markdown(f"Exécution lancée · {ci_time}  \n[Suivre le workflow]({ci_run['url']})")
        else:
            ci_columns[0].metric("Dernière CI · Playwright", "Indisponible")
            ci_columns[1].markdown("Le statut GitHub n’a pas pu être chargé. [Ouvrir les workflows](https://github.com/didouBK/decla-sinistre/actions).")
    if st.button("Lancer les contrôles qualité", type="primary", key="run_quality"):
        commands = {
            "validate_project.py": [sys.executable, "scripts/validate_project.py"],
            "pytest": [sys.executable, "-m", "pytest", "-q"],
        }
        run_record = {"started_at": datetime.now(timezone.utc).isoformat(), "checks": {}}
        with st.spinner("Exécution des contrôles du dépôt…"):
            for name, command in commands.items():
                try:
                    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=90, check=False)
                    run_record["checks"][name] = {
                        "passed": result.returncode == 0,
                        "returncode": result.returncode,
                        "output": (result.stdout + result.stderr).strip(),
                    }
                except subprocess.TimeoutExpired as exc:
                    partial = (exc.stdout or "") + (exc.stderr or "")
                    run_record["checks"][name] = {"passed": False, "returncode": None, "output": f"Délai dépassé.\n{partial}"}
                except Exception as exc:  # display environment failures in the QA console
                    run_record["checks"][name] = {"passed": False, "returncode": None, "output": f"Impossible de lancer le contrôle : {exc}"}
        st.session_state.qa_auto_runs.insert(0, run_record)

    if st.session_state.qa_auto_runs:
        latest_run = st.session_state.qa_auto_runs[0]
        run_time = latest_run["started_at"].replace("T", " ").split(".")[0] + " UTC"
        st.caption(f"Dernière exécution automatique : {run_time}")
        cols = st.columns(len(latest_run["checks"]))
        for column, (name, result) in zip(cols, latest_run["checks"].items()):
            column.metric(name, "Réussi" if result["passed"] else "Échec")
            with st.expander(f"Détails · {name}"):
                st.code(result["output"] or "Aucune sortie.", language="text")
    else:
        st.info("Aucun contrôle automatique lancé dans cette session.")

    st.divider()
    st.subheader("Couverture liée aux user stories")
    st.caption("Les cas E2E sont déduits des identifiants TC présents dans tests/e2e/prototype.spec.js. La couverture de conception vient des liens déclarés dans docs/ba/user-stories.md. TC-014 et TC-015 sont transverses à tout le parcours; TC-015 reste une mesure manuelle.")

    all_results = st.session_state.qa_results
    executed_statuses = {"Réussi", "Échec"}
    story_rows = []
    for story_id, story in STORIES_BY_ID.items():
        test_ids = STORY_TESTS.get(story_id, [])
        e2e_count = sum(test_id in E2E_TEST_IDS for test_id in test_ids)
        statuses = [all_results.get(test_id, {}).get("status", "À exécuter") for test_id in test_ids]
        executed = sum(status in executed_statuses for status in statuses)
        passed = sum(status == "Réussi" for status in statuses)
        failed = sum(status == "Échec" for status in statuses)
        blocked = sum(status == "Bloqué" for status in statuses)
        coverage = executed / len(test_ids) if test_ids else 0
        if failed:
            overall = "À corriger"
        elif test_ids and passed == len(test_ids):
            overall = "Validée"
        elif executed or blocked:
            overall = "En cours"
        else:
            overall = "À exécuter"
        story_rows.append({
            "US": story_id, "User story": story["title"], "TC liés": len(test_ids),
            "Cas E2E": f"{e2e_count} / {len(test_ids)}",
            "Exécutés": executed, "Réussis": passed, "Échecs": failed,
            "Bloqués": blocked, "Couverture d’exécution": f"{coverage:.0%}", "État": overall,
        })

    design_covered = sum(bool(STORY_TESTS.get(story_id)) for story_id in STORIES_BY_ID)
    executed_stories = sum(row["Exécutés"] > 0 for row in story_rows)
    failed_count = sum(result.get("status") == "Échec" for result in all_results.values())
    passed_count = sum(result.get("status") == "Réussi" for result in all_results.values())
    blocked_count = sum(result.get("status") == "Bloqué" for result in all_results.values())
    cases_total = len(TESTS_BY_ID)
    e2e_covered = len(E2E_TEST_IDS.intersection(TESTS_BY_ID))
    qa_metrics = st.columns(5)
    qa_metrics[0].metric("US couvertes par conception", f"{design_covered} / {len(STORIES_BY_ID)}")
    qa_metrics[1].metric("TC avec scénario E2E", f"{e2e_covered} / {cases_total}")
    qa_metrics[2].metric("US avec exécution manuelle", f"{executed_stories} / {len(STORIES_BY_ID)}")
    qa_metrics[3].metric("Cas réussis manuellement", f"{passed_count} / {cases_total}")
    qa_metrics[4].metric("Échecs / bloqués", f"{failed_count} / {blocked_count}")
    st.dataframe(pd.DataFrame(story_rows), use_container_width=True, hide_index=True)

    st.subheader("Exécuter un scénario métier")
    st.markdown("Choisissez un cas, suivez ses critères et consignez le résultat après l’avoir joué dans le prototype publié.")
    test_ids = list(TESTS_BY_ID)
    selected_id = st.selectbox(
        "Cas de test",
        test_ids,
        format_func=lambda test_id: f"{test_id} · {TESTS_BY_ID[test_id]['title']}",
    )
    selected_test = TESTS_BY_ID[selected_id]
    linked_stories = TEST_STORIES.get(selected_id, [])
    links = selected_test["links"].split(";")
    linked_requirements = [REQUIREMENTS_BY_ID[link] for link in links if link in REQUIREMENTS_BY_ID]
    linked_rules = [RULES_BY_ID[link] for link in links if link in RULES_BY_ID]
    linked_story_names = [f"{story_id} · {STORIES_BY_ID[story_id]['title']}" for story_id in linked_stories]
    st.markdown("**User stories liées**<br>" + " ".join(f'<span class="trace-chip">{story}</span>' for story in linked_story_names), unsafe_allow_html=True)
    st.markdown("**Exigences liées :** " + (" · ".join(f"{item['id']} — {item['title']}" for item in linked_requirements) or "aucune"))
    if linked_rules:
        with st.expander("Règles métier et résultat attendu"):
            for rule in linked_rules:
                st.markdown(f"**{rule['id']} · {rule['title']}** — {rule['description']}")
    if selected_id in {"TC-014", "TC-015"}:
        st.info("Cas transverse : à vérifier sur le parcours complet, pour les huit US.")
    feature_names = [FEATURE_FILES[story_id].name for story_id in linked_stories if story_id in FEATURE_FILES and FEATURE_FILES[story_id].exists()]
    if feature_names:
        st.caption("Spécifications Gherkin associées : " + ", ".join(feature_names))

    previous_record = all_results.get(selected_id, {})
    status_options = ["À exécuter", "Réussi", "Échec", "Bloqué"]
    previous_status = previous_record.get("status", "À exécuter")
    with st.form("manual_test_result", clear_on_submit=False):
        result_status = st.selectbox("Résultat du scénario", status_options, index=status_options.index(previous_status))
        executor = st.text_input("Exécuté par (facultatif)", value=previous_record.get("executor", ""), placeholder="Nom ou rôle")
        evidence = st.text_area("Observation / preuve", value=previous_record.get("evidence", ""), placeholder="Résultat observé, référence de capture ou anomalie…")
        save_result = st.form_submit_button("Enregistrer le résultat")
    if save_result:
        record = {
            "status": result_status,
            "executor": executor.strip(),
            "evidence": evidence.strip(),
            "executed_at": datetime.now(timezone.utc).isoformat() if result_status != "À exécuter" else "",
        }
        st.session_state.qa_results[selected_id] = record
        if result_status != "À exécuter":
            st.session_state.qa_history.insert(0, {"test_id": selected_id, **record})
            st.session_state.qa_saved_message = f"Résultat de {selected_id} enregistré dans cette session."
        st.rerun()
    if st.session_state.get("qa_saved_message"):
        st.success(st.session_state.pop("qa_saved_message"))

    st.subheader("Journal des exécutions manuelles")
    history_rows = []
    for record in st.session_state.qa_history:
        test_id = record["test_id"]
        test = TESTS_BY_ID[test_id]
        history_rows.append({
            "Date UTC": record.get("executed_at", ""),
            "TC": test_id,
            "Scénario": test["title"],
            "US liées": ", ".join(TEST_STORIES.get(test_id, [])),
            "Résultat": record.get("status", ""),
            "Exécuté par": record.get("executor", ""),
            "Observation / preuve": record.get("evidence", ""),
        })
    if history_rows:
        history = pd.DataFrame(history_rows)
        st.dataframe(history, use_container_width=True, hide_index=True)
        csv_data = history.to_csv(index=False).encode("utf-8-sig")
        st.download_button("Exporter l’historique QA en CSV", csv_data, "decla-sinistre-journal-qa.csv", "text/csv")
    else:
        st.info("Aucun résultat manuel enregistré. Les résultats restent dans cette session Streamlit; exportez l’historique pour l’archiver.")

    plan_rows = [
        {
            "TC": test_id,
            "Scénario": test["title"],
            "US liées": ", ".join(TEST_STORIES.get(test_id, [])),
            "Liens exigences et règles": test["links"],
            "Résultat courant": all_results.get(test_id, {}).get("status", "À exécuter"),
        }
        for test_id, test in TESTS_BY_ID.items()
    ]
    plan_csv = pd.DataFrame(plan_rows).to_csv(index=False).encode("utf-8-sig")
    st.download_button("Exporter le plan de test et sa couverture CSV", plan_csv, "decla-sinistre-plan-de-test.csv", "text/csv")

    st.markdown('<div class="note-box"><strong>Portée :</strong> les résultats saisis et les contrôles lancés depuis ce tableau sont propres à cette session Streamlit. Aucun stockage durable ni synchronisation entre utilisateurs n’est configuré. La couverture affichée porte sur les scénarios par US; la couverture des lignes de code n’est pas mesurée. Les rapports Playwright sont archivés dans les artefacts GitHub Actions.</div>', unsafe_allow_html=True)
