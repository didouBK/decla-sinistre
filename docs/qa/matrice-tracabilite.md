# Matrice de traçabilité

Source unique: data/referentiel.json. Export: matrice-tracabilite.csv.

| TC | Cas | Liens | Statut initial |
|---|---|---|---|
| TC-001 | Contrat valide | REQ-001;RG-001 | À exécuter |
| TC-002 | Contrat hors période | REQ-001;RG-001 | À exécuter |
| TC-003 | Champs manquants | REQ-004;RG-002;RG-008;RG-012 | À exécuter |
| TC-004 | Date future | REQ-002;RG-003 | À exécuter |
| TC-005 | Date trop ancienne | REQ-002;RG-003 | À exécuter |
| TC-006 | Circonstance ambiguë | REQ-002;RG-004 | À exécuter |
| TC-007 | Fichier supporté | REQ-003;RG-005 | À exécuter |
| TC-008 | Fichier trop grand/invalide | REQ-003;RG-005 | À exécuter |
| TC-009 | Montant négatif | REQ-002;RG-006 | À exécuter |
| TC-010 | Montant supérieur limite | REQ-002;RG-006 | À exécuter |
| TC-011 | Seuil expert | REQ-004;RG-007;RG-012 | À exécuter |
| TC-012 | Soumission conforme | REQ-006;REQ-007;RG-009;RG-010 | À exécuter |
| TC-013 | Suivi statut | REQ-008;RG-011 | À exécuter |
| TC-014 | Absence appel externe | REQ-009 | À exécuter |
| TC-015 | Mesure durée | REQ-010 | À exécuter |

Les TC sont prévus, pas réputés exécutés par leur seule présence. TC-014/015 nécessitent aussi des vérifications manuelles.
