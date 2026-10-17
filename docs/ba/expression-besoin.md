# Expression de besoin — DéclaSinistre

> Cas entièrement fictif: organisation, personnes, contrats, données, décisions et résultats sont inventés. Aucun assureur réel n’est impliqué.

## Contexte et problème
Le scénario imagine des déclarations de dégâts des eaux reçues surtout par téléphone, avec saisie manuelle, justificatifs parfois séparés et faible visibilité. Hypothèses de départ: 30 % de dossiers incomplets et délai initial moyen de 5 jours. Ce ne sont pas des statistiques réelles.

## Objectifs métier et indicateurs
Cibles non atteintes ni mesurées: déclaration nominale <5 min; dossiers incomplets ≤10 %; prise en charge initiale ≤1 jour ouvré; meilleure traçabilité et contrôles préalables.

| Indicateur | Mesure | Périmètre/source | Limites |
|---|---|---|---|
| Durée de parcours | médiane entre début et confirmation | sessions nominales de test | interruptions exclues; échantillon non généralisable |
| Taux incomplet | dossiers nécessitant une relance ÷ dossiers reçus | période/canal définis | définition de complétude à valider |
| Délai initial | heures ouvrées dépôt→première prise en charge humaine | horodatages opérationnels | distinguer accusé automatique de prise en charge |
| Traçabilité | dossiers avec référence, événements et statut ÷ dossiers | journal applicatif | pas de journal serveur dans ce prototype |

## Parties prenantes
Assuré, gestionnaire, expert, sponsor, Product Owner, Business Analyst, développeur, QA Analyst, Scrum Master.

## Besoins, exigences, solution, hypothèses
Besoins métier BR-001 à BR-003: réduire relances, délai et opacité. Exigences REQ-001 à REQ-010 dans le référentiel. Solution envisagée: parcours web de cinq écrans avec validations et suivi local. Hypothèses de règles (fenêtre 365 jours, fichiers 10/30 Mo, plafond 100 000 €, seuil expert 5 000 €) sont fictives et à faire valider; elles ne sont ni universelles ni réglementaires.

## Fonctionnel / non fonctionnel
Identification fictive, circonstances, pièces, validation, récapitulatif, dépôt, confirmation, statut. Interface française, responsive, clavier et messages clairs, aucune transmission externe.

## Périmètre
Inclus: contrat de démonstration, saisie, photos/justificatifs locaux, contrôles, orientation indicative, référence et statut. Exclus: assureur et données réels, indemnisation, paiement, expertise réelle, signature opposable, authentification de production, stockage réel de documents personnels.

## Hypothèses, dépendances, contraintes
Les seuils doivent être validés par le référent métier du scénario. Toute production nécessite règles contractuelles, politique de conservation, sécurité et authentification à définir. Prototype local sans backend.

## Validation métier
Champs requis explicites; erreurs actionnables; ambiguïté vers revue humaine; aucune promesse de garantie; récapitulatif modifiable; confirmation uniquement après soumission valide; mention fictive visible.

## Glossaire
IARD: incendies, accidents et risques divers. Sinistre: événement déclaré. Complétude: présence des informations nécessaires à la qualification. RG: règle de gestion. TC: cas de test.

## Questions ouvertes
Définition contractuelle de complétude? Exceptions et seuils d’expertise? Délais/calendriers ouvrés? Conservation/suppression? Authentification? Validation des messages? Accessibilité et sécurité de production?
