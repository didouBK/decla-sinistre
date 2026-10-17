const { test, expect } = require('@playwright/test');

const DAY = 24 * 60 * 60 * 1000;
const dateDaysAgo = days => new Date(Date.now() - days * DAY).toISOString().slice(0, 10);

async function identify(page, contract = 'DEMO-0001') {
  await page.getByLabel('Nom de démonstration').fill('Camille Martin');
  await page.getByLabel('Référence du contrat').fill(contract);
  await page.getByRole('button', { name: 'Continuer →' }).click();
}

async function completeCircumstances(page, { date = dateDaysAgo(1), cause = 'Dégât des eaux accidentel', amount = '1200' } = {}) {
  await page.getByLabel('Date du sinistre').fill(date);
  await page.getByLabel('Adresse du sinistre').fill('12 rue de la Démonstration, Paris');
  await page.locator('#cause').selectOption(cause);
  await page.getByLabel('Estimation indicative').fill(amount);
  await page.getByLabel('Décrivez les circonstances').fill('Une fuite fictive est apparue sous l’évier.');
  await page.getByRole('button', { name: 'Continuer →' }).click();
}

async function reachSummary(page, options) {
  await identify(page);
  await completeCircumstances(page, options);
  await page.getByRole('button', { name: 'Continuer →' }).click();
}

test.beforeEach(async ({ page }) => {
  await page.goto('/');
});

test('[US-001][TC-001] accepter le contrat de démonstration valide', async ({ page }) => {
  await identify(page);
  await expect(page.getByRole('heading', { name: 'Que s’est-il passé ?' })).toBeVisible();
});

test('[US-001][TC-002] orienter une référence de contrat inconnue vers une vérification', async ({ page }) => {
  await page.getByLabel('Nom de démonstration').fill('Camille Martin');
  await page.getByLabel('Référence du contrat').fill('DEMO-0002');
  await page.getByRole('button', { name: 'Continuer →' }).click();
  await expect(page.getByRole('alert')).toContainText('nécessite une vérification humaine');
});

test('[US-002][US-004][TC-003] signaler les informations obligatoires manquantes', async ({ page }) => {
  await page.getByRole('button', { name: 'Continuer →' }).click();
  await expect(page.getByRole('alert')).toContainText('Saisissez un nom de démonstration');
  await expect(page.getByRole('alert')).toContainText('Utilisez la référence fictive DEMO-0001');
});

test('[US-002][TC-004] refuser une date de sinistre future', async ({ page }) => {
  await identify(page);
  await completeCircumstances(page, { date: '2999-12-31' });
  await expect(page.getByRole('alert')).toContainText('La date ne peut pas être dans le futur');
});

test('[US-002][TC-005] refuser une date au-delà de la fenêtre fictive', async ({ page }) => {
  await identify(page);
  await completeCircumstances(page, { date: '2000-01-01' });
  await expect(page.getByRole('alert')).toContainText('fenêtre de 365 jours');
});

test('[US-002][TC-006] orienter une circonstance ambiguë vers une revue humaine', async ({ page }) => {
  await reachSummary(page, { cause: 'Origine incertaine — revue requise' });
  await expect(page.locator('.summary-grid')).toContainText('Une revue humaine serait nécessaire');
});

test('[US-003][TC-007] accepter une pièce jointe au format autorisé', async ({ page }) => {
  await identify(page);
  await completeCircumstances(page);
  await page.getByLabel('Photos et justificatifs').setInputFiles({
    name: 'photo-fictive.png',
    mimeType: 'image/png',
    buffer: Buffer.from('image de démonstration'),
  });
  await expect(page.locator('#filelist')).toContainText('photo-fictive.png');
  await page.getByRole('button', { name: 'Continuer →' }).click();
  await expect(page.getByRole('heading', { name: 'Vérifiez votre déclaration' })).toBeVisible();
});

