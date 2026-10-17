# Règles de gestion

> Hypothèses fictives de démonstration, à valider. Elles ne sont pas des règles générales du marché.

## RG-001 — Contrat valide à la date
- **Description / résultat :** Contrat fictif actif à la date déclarée. Hors période: blocage et vérification humaine, sans décision de garantie.
- **Déclenchement :** validation de l’étape correspondante.
- **Message :** expliquer l’erreur ou l’orientation; ne pas décider une garantie.
- **Exigences :** US-001
- **Tests :** TC-001;TC-002

## RG-002 — Champs obligatoires
- **Description / résultat :** Identité, contrat, date, adresse, circonstances, description et estimation requis.
- **Déclenchement :** validation de l’étape correspondante.
- **Message :** expliquer l’erreur ou l’orientation; ne pas décider une garantie.
- **Exigences :** US-002
- **Tests :** TC-003

## RG-003 — Date sinistre
- **Description / résultat :** Date non future et dans les 365 derniers jours (hypothèse de démonstration à valider).
- **Déclenchement :** validation de l’étape correspondante.
- **Message :** expliquer l’erreur ou l’orientation; ne pas décider une garantie.
- **Exigences :** US-002
- **Tests :** TC-004;TC-005

## RG-004 — Cohérence circonstances
- **Description / résultat :** Situation ambiguë transmise au gestionnaire; aucun rejet automatique.
- **Déclenchement :** validation de l’étape correspondante.
- **Message :** expliquer l’erreur ou l’orientation; ne pas décider une garantie.
- **Exigences :** US-004
- **Tests :** TC-006

## RG-005 — Pièces jointes
- **Description / résultat :** JPG, PNG, PDF; maximum 10 Mo par fichier, 30 Mo cumulés (hypothèses).
- **Déclenchement :** validation de l’étape correspondante.
- **Message :** expliquer l’erreur ou l’orientation; ne pas décider une garantie.
- **Exigences :** US-003
- **Tests :** TC-007;TC-008

## RG-006 — Estimation
- **Description / résultat :** Valeur numérique de 0 à 100 000 €; estimation indicative, pas indemnité.
- **Déclenchement :** validation de l’étape correspondante.
- **Message :** expliquer l’erreur ou l’orientation; ne pas décider une garantie.
- **Exigences :** US-002
- **Tests :** TC-009;TC-010

## RG-007 — Orientation expert
- **Description / résultat :** À partir de 5 000 €, proposer expertise; seuil fictif à valider.
- **Déclenchement :** validation de l’étape correspondante.
- **Message :** expliquer l’erreur ou l’orientation; ne pas décider une garantie.
- **Exigences :** US-004
- **Tests :** TC-011

## RG-008 — Données manquantes
- **Description / résultat :** Lister les champs requis absents avant soumission.
- **Déclenchement :** validation de l’étape correspondante.
- **Message :** expliquer l’erreur ou l’orientation; ne pas décider une garantie.
- **Exigences :** US-004
- **Tests :** TC-003

## RG-009 — Référence
- **Description / résultat :** Après soumission conforme, générer DS-AAAA-NNNNNN unique.
- **Déclenchement :** validation de l’étape correspondante.
- **Message :** expliquer l’erreur ou l’orientation; ne pas décider une garantie.
- **Exigences :** US-006
- **Tests :** TC-012

## RG-010 — Confirmation
- **Description / résultat :** Afficher confirmation seulement après dépôt conforme.
- **Déclenchement :** validation de l’étape correspondante.
- **Message :** expliquer l’erreur ou l’orientation; ne pas décider une garantie.
- **Exigences :** US-007
- **Tests :** TC-012

## RG-011 — Statuts
- **Description / résultat :** Brouillon, Déposé, À qualifier, En traitement; transitions illustratives.
- **Déclenchement :** validation de l’étape correspondante.
- **Message :** expliquer l’erreur ou l’orientation; ne pas décider une garantie.
- **Exigences :** US-008
- **Tests :** TC-013

## RG-012 — Contrôle avant transmission
- **Description / résultat :** Seul un dossier complet peut passer en qualification; aucune transmission réelle.
- **Déclenchement :** validation de l’étape correspondante.
- **Message :** expliquer l’erreur ou l’orientation; ne pas décider une garantie.
- **Exigences :** US-006
- **Tests :** TC-003;TC-011
