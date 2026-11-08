# DKSchV-Laufstatus – 8. November 2026, ISO-KW45

Die [Sonntagsnews](2026-11-08_DKSchV_Branchennews.md) enthalten sechs priorisierte Entwicklungen aus geöffneten Primärquellen. In der ungeraden KW45 wurde **keine neue reguläre Vollpflege der zwölf Artikelpaare** durchgeführt. Die nächste ist am **15.11.2026, KW46** fällig. Die neuen Quellen und artikelbezogenen Vormerkungen liegen unter `qa/2026-11-08/`.

## Nachgeholter Abschluss des KW44-Laufs

Der unterbrochene Lauf vom 01.11. hatte zwölf lokal aktualisierte Artikel-/Arbeitsmittelpaare und Einzelberichte hinterlassen, aber ein nicht synchronisiertes CMS-Manifest. Der erste Validatorlauf vom 08.11. fand deshalb **zwölf Fehler**, jeweils einen abweichenden Quellenstand pro Artikel. Der lokale Abgleich wurde heute nachgeholt; der Quellenstand bleibt **1. November 2026**, nicht 8. November. Die [Abschlussvalidierung](qa/2026-11-08/validator-ergebnis.txt) bestätigt jetzt **0 Fehler und 0 Warnungen** für zwölf Artikel, zwölf Arbeitsmittel und die Importdaten. Das ist keine Fach- oder Publikationsfreigabe.

Am Artikel 12 und der NIS2-/DORA-Matrix wurde ausschliesslich die bereits am 01.11. belegte ISG-Fassungskorrektur übernommen: aktuelle amtliche XML-Fassung **1. Oktober 2025** statt älterer April-Fassung. Quellenumfang und -status wurden entsprechend präzisiert, der historische Erstabruf blieb im Journal erhalten. Keine neue materielle Rechtseinordnung, keine neue Vollprüfung am 08.11. Die Details stehen im [gezielten Nachtrag](qa/2026-11-08/kw44-isg-nachtrag.md). Die übrigen 22 Artikel-/Arbeitsmitteldateien wurden heute nicht geändert. SEO-Importfelder, Veröffentlichungstermine, Entwurfsstatus und alle bisherigen Fachmarker bleiben erhalten.

Das [Wartungsmanifest](../blog-paket/maintenance-manifest.md), die Paketdokumentation und das [lokale CMS-Importmanifest](../blog-paket/cms-import-manifest.csv) zeigen den tatsächlichen Quellen- und Abschlussstand. Die zwölf Einzelberichte vom 01.11. bleiben die Grundlage der fachlichen und redaktionellen Änderungen.

## Live-Synchronisierung blockiert

Der [heutige CMS-Test](qa/2026-11-08/cms-zugangsstatus.md) zeigte gegen 09:04 CET die Webador-Anmeldeseite statt einer authentifizierten DKSchV-Pro-Sitzung. Gespeicherte Zugänge sind in dieser Umgebung nicht zugreifbar. Kein Editor wurde verändert, kein geschützter Import gestartet und kein Beitrag veröffentlicht. Normale Webador-Änderungen würden sofort live gehen.

Der [öffentliche Linkchecker](qa/2026-11-08/public-link-check.csv) erhielt für alle 28 geprüften Pfade **HTTP403**, auch für bestehende Service-/Kontaktziele. Ein separater Inhaltsabruf der Kontaktseite war erfolgreich; die Ransomware-Artikeladresse lieferte keinen auslesbaren Inhalt. Deshalb ist weder ein erfolgreicher Artikel-Go-live noch ein neuer 404-Befund nachgewiesen. Die Ursache des verweigerten HTTP-Zugriffs ist offen. Die älteren 404-Messungen dürfen nicht als heutige Statuswerte ausgegeben werden.

**Live-Änderungsprotokoll:** Keine Einträge; keine Live-Änderung, keine neu veröffentlichte URL und kein Importerfolg.

## Terminlich fällige Beiträge und genaue Fachblocker

