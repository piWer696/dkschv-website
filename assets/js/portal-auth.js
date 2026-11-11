/**
 * DKSchV Schweiz · Mandanten- & Kundenportal Authentifizierung
 * 
 * Steuert den geschützten Zugriff auf Fachbeiträge, Notfall-Checklisten und Arbeitsmittel.
 * Unterstützt Mandanten-Passwort, API-Validierung über admin.dkschv.ch und sofortige
 * Lead-Generierung für Neukunden über "Zugang anfordern".
 */

(function () {
  'use strict';

  const STORAGE_KEY = 'dkschv_portal_auth';
  const API_LOGIN_URL = 'https://admin.dkschv.ch/api/portal/login';
  const API_LEAD_URL = 'https://admin.dkschv.ch/api/public-lead';
  const DEFAULT_CLIENT_PASSWORDS = ['dkschv2026', 'mandant2026', 'dkschv-kunden', 'schweiz2026'];

  // Session Helper
  function getSession() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY) || sessionStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      const data = JSON.parse(raw);
      if (data.expiresAt && Date.now() > data.expiresAt) {
        logout();
        return null;
      }
      return data;
    } catch {
      return null;
    }
  }

  function setSession(data, remember = true) {
    const sessionData = {
      ...data,
      savedAt: Date.now(),
      expiresAt: remember ? Date.now() + 1000 * 60 * 60 * 24 * 30 : Date.now() + 1000 * 60 * 60 * 8 // 30 Tage oder 8h
    };
    const storage = remember ? localStorage : sessionStorage;
    storage.setItem(STORAGE_KEY, JSON.stringify(sessionData));
    updateUIState();
  }

  function logout() {
    localStorage.removeItem(STORAGE_KEY);
    sessionStorage.removeItem(STORAGE_KEY);
    updateUIState();
    // Falls auf einer geschützten Seite, neu laden um Gate anzuzeigen
    if (document.getElementById('gatedArticleContent') || document.querySelector('.client-portal-gate')) {
      window.location.reload();
    }
  }

  function isLoggedIn() {
    return Boolean(getSession());
  }

  // Update DOM across page
  function updateUIState() {
    const session = getSession();
    const authenticated = Boolean(session);

    if (authenticated) {
      document.body.classList.add('portal-authenticated');
      document.body.classList.remove('portal-locked');
    } else {
      document.body.classList.remove('portal-authenticated');
      document.body.classList.add('portal-locked');
    }

    // 1. Update Header Buttons
    const portalBtns = document.querySelectorAll('.nav-portal-btn, #headerPortalBtn');
    portalBtns.forEach(btn => {
      if (authenticated) {
        btn.innerHTML = `<span class="portal-btn-icon">👤</span> <span class="portal-btn-text">Kundenbereich</span> <span class="portal-logout-badge" title="Abmelden" onclick="event.stopPropagation(); window.DKSchVPortal.logout();">&times;</span>`;
        btn.classList.add('logged-in');
        btn.setAttribute('title', `Angemeldet als ${session.email || 'Mandant'}. Klicken für Kundenbereich.`);
      } else {
        btn.innerHTML = `<span class="portal-btn-icon">🔒</span> <span class="portal-btn-text">Kunden-Login</span>`;
        btn.classList.remove('logged-in');
        btn.setAttribute('title', 'Mandanten- & Kunden-Login');
      }
    });

    // 2. Update Article Gates
    const gateEl = document.getElementById('clientPortalGate');
    const gatedContentEl = document.getElementById('gatedArticleContent');
    const catalogStatusEl = document.getElementById('catalogPortalStatus');

    if (gateEl) {
      gateEl.style.display = authenticated ? 'none' : 'block';
    }
    if (gatedContentEl) {
      if (authenticated) {
        gatedContentEl.classList.remove('is-locked');
      } else {
        gatedContentEl.classList.add('is-locked');
      }
    }

    if (catalogStatusEl) {
      if (authenticated) {
        catalogStatusEl.innerHTML = `
          <div class="portal-active-banner">
            <span>✅</span>
            <div><strong>Mandanten-Status: Freigeschaltet</strong> (${session.email || 'Kunde'}). Alle Fachartikel, Checklisten und Arbeitsmittel stehen Ihnen uneingeschränkt zur Verfügung.</div>
            <button onclick="window.DKSchVPortal.logout()" class="btn-logout-small">Abmelden</button>
          </div>
        `;
      } else {
        catalogStatusEl.innerHTML = `
          <div class="portal-locked-banner">
            <span>🔒</span>
            <div><strong>Exklusiver Mandanten- &amp; Kundenbereich:</strong> Für Kunden und Mandanten sind alle 12 Fachleitfäden und Vorlagen freigeschaltet.</div>
            <button onclick="window.DKSchVPortal.openModal()" class="btn-login-small">Kunden-Login &rarr;</button>
          </div>
        `;
      }
    }
  }

  // Modal Generator & Controller
  function ensureModalExists() {
    if (document.getElementById('portalModalOverlay')) return;

    const modalHtml = `
    <div id="portalModalOverlay" class="portal-modal-overlay" style="display: none;">
      <div class="portal-modal-card">
        <button class="portal-modal-close" onclick="window.DKSchVPortal.closeModal()" aria-label="Schliessen">&times;</button>
        
        <div class="portal-modal-header">
          <div class="portal-brand-badge">
            <span>🇨🇭</span>
            <span>DKSchV Mandantenbereich</span>
          </div>
          <h3 id="portalModalTitle" class="portal-modal-heading">Kunden- &amp; Mandanten-Login</h3>
          <p class="portal-modal-sub">
            Exklusiver Zugang zu allen Cyber-Security Leitfäden, Notfall-Checklisten und Rechtsentscheidungsbäumen.
          </p>
        </div>

        <!-- Tabs -->
        <div class="portal-tabs">
          <button class="portal-tab-btn active" id="tabBtnLogin" onclick="window.DKSchVPortal.switchTab('login')">
            🔑 Kunden-Login
          </button>
          <button class="portal-tab-btn" id="tabBtnRequest" onclick="window.DKSchVPortal.switchTab('request')">
            📋 Zugang anfordern
          </button>
        </div>

        <!-- Tab 1: Login -->
        <div id="portalPaneLogin" class="portal-tab-pane active">
          <form id="portalLoginForm" onsubmit="window.DKSchVPortal.handleLoginSubmit(event)">
            <div class="portal-form-group">
              <label for="portalEmail">Geschäftliche E-Mail-Adresse</label>
              <input type="email" id="portalEmail" class="portal-input" placeholder="name@ihre-firma.ch" required>
            </div>
            
            <div class="portal-form-group">
              <label for="portalPassword">
                <span>Mandanten-Passwort / Kundencode</span>
                <span style="font-weight: normal; font-size: 11.5px; color: #94a3b8;">(z. B. dkschv2026)</span>
              </label>
              <input type="password" id="portalPassword" class="portal-input" placeholder="Passwort eingeben" required>
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; font-size: 13px;">
              <label style="display: flex; align-items: center; gap: 8px; cursor: pointer; color: #cbd5e1;">
                <input type="checkbox" id="portalRemember" checked>
                <span>Angemeldet bleiben</span>
              </label>
              <a href="#" onclick="event.preventDefault(); window.DKSchVPortal.switchTab('request');" style="color: #2dd4bf; text-decoration: underline;">Code vergessen?</a>
            </div>

            <div id="portalLoginError" class="portal-alert-error" style="display: none;"></div>

            <button type="submit" id="portalLoginSubmitBtn" class="portal-submit-btn">
              <span>Anmelden &amp; Inhalte freischalten &rarr;</span>
            </button>
          </form>
        </div>

        <!-- Tab 2: Zugang anfordern -->
        <div id="portalPaneRequest" class="portal-tab-pane" style="display: none;">
          <form id="portalRequestForm" onsubmit="window.DKSchVPortal.handleRequestSubmit(event)">
            <p style="font-size: 13.5px; color: #cbd5e1; margin-bottom: 16px; line-height: 1.5;">
              Sie sind Mandant oder möchten die DKSchV-Vorlagen und Leitfäden für Ihr Schweizer Unternehmen nutzen? Fordern Sie hier unkompliziert Ihren Firmenzugang an:
            </p>

            <div class="portal-form-group">
              <label for="reqName">Ihr Name</label>
              <input type="text" id="reqName" class="portal-input" placeholder="Vorname Nachname" required>
            </div>

            <div class="portal-form-group">
              <label for="reqCompany">Unternehmen / Organisation</label>
              <input type="text" id="reqCompany" class="portal-input" placeholder="Firma AG / GmbH" required>
            </div>

            <div class="portal-form-group">
              <label for="reqEmail">Geschäftliche E-Mail-Adresse</label>
              <input type="email" id="reqEmail" class="portal-input" placeholder="name@firma.ch" required>
            </div>

            <div class="portal-form-group">
              <label for="reqPhone">Telefonnummer (optional für Rückfragen)</label>
              <input type="tel" id="reqPhone" class="portal-input" placeholder="+41 ...">
            </div>

            <div id="portalRequestStatus" class="portal-alert-success" style="display: none;"></div>

            <button type="submit" id="portalRequestSubmitBtn" class="portal-submit-btn">
              <span>Mandanten-Zugang anfordern &rarr;</span>
            </button>
          </form>
        </div>

        <div class="portal-modal-footer">
          🔒 Gesicherter Schweizer Mandantenbereich · DKSchV Dini Naters · 100% nDSG-konform
        </div>
      </div>
    </div>
    `;

    document.body.insertAdjacentHTML('beforeend', modalHtml);

    // Close on overlay background click
    const overlay = document.getElementById('portalModalOverlay');
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) {
        closeModal();
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeModal();
    });
  }

  function openModal(defaultTab = 'login') {
    ensureModalExists();
    switchTab(defaultTab);
    const overlay = document.getElementById('portalModalOverlay');
    if (overlay) {
      overlay.style.display = 'flex';
      document.body.style.overflow = 'hidden';
      // Focus first input
      setTimeout(() => {
        const input = defaultTab === 'login' ? document.getElementById('portalEmail') : document.getElementById('reqName');
        if (input) input.focus();
      }, 100);
    }
  }

  function closeModal() {
    const overlay = document.getElementById('portalModalOverlay');
    if (overlay) {
      overlay.style.display = 'none';
      document.body.style.overflow = '';
    }
  }

  function switchTab(tab) {
    const btnLogin = document.getElementById('tabBtnLogin');
    const btnReq = document.getElementById('tabBtnRequest');
    const paneLogin = document.getElementById('portalPaneLogin');
    const paneReq = document.getElementById('portalPaneRequest');
    const title = document.getElementById('portalModalTitle');

    if (tab === 'login') {
      if (btnLogin) btnLogin.classList.add('active');
      if (btnReq) btnReq.classList.remove('active');
      if (paneLogin) paneLogin.style.display = 'block';
      if (paneReq) paneReq.style.display = 'none';
      if (title) title.textContent = 'Kunden- & Mandanten-Login';
    } else {
      if (btnLogin) btnLogin.classList.remove('active');
      if (btnReq) btnReq.classList.add('active');
      if (paneLogin) paneLogin.style.display = 'none';
      if (paneReq) paneReq.style.display = 'block';
      if (title) title.textContent = 'Mandanten-Zugang anfordern';
    }
  }

  // Handle Login Submission
  async function handleLoginSubmit(e) {
    e.preventDefault();
    const email = document.getElementById('portalEmail').value.trim();
    const password = document.getElementById('portalPassword').value.trim();
    const remember = document.getElementById('portalRemember').checked;
    const errorBox = document.getElementById('portalLoginError');
    const submitBtn = document.getElementById('portalLoginSubmitBtn');

    if (errorBox) errorBox.style.display = 'none';
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.innerHTML = '🔒 Zugang wird verifiziert...';
    }

    let isValid = false;
    let clientCompany = '';

    // 1. Check if backend API validates it
    try {
      const resp = await fetch(API_LOGIN_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      });
      const data = await resp.json().catch(() => ({}));
      if (resp.ok && data.success) {
        isValid = true;
        clientCompany = data.company || '';
      }
    } catch {
      // Backend asleep or unreachable - proceed to standard verification
    }

    // 2. Client-side verified passwords fallback (e.g. dkschv2026, mandant2026)
    if (!isValid) {
      const lowerPass = password.toLowerCase();
      if (DEFAULT_CLIENT_PASSWORDS.includes(lowerPass)) {
        isValid = true;
      }
    }

    if (isValid) {
      setSession({
        email,
        company: clientCompany || email.split('@')[1]?.split('.')[0]?.toUpperCase() || 'Mandant',
        role: 'client'
      }, remember);

      if (submitBtn) {
        submitBtn.innerHTML = '✅ Erfolgreich angemeldet!';
      }

      setTimeout(() => {
        closeModal();
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = '<span>Anmelden &amp; Inhalte freischalten &rarr;</span>';
        }
        if (!window.location.pathname.includes('/wissen')) {
          window.location.href = 'wissen/';
        }
      }, 500);
    } else {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.innerHTML = '<span>Anmelden &amp; Inhalte freischalten &rarr;</span>';
      }
      if (errorBox) {
        errorBox.style.display = 'block';
        errorBox.innerHTML = '⚠️ Das eingegebene Mandanten-Passwort ist nicht korrekt. Bitte prüfen Sie die Eingabe oder fordern Sie über den Reiter «Zugang anfordern» Zugangsdaten an.';
      }
    }
  }

  // Handle Request Access Submission (Qualified Lead to Admin Cockpit)
  async function handleRequestSubmit(e) {
    e.preventDefault();
    const name = document.getElementById('reqName').value.trim();
    const company = document.getElementById('reqCompany').value.trim();
    const email = document.getElementById('reqEmail').value.trim();
    const phone = document.getElementById('reqPhone').value.trim();
    const statusBox = document.getElementById('portalRequestStatus');
    const submitBtn = document.getElementById('portalRequestSubmitBtn');

    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.innerHTML = '🔒 Anfrage wird verschlüsselt gesendet...';
    }

    try {
      const formData = new URLSearchParams();
      formData.append('contactName', name);
      formData.append('company', company);
      formData.append('email', email);
      formData.append('phone', phone);
      formData.append('requestType', 'Mandanten-Zugang Wissensportal');
      formData.append('question', 'Kunde hat Zugang zum geschützten DKSchV-Mandantenbereich und den Fach-Leitfäden angefordert.');
      formData.append('source', 'DKSchV-Kundenportal (Zugang angefordert)');
      formData.append('topic', 'Datenschutz oder Datenabfluss');
      formData.append('urgency', 'Normal');

      await fetch(API_LEAD_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: formData.toString()
      });

      // Auto-unlock immediately for high lead conversion!
      setSession({
        email,
        company,
        role: 'trial-mandant'
      }, true);

      if (statusBox) {
        statusBox.style.display = 'block';
        statusBox.innerHTML = `✅ <strong>Herzlich willkommen, ${name}!</strong> Ihre Anfrage wurde registriert. Ihr Mandanten-Zugang für <strong>${company}</strong> wurde sofort freigeschaltet.`;
      }

      setTimeout(() => {
        closeModal();
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = '<span>Mandanten-Zugang anfordern &rarr;</span>';
        }
      }, 1500);

    } catch (err) {
      console.warn('Lead submit failed, activating instant local pass:', err);
      setSession({ email, company, role: 'trial-mandant' }, true);
      closeModal();
    }
  }

  // Fast inline unlock on article page
  function handleInlineUnlock(e) {
    e.preventDefault();
    const form = e.target;
    const passInput = form.querySelector('input[type="password"]');
    const pass = passInput ? passInput.value.trim().toLowerCase() : '';
    const errBox = form.querySelector('.inline-error');

    if (DEFAULT_CLIENT_PASSWORDS.includes(pass)) {
      setSession({ email: 'mandant@dkschv.ch', company: 'Mandant', role: 'client' }, true);
    } else {
      if (errBox) {
        errBox.style.display = 'block';
        errBox.textContent = 'Ungültiges Passwort. Standard-Code eingeben oder oben auf «Zugang anfordern» klicken.';
      }
    }
  }

  // Public API
  window.DKSchVPortal = {
    isLoggedIn,
    getSession,
    logout,
    openModal,
    closeModal,
    switchTab,
    handleLoginSubmit,
    handleRequestSubmit,
    handleInlineUnlock
  };

  // Helper alias
  window.openPortalLoginModal = function (e) {
    if (e && e.preventDefault) e.preventDefault();
    if (isLoggedIn()) {
      if (!window.location.pathname.includes('/wissen')) {
        window.location.href = 'wissen/';
      } else {
        if (confirm('Sie sind derzeit als Mandant angemeldet. Möchten Sie sich abmelden?')) {
          logout();
        }
      }
    } else {
      openModal('login');
    }
  };

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateUIState);
  } else {
    updateUIState();
  }

})();
