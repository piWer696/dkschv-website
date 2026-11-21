/* ==============================================================================
   DKSchV.CH // Cyber-Security Shop Logic, Legal Compliance & Express Buy
   ============================================================================== */

const PRODUCTS = {
  notfallplan: {
    id: "notfallplan",
    title: "Schweizer KMU Cyber-Notfallplan & Ransomware-Runbook",
    price: 89,
    oldPrice: 149,
    fileMd: "01_Schweizer_KMU_Cyber_Notfallplan_Runbook.md",
    fileHtml: "01_Schweizer_KMU_Cyber_Notfallplan_Runbook.html",
    previewHtml: `
      <h2>1. Sofortmassnahmen bei Ransomware / Einbruch (Die ersten 15 Minuten)</h2>
      <p style="color:#fb7185; font-weight:600; margin-bottom:0.5rem;">⚠️ OBERSTE REGEL: GERÄTE NICHT NEUSTARTEN ODER AUSSCHALTEN (RAM-Forensik sichern)!</p>
      <ul>
        <li><strong>Netzwerk physisch trennen:</strong> LAN-Kabel an allen Servern, PCs & NAS sofort ziehen. WLAN kappen.</li>
        <li><strong>Backups schützen:</strong> USB-Laufwerke abziehen, Immutable S3 Cloud-Schreibzugriffe sperren.</li>
        <li><strong>Sessions beenden:</strong> In M365 / Google Workspace Admin "Revoke all sessions" auslösen.</li>
      </ul>
      <h2>2. Schweizer Behörden & Meldepflichten</h2>
      <ul>
        <li><strong>BACS (Bundesamt für Cybersicherheit):</strong> Meldung schwerwiegender Angriffe via Meldeportal bacs.admin.ch.</li>
        <li><strong>EDÖB (Datenschutz):</strong> Meldepflicht nach Art. 24 nDSG bei hohem Risiko innert 72 Stunden.</li>
        <li><strong>Kantonspolizei Wallis / Cybercrime:</strong> Strafanzeige & Spurensicherung vor Löschungen.</li>
      </ul>
      <h2>3. Enthaltene Muster-Texte & Druckansicht</h2>
      <p>Inklusive fixfertiger E-Mail-Vorlagen für Belegschaft und Kunden sowie druckfertiger Schweizer A4-PDF-Ansicht.</p>
    `
  },
  ndsg: {
    id: "ndsg",
    title: "Schweizer nDSG-Compliance-Paket (VdT, TOM & ADV)",
    price: 149,
    oldPrice: 249,
    fileMd: "02_Schweizer_nDSG_Datenschutz_Paket_TOM_VdT.md",
    fileHtml: "02_Schweizer_nDSG_Datenschutz_Paket_TOM_VdT.html",
    previewHtml: `
      <h2>1. Verzeichnis der Bearbeitungstätigkeiten (Art. 12 nDSG)</h2>
      <p>Vollständig ausgefüllte Schweizer Praxistabelle mit Kategorien für Personalwesen (HR), CRM, E-Commerce und Videoüberwachung.</p>
      <h2>2. Technischer & Organisatorischer Massnahmenkatalog (TOM nach Art. 8 nDSG)</h2>
      <ul>
        <li><strong>Vertraulichkeit:</strong> 2FA-Zwang, Least-Privilege-Berechtigungskonzept, Passwortmanager-Standard.</li>
        <li><strong>Integrität:</strong> BitLocker/FileVault Vollverschlüsselung (AES-256), TLS 1.3 Datentransfers.</li>
        <li><strong>Verfügbarkeit:</strong> 3-2-1-1-0 Backup-Strategie mit unveränderbaren (Immutable) Kopien in Schweizer Rechenzentren.</li>
      </ul>
      <h2>3. Auftragsbearbeitungsvertrag (ADV nach Art. 9 nDSG)</h2>
      <p>Rechtssicherer Mustervertrag für die Beauftragung externer IT-Dienstleister, Webhoster und Cloud-Anbieter.</p>
    `
  },
  audit: {
    id: "audit",
    title: "KMU IT-Sicherheits-Audit & Baseline-Prüfprotokoll",
    price: 59,
    oldPrice: 89,
    fileMd: "03_KMU_IT_Sicherheits_Audit_Checkliste.md",
    fileHtml: "03_KMU_IT_Sicherheits_Audit_Checkliste.html",
    previewHtml: `
      <h2>1. 5 Audit-Module mit 75+ Kontrollpunkten</h2>
      <ul>
        <li><strong>Modul 1 (IAM):</strong> Multi-Faktor-Authentifizierung, Passwort-Policies, Admin-Trennung, Offboarding-Checks.</li>
        <li><strong>Modul 2 (Netzwerk & Perimeter):</strong> Port-Scanning (RDP/SMB Sperren), VLAN-Segmentierung, VPN-Härtung.</li>
        <li><strong>Modul 3 (Clients & Härtung):</strong> BitLocker, EDR/Antivirus-Status, automatisiertes Patching, Entzug lokaler Adminrechte.</li>
        <li><strong>Modul 4 (Backup & Notfall):</strong> Immutability, Air-Gapped Offsite-Kopie, dokumentierte Restore-Tests, RPO/RTO.</li>
        <li><strong>Modul 5 (Mitarbeiter & Awareness):</strong> Phishing-Simulationen, Meldewege, 4-Augen-Prinzip gegen CEO-Fraud.</li>
      </ul>
      <h2>2. Management Summary & Ampelsystem</h2>
      <p>Vorgefertigte Executive-Vorlage zur Präsentation des Sicherheitsstatus vor der Geschäftsleitung.</p>
    `
  },
  policy: {
    id: "policy",
    title: "Mitarbeiter IT-Sicherheits- & KI-Nutzungsrichtlinie",
    price: 49,
    oldPrice: 79,
    fileMd: "04_Mitarbeiter_IT_Sicherheitsrichtlinie_KI_Policy.md",
    fileHtml: "04_Mitarbeiter_IT_Sicherheitsrichtlinie_KI_Policy.html",
    previewHtml: `
      <h2>1. Klare Richtlinie für Generative KI (ChatGPT, Copilot, DeepL)</h2>
      <p style="color:#fb7185;">Strikte Regeln zum Schutz vor Abfluss von Betriebsgeheimnissen und Kundendaten nach Schweizer nDSG.</p>
      <h2>2. Passwort- & 2FA-Disziplin</h2>
      <ul>
        <li>Mindestens 14 Zeichen oder 4-Wort-Passphrase.</li>
        <li>Verbot der Weitergabe von Anmeldedaten.</li>
        <li>Verhalten bei unaufgeforderten Push-MFA-Meldungen (MFA-Fatigue-Schutz).</li>
      </ul>
      <h2>3. Home-Office & Clean-Desk</h2>
      <p>Bildschirmsperre bei Verlassen des Platzes, VPN-Zwang im Zug/Hotel, Verbot privater Nutzung von Arbeitsgeräten.</p>
      <h2>4. Rechtsverbindliche Verpflichtungserklärung</h2>
      <p>Unterschriftsreife Erklärung als Anhang zum Schweizer Arbeitsvertrag für die Personalakte.</p>
    `
  },
  bundle: {
    id: "bundle",
    title: "All-in-One Cyber-Resilienz Komplettpaket",
    price: 249,
    oldPrice: 566,
    fileMd: "bundle",
    previewHtml: `
      <h2>Enthält alle 4 Premium-Vorlagen (-56% Launch-Rabatt):</h2>
      <ol style="padding-left:1.5rem; line-height:1.8;">
        <li><strong>Cyber-Notfallplan & Ransomware-Runbook</strong> (Aktion: CHF 89.– / Regulär: CHF 149.–)</li>
        <li><strong>Schweizer nDSG-Compliance-Paket</strong> (Aktion: CHF 149.– / Regulär: CHF 249.–)</li>
        <li><strong>KMU IT-Sicherheits-Audit Protokoll</strong> (Aktion: CHF 59.– / Regulär: CHF 89.–)</li>
        <li><strong>Mitarbeiter IT- & KI-Richtlinie</strong> (Aktion: CHF 49.– / Regulär: CHF 79.–)</li>
      </ol>
      <p style="margin-top:1rem; color:#34d399; font-weight:700;">✓ Inklusive aller bearbeitbaren Quelldateien (.md) und druckfertiger A4-PDF-Versionen.</p>
    `
  }
};

