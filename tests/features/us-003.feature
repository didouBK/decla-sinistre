Feature: Photos et justificatifs
  Scenario: parcours nominal
    Given des données fictives valides
    When l’assuré complète Photos et justificatifs
    Then le résultat attendu s’affiche
  Scenario: donnée requise absente
    Given l’assuré est dans le parcours
    When une donnée obligatoire manque
    Then un message indique la correction
    And la soumission reste bloquée