test('[US-003][TC-008] refuser un fichier trop volumineux', async ({ page }) => {
  await identify(page);
  await completeCircumstances(page);
  await page.getByLabel('Photos et justificatifs').setInputFiles({
    name: 'trop-grand.jpg',
    mimeType: 'image/jpeg',
    buffer: Buffer.alloc(11 * 1024 * 1024),
  });
  await expect(page.locator('#filelist')).toContainText('Fichier refusé');
});

test('[US-002][TC-009] refuser une estimation négative', async ({ page }) => {
  await identify(page);
  await completeCircumstances(page, { amount: '-1' });
  await expect(page.getByRole('alert')).toContainText('entre 0 et 100 000 €');
});

test('[US-002][TC-010] refuser une estimation au-dessus du plafond fictif', async ({ page }) => {
  await identify(page);
  await completeCircumstances(page, { amount: '100001' });
  await expect(page.getByRole('alert')).toContainText('entre 0 et 100 000 €');
});

test('[US-004][TC-011] proposer une expertise à partir du seuil illustratif', async ({ page }) => {
  await reachSummary(page, { amount: '5000' });
  await expect(page.locator('.summary-grid')).toContainText('Expertise à étudier (seuil fictif)');
});

test('[US-005][TC-012] relire puis confirmer une déclaration fictive', async ({ page }) => {
  await reachSummary(page);
  await expect(page.locator('.summary-grid')).toContainText('Camille Martin');
  await page.getByRole('button', { name: 'Précédent' }).click();
  await page.getByRole('button', { name: 'Précédent' }).click();
  await expect(page.getByLabel('Décrivez les circonstances')).toHaveValue('Une fuite fictive est apparue sous l’évier.');
  await page.getByLabel('Décrivez les circonstances').fill('La description a été corrigée dans la démonstration.');
  await page.getByRole('button', { name: 'Continuer →' }).click();
  await page.getByRole('button', { name: 'Continuer →' }).click();
  await expect(page.locator('.summary-grid')).toContainText('La description a été corrigée dans la démonstration.');
  await page.getByRole('button', { name: 'Confirmer la simulation' }).click();
  await expect(page.getByRole('heading', { name: 'Votre déclaration est prête' })).toBeVisible();
  await expect(page.locator('.summary-grid')).toContainText(/DS-DEMO-\d{6}/);
});

test('[US-006][US-007][TC-012] enregistrer une référence et afficher la confirmation', async ({ page }) => {
  await reachSummary(page);
  await page.getByRole('button', { name: 'Confirmer la simulation' }).click();
  await expect(page.getByRole('heading', { name: 'Votre déclaration est prête' })).toBeVisible();
  const saved = await page.evaluate(() => JSON.parse(localStorage.getItem('decla-status')));
  expect(saved.status).toBe('Déposé — simulation');
  expect(saved.ref).toMatch(/^DS-DEMO-\d{6}$/);
});

test('[US-008][TC-013] conserver le statut local fictif après le dépôt', async ({ page }) => {
  await reachSummary(page);
  await page.getByRole('button', { name: 'Confirmer la simulation' }).click();
  await expect(page.locator('.summary-grid')).toContainText('Déposé — simulation locale');
  const saved = await page.evaluate(() => JSON.parse(localStorage.getItem('decla-status')));
  expect(saved.status).toBe('Déposé — simulation');
  await page.getByRole('button', { name: 'Suivre une déclaration' }).click();
  await expect(page.getByRole('dialog')).toContainText('Statut de la déclaration');
  await expect(page.getByRole('dialog')).toContainText('Déposé — simulation');
});

test('[US-001..US-008][TC-014] ne transmettre aucune requête à un service tiers', async ({ page }) => {
  const externalRequests = [];
  page.on('request', request => {
    if (new URL(request.url()).origin !== 'http://127.0.0.1:4173') externalRequests.push(request.url());
  });
  await page.reload();
  await identify(page);
  await completeCircumstances(page);
  await page.getByRole('button', { name: 'Continuer →' }).click();
  await page.getByRole('button', { name: 'Confirmer la simulation' }).click();
  await expect(page.getByRole('heading', { name: 'Votre déclaration est prête' })).toBeVisible();
  expect(externalRequests).toEqual([]);
});
