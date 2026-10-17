# DéclaSinistre — étude de cas portfolio

> Projet personnel de démonstration. Le besoin, les chiffres, les règles, les données et les parcours sont fictifs. Aucun assureur réel, dossier client ou résultat métier réel n’est impliqué.

## En bref

DéclaSinistre est une étude de cas de digitalisation du parcours de déclaration d’un dégât des eaux. Elle montre comment cadrer un besoin métier, le transformer en exigences et user stories traçables, prototyper le parcours, puis organiser son assurance qualité.

**Positionnement :** Business Analysis · QA fonctionnelle · pilotage produit · conception UX de parcours.

## Problème étudié

Le scénario part de l’hypothèse que des déclarations arrivent incomplètes et que les assurés manquent de visibilité. Les valeurs « 30 % de dossiers incomplets » et « 5 jours de délai initial » sont des données de scénario, pas des statistiques du marché. Le projet explore un parcours guidé, la complétude en amont et une confirmation locale.

## Démarche et livrables

- Expression de besoin, périmètre et hypothèses à valider.
- Processus AS-IS / TO-BE et règles métier de démonstration.
- 10 exigences, 8 user stories et 12 règles reliées au référentiel.
- 15 cas de test, matrice de traçabilité et scénarios Gherkin.
- Cahier UX, maquettes SVG du parcours et du dashboard, guide de démonstration.
- Architecture, ADR de cadrage, revue des limites sécurité/données et runbook.
- Prototype responsive statique et tableau de pilotage / QA.
- Contrôles de cohérence Python, tests pytest et tests navigateur Playwright reliés aux identifiants TC et US.

## Résultats vérifiables

- Les contrôles structurels vérifient l’unicité des identifiants, la validité des liens et la cohérence des exports.
- Les tests Playwright couvrent les cas TC-001 à TC-014 et traversent les 8 US; le cas TC-015 reste une mesure manuelle du temps de parcours.
- La couverture présentée dans le tableau de bord est une couverture de scénarios par US. La couverture de lignes de code n’est pas mesurée.
- Les résultats de la dernière exécution et le rapport CI sont consultables dans les [Actions GitHub](https://github.com/didouBK/decla-sinistre/actions/workflows/ci.yml).

## Démonstration

- [Parcours de déclaration fictif](https://didoubk.github.io/decla-sinistre/)
- [Dashboard de pilotage et d’assurance qualité](https://decla-sinistre-x9mfsvb3qxpanxxc4gmnhu.streamlit.app/)
- [Code et livrables](https://github.com/didouBK/decla-sinistre)

## Limites assumées

Le prototype n’a ni backend, ni authentification, ni intégration à un assureur, ni stockage serveur. Les pièces ne sont pas téléversées; le statut est une démonstration locale au navigateur. Les règles et seuils sont des hypothèses sans valeur contractuelle. Ce projet ne constitue pas un produit prêt pour un usage réel.

## Formulation courte pour une candidature

Conception d’une étude de cas fictive de déclaration de sinistre : cadrage du besoin, modélisation de parcours, rédaction d’exigences et de user stories, traçabilité de 15 cas de test et mise en place d’un prototype web avec tests navigateur automatisés et CI. Les hypothèses et limites de la démonstration sont documentées.
