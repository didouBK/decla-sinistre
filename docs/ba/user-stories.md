# User stories

Exactement huit stories principales; estimations relatives en story points. Les scénarios Gherkin utilisent les mots-clés anglais.

## US-001 — Identification assuré et contrat
**Description :** En tant qu’assuré, je veux identification assuré et contrat, afin de déclarer et suivre le sinistre clairement.
**Valeur :** réduire les ressaisies et rendre le parcours compréhensible. **MoSCoW :** MUST. **Estimation :** 5 SP. **Dépendances :** aucune. **Exigences :** REQ-001. **Tests :** TC-001, TC-002.

**Critères d’acceptation :**

```gherkin
Feature: Identification assuré et contrat
  Scenario: parcours nominal
    Given un assuré utilise des données fictives valides
    When il complète Identification assuré et contrat
    Then l’étape affiche le résultat attendu
  Scenario: donnée invalide ou manquante
    Given l’assuré complète le parcours
    When une donnée requise manque ou est invalide
    Then un message explicite est affiché
    And la soumission est bloquée si une règle obligatoire échoue
  Scenario: limite documentée
    Given une valeur se trouve à la limite d’une règle
    When l’assuré valide
    Then le comportement respecte la règle liée sans décision de garantie
```
**Definition of Done :** critères vérifiables, erreurs accessibles, TC liés exécutés et résultat consigné, documentation à jour, aucune donnée réelle ni appel externe.

## US-002 — Circonstances et dommages
**Description :** En tant qu’assuré, je veux circonstances et dommages, afin de déclarer et suivre le sinistre clairement.
**Valeur :** réduire les ressaisies et rendre le parcours compréhensible. **MoSCoW :** MUST. **Estimation :** 5 SP. **Dépendances :** US-001 et règles liées. **Exigences :** REQ-002. **Tests :** TC-003, TC-004, TC-005, TC-009, TC-010.

**Critères d’acceptation :**

```gherkin
Feature: Circonstances et dommages
  Scenario: parcours nominal
    Given un assuré utilise des données fictives valides
    When il complète Circonstances et dommages
    Then l’étape affiche le résultat attendu
  Scenario: donnée invalide ou manquante
    Given l’assuré complète le parcours
    When une donnée requise manque ou est invalide
    Then un message explicite est affiché
    And la soumission est bloquée si une règle obligatoire échoue
  Scenario: limite documentée
    Given une valeur se trouve à la limite d’une règle
    When l’assuré valide
    Then le comportement respecte la règle liée sans décision de garantie
```
**Definition of Done :** critères vérifiables, erreurs accessibles, TC liés exécutés et résultat consigné, documentation à jour, aucune donnée réelle ni appel externe.

## US-003 — Photos et justificatifs
**Description :** En tant qu’assuré, je veux photos et justificatifs, afin de déclarer et suivre le sinistre clairement.
**Valeur :** réduire les ressaisies et rendre le parcours compréhensible. **MoSCoW :** SHOULD. **Estimation :** 5 SP. **Dépendances :** US-001 et règles liées. **Exigences :** REQ-003. **Tests :** TC-007, TC-008.

**Critères d’acceptation :**

```gherkin
Feature: Photos et justificatifs
  Scenario: parcours nominal
    Given un assuré utilise des données fictives valides
    When il complète Photos et justificatifs
    Then l’étape affiche le résultat attendu
  Scenario: donnée invalide ou manquante
    Given l’assuré complète le parcours
    When une donnée requise manque ou est invalide
    Then un message explicite est affiché
    And la soumission est bloquée si une règle obligatoire échoue
  Scenario: limite documentée
    Given une valeur se trouve à la limite d’une règle
    When l’assuré valide
    Then le comportement respecte la règle liée sans décision de garantie
```
**Definition of Done :** critères vérifiables, erreurs accessibles, TC liés exécutés et résultat consigné, documentation à jour, aucune donnée réelle ni appel externe.

## US-004 — Contrôles métier et orientation
**Description :** En tant qu’assuré, je veux contrôles métier et orientation, afin de déclarer et suivre le sinistre clairement.
**Valeur :** réduire les ressaisies et rendre le parcours compréhensible. **MoSCoW :** MUST. **Estimation :** 8 SP. **Dépendances :** US-001 et règles liées. **Exigences :** REQ-004. **Tests :** TC-006, TC-011.

**Critères d’acceptation :**

```gherkin
Feature: Contrôles métier et orientation
  Scenario: parcours nominal
    Given un assuré utilise des données fictives valides
    When il complète Contrôles métier et orientation
    Then l’étape affiche le résultat attendu
  Scenario: donnée invalide ou manquante
    Given l’assuré complète le parcours
    When une donnée requise manque ou est invalide
    Then un message explicite est affiché
    And la soumission est bloquée si une règle obligatoire échoue
  Scenario: limite documentée
    Given une valeur se trouve à la limite d’une règle
    When l’assuré valide
    Then le comportement respecte la règle liée sans décision de garantie
```
**Definition of Done :** critères vérifiables, erreurs accessibles, TC liés exécutés et résultat consigné, documentation à jour, aucune donnée réelle ni appel externe.

