# Runbook développeur et exploitation de la démo

> Pour lancer et vérifier la démonstration du dépôt. Ce runbook ne décrit pas l’exploitation d’un service métier de production.

## Pré-requis

- Python 3.11+; sur macOS, utiliser `python3` (la commande `python` peut ne pas exister).
- Node.js 24 et npm pour les tests Playwright.
- Chromium Playwright pour exécuter les tests navigateur.

## Parcours statique

Depuis la racine du dépôt :

```bash
python3 -m http.server 8000 --directory prototype
```

Ouvrir `http://localhost:8000/`. Arrêter le serveur avec `Ctrl+C`. Le parcours n’a pas de serveur métier.

## Dashboard local

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run dashboard/app.py
```

Utiliser uniquement les données fictives fournies. Les résultats QA saisis sont conservés dans la session Streamlit et ne sont pas synchronisés.

## Contrôles

```bash
python3 scripts/validate_project.py
python3 -m pytest -q tests/
npm ci
npx playwright install chromium
npm run test:e2e
```

Dans GitHub Actions, le job `checks` valide le référentiel et pytest; le job `browser` lance les tests Playwright sur Chromium et publie le rapport HTML, captures et traces comme artefact du workflow.

## Publication

| Cible | Source | Vérification après publication |
|---|---|---|
| GitHub Pages | `prototype/` sur `main` | Ouvrir le prototype; vérifier styles/JS, étape 1, confirmation fictive et suivi local |
| Streamlit Community Cloud | `dashboard/app.py` sur `main` | Ouvrir l’onglet QA; vérifier l’état du dernier workflow, le compteur US/TC et lancer les contrôles locaux |

La publication est liée au dépôt GitHub. Examiner le workflow de déploiement après un changement et vérifier le commit déployé dans l’interface d’hébergement.

## Diagnostic rapide

| Symptôme | Vérification |
|---|---|
| `python: command not found` sur macOS | Utiliser `python3`; activer le venv pour les commandes `python` |
| Page blanche / ressource 404 | Lancer le serveur avec `--directory prototype` et vérifier `/`, `/style.css`, `/app.js` |
| `npm ci` échoue | Vérifier la version Node/npm et que `package-lock.json` correspond à `package.json` |
| Playwright ne trouve pas Chromium | Lancer `npx playwright install chromium`; dans CI l’installation se fait avec `--with-deps` |
| Streamlit affiche une erreur après push | Lire Manage app → logs, vérifier la compilation de `dashboard/app.py` et attendre la synchronisation du commit |
| Test navigateur en échec | Ouvrir l’artefact Playwright du run CI; lire `error-context.md`, capture et trace avant correction |

## Gestion des incidents de démonstration

1. Identifier le commit et la cible concernée.
2. Reproduire avec des données fictives uniquement.
3. Consulter le log de déploiement ou l’artefact CI correspondant.
4. Corriger via un commit puis laisser la CI confirmer le changement.
5. Vérifier à nouveau les deux URL publiques.

Il n’existe ni astreinte, ni SLO, ni procédure de reprise de données, car aucun traitement de dossier réel n’est en service.
