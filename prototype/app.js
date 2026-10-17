const labels = ['Identification', 'Circonstances', 'Justificatifs', 'Récapitulatif', 'Confirmation'];
let step = 0;
const d = {};
const $ = selector => document.querySelector(selector);
const esc = value => String(value ?? '').replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));

function nav() {
  $('#steps').innerHTML = labels.map((label, index) => {
    const status = index < step ? 'done' : index === step ? 'active' : '';
    const number = index < step ? '✓' : index + 1;
    return `<li class="${status}" ${index === step ? 'aria-current="step"' : ''}><span class="step-number" aria-hidden="true">${number}</span><span>${label}</span></li>`;
  }).join('');
}

function field(id, label, value, options = {}) {
  const {type = 'text', placeholder = '', hint = '', full = false, required = true, max = '', min = ''} = options;
  const input = type === 'textarea'
    ? `<textarea id="${id}" name="${id}" ${required ? 'required' : ''} placeholder="${esc(placeholder)}">${esc(value)}</textarea>`
    : `<input id="${id}" name="${id}" type="${type}" value="${esc(value)}" ${required ? 'required' : ''} ${placeholder ? `placeholder="${esc(placeholder)}"` : ''} ${min !== '' ? `min="${min}"` : ''} ${max !== '' ? `max="${max}"` : ''}>`;
  return `<label class="field-label ${full ? 'field-full' : ''}" for="${id}">${label}${input}${hint ? `<span class="field-hint">${hint}</span>` : ''}</label>`;
}

function optionField(id, label, value, options) {
  const choices = options.map(option => `<option value="${esc(option.value)}" ${value === option.value ? 'selected' : ''}>${esc(option.label)}</option>`).join('');
  return `<label class="field-label" for="${id}">${label}<select id="${id}" name="${id}" required><option value="">Choisir une option</option>${choices}</select></label>`;
}

function summaryItem(label, value) {
  return `<div class="summary-item"><span>${label}</span><strong>${esc(value || 'Non renseigné')}</strong></div>`;
}

function render() {
  nav();
  let content = '';
  if (step === 0) content = `<h2>Commençons par vous identifier</h2><p class="form-lead">Les informations ci-dessous sont des exemples. Utilisez uniquement les données de démonstration.</p><div class="field-grid">${field('name','Nom de démonstration',d.name,{placeholder:'Ex. Camille Martin'})}${field('contract','Référence du contrat',d.contract,{placeholder:'DEMO-0001',hint:'Format de démonstration : DEMO-0001'})}</div><div class="callout">Aucune vérification de contrat réel n’est effectuée dans ce prototype.</div><div id="err" role="alert"></div>`;
  if (step === 1) content = `<h2>Que s’est-il passé ?</h2><p class="form-lead">Quelques détails nous aideront à illustrer la suite du parcours.</p><div class="field-grid">${field('date','Date du sinistre',d.date,{type:'date'})}${field('address','Adresse du sinistre',d.address,{placeholder:'Adresse fictive'})}${optionField('cause','Circonstances',d.cause,[{value:'Dégât des eaux accidentel',label:'Dégât des eaux accidentel'},{value:'Origine incertaine — revue requise',label:'Origine incertaine'}])}${field('amount','Estimation indicative',d.amount,{type:'number',placeholder:'Ex. 1200',min:0,max:100000,hint:'Montant en euros, estimation fictive'})}${field('desc','Décrivez les circonstances',d.desc,{type:'textarea',placeholder:'Expliquez brièvement ce qui s’est passé…',full:true})}</div><div id="err" role="alert"></div>`;
  if (step === 2) content = `<h2>Ajoutez vos justificatifs</h2><p class="form-lead">Vous pouvez joindre des images ou documents fictifs pour parcourir cette étape.</p><label class="field-label field-full" for="files">Photos et justificatifs<input id="files" name="files" type="file" accept="image/jpeg,image/png,application/pdf" multiple><span class="field-hint">JPG, PNG ou PDF · 10 Mo maximum par fichier · 30 Mo au total</span></label><div id="filelist" class="callout">${esc(d.files || 'Aucune pièce sélectionnée')}</div><div class="callout">Cette démonstration ne téléverse aucun fichier. Vous pouvez aussi poursuivre sans justificatif.</div>`;
  if (step === 3) {
    const route = d.cause?.startsWith('Origine') ? 'Une revue humaine serait nécessaire' : (+d.amount >= 5000 ? 'Expertise à étudier (seuil fictif)' : 'Qualification par un gestionnaire');
    d.route = route;
    content = `<h2>Vérifiez votre déclaration</h2><p class="form-lead">Prenez un instant pour relire les informations avant de confirmer la simulation.</p><div class="summary-grid">${summaryItem('Nom',d.name)}${summaryItem('Référence du contrat',d.contract)}${summaryItem('Date du sinistre',d.date)}${summaryItem('Adresse',d.address)}${summaryItem('Circonstances',d.cause)}${summaryItem('Estimation indicative',d.amount ? `${d.amount} €` : '')}${summaryItem('Justificatifs',d.files)}${summaryItem('Orientation simulée',route)}</div><div class="callout">En continuant, vous créez une confirmation fictive dans ce navigateur. Aucun dossier n’est transmis.</div><div id="err" role="alert"></div>`;
  }
  if (step === 4) content = `<div class="confirmation-mark" aria-hidden="true">✓</div><p class="eyebrow">SIMULATION TERMINÉE</p><h2>Votre déclaration est prête</h2><p class="form-lead">Le parcours a abouti. Aucun gestionnaire réel n’a reçu cette déclaration.</p><div class="summary-grid">${summaryItem('Référence de démonstration',d.ref)}${summaryItem('Statut','Déposé — simulation locale')}${summaryItem('Orientation',d.route)}</div><div class="callout">Vous pouvez recommencer pour explorer le parcours avec d’autres données fictives.</div>`;

  $('#screen').innerHTML = content;
  $('#screen').classList.toggle('confirmation-card', step === 4);
  if (step !== 4) $('#screen').insertAdjacentHTML('beforeend', `<div class="form-actions"><button class="button button-secondary" id="prev" type="button" ${step === 0 ? 'disabled' : ''}>← Précédent</button><button class="button button-primary" id="next" type="button">${step === 3 ? 'Confirmer la simulation' : 'Continuer →'}</button></div>`);
  else $('#screen').insertAdjacentHTML('beforeend', '<div class="form-actions"><button class="button button-secondary" id="restart" type="button">Recommencer la démonstration</button></div>');
  bind();
}

