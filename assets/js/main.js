/**
 * DKSchV Schweiz · Client JavaScript Logic
 * Modern, Dependency-Free, Secure B2B Interactivity
 */

document.addEventListener('DOMContentLoaded', function () {
  // 1. Mobile Menu Toggle
  const mobileToggle = document.getElementById('mobileMenuToggle');
  const navMenu = document.getElementById('navMenu');

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', function () {
      navMenu.classList.toggle('open');
      const isOpen = navMenu.classList.contains('open');
      mobileToggle.setAttribute('aria-expanded', isOpen);
    });
  }

  // 2. Tab Navigation
  window.switchSuiteTab = function (tabId) {
    const tabs = document.querySelectorAll('.suite-tab-btn');
    const panes = document.querySelectorAll('.suite-pane');

    tabs.forEach(t => t.classList.remove('active'));
    panes.forEach(p => p.classList.remove('active'));

    const activeBtn = document.querySelector(`[data-tab="${tabId}"]`);
    const activePane = document.getElementById(`pane-${tabId}`);

    if (activeBtn) activeBtn.classList.add('active');
    if (activePane) activePane.classList.add('active');
  };

  // 3. 60-Second Cyber Risk Calculator
  const riskScores = {
    mfa: 0,
    backup: 0,
    phishing: 0,
    incident: 0
  };

  window.selectRiskOption = function (btn, category, points) {
    const parent = btn.parentElement;
    parent.querySelectorAll('.quiz-opt-btn').forEach(b => b.classList.remove('selected'));
    btn.classList.add('selected');

    riskScores[category] = points;
    updateRiskEvaluation();
  };

  function updateRiskEvaluation() {
    const total = riskScores.mfa + riskScores.backup + riskScores.phishing + riskScores.incident;
    const circle = document.getElementById('riskGaugeCircle');
    const title = document.getElementById('riskResultTitle');
    const text = document.getElementById('riskResultDesc');

    if (!circle || !title || !text) return;

    circle.innerHTML = `${total}%<span>INDEX</span>`;

    if (total >= 80) {
      circle.style.backgroundColor = '#0f766e';
      title.textContent = `Solides Sicherheitsniveau (${total}%)`;
      text.textContent = 'Ihre Kern-Sicherheitsmassnahmen sind gut implementiert. Der Fokus sollte nun auf regelmässigen Notfall-Drills und Lieferanten-Audits liegen.';
    } else if (total >= 50) {
      circle.style.backgroundColor = '#d97706';
      title.textContent = `Erhöhtes Cyber-Risiko (${total}%)`;
      text.textContent = 'Es bestehen kritische Einfallstore (z. B. unvollständiges MFA oder unzureichend getestete Offline-Backups), die Ransomware-Angriffe begünstigen.';
    } else {
      circle.style.backgroundColor = '#dc2626';
      title.textContent = `Kritisches Sicherheitsrisiko (${total}%)`;
      text.textContent = 'Dringender Handlungsbedarf! Ihr Unternehmen verfügt über unzureichenden Schutz gegen moderne Phishing- und Erpressungs-Angriffe.';
    }
  }

  // 4. Public Lead Form Handler (Ajax submission to admin.dkschv.ch)
  const leadForms = document.querySelectorAll('.dkschv-lead-form');

  leadForms.forEach(form => {
    form.addEventListener('submit', async function (e) {
      e.preventDefault();

      // Honeypot check
      const honeypot = form.querySelector('input[name="website"]');
      if (honeypot && honeypot.value.trim() !== '') {
        console.warn('Spam detected via honeypot');
        return;
      }

      const submitBtn = form.querySelector('button[type="submit"]');
      const originalBtnText = submitBtn ? submitBtn.innerHTML : 'Absenden';
      const statusBox = form.querySelector('.form-status-message');

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '🔒 Anfrage wird sicher verschlüsselt...';
      }

      const formData = new FormData(form);
      const urlEncoded = new URLSearchParams(formData);

      try {
        const response = await fetch('https://admin.dkschv.ch/api/public-lead', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          body: urlEncoded.toString()
        });

        const result = await response.json().catch(() => ({}));

        if (response.ok && !result.error) {
          form.reset();
          if (statusBox) {
            statusBox.style.display = 'block';
            statusBox.className = 'form-status-message success';
            statusBox.innerHTML = '✅ <strong>Vielen Dank!</strong> Ihre Sicherheitsanfrage ist sicher eingegangen. Wir analysieren Ihre Angaben und melden uns vertraulich bei Ihnen.';
          }
          if (submitBtn) {
            submitBtn.innerHTML = '✅ Erfolgreich übermittelt';
          }
        } else {
          throw new Error(result.error || 'Fehler beim Senden');
        }
      } catch (err) {
        console.error('Lead submission failed:', err);
        if (statusBox) {
          statusBox.style.display = 'block';
          statusBox.className = 'form-status-message error';
          statusBox.innerHTML = `⚠️ Die Anfrage konnte nicht direkt übermittelt werden (${err.message}). Bitte senden Sie uns direkt eine vertrauliche E-Mail an <a href="mailto:info@dkschv.ch?subject=Sicherheitsanfrage" style="text-decoration:underline; font-weight:bold;">info@dkschv.ch</a> oder rufen Sie uns an: +41 79 844 66 69.`;
        }
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalBtnText;
        }
      }
    });
  });
});