const LEGAL_TEXTS = {
  agb: {
    title: "Allgemeine Geschäfts- & Lizenzbedingungen (AGB)",
    html: `
      <h2>1. Geltungsbereich & Vertragsgegenstand</h2>
      <p>Diese AGB gelten für den Erwerb digitaler Fachvorlagen, Runbooks und Dokumente über den Online-Shop von <strong>DKSchV Schweiz (DKSchV Dini, Naters, Wallis)</strong>.</p>
      <h2>2. Lizenz- & Nutzungsrechte</h2>
      <p>Mit der vollständigen Bezahlung erhält der Erwerber eine zeitlich und räumlich unbeschränkte, einfache Lizenz zur unternehmensinternen Nutzung der Vorlagen für das eigene Unternehmen. Die Weitergabe, der Wiederverkauf oder das öffentliche Bereitstellen der Vorlagen an Dritte ist untersagt.</p>
      <h2>3. Ausschluss des Widerrufsrechts bei digitalen Gütern</h2>
      <p>Gemäß Schweizer Obligationenrecht (OR) sowie internationalem Standard für digitale Inhalte stimmt der Kunde ausdrücklich zu, dass die Bereitstellung des digitalen Downloads unmittelbar nach erfolgreicher Autorisierung der Zahlung erfolgt. Das Widerrufsrecht erlischt mit Beginn des Downloads.</p>
      <h2>4. Haftungsausschluss</h2>
      <p>Die Vorlagen wurden von praxiserfahrenen Schweizer Cyber-Security- und Datenschutzexperten mit größter Sorgfalt erstellt. Sie dienen als praxiserprobte Arbeitsgrundlage und ersetzen keine individuelle Rechts- oder Steuerberatung. DKSchV haftet nicht für Folgeschäden aus fehlerhafter betrieblicher Umsetzung.</p>
    `
  },
  privacy: {
    title: "Datenschutzerklärung nach Schweizer nDSG",
    html: `
      <h2>1. Verantwortliche Stelle</h2>
      <p>DKSchV Dini, Bammattenweg 19, CH-3904 Naters (Wallis), E-Mail: info@dkschv.ch, Tel: +41 79 844 66 69.</p>
      <h2>2. Erhebung & Bearbeitung von Bestelldaten</h2>
      <p>Zur Abwicklung Ihrer Bestellung erheben wir Ihre E-Mail-Adresse und Rechnungsangaben. Die Zahlungsabwicklung erfolgt verschlüsselt über den zertifizierten Zahlungsdienstleister Stripe Payments Europe Ltd. Es werden keine vollständigen Kreditkartendaten auf unseren Servern gespeichert.</p>
      <h2>3. Ihre Rechte nach nDSG (Art. 25 ff.)</h2>
      <p>Sie haben jederzeit das Recht auf unentgeltliche Auskunft über Ihre gespeicherten Daten sowie auf Berichtigung oder Löschung, soweit keine gesetzlichen handelsrechtlichen Aufbewahrungspflichten (10 Jahre nach OR 962) entgegenstehen.</p>
    `
  },
  imprint: {
    title: "Impressum & Anbieterkennzeichnung",
    html: `
      <h2>Angaben gemäss Schweizer Recht</h2>
      <p><strong>DKSchV Schweiz</strong> (DKSchV Dini)<br>
      Cyber-Security, Penetration Testing & Datenschutzberatung<br>
      Bammattenweg 19<br>
      CH-3904 Naters (Kanton Wallis), Schweiz</p>
      <p><strong>Kontakt:</strong><br>
      Telefon (Notfälle / Anfragen): +41 79 844 66 69<br>
      E-Mail: info@dkschv.ch<br>
      Website: https://dkschv.ch</p>
      <p><strong>Rechtsform:</strong> Einzelunternehmen nach Schweizer Recht</p>
    `
  }
};

