# Référentiel des exigences

BR = besoin, REQ = exigence, RG = règle, US = story, TC = test, DEF = anomalie fictive.

Besoins métier: BR-001 réduire les relances; BR-002 viser ≤1 jour ouvré de prise en charge; BR-003 visibilité accrue. Ce sont des objectifs.

| ID | Exigence | Testable | Tests associés |
|---|---|---|---|
| REQ-001 | Identification et contrat fictif | Oui | TC-001, TC-002 |
| REQ-002 | Circonstances, dommages et montant | Oui | TC-004, TC-005, TC-006, TC-009, TC-010 |
| REQ-003 | Ajout et validation des pièces | Oui | TC-007, TC-008 |
| REQ-004 | Complétude, règles et orientation | Oui | TC-003, TC-011 |
| REQ-005 | Récapitulatif modifiable | Oui |  |
| REQ-006 | Soumission et référence fictive | Oui | TC-012 |
| REQ-007 | Confirmation de dépôt | Oui | TC-012 |
| REQ-008 | Suivi de statut | Oui | TC-013 |
| REQ-009 | Aucune transmission externe ni donnée réelle | Oui | TC-014 |
| REQ-010 | Parcours nominal inférieur à cinq minutes, objectif à mesurer | Oui | TC-015 |

Chaque exigence testable est reliée à au moins un cas. BR-001..003 non vérifiables par le prototype. REQ-009 exige contrôle réseau complémentaire; REQ-010 exige mesure manuelle. Exigences contractuelles, conservation, sécurité et authentification restent à préciser. Aucun DEF n’est inventé.

SpecGen QA: aucune interface réelle n’est disponible ici; aucune génération n’est attribuée à cet outil. data/referentiel.json est un référentiel local, sans prétendre au format officiel de SpecGen QA.
