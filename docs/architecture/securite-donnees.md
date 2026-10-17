# Sécurité, données et limites de la démonstration

> Revue de conception au 17 octobre 2026. Ce document ne constitue ni une analyse juridique, ni une homologation sécurité, ni une AIPD/RGPD.

## Classification des données

| Élément | Démonstration | Emplacement / durée | À faire en production |
|---|---|---|---|
| Identité, adresse, contrat | Valeurs fictives uniquement | État mémoire de la page; non envoyées | Authentification, contrôle d’accès, minimisation, règles de conservation |
| Référence et statut | Générés pour la simulation | `localStorage` du navigateur jusqu’à suppression des données locales | Référence serveur non devinable, accès après authentification, journal d’événements |
| Justificatifs | Fichiers de test uniquement | Le prototype vérifie format et taille; aucun envoi | Stockage isolé et chiffré, analyse antivirus, contrôle d’accès, suppression et preuve d’accès |
| Résultats de test | Résultats fictifs | Session Streamlit; les rapports CI ont une durée de rétention configurée | Stockage pérenne adapté, rôles et rétention définis si nécessaire |

## Menaces et mesures présentes

| Menace | Mesure dans le prototype | Risque restant |
|---|---|---|
| Saisie de données personnelles réelles dans la démo | Mentions « cas fictif » et « aucune transmission » dans les écrans | La mention ne peut empêcher un utilisateur d’entrer une vraie donnée |
| Téléversement accidentel de justificatifs | Aucun endpoint d’upload; validation locale type/taille | Le navigateur peut lire les métadonnées nécessaires à l’interface; ne pas choisir de vrai document |
| Référence supposée être un vrai dossier | Préfixes et statuts de simulation; pas de backend | `localStorage` est modifiable et ne doit jamais être interprété comme une preuve |
| Décision métier automatisée à tort | L’ambiguïté est orientée vers une revue humaine; seuils signalés comme fictifs | Les règles ne sont pas validées par un assureur |
| Dépendance compromise | Dépendances de test verrouillées par `package-lock.json`; CI GitHub | Pas de SBOM, signature de build ou contrôle complet de chaîne logicielle |
| Défaut d’accessibilité ou rendu mobile | Maquettes et tests fonctionnels; styles responsive | Audit WCAG et tests sur appareil réel non réalisés |

## Exigences de sécurité avant production

- Concevoir un modèle de menace et des rôles, puis tester l’autorisation côté serveur.
- Décider du fournisseur d’identité, MFA pour les rôles sensibles, gestion des sessions et révocation.
- Chiffrer les données en transit et au repos; isoler les pièces; définir les clés et rotations.
- Définir minimisation, base légale, information, conservation, effacement, export et procédure d’incident avec les fonctions responsables.
- Ajouter journalisation protégée contre l’altération, alertes, sauvegardes, restauration et tests de reprise.
- Analyser les pièces jointes et limiter les types réellement autorisés côté serveur.
- Effectuer revue de dépendances, SBOM, analyse statique/dynamique et test d’intrusion selon le contexte.
- Faire valider le parcours et les messages par les responsables métier, juridique, sécurité et accessibilité.

## Comportements explicitement interdits pour la démo

- Ne pas saisir de nom, adresse, contrat ou sinistre réels.
- Ne pas sélectionner un document personnel, même pour « essayer » l’ajout de pièce.
- Ne pas présenter la référence locale comme un numéro de dossier opposable.
- Ne pas utiliser les seuils du référentiel comme consigne opérationnelle.

## État de conformité

Le dépôt décrit et démontre des garde-fous de conception; il ne prétend pas être conforme à un référentiel de sécurité, à WCAG ou aux obligations applicables à un assureur. Une évaluation formelle est un prérequis distinct pour une mise en production.