let cart = [];

document.addEventListener("DOMContentLoaded", () => {
  loadCartFromStorage();
  updateCartUI();
});

function loadCartFromStorage() {
  try {
    const saved = localStorage.getItem("dkschv_cart");
    if (saved) cart = JSON.parse(saved);
  } catch (e) {
    cart = [];
  }
}

function saveCartToStorage() {
  try {
    localStorage.setItem("dkschv_cart", JSON.stringify(cart));
  } catch (e) {}
}

function addToCart(id, title, price, oldPrice = price) {
  const existing = cart.find(item => item.id === id);
  if (existing) {
    existing.qty += 1;
  } else {
    cart.push({ id, title, price, oldPrice, qty: 1 });
  }
  saveCartToStorage();
  updateCartUI();
  openCart();
}

// 1-Klick-Sofortkauf (Express Checkout)
function expressCheckout(id, title, price, oldPrice = price) {
  cart = [{ id, title, price, oldPrice, qty: 1 }];
  saveCartToStorage();
  updateCartUI();
  openCart();
}

function removeFromCart(id) {
  cart = cart.filter(item => item.id !== id);
  saveCartToStorage();
  updateCartUI();
}

function updateCartUI() {
  const badge = document.getElementById("cartCount");
  const list = document.getElementById("cartItemsList");
  const total = document.getElementById("cartTotalPrice");
  const savingsRow = document.getElementById("cartSavingsRow");
  const savingsPrice = document.getElementById("cartSavingsPrice");
  
  const totalQty = cart.reduce((sum, item) => sum + item.qty, 0);
  const totalPrice = cart.reduce((sum, item) => sum + (item.price * item.qty), 0);
  const totalOriginalPrice = cart.reduce((sum, item) => sum + ((item.oldPrice || item.price) * item.qty), 0);
  const totalSavings = totalOriginalPrice - totalPrice;
  
  if (badge) badge.textContent = totalQty;
  if (total) total.textContent = `CHF ${totalPrice}.–`;
  
  if (savingsRow && savingsPrice) {
    if (totalSavings > 0) {
      savingsRow.style.display = "flex";
      savingsPrice.textContent = `- CHF ${totalSavings}.–`;
    } else {
      savingsRow.style.display = "none";
    }
  }
  
  if (!list) return;
  
  if (cart.length === 0) {
    list.innerHTML = `
      <div style="text-align: center; color: var(--text-dim); margin-top: 3rem;">
        <i class="fa-solid fa-cart-shopping" style="font-size: 2.5rem; margin-bottom: 1rem; opacity: 0.3;"></i>
        <p>Ihr Warenkorb ist leer.</p>
      </div>
    `;
    const checkoutBtn = document.getElementById("checkoutBtn");
    if (checkoutBtn) checkoutBtn.disabled = true;
  } else {
    list.innerHTML = cart.map(item => `
      <div class="cart-item">
        <div>
          <div class="cart-item-title">${item.title}</div>
          <div class="cart-item-price-wrap">
            ${item.oldPrice && item.oldPrice > item.price ? `<span class="cart-item-old-price">CHF ${item.oldPrice}.–</span>` : ''}
            <span class="cart-item-price">CHF ${item.price}.– ${item.qty > 1 ? `(x${item.qty})` : ''}</span>
          </div>
        </div>
        <button class="cart-item-remove" onclick="removeFromCart('${item.id}')" title="Entfernen">
          <i class="fa-solid fa-trash-can"></i>
        </button>
      </div>
    `).join("");
    const checkoutBtn = document.getElementById("checkoutBtn");
    if (checkoutBtn) checkoutBtn.disabled = false;
  }
}

