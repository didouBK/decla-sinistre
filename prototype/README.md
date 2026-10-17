# Prototype DéclaSinistre

Ouvrir index.html dans un navigateur moderne, ou lancer python3 -m http.server 8000 depuis ce dossier et visiter http://localhost:8000. Le parcours comporte cinq étapes, des validations locales, un récapitulatif modifiable, des justificatifs non transmis et une référence fictive. Le bouton « Suivre une déclaration » consulte le dernier dépôt conservé dans le stockage local du navigateur. Les données sont fictives; ne saisir aucune donnée personnelle.

Les tests navigateur reliés aux TC/US sont décrits dans `tests/e2e/prototype.spec.js` et se lancent depuis la racine du dépôt avec `npm ci`, `npx playwright install chromium`, puis `npm run test:e2e`.
