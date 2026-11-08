/**
 * DKSchV Schweiz · Automatischer Sonntags-Paket Importer
 * 
 * Verarbeitet die wöchentlichen Manus-ZIP-Dateien automatisch:
 * 1. Erkennt neue ZIP-Archive in ~/Downloads (z.B. per KDE Connect empfangen)
 * 2. Entpackt Artikel, Arbeitsmittel und Branchennews nach content/
 * 3. Führt den statischen Knowledge Hub Builder aus
 * 4. Erstellt auf Wunsch direkt das fertige Deployment-Archiv für Infomaniak
 * 
 * Aufruf:
 *   node scripts/import-sunday-package.mjs [pfad-zur-zip-datei]
 */

import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import os from 'os';

const ROOT_DIR = path.resolve(import.meta.dirname, '..');
const DOWNLOADS_DIR = path.join(os.homedir(), 'Downloads');
const CONTENT_DIR = path.join(ROOT_DIR, 'content');

console.log('📦 DKSchV Sonntags-Paket Import gestartet...');

// 1. Finde ZIP-Datei
let zipPath = process.argv[2];

if (!zipPath) {
  if (fs.existsSync(DOWNLOADS_DIR)) {
    const candidateFiles = fs.readdirSync(DOWNLOADS_DIR)
      .filter(f => f.endsWith('.zip') && (f.includes('DKSchV') || f.includes('News') || f.includes('KW')))
      .map(f => {
        const full = path.join(DOWNLOADS_DIR, f);
        return { file: f, path: full, mtime: fs.statSync(full).mtimeMs };
      })
      .sort((a, b) => b.mtime - a.mtime);

    if (candidateFiles.length > 0) {
      zipPath = candidateFiles[0].path;
      console.log(`🔍 Neuestes Paket in Downloads gefunden: ${path.basename(zipPath)}`);
    }
  }
}

if (!zipPath || !fs.existsSync(zipPath)) {
  console.log('ℹ️ Keine neue ZIP-Datei angegeben oder in ~/Downloads gefunden.');
  console.log('👉 Führe stattdessen Re-Build des bestehenden Inhalts aus...');
} else {
  console.log(`📂 Entpacke Paket: ${zipPath}`);
  const tempExtractDir = path.join(os.tmpdir(), `dkschv-import-${Date.now()}`);
  fs.mkdirSync(tempExtractDir, { recursive: true });

  try {
    execSync(`unzip -q -o "${zipPath}" -d "${tempExtractDir}"`);

    // Suche nach articles, resources, news
    function copyIfExists(srcSub, destSub) {
      const candidates = [
        path.join(tempExtractDir, srcSub),
        path.join(tempExtractDir, 'content', srcSub),
        path.join(tempExtractDir, 'blog-paket', srcSub),
      ];

      for (const cand of candidates) {
        if (fs.existsSync(cand) && fs.statSync(cand).isDirectory()) {
          const dest = path.join(CONTENT_DIR, destSub);
          fs.mkdirSync(dest, { recursive: true });
          fs.cpSync(cand, dest, { recursive: true });
          console.log(`  ✓ Kopiert: ${path.basename(cand)} -> content/${destSub}`);
          return true;
        }
      }
      return false;
    }

    // Copy articles & resources
    copyIfExists('articles', 'blog-paket/articles');
    copyIfExists('resources', 'blog-paket/resources');
    copyIfExists('news', 'news');

    // Also look for root .md news files in extract dir
    const files = fs.readdirSync(tempExtractDir);
    files.forEach(f => {
      if (f.endsWith('_Branchennews.md') || f.endsWith('_News.md')) {
        const dest = path.join(CONTENT_DIR, 'news', f);
        fs.mkdirSync(path.dirname(dest), { recursive: true });
        fs.copyFileSync(path.join(tempExtractDir, f), dest);
        console.log(`  ✓ Branchennews kopiert: ${f}`);
      }
      if (f.endsWith('manifest.csv')) {
        fs.copyFileSync(path.join(tempExtractDir, f), path.join(CONTENT_DIR, 'blog-paket', 'cms-import-manifest.csv'));
        console.log(`  ✓ Manifest kopiert: ${f}`);
      }
    });

  } catch (err) {
    console.error('❌ Fehler beim Entpacken:', err.message);
  } finally {
    try {
      fs.rmSync(tempExtractDir, { recursive: true, force: true });
    } catch {}
  }
}

// 2. Build ausführen
console.log('\n🔨 Generiere Knowledge Hub HTML-Seiten neu...');
try {
  execSync(`node "${path.join(ROOT_DIR, 'scripts', 'build-knowledge-hub.mjs')}"`, { stdio: 'inherit' });
} catch (err) {
  console.error('❌ Fehler beim HTML-Build:', err.message);
  process.exit(1);
}

// 3. Deployment-Pakete vorbereiten
const deployFullArchive = path.join(ROOT_DIR, 'dkschv-website-deploy.zip');
const deployWissenOnlyArchive = path.join(ROOT_DIR, 'wissen-ordner-deploy.zip');

try {
  if (fs.existsSync(deployFullArchive)) fs.unlinkSync(deployFullArchive);
  if (fs.existsSync(deployWissenOnlyArchive)) fs.unlinkSync(deployWissenOnlyArchive);

  // 1. Komplettes Website-Archiv
  execSync(`zip -q -r "${deployFullArchive}" index.html sicherheitsanalyse.html risikomanagement.html notfallplanung.html ueber-uns.html kontakt.html impressum.html datenschutz.html wissen.html assets wissen .htaccess`, { cwd: ROOT_DIR });

  // 2. Nur das Verzeichnis 'wissen' (eigenständig)
  execSync(`zip -q -r "${deployWissenOnlyArchive}" wissen`, { cwd: ROOT_DIR });

  console.log(`\n📦 Bereitgestellte Upload-Archive für Infomaniak:`);
  console.log(`   1. Komplett-Paket (inkl. Menü-Links & Assets):`);
  console.log(`      👉 ${deployFullArchive}`);
  console.log(`   2. Nur Verzeichnis 'wissen' (eigenständig ohne Rest der Website zu berühren):`);
  console.log(`      👉 ${deployWissenOnlyArchive}`);
} catch (err) {
  console.warn('⚠️ Warnung beim Erstellen der Deploy-Zips:', err.message);
}

console.log('\n🎉 Fertig! Die Website und alle Blogbeiträge sind aktualisiert.');