function save() {
  ['name','contract','date','address','cause','desc','amount'].forEach(key => {
    const element = document.getElementById(key);
    if (element) d[key] = element.value;
  });
}

function validate() {
  save();
  const messages = [];
  if (step === 0) {
    if (!d.name?.trim()) messages.push('Saisissez un nom de démonstration.');
    if (!/^DEMO-\d{4}$/.test(d.contract || '')) messages.push('Utilisez la référence fictive DEMO-0001.');
    else if (d.contract !== 'DEMO-0001') messages.push('Cette référence fictive nécessite une vérification humaine.');
  }
  if (step === 1) {
    if (!d.date || !d.address || !d.cause || !d.desc?.trim() || d.amount === '') messages.push('Complétez tous les champs requis.');
    if (d.date && new Date(`${d.date}T00:00:00`) > new Date()) messages.push('La date ne peut pas être dans le futur.');
    if (d.date && (Date.now() - new Date(`${d.date}T00:00:00`).getTime()) > 365 * 86400000) messages.push('La fenêtre de 365 jours est une hypothèse de démonstration.');
    if (+d.amount < 0 || +d.amount > 100000) messages.push('Le montant doit se situer entre 0 et 100 000 €.');
  }
  return messages;
}

function bind() {
  const fileInput = $('#files');
  if (fileInput) fileInput.onchange = () => {
    const files = [...fileInput.files];
    const invalid = files.some(file => !['image/jpeg','image/png','application/pdf'].includes(file.type) || file.size > 10 * 1024 * 1024) || files.reduce((sum,file) => sum + file.size,0) > 30 * 1024 * 1024;
    if (invalid) {
      $('#filelist').innerHTML = '<span class="error">Fichier refusé. Formats acceptés : JPG, PNG ou PDF, 10 Mo chacun et 30 Mo au total.</span>';
      d.files = '';
    } else {
      d.files = files.map(file => file.name).join(', ');
      $('#filelist').textContent = d.files || 'Aucune pièce sélectionnée';
    }
  };
  const previous = $('#prev');
  const next = $('#next');
  const restart = $('#restart');
  if (previous) previous.onclick = () => { save(); step = Math.max(0,step - 1); render(); };
  if (restart) restart.onclick = () => { step = 0; Object.keys(d).forEach(key => delete d[key]); render(); window.scrollTo({top:0,behavior:'smooth'}); };
  if (next) next.onclick = () => {
    const errors = validate();
    if (errors.length) {
      $('#err').innerHTML = `<div class="error">${errors.map(esc).join('<br>')}</div>`;
      $('#err').focus?.();
      return;
    }
    if (step === 3) {
      d.ref = `DS-DEMO-${String(Math.floor(Math.random() * 900000) + 100000)}`;
      try { localStorage.setItem('decla-status',JSON.stringify({ref:d.ref,status:'Déposé — simulation'})); } catch {}
      step = 4;
    } else step += 1;
    render();
    window.scrollTo({top:0,behavior:'smooth'});
  };
}

function bindTracking() {
  const dialog = $('#tracking-dialog');
  const reference = $('#tracking-reference');
  const result = $('#tracking-result');
  const savedStatus = () => {
    try { return JSON.parse(localStorage.getItem('decla-status') || 'null'); }
    catch { return null; }
  };
  const displayStatus = value => {
    const saved = savedStatus();
    if (!saved || saved.ref !== value.trim()) {
      result.innerHTML = '<p class="error">Aucune déclaration de démonstration ne correspond à cette référence dans ce navigateur.</p>';
      return;
    }
    result.innerHTML = `<div class="tracking-success"><span>Statut de la déclaration</span><strong>${esc(saved.status)}</strong><small>Référence ${esc(saved.ref)} · Donnée fictive enregistrée localement</small></div>`;
  };
  $('#tracking-trigger').onclick = () => {
    const saved = savedStatus();
    reference.value = saved?.ref || '';
    result.innerHTML = saved ? '' : '<p class="callout">Aucun dépôt fictif n’a encore été enregistré dans ce navigateur.</p>';
    if (saved) displayStatus(saved.ref);
    dialog.showModal();
    reference.focus();
  };
  $('#tracking-close').onclick = () => dialog.close();
  $('#tracking-form').onsubmit = event => {
    event.preventDefault();
    displayStatus(reference.value);
  };
}

bindTracking();
render();
