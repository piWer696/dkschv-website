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

  // 5. Knowledge Hub Search & Filter Logic
  const hubSearchInput = document.getElementById('hubSearchInput');
  const filterChips = document.querySelectorAll('.filter-chip');
  const articleCards = document.querySelectorAll('.hub-article-card');

  let activeCategory = 'all';
  let activeSearchTerm = '';

  function filterHubCards() {
    let visibleCount = 0;
    articleCards.forEach(card => {
      const cardCategory = card.getAttribute('data-category') || '';
      const cardTitle = (card.querySelector('.card-title') ? card.querySelector('.card-title').textContent : '').toLowerCase();
      const cardDesc = (card.querySelector('.card-description') ? card.querySelector('.card-description').textContent : '').toLowerCase();
      const cardTags = (card.getAttribute('data-keywords') || '').toLowerCase();

      const matchesCategory = (activeCategory === 'all' || cardCategory === activeCategory);
      const matchesSearch = !activeSearchTerm ||
        cardTitle.includes(activeSearchTerm) ||
        cardDesc.includes(activeSearchTerm) ||
        cardTags.includes(activeSearchTerm);

      if (matchesCategory && matchesSearch) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    const noResultsEl = document.getElementById('hubNoResults');
    if (noResultsEl) {
      noResultsEl.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  }

  if (hubSearchInput) {
    hubSearchInput.addEventListener('input', function (e) {
      activeSearchTerm = e.target.value.trim().toLowerCase();
      filterHubCards();
    });
  }

  if (filterChips.length > 0) {
    filterChips.forEach(chip => {
      chip.addEventListener('click', function () {
        filterChips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        activeCategory = chip.getAttribute('data-filter') || 'all';
        filterHubCards();
      });
    });
  }

  // 6. Article Reading Progress & TOC Scrollspy
  const progressBar = document.querySelector('.reading-progress-bar');
  const tocLinks = document.querySelectorAll('.toc-list a');
  const articleSections = document.querySelectorAll('.article-content h2[id]');

  if (progressBar || (tocLinks.length > 0 && articleSections.length > 0)) {
    window.addEventListener('scroll', function () {
      const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;

      if (progressBar && height > 0) {
        const scrolled = (winScroll / height) * 100;
        progressBar.style.width = scrolled + '%';
      }

      if (articleSections.length > 0 && tocLinks.length > 0) {
        let currentSectionId = '';
        articleSections.forEach(section => {
          const sectionTop = section.offsetTop - 120;
          if (winScroll >= sectionTop) {
            currentSectionId = section.getAttribute('id');
          }
        });

        if (currentSectionId) {
          tocLinks.forEach(link => {
            if (link.getAttribute('href') === '#' + currentSectionId) {
              link.classList.add('active');
            } else {
              link.classList.remove('active');
            }
          });
        }
      }
    }, { passive: true });
  }
});
