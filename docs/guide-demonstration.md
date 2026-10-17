# Guide de démonstration

> Guide de visite pour une revue de portfolio. Toutes les valeurs ci-dessous sont fictives.

## 1. Parcours assuré

Ouvrir le [prototype publié](https://didoubk.github.io/decla-sinistre/) et utiliser les exemples ci-dessous :

| Champ | Valeur de démonstration |
|---|---|
| Nom | Camille Martin |
| Contrat | DEMO-0001 |
| Date | Une date récente dans la fenêtre illustrative de 365 jours |
| Adresse | 10 rue Exemple, 75000 Paris |
| Circonstances | Dégât des eaux accidentel |
| Estimation | 1 200 € |
| Description | Une fuite fictive est apparue sous l’évier. |

Continuer jusqu’au récapitulatif, modifier une valeur avec « Précédent », puis confirmer la simulation. La référence `DS-DEMO-…` et le statut sont enregistrés dans le navigateur uniquement. Le bouton « Suivre une déclaration » rouvre ce statut local.

Pour explorer les contrôles : utiliser une référence différente de `DEMO-0001` pour observer le message de revue humaine; essayer une date future, une estimation hors limites ou un type de pièce non pris en charge. Ne sélectionner aucun document personnel.

## 2. Tableau de bord produit et QA

Ouvrir le [dashboard Streamlit](https://decla-sinistre-x9mfsvb3qxpanxxc4gmnhu.streamlit.app/) puis l’onglet **QA · Tests et couverture** :

1. Consulter le statut du dernier workflow Playwright et suivre le lien vers son rapport.
2. Lancer « Lancer les contrôles qualité » pour exécuter le validateur du dépôt et pytest dans la session.
3. Parcourir le tableau de couverture : 8 user stories liées, 14 identifiants TC automatisés sur 15; TC-015 reste manuel.
4. Choisir un cas dans « Exécuter un scénario métier », lire les exigences et règles associées, puis consigner un résultat manuel avec une preuve fictive.
5. Exporter le plan ou l’historique QA en CSV si un exemple de livrable est utile.

Les saisies QA manuelles ne sont pas sauvegardées durablement et disparaissent avec la session Streamlit. La CI est la source des résultats automatisés; les contrôles manuels ne modifient pas le statut GitHub.

## 3. Documents à consulter pendant la revue

- [Étude de cas portfolio](portfolio/cas-portfolio.md) pour le contexte et les résultats vérifiables.
- [Cahier UX](ux/cahier-ux.md) et ses [maquettes SVG du parcours](ux/maquette-parcours.svg) / [dashboard](ux/maquette-dashboard.svg).
- [Matrice de traçabilité](qa/matrice-tracabilite.md) pour le lien besoin → exigences → US → tests.
- [Architecture](architecture/architecture.md) et [sécurité/données](architecture/securite-donnees.md) pour les limites techniques.

## 4. Message de prudence

La démonstration ne reçoit ni ne traite de vrais dossiers. Les règles, dates, montants, références et objectifs sont des exemples. Les tests automatisés vérifient le comportement du prototype; ils ne valident pas une indemnisation ou un processus réel.