function toggleCart() {
  const drawer = document.getElementById("cartModal");
  const backdrop = document.getElementById("modalBackdrop");
  if (drawer.classList.contains("open")) {
    drawer.classList.remove("open");
    backdrop.style.display = "none";
  } else {
    drawer.classList.add("open");
    backdrop.style.display = "block";
  }
}

function openCart() {
  const drawer = document.getElementById("cartModal");
  const backdrop = document.getElementById("modalBackdrop");
  drawer.classList.add("open");
  backdrop.style.display = "block";
}

function openPreview(id) {
  const prod = PRODUCTS[id];
  if (!prod) return;
  
  document.getElementById("modalTitle").textContent = prod.title;
  document.getElementById("modalBody").innerHTML = prod.previewHtml;
  
  const buyBtn = document.getElementById("modalBuyBtn");
  buyBtn.innerHTML = `<i class="fa-solid fa-cart-plus"></i> Für CHF ${prod.price}.– in den Korb`;
  buyBtn.onclick = () => {
    addToCart(prod.id, prod.title, prod.price, prod.oldPrice);
    closePreview();
  };
  
  document.getElementById("previewModal").style.display = "flex";
  document.getElementById("modalBackdrop").style.display = "block";
}

function closePreview() {
  document.getElementById("previewModal").style.display = "none";
  document.getElementById("modalBackdrop").style.display = "none";
}

function openLegal(type) {
  const data = LEGAL_TEXTS[type];
  if (!data) return;
  document.getElementById("legalTitle").textContent = data.title;
  document.getElementById("legalBody").innerHTML = data.html;
  document.getElementById("legalModal").style.display = "flex";
  document.getElementById("modalBackdrop").style.display = "block";
}

function closeLegal() {
  document.getElementById("legalModal").style.display = "none";
  document.getElementById("modalBackdrop").style.display = "none";
}