**01 – Ransomware, vorgesehen 01.10.:** Organisationsbezogene BACS-Unterstellung, Ausnahmen, Angriffstatbestand und Entdeckungszeitpunkt sowie EDÖB-Risiko/Meldung/Betroffeneninformation sind offen. Forensik, Beweissicherung, Bereinigung und sicherer Wiederanlauf sind nicht konkret freigegeben.

**02 – CEO-Betrug/BEC, vorgesehen 08.10.:** Personen- und Vorfallbezug, Meldepflichten, Mailbox-/Sitzungs-/MFA-/Weiterleitungsprüfung sowie Zahlungsgrenzen, Freigaberollen und verlässliche Bank-/Lieferantenkontakte sind nicht organisationsbezogen geprüft.

**03 – Datenpanne, vorgesehen 15.10.:** Hohes Risiko nach DSG Art. 24, erforderliche Betroffeneninformation, Verantwortlichen-/Auftragsbearbeiterrollen und Datenflüsse sowie BACS-Unterstellung, CSV-Ausnahmen und Angriffstatbestand bleiben Einzelfallfragen.

**04 – Backups, vorgesehen 22.10.:** Konkrete Architektur, Object Lock, Schlüssel, Rechte, Aufbewahrung/Löschung und Dienstleisterverträge sind nicht freigegeben. Die Einhaltung von RPO/RTO ist nur mit dokumentiertem Restore-Test der tatsächlichen Umgebung nachweisbar.

**05 – MFA/Passkeys, vorgesehen 29.10.:** Benutzerpopulationen, Lizenzen, Conditional Access, Passkey-/TAP-/Notfallzugangstests sind offen. Die am 01.11. geprüfte CYOT-GA gilt nur im dokumentierten Herstellerumfang; Schweizer Providerabdeckung, Verträge, Kosten, Azure-Voraussetzungen, Datenschutz, Zustellung und Failover sind nicht bestätigt.

**06 – Microsoft365, vorgesehen 05.11.:** Keine konkrete Prüfung von Tenant, Application IDs, Dienstprinzipalen, Consent, Berechtigungen, Protokollen, Lizenzen, Notfallkonten oder Lieferantenintegration. Beweissicherung, Eindämmung und Credential-/Tokenbehandlung erfordern zuständige Fachstellen; kein eigener Kompromittierungsbefund.

Die Beiträge 07–12 sind am 08.11. noch nicht terminlich fällig und ebenfalls nicht freigegeben. Ihre detaillierten offenen Architektur-, KI-/Datenschutz-, Kommunikations-, Lieferanten- beziehungsweise EU-Rechtsfragen stehen im [Pflegebericht mit zwölf Einzelprotokollen](../reviews/2026-11-01/DKSchV_Pflegebericht_KW44.md). Für Artikelverbund 11 bleibt zusätzlich der am 01.11. dokumentierte generische HTTP403-Abruf einer kanadischen KI-Quelle zu klären; der damalige Inhaltsabruf war lesbar. Dieser Unterschied ist keine erfüllte Go-live-Erreichbarkeitsprüfung.

## Vormerkungen für 15. November

Die fünf Newsfeld-Berichte halten die konkreten nächsten Prüfpunkte fest: SonicWall-Plattformmatrix und KEV-Revisionen; WordPress-Backports und aktuelle Apple-Sicherheitsstände; Microsoft-App-Identitäten, historische Secret-Nutzung und Sicherheitsausnahmen; EHRA-Imitation und Homeoffice-Dienste; die EDÖB-Mitteilung samt Urteil A-3790/2024 zur Betroffeneninformation. Eine öffentliche Bekanntmachung ist daraus nicht als allgemeine KMU-Pflicht abzuleiten.

Die neue NIST-Agentenidentitätsorientierung vom 27.10. aus KW44 ist bei der KI-Artikelpflege weiterhin mit den schon bestehenden produktneutralen Kontrollen abzugleichen. Sie ist ein Vorschlag, keine Schweizer Norm. Der heutige begrenzte Lauf hat keine weitere eigenständige KI- oder EU-Regelwerksneuigkeit belegt; fehlende Neuigkeit ist kein vollständiger Nichtfundnachweis.
