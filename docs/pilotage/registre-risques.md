# Registre des risques

Échelle probabilité/impact de 1 (faible) à 5 (très fort); criticité = P×I; seuil haut ≥15. État simulé.

| ID | Risque / cause | P | I | Score | Responsable | Prévention | Contingence | État |
|---|---|---:|---:|---:|---|---|---|---|
| R-001 | Fraude documentaire / justificatif falsifié | 3 | 4 | 12 | QA | contrôles humains et conservation prudente | revue gestionnaire | Ouvert |
| R-002 | Données personnelles sur photos | 4 | 5 | 20 | PO | avertissement, aucune vraie pièce en démo | supprimer localement, escalader | Ouvert |
| R-003 | Règle mal interprétée / hypothèses | 3 | 5 | 15 | BA | validation référent métier | bloquer décision et revue humaine | À valider |
| R-004 | Fichier volumineux/illisible | 3 | 3 | 9 | Développeur | formats/tailles et messages | nouveau fichier ou traitement humain | Atténué |
| R-005 | Dépendance technique retard | 2 | 4 | 8 | Scrum Master | prototype léger, suivi dépendances | réduire périmètre | Surveillé |