function closeAllModals() {
  document.getElementById("previewModal").style.display = "none";
  document.getElementById("legalModal").style.display = "none";
  document.getElementById("cartModal").classList.remove("open");
  document.getElementById("successModal").style.display = "none";
  document.getElementById("modalBackdrop").style.display = "none";
}

function closeSuccessModal() {
  document.getElementById("successModal").style.display = "none";
  document.getElementById("modalBackdrop").style.display = "none";
}

// Stripe Checkout Logik
function startStripeCheckout() {
  if (cart.length === 0) return;
  
  const agbCheck = document.getElementById("agbCheck");
  if (agbCheck && !agbCheck.checked) {
    alert("Bitte bestätigen Sie die AGB & Lizenzbedingungen für digitale Güter vor dem Kauf.");
    return;
  }
  
  const btn = document.getElementById("checkoutBtn");
  const originalText = btn.innerHTML;
  btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Stripe Checkout wird vorbereitet...`;
  btn.disabled = true;

  // Anfrage an Backend senden
  fetch("/api/create-checkout", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ items: cart })
  })
  .then(res => res.json())
  .then(data => {
    btn.innerHTML = originalText;
    btn.disabled = false;
    toggleCart();
    showSuccessDownloadModal(data.tokens || {});
  })
  .catch(err => {
    // Fallback bei statischem Hosting
    btn.innerHTML = originalText;
    btn.disabled = false;
    toggleCart();
    showSuccessDownloadModal({});
  });
}

function showSuccessDownloadModal(tokens = {}) {
  const modal = document.getElementById("successModal");
  const downloadContainer = document.getElementById("downloadLinksList");
  
  let groups = [];
  cart.forEach(item => {
    if (item.id === "bundle") {
      groups.push(
        { title: "1. KMU Cyber-Notfallplan & Runbook", md: "01_Schweizer_KMU_Cyber_Notfallplan_Runbook.md", html: "01_Schweizer_KMU_Cyber_Notfallplan_Runbook.html", token: tokens["bundle"] || "" },
        { title: "2. Schweizer nDSG-Compliance-Paket", md: "02_Schweizer_nDSG_Datenschutz_Paket_TOM_VdT.md", html: "02_Schweizer_nDSG_Datenschutz_Paket_TOM_VdT.html", token: tokens["bundle"] || "" },
        { title: "3. KMU IT-Sicherheits-Audit Protokoll", md: "03_KMU_IT_Sicherheits_Audit_Checkliste.md", html: "03_KMU_IT_Sicherheits_Audit_Checkliste.html", token: tokens["bundle"] || "" },
        { title: "4. Mitarbeiter IT- & KI-Richtlinie", md: "04_Mitarbeiter_IT_Sicherheitsrichtlinie_KI_Policy.md", html: "04_Mitarbeiter_IT_Sicherheitsrichtlinie_KI_Policy.html", token: tokens["bundle"] || "" }
      );
    } else {
      const prod = PRODUCTS[item.id];
      if (prod) {
        groups.push({
          title: prod.title,
          md: prod.fileMd,
          html: prod.fileHtml,
          token: tokens[item.id] || ""
        });
      }
    }
  });

  // Duplikate filtern
  const uniqueGroups = Array.from(new Set(groups.map(g => g.title))).map(title => groups.find(g => g.title === title));

  downloadContainer.innerHTML = uniqueGroups.map(grp => {
    const mdLink = grp.token ? `/api/download?token=${grp.token}&file=${grp.md}` : `templates/${grp.md}`;
    const htmlLink = grp.token ? `/api/download?token=${grp.token}&file=${grp.html}` : `templates_printable/${grp.html}`;
    
    return `
      <div class="download-group">
        <div class="download-group-title"><i class="fa-solid fa-file-shield text-green"></i> ${grp.title}</div>
        <div class="download-actions-grid">
          <a href="${htmlLink}" target="_blank" class="btn-dl btn-dl-pdf">
            <i class="fa-solid fa-print"></i> Druckreife A4-Ansicht / PDF
          </a>
          <a href="${mdLink}" download class="btn-dl">
            <i class="fa-solid fa-download"></i> Quelldatei (.md / Word)
          </a>
        </div>
      </div>
    `;
  }).join("");

  modal.style.display = "flex";
  document.getElementById("modalBackdrop").style.display = "block";
  
  cart = [];
  saveCartToStorage();
  updateCartUI();
}