## US-005 — Récapitulatif avant envoi
**Description :** En tant qu’assuré, je veux récapitulatif avant envoi, afin de déclarer et suivre le sinistre clairement.
**Valeur :** réduire les ressaisies et rendre le parcours compréhensible. **MoSCoW :** MUST. **Estimation :** 3 SP. **Dépendances :** US-001 et règles liées. **Exigences :** REQ-005. **Tests :** TC-012.

**Critères d’acceptation :**

```gherkin
Feature: Récapitulatif avant envoi
  Scenario: parcours nominal
    Given un assuré utilise des données fictives valides
    When il complète Récapitulatif avant envoi
    Then l’étape affiche le résultat attendu
  Scenario: donnée invalide ou manquante
    Given l’assuré complète le parcours
    When une donnée requise manque ou est invalide
    Then un message explicite est affiché
    And la soumission est bloquée si une règle obligatoire échoue
  Scenario: limite documentée
    Given une valeur se trouve à la limite d’une règle
    When l’assuré valide
    Then le comportement respecte la règle liée sans décision de garantie
```
**Definition of Done :** critères vérifiables, erreurs accessibles, TC liés exécutés et résultat consigné, documentation à jour, aucune donnée réelle ni appel externe.

## US-006 — Soumission de déclaration
**Description :** En tant qu’assuré, je veux soumission de déclaration, afin de déclarer et suivre le sinistre clairement.
**Valeur :** réduire les ressaisies et rendre le parcours compréhensible. **MoSCoW :** MUST. **Estimation :** 5 SP. **Dépendances :** US-001 et règles liées. **Exigences :** REQ-006. **Tests :** TC-012.

**Critères d’acceptation :**

```gherkin
Feature: Soumission de déclaration
  Scenario: parcours nominal
    Given un assuré utilise des données fictives valides
    When il complète Soumission de déclaration
    Then l’étape affiche le résultat attendu
  Scenario: donnée invalide ou manquante
    Given l’assuré complète le parcours
    When une donnée requise manque ou est invalide
    Then un message explicite est affiché
    And la soumission est bloquée si une règle obligatoire échoue
  Scenario: limite documentée
    Given une valeur se trouve à la limite d’une règle
    When l’assuré valide
    Then le comportement respecte la règle liée sans décision de garantie
```
**Definition of Done :** critères vérifiables, erreurs accessibles, TC liés exécutés et résultat consigné, documentation à jour, aucune donnée réelle ni appel externe.

## US-007 — Confirmation de dépôt
**Description :** En tant qu’assuré, je veux confirmation de dépôt, afin de déclarer et suivre le sinistre clairement.
**Valeur :** réduire les ressaisies et rendre le parcours compréhensible. **MoSCoW :** MUST. **Estimation :** 2 SP. **Dépendances :** US-001 et règles liées. **Exigences :** REQ-007. **Tests :** TC-012.

**Critères d’acceptation :**

```gherkin
Feature: Confirmation de dépôt
  Scenario: parcours nominal
    Given un assuré utilise des données fictives valides
    When il complète Confirmation de dépôt
    Then l’étape affiche le résultat attendu
  Scenario: donnée invalide ou manquante
    Given l’assuré complète le parcours
    When une donnée requise manque ou est invalide
    Then un message explicite est affiché
    And la soumission est bloquée si une règle obligatoire échoue
  Scenario: limite documentée
    Given une valeur se trouve à la limite d’une règle
    When l’assuré valide
    Then le comportement respecte la règle liée sans décision de garantie
```
**Definition of Done :** critères vérifiables, erreurs accessibles, TC liés exécutés et résultat consigné, documentation à jour, aucune donnée réelle ni appel externe.

## US-008 — Suivi du statut
**Description :** En tant qu’assuré, je veux suivi du statut, afin de déclarer et suivre le sinistre clairement.
**Valeur :** réduire les ressaisies et rendre le parcours compréhensible. **MoSCoW :** COULD. **Estimation :** 3 SP. **Dépendances :** US-001 et règles liées. **Exigences :** REQ-008. **Tests :** TC-013.

**Critères d’acceptation :**

```gherkin
Feature: Suivi du statut
  Scenario: parcours nominal
    Given un assuré utilise des données fictives valides
    When il complète Suivi du statut
    Then l’étape affiche le résultat attendu
  Scenario: donnée invalide ou manquante
    Given l’assuré complète le parcours
    When une donnée requise manque ou est invalide
    Then un message explicite est affiché
    And la soumission est bloquée si une règle obligatoire échoue
  Scenario: limite documentée
    Given une valeur se trouve à la limite d’une règle
    When l’assuré valide
    Then le comportement respecte la règle liée sans décision de garantie
```
**Definition of Done :** critères vérifiables, erreurs accessibles, TC liés exécutés et résultat consigné, documentation à jour, aucune donnée réelle ni appel externe.
