# DéclaSinistre

[![Qualité CI](https://github.com/didouBK/decla-sinistre/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/didouBK/decla-sinistre/actions/workflows/ci.yml)

**Étude de cas portfolio — Business Analysis, QA et pilotage produit**

**Digitalisation fictive du parcours de déclaration d’un dégât des eaux — assurance IARD**

> Cas pratique portfolio intégralement fictif. Les chiffres, acteurs, règles, données et résultats de pilotage sont des hypothèses ou simulations. Aucun assureur réel ni donnée client réelle ne sont impliqués. Ce projet n’est pas utilisé en production.

## Sommaire
- [Contexte et objectifs](#contexte-et-objectifs)
- [Périmètre](#périmètre)
- [Architecture](#architecture)
- [Compétences démontrées](#compétences-démontrées)
- [Livrables](#livrables)
- [Installation et exécution](#installation-et-exécution)
- [Tests](#tests)
- [Limites et améliorations](#limites-et-améliorations)
- [Publication](#publication)

## Contexte et objectifs
Le scénario part d’une hypothèse de déclarations principalement téléphoniques, 30 % de dossiers incomplets et 5 jours de délai initial moyen. Ce ne sont pas des statistiques réelles. Cibles à étudier: déclaration nominale en moins de 5 minutes, taux incomplet ≤10 %, prise en charge initiale ≤1 jour ouvré, meilleure visibilité et contrôles en amont. Elles ne sont pas présentées comme des résultats obtenus.

## Périmètre
Parcours fictif d’identification, circonstances, justificatifs locaux, contrôles, récapitulatif, dépôt, confirmation et suivi simplifié. Exclusions: contrat/assureur réel, indemnisation, paiement, expertise réelle, signature opposable, authentification et stockage de vrais documents. Seuil expert, fenêtre de date et limites fichiers sont des hypothèses à valider, pas des règles universelles.

## Architecture
Le prototype statique est dans `prototype/`; le dashboard Streamlit dans `dashboard/`. Les référentiels canoniques sont `data/referentiel.json` et `data/pilotage.json`; CSV versionnés servent aux exports. Contrôles automatiques: `scripts/validate_project.py` et pytest. CI GitHub Actions vérifie le dépôt.

## Compétences démontrées
- **BA :** expression de besoin, périmètre, règles, processus AS-IS/TO-BE, exigences et traçabilité.
- **QA :** stratégie, plan, cas, critères Gherkin, données fictives, contrôles automatisés et limites.
- **Pilotage :** MoSCoW, roadmap, sprints simulés, risques, RACI, COPIL, vélocité/burndown.
- **UX/technique :** prototype accessible de base, responsive, Streamlit/Pandas/Plotly.

## Livrables
Commencer par [l’étude de cas portfolio](docs/portfolio/cas-portfolio.md) et [l’index documentaire](docs/index.md), puis [expression de besoin](docs/ba/expression-besoin.md), [stories](docs/ba/user-stories.md), [règles](docs/ba/regles-gestion.md), [matrice QA](docs/qa/matrice-tracabilite.md), [roadmap](docs/pilotage/roadmap.md), [registre des risques](docs/pilotage/registre-risques.md) et [architecture](docs/architecture/architecture.md).

## Installation et exécution
Python 3.11+ recommandé.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Prototype: `cd prototype && python3 -m http.server 8000`, puis ouvrir http://localhost:8000. Ou ouvrir `prototype/index.html`. Le prototype n’envoie aucune donnée; éviter toute donnée personnelle.

Dashboard depuis la racine: `streamlit run dashboard/app.py`.

## Tests
`python3 scripts/validate_project.py` puis `python3 -m pytest -q`. Les fichiers `.feature` sont des spécifications; l’automatisation pytest vérifie les référentiels, liens et exports, pas l’exécution navigateur. Les scénarios UI doivent être joués manuellement et consignés. Les nombres de tests passés ne sont pas inventés.

Les parcours navigateur automatisés sont exécutés avec Playwright et reliés aux TC/US par leur identifiant dans le nom de chaque test. Pour les lancer localement :

```bash
npm ci
npx playwright install chromium
npm run test:e2e
```

La CI publie le rapport Playwright comme artefact de chaque exécution. TC-015 reste une mesure manuelle du temps de parcours : le dépôt ne prétend pas avoir mesuré un résultat utilisateur. La couverture QA suivie dans le dashboard est la couverture des scénarios métier par US; aucune couverture de lignes de code n’est revendiquée.

## Limites et améliorations
Aucun backend, compte réel, sécurité de production, contrôle antivirus, stockage documentaire, audit de conformité ou validation métier indépendante. Les statuts et données de pilotage sont simulés. Suite possible: tests navigateur automatisés, validation des règles par un référent métier, étude de sécurité/confidentialité, puis architecture authentifiée et journalisée avant tout usage réel.

## Déploiement

- **Prototype GitHub Pages :** [ouvrir la démonstration](https://didoubk.github.io/decla-sinistre/). Le workflow `.github/workflows/deploy-pages.yml` publie `prototype/` à chaque changement sur `main`.
- **Dashboard Streamlit :** [ouvrir le tableau de pilotage](https://decla-sinistre-x9mfsvb3qxpanxxc4gmnhu.streamlit.app/). Il est connecté au dépôt `didouBK/decla-sinistre`, branche `main`, fichier `dashboard/app.py`.

Le dashboard propose aussi un onglet **QA · Tests et couverture** : lancement des contrôles du dépôt, suivi des 15 cas liés aux US, couverture d’exécution par US et export CSV du plan et du journal. Les résultats manuels sont conservés pendant la session Streamlit; ils ne sont pas partagés entre utilisateurs ni stockés durablement. Les tests navigateur automatisés sont exécutés en CI et leur rapport est disponible comme artefact GitHub Actions.

Aucun backend ni service externe ne reçoit les données du prototype. Les données du dashboard sont fictives et les indicateurs sont des simulations.
