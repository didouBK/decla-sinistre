# Stratégie de test

Périmètre: artefacts, validations locales, fichiers, règles, récapitulatif, référence et statut. Exclus: garantie, indemnisation, intégrations, expertise réelle, conformité et sécurité de production.

Niveaux: unitaires Python (référentiel, liens, exports); intégration des données; tests fonctionnels manuels navigateur; tests négatifs/limites; non-régression; exploration clavier, responsive et messages. Gherkin est fourni comme spécification lisible; pytest contrôle les artefacts.

Entrée: données fictives et référentiel présents. Sortie: contrôles automatisés réussis, lacunes inscrites et tests manuels enregistrés. Un test n’est « exécuté » qu’après preuve observable. Anomalies: DEF, sévérité, étapes, attendu/observé, environnement, statut et lien TC. Risques: règles hypothétiques, absence backend, stockage navigateur, accessibilité et absence audit sécurité. Aucun résultat métier ne se déduit de ces tests.
