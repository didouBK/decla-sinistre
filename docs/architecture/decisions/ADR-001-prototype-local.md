# ADR-001 — Garder la déclaration sans backend

- **État :** accepté pour le prototype de portfolio
- **Date :** 2026-10-17
- **Décideurs du scénario :** Product Owner et équipe projet fictifs

## Contexte

Le projet illustre un parcours de déclaration d’assurance pour un portfolio. Les écrans utilisent des informations qui ressembleraient à des données personnelles et des justificatifs. Il faut pouvoir montrer le flux sans exposer de vraies données ni prétendre fournir un service de déclaration réel.

## Décision

Le parcours est une application statique HTML/CSS/JavaScript, sans API, compte, base de données ni téléversement. Le suivi est une simulation locale dans `localStorage`; les fichiers sélectionnés ne quittent pas la page. Le dashboard Streamlit sert au pilotage et à la QA uniquement.

## Conséquences positives

- Aucun dossier ou justificatif n’est transmis à un serveur.
- Le prototype se lance facilement sur un poste ou via GitHub Pages.
- Les limites techniques sont visibles et le scénario reste testable par Playwright.

## Conséquences négatives et limites

- L’état est modifiable, effaçable ou isolé par navigateur; il ne représente pas un vrai suivi de dossier.
- Il n’y a ni authentification, ni autorisation, ni persistance serveur, ni notification.
- Les indicateurs métier et règles doivent rester identifiés comme fictifs.

## Options écartées pour ce périmètre

- **Backend de démonstration** : ajouterait une collecte inutile et donnerait une impression de dépôt réel.
- **Base de données / espace assuré** : hors objectif du portfolio et implique des exigences de sécurité, confidentialité et exploitation absentes.
- **Stockage cloud des pièces** : inutile pour illustrer les validations; augmente le risque de données réelles.

## Conditions de réexamen

Réexaminer cette décision si le besoin devient un pilote utilisateur avec de vraies personnes, ou si une organisation demande un dépôt réel. Dans ce cas, cette ADR ne vaut pas approbation de réutiliser le code en production; une architecture, une analyse d’impact, des règles validées et une revue sécurité/accessibilité sont nécessaires.
