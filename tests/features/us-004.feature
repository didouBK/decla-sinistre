Feature: Contrôles métier et orientation
  Scenario: parcours nominal
    Given des données fictives valides
    When l’assuré complète Contrôles métier et orientation
    Then le résultat attendu s’affiche
  Scenario: donnée requise absente
    Given l’assuré est dans le parcours
    When une donnée obligatoire manque
    Then un message indique la correction
    And la soumission reste bloquée
