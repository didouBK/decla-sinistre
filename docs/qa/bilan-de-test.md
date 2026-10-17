# Bilan de test

> Dernière exécution documentée : 17 octobre 2026 · Commit `43726ee913d26d0d24c6e5ce3b63ebd8706dd587` · Workflow GitHub Actions n° 22.

## Résultats automatisés

| Niveau | Résultat | Portée |
|---|---|---|
| Validation du référentiel | Réussi | Unicité des identifiants, liens, exports et cohérence des 8 user stories |
| pytest | 4 réussis | Contrôles du référentiel et des artefacts Python |
| Playwright / Chromium | 15 réussis | Parcours navigateur associés aux user stories; 14 identifiants TC distincts sur les 15 définis |

Les deux jobs du dernier [workflow GitHub Actions](https://github.com/didouBK/decla-sinistre/actions/runs/39030239463) sont réussis : `checks` et `browser`. Le rapport Playwright et les traces sont conservés comme artefact pendant 30 jours. Le [dashboard QA](https://decla-sinistre-x9mfsvb3qxpanxxc4gmnhu.streamlit.app/) affiche l’état de la dernière exécution automatisée.

## Couverture

- 8/8 user stories ont au moins un lien vers un cas de test.
- 14/15 identifiants TC disposent d’un scénario Playwright; le TC restant est TC-015, mesure manuelle du temps nominal.
- La suite contient 15 tests Playwright, car le parcours de confirmation couvre des cas distincts de récapitulatif et de soumission sous un identifiant partagé.
- La couverture de lignes de code n’est pas mesurée. Les scénarios exécutés dans la CI ne sont pas des résultats d’exécution manuelle enregistrés dans le dashboard.

## Tests non réalisés / limites

Mesure utilisateur de durée, tests sur appareils réels, audit formel d’accessibilité, charge, sécurité, conformité, intégrations et validation métier indépendante non réalisés. Les seuils et données sont fictifs. Ces tests réussis démontrent le fonctionnement de la maquette automatisée, pas la qualité d’un service d’assurance réel.
