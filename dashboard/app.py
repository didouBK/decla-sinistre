"""Dashboard de pilotage fictif construit à partir des référentiels versionnés."""

import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


ROOT = Path(__file__).resolve().parents[1]
ref = json.loads((ROOT / "data/referentiel.json").read_text(encoding="utf-8"))
pilot = json.loads((ROOT / "data/pilotage.json").read_text(encoding="utf-8"))
backlog = pd.read_csv(ROOT / "docs/pilotage/backlog.csv")
risk = pd.read_csv(ROOT / "docs/pilotage/registre-risques.csv")
stories = backlog[backlog["type"] == "Story"].copy()

st.set_page_config(page_title="DéclaSinistre · Pilotage", page_icon="◈", layout="wide")
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');
    :root { --ink:#193342; --navy:#102c3b; --teal:#087e78; --muted:#687c82; --line:#e3ebe8; }
    .stApp { background:linear-gradient(180deg,#f2f6f5 0,#f7f9f8 340px,#f7f9f8 100%); color:var(--ink); font-family:'DM Sans',sans-serif; }
    .block-container { max-width:1320px; padding-top:2.3rem; padding-bottom:3.5rem; }
    h1,h2,h3 { font-family:'Manrope',sans-serif!important; letter-spacing:-.5px; color:var(--navy)!important; }
    h1 { font-size:2.1rem!important; font-weight:700!important; margin:.25rem 0 .3rem!important; }
    h2 { font-size:1.22rem!important; font-weight:700!important; margin-top:1.2rem!important; }
    h3 { font-size:1rem!important; font-weight:700!important; }
    .dash-topline { display:flex; align-items:center; justify-content:space-between; gap:16px; margin-bottom:18px; }
    .dash-brand { display:flex; align-items:center; gap:10px; color:#60767c; font-size:13px; font-weight:700; letter-spacing:.02em; }
    .dash-mark { width:31px; height:31px; display:grid; place-items:center; border-radius:10px; background:#102c3b; color:#a9dfd3; font:800 16px 'Manrope',sans-serif; }
    .demo-pill { border:1px solid #e5d9b8; border-radius:99px; background:#fbf6e9; color:#85662a; font-size:11px; font-weight:700; padding:6px 11px; letter-spacing:.03em; }
    .hero-copy { color:#6a7c80; font-size:14px; margin:0 0 1.35rem; }
    [data-testid="stMetric"] { background:#fff; border:1px solid var(--line); border-radius:13px; padding:17px 18px; box-shadow:0 5px 20px rgba(20,51,61,.035); min-height:112px; }
    [data-testid="stMetricLabel"] p { color:#73858a!important; font-size:12px!important; font-weight:600!important; }
    [data-testid="stMetricValue"] { color:var(--navy)!important; font-family:'Manrope',sans-serif; font-size:1.65rem!important; font-weight:700!important; }
    [data-testid="stMetricDelta"] { display:none; }
    div[data-testid="stVerticalBlockBorderWrapper"] { background:#fff; border:1px solid var(--line); border-radius:14px; padding:17px 19px; }
    .section-kicker { color:#72868a; font-size:10px; font-weight:700; letter-spacing:1px; text-transform:uppercase; margin:0 0 5px; }
    .note-box { border:1px solid #dceae5; border-left:3px solid #268b7e; border-radius:8px; background:#f0f7f4; color:#58716e; padding:11px 14px; font-size:12px; line-height:1.55; margin-top:12px; }
    .stDataFrame { border:1px solid var(--line); border-radius:11px; overflow:hidden; }
    div[data-testid="stAlert"] { border-radius:11px; }
    @media (max-width:700px) { .block-container { padding:1.3rem 1rem 2rem; } h1 { font-size:1.65rem!important; } .dash-topline { align-items:flex-start; } }
    </style>
    <div class="dash-topline"><div class="dash-brand"><span class="dash-mark">D</span> DÉCLASINISTRE <span style="color:#a9b7b7;font-weight:500">/ PILOTAGE</span></div><span class="demo-pill">CAS FICTIF · DONNÉES SIMULÉES</span></div>
    <p class="section-kicker">Pilotage produit</p>
    <h1>Vue d’ensemble</h1>
    <p class="hero-copy">Repères de suivi du parcours de déclaration — les chiffres ci-dessous illustrent un scénario, ils ne décrivent pas une activité réelle.</p>
    """,
    unsafe_allow_html=True,
)

done = int(stories["statut"].str.startswith("Terminé").sum())
total = len(stories)
completion = done / total if total else 0
testable = [item for item in ref["requirements"] if item["testable"]]
covered = sum(any(item["id"] in test["links"] for test in ref["tests"]) for item in testable)

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
        stories,
        x="priorite",
        color="statut",
        barmode="group",
        category_orders={"priorite": priority_order},
        color_discrete_sequence=["#0b7f78", "#d9a64e", "#9baeb0", "#d97e68"],
        labels={"priorite": "Priorité", "statut": "Statut", "count": "Stories"},
    )
    backlog_chart.update_layout(
        template="plotly_white", height=320, margin=dict(l=8, r=10, t=20, b=8),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="DM Sans, sans-serif", color="#61747b", size=11),
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
        font=dict(family="DM Sans, sans-serif", color="#61747b", size=11), showlegend=False,
    )
    velocity_chart.update_xaxes(title=None, showgrid=False, linecolor="#e5ece9")
    velocity_chart.update_yaxes(title=None, gridcolor="#edf1ef", zeroline=False, rangemode="tozero")
    st.plotly_chart(velocity_chart, use_container_width=True, config={"displayModeBar": False})
    st.caption("Story points relatifs, définis pour le scénario. Ils ne mesurent pas une performance individuelle.")

st.subheader("Burndown illustratif")
burndown_rows = [
    {"Sprint": sprint["name"], "Jour": day, "Points restants": remaining}
    for sprint in pilot["sprints"]
    for day, remaining in enumerate(sprint["remaining_daily"])
]
burndown = px.line(
    pd.DataFrame(burndown_rows), x="Jour", y="Points restants", color="Sprint", markers=True,
    color_discrete_sequence=["#087e78", "#d5a04c", "#6b8491"],
    labels={"Jour": "Jour du sprint", "Points restants": "Story points restants"},
)
burndown.update_layout(
    template="plotly_white", height=300, margin=dict(l=8, r=10, t=15, b=8),
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Sans, sans-serif", color="#61747b", size=11),
    legend=dict(orientation="h", y=1.12, x=0),
)
burndown.update_xaxes(title=None, showgrid=False, linecolor="#e5ece9")
burndown.update_yaxes(title=None, gridcolor="#edf1ef", zeroline=False)
st.plotly_chart(burndown, use_container_width=True, config={"displayModeBar": False})
st.caption("Source : data/pilotage.json. Les valeurs de vélocité et de burndown sont des simulations.")

st.markdown('<p class="section-kicker" style="margin-top:28px">Maîtrise et couverture</p>', unsafe_allow_html=True)
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
