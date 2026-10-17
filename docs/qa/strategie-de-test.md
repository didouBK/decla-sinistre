# Stratégie de test

Périmètre: artefacts, validations locales, fichiers, règles, récapitulatif, référence et statut. Exclus: garantie, indemnisation, intégrations, expertise réelle, conformité et sécurité de production.

Niveaux: contrôles structurels Python (référentiel, liens, exports); tests fonctionnels navigateur Playwright pour les cas TC-001 à TC-014; tests manuels pour la mesure de durée TC-015, l’exploration clavier et certains contrôles responsive. Gherkin reste une spécification lisible; les noms des tests Playwright portent les identifiants US/TC pour rendre la couverture vérifiable.

Entrée: données fictives et référentiel présents. Sortie: contrôles automatisés réussis, lacunes inscrites et tests manuels enregistrés. Un test n’est « exécuté » qu’après preuve observable. Anomalies: DEF, sévérité, étapes, attendu/observé, environnement, statut et lien TC. Risques: règles hypothétiques, absence backend, stockage navigateur, accessibilité et absence audit sécurité. Aucun résultat métier ne se déduit de ces tests.
