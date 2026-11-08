/**
 * DKSchV Schweiz · Knowledge Hub & Sunday Blog Package Generator
 * 
 * Automatically compiles weekly Manus blog packages (articles, resources, news)
 * into high-performance, responsive, Swiss-compliant HTML pages.
 * 
 * Usage: node scripts/build-knowledge-hub.mjs
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');

const ARTICLES_DIR = path.join(ROOT_DIR, 'content', 'blog-paket', 'articles');
const RESOURCES_DIR = path.join(ROOT_DIR, 'content', 'blog-paket', 'resources');
const NEWS_DIR = path.join(ROOT_DIR, 'content', 'news');
const MANIFEST_FILE = path.join(ROOT_DIR, 'content', 'blog-paket', 'cms-import-manifest.csv');

const WISSEN_DIR = path.join(ROOT_DIR, 'wissen');
const WISSEN_RESOURCES_DIR = path.join(WISSEN_DIR, 'resources');
const WISSEN_NEWS_DIR = path.join(WISSEN_DIR, 'news');

// Ensure output dirs exist
fs.mkdirSync(WISSEN_DIR, { recursive: true });
fs.mkdirSync(WISSEN_RESOURCES_DIR, { recursive: true });
fs.mkdirSync(WISSEN_NEWS_DIR, { recursive: true });

// Category mapping based on filename or slug
const CATEGORY_MAP = {
  '01': { category: 'notfall', label: 'Ransomware & Notfall' },
  '02': { category: 'email', label: 'E-Mail & Betrug' },
  '03': { category: 'datenschutz', label: 'Datenschutz & nDSG' },
  '04': { category: 'backup', label: 'Backup & Resilienz' },
  '05': { category: 'cloud', label: 'Cloud & M365' },
  '06': { category: 'cloud', label: 'Cloud & M365' },
  '07': { category: 'backup', label: 'Backup & Resilienz' },
  '08': { category: 'governance', label: 'Audit & Risikomanagement' },
  '09': { category: 'ki', label: 'Künstliche Intelligenz' },
  '10': { category: 'notfall', label: 'Krisenkommunikation' },
  '11': { category: 'governance', label: 'Lieferanten & Dritte' },
  '12': { category: 'governance', label: 'Compliance (NIS2/DORA)' },
};

function slugify(text) {
  return text
    .toString()
    .toLowerCase()
    .replace(/ä/g, 'ae')
    .replace(/ö/g, 'oe')
    .replace(/ü/g, 'ue')
    .replace(/ß/g, 'ss')
    .replace(/[^\w\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-');
}

function parseFrontmatter(markdown) {
  const match = markdown.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/);
  if (!match) {
    return { frontmatter: {}, body: markdown };
  }
  const rawYaml = match[1];
  const body = match[2];
  const frontmatter = {};

  const lines = rawYaml.split(/\r?\n/);
  let currentKey = null;

  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;

    const colonIdx = line.indexOf(':');
    if (colonIdx > -1 && !line.startsWith(' ') && !line.startsWith('\t')) {
      const key = line.slice(0, colonIdx).trim();
      let val = line.slice(colonIdx + 1).trim();
      if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
        val = val.slice(1, -1);
      }
      frontmatter[key] = val;
      currentKey = key;
    } else if (currentKey && (line.startsWith(' ') || line.startsWith('\t'))) {
      // Continuation of multiline string or subkey
      frontmatter[currentKey] += ' ' + trimmed;
    }
  }

  return { frontmatter, body };
}

function getAuthorityBadge(url) {
  if (!url) return '';
  if (url.includes('bacs.admin.ch') || url.includes('ncsc.admin.ch')) return '🇨🇭 BACS Bund';
  if (url.includes('edoeb.admin.ch')) return '🇨🇭 EDÖB Datenschutz';
  if (url.includes('fedlex.admin.ch')) return '🇨🇭 Fedlex Bundesrecht';
  if (url.includes('suisse-epolice.ch')) return '🇨🇭 Suisse ePolice';
  if (url.includes('cisa.gov')) return '🛡️ CISA US';
  if (url.includes('nist.gov')) return '🔒 NIST Standard';
  if (url.includes('microsoft.com')) return '🟦 Microsoft';
  return '🔗 Primärquelle';
}

function formatMarkdown(markdown, options = {}) {
  const { isArticle = true, isResource = false, isNews = false, currentSlug = '' } = options;
  const lines = markdown.split(/\r?\n/);
  const headings = [];
  const references = [];
  const htmlParts = [];
  const leadParts = [];
  const restParts = [];
  let reachedFirstHeading = false;

  function pushHtml(chunk) {
    htmlParts.push(chunk);
    if (!reachedFirstHeading) {
      leadParts.push(chunk);
    } else {
      restParts.push(chunk);
    }
  }

  // Determine relative root based on page type
  let rootPrefix = '..'; // Default for articles in wissen/
  if (isResource || isNews) {
    rootPrefix = '../..'; // For pages in wissen/resources/ or wissen/news/
  } else if (!isArticle && !isResource && !isNews) {
    rootPrefix = '.'; // For root pages
  }

  let inList = false;
  let listType = null; // 'ul' or 'ol'
  let inTable = false;
  let tableHeader = [];
  let tableRows = [];
  let inBlockquote = false;
  let blockquoteLines = [];

  function flushList() {
    if (inList) {
      pushHtml(`</${listType}>`);
      inList = false;
      listType = null;
    }
  }

  function flushTable() {
    if (inTable) {
      let tHtml = '<div class="table-responsive"><table class="kb-table"><thead><tr>';
      tableHeader.forEach(h => {
        tHtml += `<th>${processInline(h)}</th>`;
      });
      tHtml += '</tr></thead><tbody>';
      tableRows.forEach(row => {
        tHtml += '<tr>';
        row.forEach(c => {
          tHtml += `<td>${processInline(c)}</td>`;
        });
        tHtml += '</tr>';
      });
      tHtml += '</tbody></table></div>';
      pushHtml(tHtml);
      inTable = false;
      tableHeader = [];
      tableRows = [];
    }
  }

  function flushBlockquote() {
    if (inBlockquote) {
      const text = blockquoteLines.join('\n');
      let calloutClass = 'callout callout-note';
      let icon = 'ℹ️';

      if (text.includes('[FACHPRÜFUNG ERFORDERLICH]')) {
        calloutClass = 'callout callout-warning';
        icon = '⚖️';
      } else if (text.includes('**Wichtig:**') || text.includes('**Notfall:**')) {
        calloutClass = 'callout callout-danger';
        icon = '🚨';
      } else if (text.includes('Hypothetisches Beispiel') || text.includes('Praxisbeispiel')) {
        calloutClass = 'callout callout-info';
        icon = '💡';
      }

      const processed = processInline(text.replace(/^[> ]+/gm, ''));
      pushHtml(`<div class="${calloutClass}"><div class="callout-icon">${icon}</div><div class="callout-body">${processed}</div></div>`);
      inBlockquote = false;
      blockquoteLines = [];
    }
  }

  function processInline(text) {
    if (!text) return '';
    let out = text;

    // Special verification marker
    out = out.replace(/\[FACHPRÜFUNG ERFORDERLICH\]/g, '<span class="badge-warning-pill">⚖️ Fachprüfung erforderlich</span>');

    // Bold & italic
    out = out.replace(/\*\*\*([^*]+)\*\*\*/g, '<strong><em>$1</em></strong>');
    out = out.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    out = out.replace(/\*([^*]+)\*/g, '<em>$1</em>');
    out = out.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Citations [1], [2], etc.
    out = out.replace(/(?<!\[)\[([0-9]{1,2})\](?!\()/g, '<sup class="ref-link"><a href="#ref-$1">[$1]</a></sup>');

    // Markdown Links [text](url)
    out = out.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (match, linkText, url) => {
      // Rewrite internal package links
      let finalUrl = url;
      let targetAttr = '';

      if (finalUrl.includes('Laufstatus.md') || finalUrl.includes('AUTOMATION_STATUS.md')) {
        return linkText; // Plain text for internal dev files
      }

      if (finalUrl.startsWith('/wissen/') || finalUrl.startsWith('wissen/')) {
        const slug = finalUrl.replace(/^\/?wissen\//, '').replace(/\.html$/, '');
        if (isArticle) finalUrl = `./${slug}.html`;
        else if (isResource || isNews) finalUrl = `../${slug}.html`;
        else finalUrl = `wissen/${slug}.html`;
      } else if (finalUrl.startsWith('/resources/') || finalUrl.startsWith('resources/')) {
        const slug = finalUrl.replace(/^\/?resources\//, '').replace(/\.html$/, '');
        if (isArticle) finalUrl = `./resources/${slug}.html`;
        else if (isResource) finalUrl = `./${slug}.html`;
        else if (isNews) finalUrl = `../resources/${slug}.html`;
        else finalUrl = `wissen/resources/${slug}.html`;
      } else if (finalUrl.includes('sicherheitsanalyse')) {
        finalUrl = `${rootPrefix}/sicherheitsanalyse.html`;
      } else if (finalUrl.includes('risikomanagement')) {
        finalUrl = `${rootPrefix}/risikomanagement.html`;
      } else if (finalUrl.includes('notfallplanung')) {
        finalUrl = `${rootPrefix}/notfallplanung.html`;
      } else if (finalUrl.includes('kontakt')) {
        finalUrl = `${rootPrefix}/kontakt.html`;
      } else if (finalUrl.startsWith('http')) {
        targetAttr = ' target="_blank" rel="noopener noreferrer"';
      }

      return `<a href="${finalUrl}"${targetAttr}>${linkText}</a>`;
    });

    return out;
  }

  let isFirstParagraph = true;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmed = line.trim();

    // Reference definitions at end of file: [1]: https://... "Title"
    const refMatch = line.match(/^\[([0-9]{1,2})\]:\s*(\S+)(?:\s+"([^"]+)")?/);
    if (refMatch) {
      flushList();
      flushTable();
      flushBlockquote();
      references.push({
        num: refMatch[1],
        url: refMatch[2],
        title: refMatch[3] || refMatch[2]
      });
      continue;
    }

    // Horizontal rule
    if (trimmed === '---' || trimmed === '***') {
      flushList();
      flushTable();
      flushBlockquote();
      pushHtml('<hr style="margin: 32px 0; border: none; border-top: 1px solid var(--border);">');
      continue;
    }

    // Headings
    if (line.startsWith('# ')) {
      flushList();
      flushTable();
      flushBlockquote();
      // Main H1 is handled by page header
      continue;
    }

    if (line.startsWith('## ')) {
      flushList();
      flushTable();
      flushBlockquote();
      reachedFirstHeading = true;
      const title = line.replace(/^## /, '').trim();
      const id = slugify(title);
      headings.push({ level: 2, title, id });
      pushHtml(`<h2 id="${id}">${processInline(title)}</h2>`);
      continue;
    }

    if (line.startsWith('### ')) {
      flushList();
      flushTable();
      flushBlockquote();
      const title = line.replace(/^### /, '').trim();
      const id = slugify(title);
      headings.push({ level: 3, title, id });
      pushHtml(`<h3 id="${id}">${processInline(title)}</h3>`);
      continue;
    }

    if (line.startsWith('#### ')) {
      flushList();
      flushTable();
      flushBlockquote();
      const title = line.replace(/^#### /, '').trim();
      pushHtml(`<h4>${processInline(title)}</h4>`);
      continue;
    }

    // Blockquote
    if (line.startsWith('>')) {
      flushList();
      flushTable();
      inBlockquote = true;
      blockquoteLines.push(line.replace(/^>\s?/, ''));
      continue;
    } else if (inBlockquote) {
      flushBlockquote();
    }

    // Markdown Table
    if (line.trim().startsWith('|') && line.trim().endsWith('|')) {
      flushList();
      const cells = line.split('|').slice(1, -1).map(c => c.trim());
      if (!inTable) {
        inTable = true;
        tableHeader = cells;
      } else if (cells.every(c => /^[-:\s]+$/.test(c))) {
        // Separator line - skip
      } else {
        tableRows.push(cells);
      }
      continue;
    } else if (inTable) {
      flushTable();
    }

    // Task Checklist
    const taskMatch = line.match(/^(\s*)-\s+\[([ xX])\]\s+(.*)$/);
    if (taskMatch) {
      flushTable();
      if (!inList) {
        inList = true;
        listType = 'ul';
        pushHtml('<ul style="list-style: none; padding-left: 0;">');
      }
      const isChecked = taskMatch[2].toLowerCase() === 'x';
      const itemText = processInline(taskMatch[3]);
      pushHtml(`<li class="task-item"><input type="checkbox" ${isChecked ? 'checked' : ''} onclick="return false;"> <span>${itemText}</span></li>`);
      continue;
    }

    // Unordered List
    const ulMatch = line.match(/^(\s*)[-*]\s+(.*)$/);
    if (ulMatch) {
      flushTable();
      if (!inList || listType !== 'ul') {
        flushList();
        inList = true;
        listType = 'ul';
        pushHtml('<ul>');
      }
      pushHtml(`<li>${processInline(ulMatch[2])}</li>`);
      continue;
    }

    // Ordered List
    const olMatch = line.match(/^(\s*)[0-9]+\.\s+(.*)$/);
    if (olMatch) {
      flushTable();
      if (!inList || listType !== 'ol') {
        flushList();
        inList = true;
        listType = 'ol';
        pushHtml('<ol>');
      }
      pushHtml(`<li>${processInline(olMatch[2])}</li>`);
      continue;
    }

    // If we were in a list and hit normal line
    if (inList && trimmed === '') {
      flushList();
      continue;
    }

    // Paragraph
    if (trimmed !== '') {
      flushList();
      flushTable();
      flushBlockquote();

      if (isFirstParagraph && trimmed.startsWith('**Kurzantwort:**')) {
        pushHtml(`<div class="article-lead">${processInline(trimmed)}</div>`);
        isFirstParagraph = false;
      } else {
        pushHtml(`<p>${processInline(trimmed)}</p>`);
      }
      continue;
    }
  }

  flushList();
  flushTable();
  flushBlockquote();

  // References Section HTML
  let referencesHtml = '';
  if (references.length > 0) {
    referencesHtml += `
      <div class="references-section">
        <h3 id="quellen-und-referenzen" style="font-size: 20px; font-weight: 700; margin-bottom: 16px;">
          Geprüfte Primärquellen &amp; Rechtsreferenzen
        </h3>
        <p style="font-size: 13.5px; color: var(--text-muted); margin-bottom: 16px;">
          Alle behördlichen Vorgaben, Gesetzesartikel und technischen Richtlinien wurden im Rahmen der DKSchV-Quellenprüfung verifiziert:
        </p>
        <ul class="references-list">
    `;

    references.forEach(ref => {
      const badge = getAuthorityBadge(ref.url);
      referencesHtml += `
        <li class="ref-item" id="ref-${ref.num}">
          <span class="ref-num">[${ref.num}]</span>
          <div>
            ${badge ? `<span style="font-size: 11px; font-weight: 700; background: #e2e8f0; color: #334155; padding: 2px 6px; border-radius: 3px; margin-right: 6px;">${badge}</span>` : ''}
            <a href="${ref.url}" target="_blank" rel="noopener noreferrer">${ref.title}</a>
          </div>
        </li>
      `;
    });

    referencesHtml += `
        </ul>
      </div>
    `;
  }

  return {
    contentHtml: htmlParts.join('\n'),
    leadHtml: leadParts.join('\n'),
    restContentHtml: restParts.join('\n'),
    headings,
    references,
    referencesHtml
  };
}

function renderHeader(activeNav = 'wissen', relativeRoot = '.') {
  const wissenHref = relativeRoot === '.' ? 'wissen/' : (relativeRoot === '..' ? './' : '../');
  return `
  <!-- Top Emergency Bar -->
  <div class="top-emergency-bar">
    <div class="container top-bar-inner">
      <div class="top-trust-tags">
        <span class="top-trust-tag">🇨🇭 Schweizer Cyber-Security &amp; Datenschutz</span>
        <span class="top-trust-tag">⚖️ 100% nDSG- &amp; BACS-orientiert</span>
        <span class="top-trust-tag">📍 Naters / Wallis</span>
      </div>
      <div>
        <a href="${relativeRoot}/kontakt.html#notfall" class="emergency-quicklink">
          🚨 Akuter IT-Notfall? Sofortige Triage &rarr;
        </a>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="site-header">
    <div class="container navbar">
      <a href="${relativeRoot}/index.html" class="brand-link" title="DKSchV Schweiz Startseite">
        <img src="${relativeRoot}/assets/images/dkschv_logo.png" alt="DKSchV Schweiz Logo" class="brand-logo-img">
      </a>
      <nav>
        <ul class="nav-menu" id="navMenu">
          <li><a href="${relativeRoot}/index.html" class="nav-link ${activeNav === 'home' ? 'active' : ''}">Home</a></li>
          <li><a href="${relativeRoot}/sicherheitsanalyse.html" class="nav-link ${activeNav === 'sicherheitsanalyse' ? 'active' : ''}">Sicherheitsanalyse</a></li>
          <li><a href="${relativeRoot}/risikomanagement.html" class="nav-link ${activeNav === 'risikomanagement' ? 'active' : ''}">Risikomanagement</a></li>
          <li><a href="${relativeRoot}/notfallplanung.html" class="nav-link ${activeNav === 'notfallplanung' ? 'active' : ''}">Notfallplanung</a></li>
          <li><a href="${wissenHref}" class="nav-link ${activeNav === 'wissen' ? 'active' : ''}">Wissen &amp; Ratgeber</a></li>
          <li><a href="${relativeRoot}/ueber-uns.html" class="nav-link ${activeNav === 'ueber-uns' ? 'active' : ''}">Über uns</a></li>
          <li><a href="${relativeRoot}/kontakt.html" class="nav-link ${activeNav === 'kontakt' ? 'active' : ''}">Kontakt</a></li>
          <li><a href="${relativeRoot}/kontakt.html" class="nav-cta-btn">Audit anfragen</a></li>
        </ul>
      </nav>
      <button class="mobile-toggle" id="mobileMenuToggle" aria-label="Menü öffnen" aria-expanded="false">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      </button>
    </div>
  </header>
  `;
}

function renderFooter(relativeRoot = '.') {
  const wissenHref = relativeRoot === '.' ? 'wissen/' : (relativeRoot === '..' ? './' : '../');
  return `
  <!-- Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="${relativeRoot}/assets/images/dkschv_logo.png" alt="DKSchV Schweiz" style="height: 38px; filter: brightness(0) invert(1);">
          <p>DKSchV Dini ist Ihr spezialisierter Schweizer Partner für Cyber-Security, Sicherheitsanalysen, IT-Notfallplanung und Datenschutz nach Schweizer Standard.</p>
        </div>
        <div class="footer-col">
          <h4>Dienstleistungen</h4>
          <ul class="footer-links">
            <li><a href="${relativeRoot}/sicherheitsanalyse.html">Sicherheitsanalyse</a></li>
            <li><a href="${relativeRoot}/risikomanagement.html">Risikomanagement</a></li>
            <li><a href="${relativeRoot}/notfallplanung.html">Notfallplanung</a></li>
            <li><a href="${wissenHref}">Wissen &amp; Ratgeber</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Unternehmen</h4>
          <ul class="footer-links">
            <li><a href="${relativeRoot}/ueber-uns.html">Über uns</a></li>
            <li><a href="${relativeRoot}/kontakt.html">Kontakt &amp; Standort</a></li>
            <li><a href="${relativeRoot}/impressum.html">Impressum</a></li>
            <li><a href="${relativeRoot}/datenschutz.html">Datenschutz (nDSG)</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Standort &amp; Notfallkontakt</h4>
          <p style="font-size: 14px; color: #94a3b8; line-height: 1.6; margin-bottom: 12px;">
            <strong>DKSchV Dini</strong><br>Andreas Dini<br>Bammattenweg 19<br>CH-3904 Naters (Wallis)
          </p>
          <p style="font-size: 14px; color: #94a3b8;">
            E-Mail: <a href="mailto:info@dkschv.ch" style="color: #ffffff;">info@dkschv.ch</a><br>
            Telefon: <a href="tel:+41798446669" style="color: #ffffff;">+41 79 844 66 69</a>
          </p>
        </div>
      </div>
      <div class="footer-bottom">
        <div>© 2026 DKSchV Dini · Alle Rechte vorbehalten.</div>
        <div class="footer-legal-links">
          <a href="${relativeRoot}/impressum.html">Impressum</a>
          <a href="${relativeRoot}/datenschutz.html">Datenschutz</a>
        </div>
      </div>
    </div>
  </footer>
  <script src="${relativeRoot}/assets/js/main.js"></script>
  `;
}

// =============================================================================
// Build Execution
// =============================================================================
console.log('🚀 DKSchV Knowledge Hub Builder gestartet...');

// 1. Scan Articles
const articleFiles = fs.readdirSync(ARTICLES_DIR).filter(f => f.endsWith('.md')).sort();
const resourceFiles = fs.readdirSync(RESOURCES_DIR).filter(f => f.endsWith('.md')).sort();

console.log(`📁 Gefunden: ${articleFiles.length} Artikel, ${resourceFiles.length} Arbeitsmittel`);

// Map resources by prefix (e.g. '01')
const resourcesByPrefix = {};
resourceFiles.forEach(file => {
  const prefix = file.slice(0, 2);
  const raw = fs.readFileSync(path.join(RESOURCES_DIR, file), 'utf-8');
  const { frontmatter, body } = parseFrontmatter(raw);
  const slug = (frontmatter.slug || `/resources/${file.replace('.md', '')}`).replace('/resources/', '');
  resourcesByPrefix[prefix] = {
    file,
    slug,
    frontmatter,
    body
  };
});

// Process Articles
const articles = [];

articleFiles.forEach(file => {
  const prefix = file.slice(0, 2);
  const raw = fs.readFileSync(path.join(ARTICLES_DIR, file), 'utf-8');
  const { frontmatter, body } = parseFrontmatter(raw);

  const titleMatch = body.match(/^#\s+(.+)$/m);
  const title = frontmatter.meta_title?.split('|')[0]?.trim() || (titleMatch ? titleMatch[1] : file);
  const cleanSlug = (frontmatter.slug || `/wissen/${file.replace('.md', '')}`).replace('/wissen/', '').replace(/^\/+/, '');
  const catInfo = CATEGORY_MAP[prefix] || { category: 'notfall', label: 'Ratgeber' };

  // Calculate estimated reading time
  const wordCount = body.split(/\s+/).length;
  const readTimeMin = Math.max(4, Math.ceil(wordCount / 180));

  const matchedResource = resourcesByPrefix[prefix] || null;

  articles.push({
    file,
    prefix,
    slug: cleanSlug,
    title,
    category: catInfo.category,
    categoryLabel: catInfo.label,
    readTimeMin,
    wordCount,
    frontmatter,
    body,
    resource: matchedResource
  });
});

// 2. Generate Article Pages in /wissen/<slug>.html
articles.forEach(art => {
  const { contentHtml, headings, referencesHtml } = formatMarkdown(art.body, {
    isArticle: true,
    currentSlug: art.slug
  });

  // Build TOC
  let tocHtml = '';
  if (headings.length > 0) {
    tocHtml = `
      <aside class="article-sidebar">
        <div class="toc-title">Inhaltsverzeichnis</div>
        <ul class="toc-list">
          ${headings.filter(h => h.level === 2).map(h => `<li><a href="#${h.id}">${h.title}</a></li>`).join('\n')}
          ${referencesHtml ? '<li><a href="#quellen-und-referenzen">Quellen &amp; Referenzen</a></li>' : ''}
        </ul>
      </aside>
    `;
  }

  // Resource Box HTML
  let resourceBoxHtml = '';
  if (art.resource) {
    const resTitle = art.resource.frontmatter.titel || art.resource.frontmatter.meta_title || 'Arbeitsvorlage & Notfall-Checkliste';
    const resDesc = art.resource.frontmatter.meta_description || 'Strukturierte Checkliste für Schweizer KMU zur Dokumentation und Erstreaktion.';
    resourceBoxHtml = `
      <div class="article-resource-box">
        <div class="resource-box-content">
          <h4>📥 Passendes Arbeitsmittel: ${resTitle}</h4>
          <p>${resDesc}</p>
        </div>
        <a href="./resources/${art.resource.slug}.html" class="resource-btn">
          <span>🖨️ Arbeitsvorlage öffnen</span>
          <span>&rarr;</span>
        </a>
      </div>
    `;
  }

  const html = `<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${art.frontmatter.meta_title || `${art.title} | DKSchV Schweiz`}</title>
  <meta name="description" content="${art.frontmatter.meta_description || ''}">
  <link rel="canonical" href="https://www.dkschv.ch/wissen/${art.slug}.html">
  <link rel="icon" type="image/png" href="../assets/images/dkschv_icon.png">
  <link rel="stylesheet" href="../assets/css/style.css">
  
  <!-- OpenGraph -->
  <meta property="og:title" content="${art.title}">
  <meta property="og:description" content="${art.frontmatter.meta_description || ''}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://www.dkschv.ch/wissen/${art.slug}.html">
  <meta property="article:published_time" content="${art.frontmatter.veröffentlichungsdatum || '2026-11-01'}">
  <meta property="article:author" content="DKSchV Redaktion">

  <!-- Schema.org Article JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "${art.title.replace(/"/g, '\\"')}",
    "description": "${(art.frontmatter.meta_description || '').replace(/"/g, '\\"')}",
    "inLanguage": "de-CH",
    "mainEntityOfPage": "https://www.dkschv.ch/wissen/${art.slug}.html",
    "author": {
      "@type": "Organization",
      "name": "DKSchV Dini Cyber-Security",
      "url": "https://www.dkschv.ch"
    },
    "publisher": {
      "@type": "Organization",
      "name": "DKSchV Schweiz",
      "logo": {
        "@type": "ImageObject",
        "url": "https://www.dkschv.ch/assets/images/dkschv_logo.png"
      }
    },
    "datePublished": "${art.frontmatter.veröffentlichungsdatum || '2026-11-01'}",
    "dateModified": "${art.frontmatter.stand || '2026-11-08'}"
  }
  </script>
</head>
<body>
  <div class="reading-progress-bar"></div>
  ${renderHeader('wissen', '..')}

  <!-- Article Page Header -->
  <header class="article-page-header">
    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="../index.html">Home</a>
        <span class="sep">/</span>
        <a href="../wissen.html">Wissen &amp; Ratgeber</a>
        <span class="sep">/</span>
        <span style="color:#ffffff;">${art.categoryLabel}</span>
      </nav>

      <span class="category-tag" style="margin-bottom: 16px;">${art.categoryLabel}</span>
      <h1 class="article-page-title">${art.title}</h1>

      <div class="article-page-meta">
        <span class="article-meta-item">📅 Stand: <strong>${art.frontmatter.stand || 'November 2026'}</strong></span>
        <span class="article-meta-item">⏱️ Lesezeit: <strong>ca. ${art.readTimeMin} Min.</strong></span>
        <span class="article-meta-item">🇨🇭 Fokus: <strong>Schweizer KMU (nDSG / BACS)</strong></span>
        <span class="article-meta-item">✍️ Redaktion: <strong>DKSchV Fachredaktion</strong></span>
      </div>
    </div>
  </header>

  <!-- Article Main Content -->
  <main class="container">
    <div class="article-container">
      <article class="article-content">
        ${resourceBoxHtml}
        ${contentHtml}
        ${referencesHtml}
        
        <!-- Post-article consultation box -->
        <div style="margin-top: 48px; background: #0f172a; border-radius: var(--radius-lg); padding: 36px; color: #ffffff; display: flex; flex-direction: column; gap: 16px;">
          <span class="badge badge-teal" style="align-self: flex-start;">Individuelle Schweizer Sicherheitsberatung</span>
          <h3 style="font-size: 22px; font-weight: 700; color: #ffffff; margin: 0;">Benötigen Sie Unterstützung bei der Umsetzung?</h3>
          <p style="font-size: 15px; color: #cbd5e1; margin: 0; line-height: 1.6;">
            Ob fundierte Sicherheitsanalyse, Microsoft 365 Cloud-Audit oder die Vorbereitung eines massgeschneiderten IT-Notfallplans: Wir unterstützen Sie pragmatisch und diskret im Wallis und der gesamten Schweiz.
          </p>
          <div style="display: flex; gap: 14px; flex-wrap: wrap; margin-top: 8px;">
            <a href="../kontakt.html" class="btn btn-primary" style="background: var(--teal-accent);">Kostenloses Erstgespräch anfragen &rarr;</a>
            <a href="../notfallplanung.html" class="btn btn-secondary" style="border-color: #334155; color: #ffffff;">Notfallplanung für KMU</a>
          </div>
        </div>
      </article>

      ${tocHtml}
    </div>
  </main>

  ${renderFooter('..')}
</body>
</html>`;

  fs.writeFileSync(path.join(WISSEN_DIR, `${art.slug}.html`), html);
});

console.log(`✅ ${articles.length} Fachartikel unter wissen/<slug>.html generiert`);

// 3. Generate Printable Resource Pages in /wissen/resources/<slug>.html
Object.values(resourcesByPrefix).forEach(res => {
  const { contentHtml } = formatMarkdown(res.body, { isArticle: false, isResource: true });
  const parentArticle = articles.find(a => a.prefix === res.file.slice(0, 2));
  const resTitle = res.frontmatter.titel || res.frontmatter.meta_title || 'Arbeitsvorlage';

  const html = `<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${res.frontmatter.meta_title || `${resTitle} | DKSchV Schweiz`}</title>
  <meta name="description" content="${res.frontmatter.meta_description || ''}">
  <link rel="icon" type="image/png" href="../../assets/images/dkschv_icon.png">
  <link rel="stylesheet" href="../../assets/css/style.css">
  <style>
    /* Print-specific tweaks */
    @page { margin: 1.5cm; }
  </style>
</head>
<body style="background: var(--bg-light);">

  <!-- Printable Action Bar -->
  <div class="resource-top-bar no-print">
    <div class="container resource-bar-inner">
      <div>
        ${parentArticle ? `<a href="../${parentArticle.slug}.html" style="color: #cbd5e1; text-decoration: none; font-size: 13.5px; font-weight: 500;">&larr; Zurück zum Fachleitfaden</a>` : '<a href="../../wissen.html" style="color: #cbd5e1; text-decoration: none; font-size: 13.5px;">&larr; Zum Wissensportal</a>'}
      </div>
      <div style="display: flex; gap: 12px; align-items: center;">
        <span style="font-size: 12.5px; color: #94a3b8;">Format: DIN A4 Druckvorlage</span>
        <button onclick="window.print()" class="btn-print">
          <span>🖨️ Arbeitsblatt drucken / PDF</span>
        </button>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="resource-sheet">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid var(--border); padding-bottom: 20px; margin-bottom: 28px;">
        <div>
          <span style="font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; color: var(--teal-accent);">
            DKSchV Schweiz · Dokumentiertes Arbeitsmittel
          </span>
          <h1 style="font-size: 26px; font-weight: 800; color: var(--text-dark); margin: 6px 0 8px;">
            ${resTitle}
          </h1>
          <p style="font-size: 13.5px; color: var(--text-muted); margin: 0;">
            ${res.frontmatter.version || res.frontmatter.stand || 'Stand: November 2026'} · Zielgruppe: Schweizer KMU Geschäftsleitungen &amp; IT
          </p>
        </div>
        <img src="../../assets/images/dkschv_logo.png" alt="DKSchV Schweiz" style="height: 34px;">
      </div>

      <div class="article-content" style="font-size: 15px;">
        ${contentHtml}
      </div>

      <div style="margin-top: 48px; padding-top: 20px; border-top: 1px solid var(--border); display: flex; justify-content: space-between; font-size: 11px; color: #94a3b8;">
        <div>DKSchV Dini · Bammattenweg 19, CH-3904 Naters · <a href="https://www.dkschv.ch" style="color: inherit;">www.dkschv.ch</a></div>
        <div>Vertrauliche Arbeitsunterlage · Rechts- &amp; Fachprüfung vorbehalten</div>
      </div>
    </div>
  </div>

</body>
</html>`;

  fs.writeFileSync(path.join(WISSEN_RESOURCES_DIR, `${res.slug}.html`), html);
});

console.log(`✅ ${Object.keys(resourcesByPrefix).length} druckbare Arbeitsvorlagen unter wissen/resources/<slug>.html generiert`);

// 4. Generate Weekly News Page in /wissen/news/2026-11-08-branchennews.html
const newsFiles = fs.readdirSync(NEWS_DIR).filter(f => f.endsWith('_DKSchV_Branchennews.md')).sort().reverse();
let latestNewsPoints = [];
let latestNewsTitle = 'DKSchV-Branchennews: Sonntagsausgabe';
let latestNewsDate = '08.11.2026';
let latestNewsFile = '';

if (newsFiles.length > 0) {
  latestNewsFile = newsFiles[0];
  const rawNews = fs.readFileSync(path.join(NEWS_DIR, latestNewsFile), 'utf-8');
  const { frontmatter, body } = parseFrontmatter(rawNews);
  latestNewsDate = frontmatter.datum || '08.11.2026';

  const { contentHtml, headings, referencesHtml } = formatMarkdown(body, { isArticle: false, isNews: true });

  // Extract quick highlights from H2s in news
  latestNewsPoints = headings.filter(h => h.level === 2 && !h.title.includes('Vormerkung') && !h.title.includes('References')).slice(0, 4);

  const newsHtml = `<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cyber-Security Branchennews KW 45 (${latestNewsDate}) | DKSchV Schweiz</title>
  <meta name="description" content="Wöchentliche Lagebeurteilung für Schweizer KMU: SonicWall SAML-Bypass, Microsoft Secret-Hunting, EHRA-Phishing und EDÖB-Urteil.">
  <link rel="icon" type="image/png" href="../../assets/images/dkschv_icon.png">
  <link rel="stylesheet" href="../../assets/css/style.css">
</head>
<body>
  ${renderHeader('wissen', '../..')}

  <header class="article-page-header">
    <div class="container">
      <nav class="breadcrumbs" aria-label="Breadcrumb">
        <a href="../../index.html">Home</a>
        <span class="sep">/</span>
        <a href="../../wissen.html">Wissen &amp; Ratgeber</a>
        <span class="sep">/</span>
        <span style="color:#ffffff;">Wochenausgabe KW 45</span>
      </nav>

      <span class="news-badge"><span class="news-pulse-dot"></span> Sonntagsausgabe · ISO-KW 45</span>
      <h1 class="article-page-title">DKSchV-Branchennews: Wöchentliche Lage für Schweizer KMU</h1>
      <div class="article-page-meta">
        <span class="article-meta-item">📅 Ausgabedatum: <strong>${latestNewsDate}</strong></span>
        <span class="article-meta-item">🇨🇭 Fokus: <strong>Schweiz, BACS, EDÖB &amp; KMU-Prüfpunkte</strong></span>
        <span class="article-meta-item">⏱️ Lesezeit: <strong>5 Min.</strong></span>
      </div>
    </div>
  </header>

  <main class="container">
    <div class="article-container" style="grid-template-columns: 1fr;">
      <article class="article-content" style="max-width: 860px; margin: 0 auto;">
        ${contentHtml}
        ${referencesHtml}
        
        <div style="margin-top: 40px; text-align: center;">
          <a href="../../wissen.html" class="btn btn-secondary">&larr; Zurück zur Übersicht aller Ratgeber &amp; Checklisten</a>
        </div>
      </article>
    </div>
  </main>

  ${renderFooter('../..')}
</body>
</html>`;

  fs.writeFileSync(path.join(WISSEN_NEWS_DIR, '2026-11-08-branchennews.html'), newsHtml);
  fs.writeFileSync(path.join(WISSEN_NEWS_DIR, 'index.html'), newsHtml);
  console.log('✅ Wöchentliche Branchennews unter wissen/news/2026-11-08-branchennews.html generiert');
}

// 5. Generate Knowledge Hub Catalog: wissen.html & wissen/index.html
function generateCatalogHtml(relativeRoot = '.') {
  return `<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wissen &amp; Ratgeber: Cyber-Security &amp; Datenschutz für Schweizer KMU | DKSchV</title>
  <meta name="description" content="Verifizierte Leitfäden, Notfall-Checklisten, Microsoft 365 Best Practices und nDSG/BACS-Entscheidungshilfen für Geschäftsführer und IT-Verantwortliche in der Schweiz.">
  <link rel="canonical" href="https://www.dkschv.ch/wissen.html">
  <link rel="icon" type="image/png" href="${relativeRoot}/assets/images/dkschv_icon.png">
  <link rel="stylesheet" href="${relativeRoot}/assets/css/style.css">
</head>
<body>
  ${renderHeader('wissen', relativeRoot)}

  <!-- Hero Section -->
  <section class="hub-hero">
    <div class="container">
      <div class="hub-hero-badge">
        <span>🇨🇭</span>
        <span>Praxiswissen für Schweizer KMU &amp; Verwaltungsräte</span>
      </div>
      <h1 class="hub-hero-title">
        Wissen &amp; Ratgeber: Cyber-Security &amp; Datenschutz
      </h1>
      <p class="hub-hero-lead">
        Klare Handlungsanleitungen, verifizierte Rechtsgrundlagen nach neuem Schweizer Datenschutzgesetz (nDSG) und BACS-Meldepflicht sowie sofort einsetzbare Notfall-Checklisten für Ihre Organisation.
      </p>

      <!-- Search & Filters -->
      <div class="hub-toolbar">
        <div class="hub-search-wrapper">
          <svg class="hub-search-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" id="hubSearchInput" class="hub-search-input" placeholder="Nach Thema suchen (z. B. Ransomware, Backups, M365, EDÖB, NIS2)..." aria-label="Ratgeber durchsuchen">
        </div>

        <div class="hub-filter-chips">
          <button class="filter-chip active" data-filter="all">Alle Themen (${articles.length})</button>
          <button class="filter-chip" data-filter="notfall">Ransomware &amp; Notfall</button>
          <button class="filter-chip" data-filter="cloud">Cloud &amp; Microsoft 365</button>
          <button class="filter-chip" data-filter="datenschutz">Datenschutz &amp; nDSG</button>
          <button class="filter-chip" data-filter="backup">Backup &amp; Resilienz</button>
          <button class="filter-chip" data-filter="governance">Audit &amp; Compliance</button>
          <button class="filter-chip" data-filter="ki">Künstliche Intelligenz</button>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Content Area -->
  <main class="section" style="padding-top: 48px;">
    <div class="container">

      <!-- Sunday News Highlight -->
      <div class="news-highlight-card">
        <div class="news-badge">
          <span class="news-pulse-dot"></span>
          <span>Wochenlage Sonntagsausgabe · KW 45 (${latestNewsDate})</span>
        </div>
        <h2 class="news-title">Aktuelle Schweizer Cyber-Security Branchennews</h2>
        <p style="font-size: 14.5px; color: #cbd5e1; max-width: 820px; line-height: 1.6; margin-bottom: 16px;">
          Wöchentlicher Lagebericht für Schweizer KMU: Wichtige Warnungen von BACS und EDÖB, KEV-Aufnahmen und konkrete Handlungspunkte für Geschäftsleitungen.
        </p>

        <div class="news-points">
          <div class="news-point-item">
            <span>🛡️</span>
            <div><strong>SonicWall VPN:</strong> CISA KEV Aufnahme für SAML-Bypass; Modell- und Patchstände prüfen.</div>
          </div>
          <div class="news-point-item">
            <span>🔍</span>
            <div><strong>Schatten-Secrets:</strong> KI-gestützte Secret-Jagd bedroht Azure/M365 Tokens &amp; Repositories.</div>
          </div>
          <div class="news-point-item">
            <span>⚠️</span>
            <div><strong>EHRA-Phishing:</strong> BACS warnt vor gefälschten Handelsregister-Aktualisierungsmails.</div>
          </div>
          <div class="news-point-item">
            <span>⚖️</span>
            <div><strong>EDÖB / SkySale:</strong> Bundesverwaltungsgericht bestätigt Betroffenen-Informationspflicht.</div>
          </div>
        </div>

        <a href="${relativeRoot === '.' ? 'wissen/news/2026-11-08-branchennews.html' : './news/2026-11-08-branchennews.html'}" class="btn btn-primary" style="background: var(--teal-accent); display: inline-flex; align-items: center; gap: 8px;">
          <span>Vollständige Sonntagsausgabe lesen</span>
          <span>&rarr;</span>
        </a>
      </div>

      <!-- Section Title -->
      <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 24px; flex-wrap: wrap; gap: 16px;">
        <div>
          <h2 style="font-size: 26px; font-weight: 800; color: var(--text-dark); margin-bottom: 6px;">
            Fundierte Fachbeiträge &amp; Handlungsanleitungen
          </h2>
          <p style="font-size: 15px; color: var(--text-muted); margin: 0;">
            Alle Artikel basieren auf geprüften Primärquellen (BACS, Fedlex, EDÖB, NIST, CISA) mit Stand November 2026.
          </p>
        </div>
        <div style="font-size: 13.5px; color: var(--text-muted); font-weight: 500;">
          Gesamt: <strong>${articles.length} Fachartikel</strong> mit Arbeitsvorlagen
        </div>
      </div>

      <!-- No Results State -->
      <div id="hubNoResults" style="display: none; padding: 60px 20px; text-align: center; background: var(--bg-light); border-radius: var(--radius-md); border: 1px dashed var(--border);">
        <p style="font-size: 18px; font-weight: 700; color: var(--text-dark); margin-bottom: 8px;">Keine Artikel zu diesem Suchbegriff gefunden</p>
        <p style="font-size: 14.5px; color: var(--text-muted); margin: 0;">Versuchen Sie es mit einem anderen Begriff wie «MFA», «Ransomware», «Backups» oder «EDÖB».</p>
      </div>

      <!-- Articles Grid -->
      <div class="articles-grid">
        ${articles.map(art => {
          const articleUrl = relativeRoot === '.' ? `wissen/${art.slug}.html` : `./${art.slug}.html`;
          const resourceUrl = relativeRoot === '.' ? `wissen/resources/${art.resource?.slug}.html` : `./resources/${art.resource?.slug}.html`;
          const keywords = `${art.frontmatter.hauptkeyword || ''} ${art.frontmatter.suchintention || ''} ${art.categoryLabel}`;

          return `
          <article class="hub-article-card" data-category="${art.category}" data-keywords="${keywords}">
            <div class="card-top-meta">
              <span class="category-tag">${art.categoryLabel}</span>
              <span class="read-time">⏱️ ${art.readTimeMin} Min.</span>
            </div>

            <h3 class="card-title">
              <a href="${articleUrl}">${art.title}</a>
            </h3>

            <p class="card-description">
              ${art.frontmatter.meta_description || ''}
            </p>

            ${art.resource ? `
            <div class="card-resource-pill">
              <span>📄</span>
              <span>Inkl. Arbeitsmittel: ${art.resource.frontmatter.titel ? art.resource.frontmatter.titel.slice(0, 32) + '...' : 'Checkliste'}</span>
            </div>
            ` : ''}

            <div class="card-footer-meta">
              <span>Stand: ${art.frontmatter.stand || 'Nov. 2026'}</span>
              <a href="${articleUrl}" class="card-read-link">
                <span>Leitfaden lesen</span>
                <span>&rarr;</span>
              </a>
            </div>
          </article>
          `;
        }).join('\n')}
      </div>

      <!-- Downloadable Worksheets Directory Section -->
      <div style="margin-top: 72px; background: var(--bg-light); border: 1px solid var(--border); border-radius: var(--radius-xl); padding: 40px;">
        <div style="max-width: 680px; margin-bottom: 28px;">
          <span class="badge badge-teal" style="margin-bottom: 12px;">Druckfertige Vorlagen</span>
          <h3 style="font-size: 24px; font-weight: 800; color: var(--text-dark); margin-bottom: 10px;">
            Notfall-Checklisten, Protokolle &amp; Entscheidungshilfen
          </h3>
          <p style="font-size: 15px; color: var(--text-muted); line-height: 1.6; margin: 0;">
            Alle Arbeitsmittel sind für den Ausdruck optimiert (DIN A4) und können direkt im Ernstfall handschriftlich oder digital zur Triage und Beweissicherung verwendet werden.
          </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px;">
          ${articles.filter(a => a.resource).map(a => {
            const res = a.resource;
            const resUrl = relativeRoot === '.' ? `wissen/resources/${res.slug}.html` : `./resources/${res.slug}.html`;
            const title = res.frontmatter.titel || a.title;
            return `
            <a href="${resUrl}" style="background: #ffffff; border: 1px solid var(--border); border-radius: var(--radius-md); padding: 18px; text-decoration: none; color: inherit; display: flex; flex-direction: column; justify-content: space-between; transition: var(--transition);" onmouseover="this.style.borderColor='var(--teal-accent)'" onmouseout="this.style.borderColor='var(--border)'">
              <div style="font-weight: 700; font-size: 14.5px; color: var(--text-dark); margin-bottom: 8px; line-height: 1.4;">
                ${title}
              </div>
              <div style="font-size: 12px; color: var(--teal-accent); font-weight: 600; display: flex; align-items: center; gap: 4px;">
                <span>🖨️ Druckbare Vorlage</span>
                <span>&rarr;</span>
              </div>
            </a>
            `;
          }).join('\n')}
        </div>
      </div>

      <!-- Advisory CTA Banner -->
      <div style="margin-top: 56px; background: linear-gradient(135deg, #0a0f1d 0%, #1e293b 100%); border-radius: var(--radius-xl); padding: 48px; color: #ffffff; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 32px;">
        <div style="max-width: 620px;">
          <h3 style="font-size: 26px; font-weight: 800; color: #ffffff; margin-bottom: 12px;">
            Haben Sie offene Fragen zu Ihrem Cyber-Sicherheitsniveau?
          </h3>
          <p style="font-size: 16px; color: #cbd5e1; line-height: 1.6; margin: 0;">
            Wir analysieren Ihre IT-Infrastruktur unabhängig, objektiv und nach anerkannten Schweizer Massstäben. Vereinbaren Sie ein vertrauliches Beratungsgespräch.
          </p>
        </div>
        <div>
          <a href="${relativeRoot}/kontakt.html" class="btn btn-primary" style="background: var(--teal-accent); font-size: 15px; padding: 14px 28px;">
            Sicherheitsaudit anfragen &rarr;
          </a>
        </div>
      </div>

    </div>
  </main>

  ${renderFooter(relativeRoot)}
</body>
</html>`;
}

// Copy assets into wissen/assets so the directory is completely self-contained
const WISSEN_ASSETS_DIR = path.join(WISSEN_DIR, 'assets');
fs.cpSync(path.join(ROOT_DIR, 'assets'), WISSEN_ASSETS_DIR, { recursive: true });
console.log('✅ Assets in wissen/assets synchronisiert (eigenständiges Verzeichnis)');

// Write wissen/index.html as canonical directory index
fs.writeFileSync(path.join(WISSEN_DIR, 'index.html'), generateCatalogHtml('..'));

// Write root wissen.html as redirect / fallback to wissen/
const rootWissenRedirect = `<!DOCTYPE html>
<html lang="de-CH">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=wissen/">
  <link rel="canonical" href="https://www.dkschv.ch/wissen/">
  <title>Wissen &amp; Ratgeber | DKSchV Schweiz</title>
  <script>window.location.replace("wissen/");</script>
</head>
<body style="font-family: -apple-system, sans-serif; padding: 40px; text-align: center;">
  <h2>Weiterleitung zum Wissensportal...</h2>
  <p>Falls Sie nicht automatisch weitergeleitet werden, klicken Sie bitte hier: <a href="wissen/">https://www.dkschv.ch/wissen/</a></p>
</body>
</html>`;
fs.writeFileSync(path.join(ROOT_DIR, 'wissen.html'), rootWissenRedirect);
console.log('✅ wissen/index.html und Weiterleitung wissen.html erfolgreich generiert');

// 6. Automatically Update Navigation in All Root HTML Pages
const ROOT_PAGES = [
  'index.html',
  'sicherheitsanalyse.html',
  'risikomanagement.html',
  'notfallplanung.html',
  'ueber-uns.html',
  'kontakt.html',
  'impressum.html',
  'datenschutz.html'
];

let updatedPagesCount = 0;
ROOT_PAGES.forEach(filename => {
  const filePath = path.join(ROOT_DIR, filename);
  if (!fs.existsSync(filePath)) return;

  let html = fs.readFileSync(filePath, 'utf-8');
  let changed = false;

  // Replace wissen.html with clean directory wissen/
  if (html.includes('href="wissen.html"')) {
    html = html.replace(/href="wissen\.html"/g, 'href="wissen/"');
    changed = true;
  }

  // If missing entirely, insert after notfallplanung
  if (!html.includes('href="wissen/"')) {
    const targetTag = '<li><a href="notfallplanung.html" class="nav-link">Notfallplanung</a></li>';
    const targetTagActive = '<li><a href="notfallplanung.html" class="nav-link active">Notfallplanung</a></li>';

    if (html.includes(targetTag)) {
      html = html.replace(targetTag, `${targetTag}\n          <li><a href="wissen/" class="nav-link">Wissen &amp; Ratgeber</a></li>`);
      changed = true;
    } else if (html.includes(targetTagActive)) {
      html = html.replace(targetTagActive, `${targetTagActive}\n          <li><a href="wissen/" class="nav-link">Wissen &amp; Ratgeber</a></li>`);
      changed = true;
    }

    const footerTarget = '<li><a href="notfallplanung.html">Notfallplanung</a></li>';
    if (html.includes(footerTarget)) {
      html = html.replace(footerTarget, `${footerTarget}\n            <li><a href="wissen/">Wissen &amp; Ratgeber</a></li>`);
      changed = true;
    }
  }

  if (changed) {
    fs.writeFileSync(filePath, html);
    updatedPagesCount++;
  }
});

console.log(`✅ Navigation in ${updatedPagesCount} bestehenden HTML-Seiten aktualisiert`);
console.log('🎉 Build vollständig abgeschlossen!');
