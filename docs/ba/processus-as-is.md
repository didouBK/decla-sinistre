# Processus AS-IS

> Mermaid simplifié, pas une modélisation BPMN 2.0. Scénario fictif.

```mermaid
flowchart LR
 subgraph Assuré
 A((Début: dégât))-->B[Appeler et décrire]-->C[Envoyer pièces]-->Z((Attente / fin))
 end
 subgraph Gestionnaire
 D[Saisir manuellement]-->E{Dossier complet?}
 E--Non-->F[Demander compléments]
 E--Oui-->G[Contrôler et qualifier]-->H{Expert utile?}
 F-.relance.->B
 H--Non-->I[Prendre en charge]
 end
 subgraph Expert
 J[Évaluer sur mandat fictif]-->K[Retour au gestionnaire]
 end
 B-.appel.->D
 C-.pièces séparées.->G
 H--Oui-->J
 K-->I-->X((Fin étape))
```

Les ressaisies, pièces séparées et relances peuvent allonger le parcours; aucun résultat réel n’est revendiqué.
