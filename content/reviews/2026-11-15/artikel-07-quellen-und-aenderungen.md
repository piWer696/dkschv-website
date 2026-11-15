# Artikel 07 – Quellen- und Änderungsprüfung

**Prüfdatum:** 15. November 2026, ISO-KW 46, Europe/Zurich CET.  
**Tatsächliche Abrufe:** Erste Suchrückgabe 09:06:14 CET; Originalrückgaben 09:06:11–09:08:59 CET. Lokale Lektüre der vollständigen bzw. dekodierten Quellen zwischen 09:06:45 und 09:08:59 CET. Sämtliche Abrufe nach 09:00; kein historischer Wortlaut um exakt 09:00 behauptet.  
**Gegenstand:** Nur Artikel 07 und Restore-Testprotokoll. Keine CMS-, Browser-, Login-, Tenant-, Produkt-, Rechts- oder Forensikoperation. Keine tatsächliche Einzelfallprüfung oder Veröffentlichungsfreigabe.

## Bereits belegte Befunde

Die neun bisherigen externen Artikelquellen, darunter alle sechs Arbeitsmittelquellen, wurden direkt mit fetch geöffnet. CISA und Fedlex lieferten vollständige gespeicherte Extraktionen trotz gekürzter Vorschau. Die CISA-Wiederherstellungspassagen wurden daraus lokal gelesen. Die BACS-Notfallkonzeptseite datiert den KMU-Download heute auf **11. November 2026**, statt auf den bisher genannten 18. Mai. Der Download lieferte bei fetch Base64 statt lesbaren Word-Text; er wurde anschliessend im Speicher als DOCX dekodiert und seine Wiederanlaufpassagen gelesen. Das Dokument verlangt eine durch Experten bestätigte Gefahrenbeseitigung vor Wiederanlauf. Beispielnamen, interne Versionsdaten und Genehmigungsangaben im Template sind keine Freigabe dieses Artikels.

**Nicht auslesbare Quelle:** Fedlex `/changes` lieferte am 15.11.2026 um 09:06:42 CET lediglich den Javascript-Hinweis. Die technische Toolmeldung «success» bedeutet hier keine erfolgreiche Inhaltsprüfung. Die Chronologie war um 09:06:41 lesbar; die vorhandene amtliche XML-Fassung vom 7. Juli 2025 war um 09:06:45 lesbar und bestätigt Art. 24 Abs. 1–4. Der Blocker der Änderungsseite bleibt separat bestehen. Keine erfundene alternative URL und keine Wiederholungsschleife.

## Quellenjournal – Originalabrufe

1. **BACS Notfallkonzept:** https://www.bacs.admin.ch/de/notfallkonzept – 15.11., 09:06:11 CET, lesbar. Vier Phasen, Rollen, Debriefing, KMU- und Gemeinde-Download mit Datum 11.11.2026. Kein minutengenauer Revisionsnachweis. [1]
2. **BACS Ransomware:** https://www.bacs.admin.ch/de/ransomware-was-nun – 15.11., 09:06:11 CET, lesbar. Logs sichern, Infektionsweg ermitteln, neu installieren, Beweissicherung vor Reparatur/Neustart durch Fachkundige. Kein eigener sichtbarer Revisionsstand und keine Forensikfreigabe. [2]
3. **CISA Guide:** https://www.cisa.gov/stopransomware/ransomware-guide – 15.11., 09:06:12 CET, lesbare Voll-Extraktion; Wiederherstellungspassagen lokal 09:06:45 gelesen. Offline-Backups, Golden Images, Offline-Pläne, Priorisierung, Beweiserhalt und keine Reinfektion sauberer Systeme. US-Orientierung, keine Schweizer Pflicht oder Restorefreigabe. [3]
4. **NIST Publikation:** https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final – 15.11., 09:06:14 CET, lesbar. Mai 2010, aktualisiert 11.11.2010. Planungs- und Testleitlinie, keine Schweizer Norm. [4]
5. **BACS Meldepflicht:** https://www.bacs.admin.ch/de/meldepflicht – 15.11., 09:06:14 CET, lesbar. Seit 01.04.2025, 24 Stunden nach Entdeckung und 14 Tage zur Vervollständigung. Unterstellung und Tatbestand bleiben Einzelfallfragen. [5]
6. **Fedlex DSG Webfassung:** https://www.fedlex.admin.ch/eli/cc/2022/491/de – 15.11., 09:06:16 CET, lesbare Extraktion. In Kraft, neueste gelistete Fassung 07.07.2025; Wartungshinweis 13.11. 20:00 bis 15.11. 20:00. Keine neue Fachfreigabe. [6]
7. **EDÖB Leitfaden-Landingpage:** https://www.edoeb.admin.ch/de/leitfaden-data-breach – 15.11., 09:06:15 CET, lesbar. Mitteilung 07.02.2025; PDF vom 23.04.2025. Art. 5 lit. h und hohes Risiko sowie separate Betroffeneninformation. Keine Rechtsberatung. [7]
8. **BACS Malwareverdacht:** https://www.bacs.admin.ch/de/26w40-de – 15.11., 09:06:16 CET, lesbar. Meldung 06.10.2026; Einzelanzeichen kein Infektionsbeweis, Fachuntersuchung, Neuinstallation, danach Passwörter ändern. Kein Einzelfallbefund. [8]
9. **BACS PHP:** https://www.bacs.admin.ch/de/warnung-php-de – 15.11., 09:06:16 CET, lesbar. Meldung 21.10.2026; integrierte Komponenten und Betreiber berücksichtigen, laufenden korrigierten Stand bestätigen; Update beseitigt keine erfolgte Kompromittierung. Keine individuelle Produktbetroffenheit. [9]
10. **BACS Heimnetz:** https://www.bacs.admin.ch/de/26w44-de – 15.11., 09:06:35 CET, lesbar. Meldung 03.11.2026; interne Geräte/Dienste aktuell halten, Exposition und Segmente beachten, VPN und wenn möglich zweiter Faktor. Privatnetzkontext, keine gemessene KMU-Inzidenz oder Bestätigung eines Homeoffice-Geräts. [10]
11. **BACS Übersicht:** https://www.bacs.admin.ch/de/im-fokus – 15.11., 09:06:36 CET, lesbarer relevanter Novemberteil. Neue Meldungen 02.–10.11. gefunden. Übersicht keine weltweite Vollständigkeitsprüfung. [11]
12. **CISA Resilienzmonat:** https://www.cisa.gov/news-events/news/cisa-kicks-critical-infrastructure-security-and-resilience-month-2026 – 15.11., 09:06:35 CET, lesbar. 02.11.2026; wichtige Systeme, externe Abhängigkeiten, Response/Recovery-Pläne und Lessons Learned. US-Kampagne, keine neue Schweizer Wiederanlaufvorgabe. [12]
13. **Fedlex Chronologie:** https://www.fedlex.admin.ch/eli/cc/2022/491/de/history – 15.11., 09:06:41 CET, lesbar. Neueste Fassung 07.07.2025. Chronologie ersetzt nicht alle Erläuterungen der heute nicht auslesbaren Änderungsseite. [13]
14. **Fedlex Änderungen:** https://www.fedlex.admin.ch/eli/cc/2022/491/de/changes – 15.11., 09:06:42 CET, **inhaltlich blockiert**: nur Javascript-Hinweis. Kein heutiger Wortlaut-/Änderungsabgleich möglich. Nicht als erfolgreich geprüft zählen. [14]
15. **Fedlex vorhandene XML:** https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml – 15.11., 09:06:45 CET, lesbar. Art. 24 Abs. 1–4 bestätigt allgemeine bestehende Aussagen. Rechtsquellenstand 07.07.2025, nicht Fachprüfdatum 15.11. [15]
16. **NIST Original-PDF:** https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf – 15.11., 09:06:45 CET, lesbar. RTO/RPO, BIA, Tests und Reconstitution; konkrete RPO-Passage lokal 09:07:30 gelesen. Ältere US-Leitlinie, organisationsspezifische Ziele offen. [16]
17. **EDÖB Original-PDF:** https://www.edoeb.admin.ch/dam/de/sd-web/T64CAUyvAMcF/1_2%20Leitfaden%20des%20ED%C3%96B%20betreffend%20die%20Meldung%20von%20Datensicherheitsverletzungen%20und%20Information%20der%20Betroffenen%20nach%20Art.%2024%20DSG_DE.pdf – 15.11., 09:06:43 CET, lesbare Extraktion. Version 1.2, 23.04.2025. Meldung und Information unterscheiden; keine Einzelfallauslegung. [17]
18. **BACS KMU-Wordtemplate:** https://www.bacs.admin.ch/dam/de/sd-web/AU4cjn0YWqWM/Notfallplan_Template_KMU_DE.docx – 15.11., 09:06:48 CET, fetch lieferte Base64. Lokal um 09:07:30 als DOCX erfolgreich dekodiert, Wiederanlauftext gelesen. Download-Datum auf Landingpage 11.11.2026; interne Musterdaten sind keine amtliche Versionsfreigabe oder Änderungsvergleich. Bestätigte Gefahrenbeseitigung durch Experten vor Wiederanlauf. [18]
19. **CISA Guide Ressourceneintrag:** https://www.cisa.gov/resources-tools/resources/stopransomware-guide – 15.11., 09:06:45 CET, lesbar. Revision Date 19.10.2023. PDF-Pfad 2025-03 beweist keine spätere inhaltliche Revision. [19]
20. **CISA KEV JSON:** https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json – 15.11., 09:06:48 CET, lesbare Voll-Extraktion. Katalogversion 2026.11.13, dateReleased 2026-11-13T20:24:18.3008Z. SonicWall CVE-2026-19868 dateAdded 06.11., WordPress CVE-2026-119977 dateAdded 03.11.; kein Organisationsbefund oder Restoreentscheid. Keine Historie aller Feldrevisionen nachgewiesen. [20]
21. **BACS Brown-Bag-Lunches:** https://www.bacs.admin.ch/de/26-brownbag-cyberresilienz-de – 15.11., 09:07:08 CET, lesbar. 02.11.2026; Geschäftsprozesse, IT/OT, externe Dienste, eingeübte Pläne. Ankündigung keine absolvierte Übung oder Fachfreigabe. [21]
22. **BACS Kühlanlagen:** https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de – 15.11., 09:07:08 CET, lesbar. 10.11.2026; Steuerungen und externe Betreiber erfassen, Fernzugriff und Firmware prüfen, veränderte Temperaturen/Alarme können Schäden bewirken. Konkrete Anlage und sichere Schalt-/Wiederanlaufentscheidung offen. [22]
23. **CISA BOD 26-04:** https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk – 15.11., 09:07:08 CET, relevante Scope-/Triagepassagen lesbar. 10.06.2026; bindend im definierten US-FCEB-Umfang. Keine automatisch geltende Schweizer KMU-Frist. [23]
24. **CISA BOD Implementierung:** https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk – 15.11., 09:07:09 CET, relevante Triagepassagen lesbar. Updated 25.08.2026; Beweise, Analyse und getrennte Resultate «No Evidence», «Confirmed», «Suspected». Baseline für US-Behörden, keine lokale Forensikfreigabe; vorgeschlagene Zwischenzeiten nicht verbindlicher neuer Schweizer Testtakt. [24]
25. **SonicWall Advisory:** https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014 – 15.11., 09:07:31 CET, lesbar. First Published 06.11., Last Updated 09.11.2026; History initial 05.11. widerspricht Kopfdatum um einen Tag. Revision 1.1 verändert Workaround/Credits. SAML-SSLVPN-Bedingung und liniengenaue Fixe; keine hier geprüfte Appliance und keine Umsetzung des Workarounds. [25]
26. **WordPress Version 7.1.4:** https://wordpress.org/documentation/wordpress-version/version-7-1-4/ – 15.11., 09:07:31 CET, lesbar. Publiziert 28.10.2026, Core-Upgrade-Race-Fix und liniengenaue Backports. Neu im November ist KEV-Aufnahme, nicht dieses Release; keine Hosterprüfung. [26]
27. **EDÖB SkySale-Mitteilung:** https://www.edoeb.admin.ch/de/datensicherheitsverletzung-bundesverwaltungsgericht-bestaetigt-informationspflicht-der-onlineshop-betreiberin – 15.11., 09:07:31 CET, lesbar. Mitteilung 06.11.2026; Urteil 08.04.2026 laut Behörde rechtskräftig, nachträgliche technische Massnahmen ersetzen Betroffeneninformation im konkreten Fall nicht. Keine neue allgemeine öffentliche Bekanntmachungspflicht. [27]

## Änderungen, lokale Prüfung und Veröffentlichung

Materiell aktualisiert wurden der sichtbare BACS-KMU-Downloadstand, der gesonderte Sicherheitsentscheid vor Wiederanlauf, Rückfallszenarien und Beweissicherungsübergabe. Die Heimnetz-Vormerkung ist auf tatsächlich zugelassene Geschäftsprozessabhängigkeiten begrenzt. Die neue BACS-Kühlanlagenwarnung begründet eine bedingte OT-Abnahme, keine Produkt- oder Schaltfreigabe. KEV, Update, Funktionstest und Betroffeneninformation bleiben getrennte Beurteilungen. Die Quellenbelege dazu stehen im Journal und bei jeder neuen Passage. Arbeitsmittelversion **1.2 → 1.3**, weil neue verbindliche Protokollfelder und Erläuterungen hinzukamen; sichtbare Version und Frontmatter stimmen überein.

Die lokale Erhaltungsprüfung am 15.11.2026 um 09:11:08 CET bestätigte **3'133 Wörter im Artikel** und **2'508 Wörter im Arbeitsmittel**, gezählt durch Trennung an Leerraum über die vollständige Datei. Beide bleiben über 1'400 Wörter. Alle sechs ursprünglichen Fachmarker-Zeilen, je drei pro Datei, wurden wortgleich gegen den vor der Änderung gelesenen Volltext abgeglichen. Slugs, Meta-Title, Meta-Description, Veröffentlichungsdatum, Autor, Entwurfs-/Arbeitsvorlagenstatus und Fachstatus sind unverändert. `rechtsstand` und `fachlich_geprüft_am` waren in beiden Dateien nicht vorhanden und wurden nicht eingeführt. Der neue Rechtsquellenabgleich bleibt im Journal, ohne historisches Fachdatum zu ersetzen.

Artikeldefinitionen [1]–[15] und Arbeitsmitteldefinitionen [1]–[12] sind jeweils genau die im Volltext zitierten Definitionen: **defined = cited**. Die neun bisherigen Artikelquellen und sechs bisherigen Arbeitsmittelquellen bleiben erhalten; je sechs neue Quellen sind passend zitiert. Im gemeinsamen Journal wurden **28 unterschiedliche externe Original-URLs** geöffnet: 27 inhaltlich nutzbar, darunter das lokal dekodierte Wordtemplate, und **eine nur technisch erreichbare, inhaltlich blockierte Fedlex-Änderungsseite**. Der lesbare XML-Zugang hebt diesen getrennten Blocker nicht auf. Keine HTTP-Statuszahl wurde aus einer blossen Toolmeldung abgeleitet.

Artikeltermin **12.11.2026** liegt vor dem Prüfdatum; er bleibt der ursprüngliche Planungstermin und ist kein Veröffentlichungsnachweis. Artikel bleibt **Entwurf**, Arbeitsmittel **Arbeitsvorlage – nicht freigegeben**. Es gab keine CMS-/Browseroperation, keinen Login, Import oder Live-Änderungsversuch und keine Zugangsdatenverwendung. Öffentliche Veröffentlichung und Live-Erreichbarkeit wurden nicht geprüft. Nur die zwei Inhalte und dieser Bericht wurden gezielt geschrieben; keine anderen Artikel, Manifeste oder globalen QA-Skripte wurden verändert.

## Genau betroffene Passagen – vorher und nachher

Die folgenden Blöcke dokumentieren sämtliche Ersetzungen und Einfügungen. Bei Einfügungen ist der unveränderte Anker für die genaue Position mitgeführt. Alle übrigen Originalpassagen bleiben wortgleich erhalten.

### 07-backup-wiederherstellung-testen.md – Frontmatter: stand

**Vorher:**

```text
stand: "1. November 2026"
```

**Nachher:**

```text
stand: "15. November 2026"
```

### 07-backup-wiederherstellung-testen.md – Frontmatter: quellenpruefung_umfang

**Vorher:**

```text
quellenpruefung_umfang: "9 zitierte externe Originalquellen, darunter Fedlex zusätzlich über amtliche Chronologie, Änderungen und XML; ergänzend BACS Im Fokus, BACS-KMU-Studie, CISA SafePay und CISA-Ressourceneintrag geprüft. Abrufe am 01.11.2026, 09:05–09:09 CET Europe/Zurich. Interne bzw. geplante DKSchV-URLs wurden nicht live geprüft."
```

**Nachher:**

```text
quellenpruefung_umfang: "15 zitierte externe Originalquellen direkt geprüft; gemeinsames Quellenjournal mit 28 Originalabrufen, darunter Fedlex-Chronologie und vorhandene amtliche XML sowie 13 ergänzende Quellen. Abrufrückgaben am 15.11.2026, 09:06:11–09:08:59 CET Europe/Zurich, nach 09:00. BACS-Wordtemplate nach Base64-Rückgabe lokal dekodiert und gelesen. Interne Ziele nur lokal abgeglichen, keine Live-Prüfung."
```

### 07-backup-wiederherstellung-testen.md – Frontmatter: quellenpruefung_status

**Vorher:**

```text
quellenpruefung_status: "vollständig für die 9 zitierten externen Originalquellen; kein Nachweis eines minutengenauen historischen Website-Wortlauts und keine Fach-, Rechts- oder Veröffentlichungsfreigabe"
```

**Nachher:**

```text
quellenpruefung_status: "15/15 zitierte Quellen inhaltlich lesbar; 1 ergänzender Inhaltsblocker: Fedlex-Änderungsseite liefert nur Javascript-Hinweis, nicht erfolgreich verifiziert. DSG-Wortlaut separat per amtlicher XML bestätigt. Kein historischer 09:00-Wortlaut, keine tatsächliche Einzelfallprüfung und keine Fach-, Rechts-, Forensik-, Tenant-, Produkt-, Veröffentlichungs- oder Nutzungsfreigabe."
```

### 07-restore-testprotokoll.md – Frontmatter: stand

**Vorher:**

```text
stand: "1. November 2026"
```

**Nachher:**

```text
stand: "15. November 2026"
```

### 07-restore-testprotokoll.md – Frontmatter: quellenpruefung_umfang

**Vorher:**

```text
quellenpruefung_umfang: "6 zitierte externe Originalquellen, darunter Fedlex zusätzlich über amtliche Chronologie, Änderungen und XML; ergänzend BACS Im Fokus, BACS-KMU-Studie, CISA SafePay und CISA-Ressourceneintrag geprüft. Abrufe am 01.11.2026, 09:05–09:09 CET Europe/Zurich. Interne bzw. geplante DKSchV-URLs wurden nicht live geprüft."
```

**Nachher:**

```text
quellenpruefung_umfang: "12 zitierte externe Originalquellen direkt geprüft; gemeinsames Quellenjournal mit 28 Originalabrufen, darunter Fedlex-Chronologie und vorhandene amtliche XML sowie 16 ergänzende Quellen. Abrufrückgaben am 15.11.2026, 09:06:11–09:08:59 CET Europe/Zurich, nach 09:00. BACS-Wordtemplate nach Base64-Rückgabe lokal dekodiert und gelesen. Interne Ziele nur lokal abgeglichen, keine Live-Prüfung."
```

### 07-restore-testprotokoll.md – Frontmatter: quellenpruefung_status

**Vorher:**

```text
quellenpruefung_status: "vollständig für die 6 zitierten externen Originalquellen; kein Nachweis eines minutengenauen historischen Website-Wortlauts und keine Fach-, Rechts- oder Nutzungsfreigabe"
```

**Nachher:**

```text
quellenpruefung_status: "12/12 zitierte Quellen inhaltlich lesbar; 1 ergänzender Inhaltsblocker: Fedlex-Änderungsseite liefert nur Javascript-Hinweis, nicht erfolgreich verifiziert. DSG-Wortlaut separat per amtlicher XML bestätigt. Kein historischer 09:00-Wortlaut, keine tatsächliche Einzelfallprüfung und keine Fach-, Rechts-, Forensik-, Tenant-, Produkt-, Veröffentlichungs- oder Nutzungsfreigabe."
```

### 07-backup-wiederherstellung-testen.md – Sichtbarer Quellenstand

**Vorher:**

```text
*Quellenstand: 1. November 2026. Die Standangabe bezeichnet die Quellenpflege und keine Fach-, Rechts- oder Veröffentlichungsfreigabe.*
```

**Nachher:**

```text
*Quellenstand: 15. November 2026. Die Standangabe bezeichnet die Quellenpflege und keine Fach-, Rechts- oder Veröffentlichungsfreigabe. Die ergänzende Fedlex-Änderungsseite war nicht inhaltlich auslesbar; der amtliche DSG-XML-Wortlaut war lesbar.*
```

### 07-backup-wiederherstellung-testen.md – Einleitung: KMU-Vorlagenstand

**Vorher:**

```text
Für Schweizer KMU steht seit dem 18. Mai 2026 zudem eine angepasste Vorlage für einen IT-Notfall- und Krisenplan bereit.[1]
```

**Nachher:**

```text
Die dort angebotene KMU-Vorlage für den IT-Notfall- und Krisenplan ist beim heutigen Abruf mit **11. November 2026** datiert.[1] Das Download-Datum ist keine organisationsbezogene Genehmigung des Plans.
```

### 07-backup-wiederherstellung-testen.md – Der saubere Wiederanlauf: Fachentscheid und Beweissicherungsübergabe

**Vorher:**

```text
Die BACS-Meldung vom 6. Oktober 2026 präzisiert den Umgang mit Malware-Verdacht:
```

**Nachher:**

```text
Die aktuell angebotene BACS-KMU-Vorlage verlangt, dass Experten die Beseitigung der Gefahr bestätigen, bevor der Wiederanlauf betroffener Systeme und Dienste beginnt.[11] Im Test wird dieser Entscheidungspunkt mit benannter Rolle, Kriterien und Nachweis simuliert. Bei einem echten Vorfall bleibt er ein gesonderter Fachentscheid. Halten Sie zudem den vorgesehenen Erhalt relevanter Logs, die zuständige Fachstelle und den Entscheid über Beweissicherung vor verändernden Eingriffen fest. BACS und CISA weisen auf den Erhalt von Logdateien und flüchtigen Beweisen hin.[2] [3] Das Testprotokoll hält Zuständigkeit und Übergabe fest, führt aber selbst keine forensische Sicherung aus und bestätigt keine Beweiskette.

Die BACS-Meldung vom 6. Oktober 2026 präzisiert den Umgang mit Malware-Verdacht:
```

### 07-backup-wiederherstellung-testen.md – Neu: Rückfallszenarien vor der Übergabe üben

**Vorher:**

```text
### Komponenten- und Patchnachweise vom Vorfallsbefund trennen
```

**Nachher:**

```text
### Rückfallszenarien vor der Übergabe üben

Machen Sie den bisherigen Rückfallweg konkret: Was geschieht, wenn der Sicherungssatz nicht nutzbar ist, der Datenstand das RPO verfehlt, der Fachtest scheitert oder nach dem Start ein verdächtiger Zugriff auftritt? Legen Sie im Testauftrag Auslöser, stoppberechtigte Rolle, Trennung der Testumgebung, freigegebenen Behelfsprozess und den Nachtest fest. Ein älterer Sicherungsstand ist nicht automatisch akzeptabel; eine zusätzliche Datenlücke benötigt einen dokumentierten Entscheid der Prozessverantwortung. Diese Szenarien sind eine Testkonkretisierung, keine neu eingeführte BACS-Pflicht. Sie setzen die bestehenden Anforderungen an Backup-Prüfung, fachliche Validierung und Schutz vor Reinfektion um.[3] [4]

Ein Rückfall bedeutet insbesondere nicht, zur als kompromittiert angenommenen Produktion oder zu einem unkontrollierten Heimgerät zurückzukehren. Die BACS-Meldung vom **3. November 2026** warnt im Privatnetzkontext vor exponierten, ungepatchten Diensten und empfiehlt aktuelle Geräte und Dienste, getrennte Netzsegmente sowie einen geschützten VPN-Zugang und wenn möglich einen zweiten Faktor.[10] Falls Homeoffice-Zugänge oder private NAS eine tatsächlich zugelassene Abhängigkeit des Geschäftsprozesses sind, erfassen Sie deren Betreiber, Exposition, Aktualisierungsnachweis und Zugang im Test. Das ist keine Bestätigung der Sicherheit eines konkreten Heimnetzes und keine Erlaubnis, Geschäftsdaten dorthin auszulagern.

### Komponenten- und Patchnachweise vom Vorfallsbefund trennen
```

### 07-backup-wiederherstellung-testen.md – Komponenten- und Patchnachweise: KEV- und OT-Abgrenzung

**Vorher:**

```text
Die Wiederanlaufreihenfolge gehört in den IT-Notfallplan, nicht nur in das Wissen einzelner Administratoren.
```

**Nachher:**

```text
Dasselbe gilt für eine Aufnahme in den CISA-Katalog bekannter ausgenutzter Schwachstellen (KEV): Der Katalog ist ein Priorisierungshinweis, kein Nachweis einer Kompromittierung Ihrer Organisation und keine Restorefreigabe.[13] Seine US-Behördenvorgaben werden nicht automatisch zu Schweizer KMU-Fristen.[14] Weder ein KEV-Eintrag noch ein Update, eine Herstellerbestätigung oder ein bestandener Funktionstest erlaubt für sich allein die produktive Wiederverbindung.

Beziehen Sie auch betriebliche Steuerungen ein, wenn sie zum priorisierten Prozess gehören. Die BACS-Warnung vom **10. November 2026** nennt Kühl- und Kältesteuerungen, externe Betreiber, Firmware und Fernzugriff; manipulierte Temperaturen oder Alarme können reale Schäden verursachen.[12] Ein lesbarer Backup-Datenstand genügt bei solchen Abhängigkeiten nicht. Die zuständigen Betriebs- und Sicherheitsfachpersonen müssen Sollwerte, Alarme und sichere Wiederaufnahme bestimmen. Dieser Leitfaden gibt keine Anlage, Firmware oder Schalthandlung frei.

Die Wiederanlaufreihenfolge gehört in den IT-Notfallplan, nicht nur in das Wissen einzelner Administratoren.
```

### 07-backup-wiederherstellung-testen.md – Melde- und Datenschutzfragen: Betroffeneninformation

**Vorher:**

```text
**[FACHPRÜFUNG ERFORDERLICH]** Diese Hinweise sind keine individuelle Rechtsberatung.
```

**Nachher:**

```text
Betroffeneninformation ist gesondert zu beurteilen. Im konkreten Fall SkySale hält die EDÖB-Mitteilung vom **6. November 2026** fest, dass nachträgliche technische Massnahmen die bestätigte Informationspflicht nicht beseitigten.[15] Ein erfolgreicher Restore oder ein Update entscheidet diese Frage deshalb nicht. Art. 24 Abs. 4 DSG verlangt Information, wenn sie zum Schutz der betroffenen Person erforderlich ist oder der EDÖB sie verlangt; daraus folgt keine allgemeine Pflicht jedes KMU zur öffentlichen Bekanntmachung.[6] [7]

**[FACHPRÜFUNG ERFORDERLICH]** Diese Hinweise sind keine individuelle Rechtsberatung.
```

### 07-restore-testprotokoll.md – Frontmatter: version

**Vorher:**

```text
version: "1.2"
```

**Nachher:**

```text
version: "1.3"
```

### 07-restore-testprotokoll.md – Sichtbare Version und Quellenstand

**Vorher:**

```text
**Version 1.2 · Quellenstand: 1. November 2026.** Die Standangabe bezeichnet die Quellenpflege und keine Fach-, Rechts- oder Nutzungsfreigabe.
```

**Nachher:**

```text
**Version 1.3 · Quellenstand: 15. November 2026.** Die Standangabe bezeichnet die Quellenpflege und keine Fach-, Rechts- oder Nutzungsfreigabe. Die ergänzende Fedlex-Änderungsseite war nicht inhaltlich auslesbar; der amtliche DSG-XML-Wortlaut war lesbar.
```

### 07-restore-testprotokoll.md – 4. Durchführung: neue Rückfall- und Beweissicherungsübergabe

**Vorher:**

```text
### Fachliche Abnahme
```

**Nachher:**

```text
### Rückfall und Beweissicherungsübergabe

Die aktuell angebotene BACS-KMU-Vorlage verlangt eine durch Experten bestätigte Beseitigung der Gefahr vor dem Wiederanlauf betroffener Systeme und Dienste.[8] Im Test wird dieser Freigabepunkt nur simuliert. Protokollieren Sie Kriterien, benannte Rolle, Entscheid und offene Befunde; damit wird keine echte Umgebung zur Wiederverbindung freigegeben.

| Prüfpunkt | Festlegung vor Test / Ergebnis / verantwortliche Person |
|---|---|
| Simulierter Sicherheitsentscheid vor Wiederanlauf: Kriterien, Rolle, Uhrzeit und Nachweis |  |
| Nicht nutzbarer Sicherungssatz: zulässige Alternative und zusätzlicher Datenverlust |  |
| RPO verfehlt oder Fachtest gescheitert: Abbruchentscheid, Behelfsprozess und Nachtest |  |
| Verdächtiger Zugriff nach Start: Stoppbefugnis, sichere Trennung und Eskalationsweg |  |
| Rückfall durchgeführt: Auslöser, Zeitpunkt, Ergebnis und erneute Abnahme |  |
| Log-Erhalt und Beweissicherungsübergabe: betroffene Quellen, zuständige Fachstelle, Entscheid vor veränderndem Eingriff |  |
| Zugelassene Homeoffice-/Heimnetzabhängigkeit: Betreiber, Exposition, Geräte-/Dienststand und Zugangsweg |  |
| Prozessrelevante OT-/Kühlsteuerung: Betreiber, Sollwerte, Alarme und sichere Betriebsabnahme |  |

Die Rückfallszenarien konkretisieren die bisherigen Test-, Abbruch- und Freigabefelder, sie sind keine neu eingeführte allgemeine Behördenpflicht. BACS und CISA betonen den Erhalt relevanter Logs und flüchtiger Beweise.[3] [2] Die Zeile zur Beweissicherungsübergabe hält nur Planung, Zuständigkeit und Entscheid fest; sie ist keine forensische Sicherung oder Bestätigung einer Beweiskette. Bei einem tatsächlichen Vorfall bestimmt die zuständige Fachstelle das risikogerechte Vorgehen. Der Rückfall darf nicht in die als kompromittiert angenommene Produktion führen.

Die BACS-Meldung vom 3. November 2026 verlangt im Heimnetzkontext aktuelle Geräte und Dienste und empfiehlt getrennte Segmente, VPN sowie wenn möglich einen zweiten Faktor.[7] Die Zeile gilt nur für tatsächlich zugelassene Geschäftsprozessabhängigkeiten; sie erlaubt keine Auslagerung auf private Geräte und bestätigt keine Heimnetzsicherheit. Die BACS-Warnung vom 10. November 2026 zu Kühlsteuerungen begründet den OT-Prüfpunkt, sofern solche Anlagen zum Prozess gehören.[9] Sollwerte, Alarme und sichere Schalthandlungen sind durch zuständige Betriebsfachpersonen zu bestimmen, nicht durch dieses Protokoll.

Eine KEV-Aufnahme ist kein Kompromittierungsbefund und kein Restoreentscheid.[10] CISA-BOD-Fristen gelten im dort definierten US-Behördenumfang, nicht automatisch für Schweizer KMU.[11] Update, Anbieterbestätigung und Funktionstest ersetzen keinen gesonderten Sicherheitsentscheid.

### Fachliche Abnahme
```

### 07-restore-testprotokoll.md – Grenzen und Eskalation: technische Behebung und Betroffeneninformation

**Vorher:**

```text
**[FACHPRÜFUNG ERFORDERLICH]** Ergibt ein Test Hinweise auf eine reale Kompromittierung oder einen Datenabfluss, stoppen Sie den Test nach dem definierten Sicherheitsverfahren.
```

**Nachher:**

```text
Ein Restore- oder Patch-Ergebnis ersetzt auch die gesonderte Beurteilung der Betroffeneninformation nicht. Die EDÖB-Mitteilung vom 6. November 2026 zum konkreten Fall SkySale hält fest, dass nachträgliche technische Massnahmen die bestätigte Informationspflicht nicht beseitigten.[12] Art. 24 Abs. 4 DSG und die konkrete Schutzbedürftigkeit sind getrennt zu beurteilen; daraus wird keine allgemeine Pflicht zur öffentlichen Bekanntmachung abgeleitet.[4]

**[FACHPRÜFUNG ERFORDERLICH]** Ergibt ein Test Hinweise auf eine reale Kompromittierung oder einen Datenabfluss, stoppen Sie den Test nach dem definierten Sicherheitsverfahren.
```

### 07-backup-wiederherstellung-testen.md – Quellen: sechs neue Definitionen mit passenden Inlinezitationen

**Vorher:**

```text
Keine Definitionen 10–15.
```

**Nachher:**

```text
[10]: https://www.bacs.admin.ch/de/26w44-de "BACS – Woche 44: Wenn das Heimnetzwerk zum Einfallstor für Cyberkriminelle wird, 3. November 2026"
[11]: https://www.bacs.admin.ch/dam/de/sd-web/AU4cjn0YWqWM/Notfallplan_Template_KMU_DE.docx "BACS – Template IT-Notfall- und Krisenplan für KMU, Download-Datum 11. November 2026"
[12]: https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de "BACS – Kühl- und Kältesteuerungen: Systeme identifizieren, aktualisieren und schützen, 10. November 2026"
[13]: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "CISA – Known Exploited Vulnerabilities Catalog, abgerufen am 15. November 2026"
[14]: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk "CISA – BOD 26-04: Prioritizing Security Updates Based on Risk, US-Geltungsbereich"
[15]: https://www.edoeb.admin.ch/de/datensicherheitsverletzung-bundesverwaltungsgericht-bestaetigt-informationspflicht-der-onlineshop-betreiberin "EDÖB – Bundesverwaltungsgericht bestätigt Informationspflicht der Onlineshop-Betreiberin, 6. November 2026"
```

### 07-restore-testprotokoll.md – Quellen: sechs neue Definitionen mit passenden Inlinezitationen

**Vorher:**

```text
Keine Definitionen 7–12.
```

**Nachher:**

```text
[7]: https://www.bacs.admin.ch/de/26w44-de "BACS – Woche 44: Wenn das Heimnetzwerk zum Einfallstor für Cyberkriminelle wird, 3. November 2026"
[8]: https://www.bacs.admin.ch/dam/de/sd-web/AU4cjn0YWqWM/Notfallplan_Template_KMU_DE.docx "BACS – Template IT-Notfall- und Krisenplan für KMU, Download-Datum 11. November 2026"
[9]: https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de "BACS – Kühl- und Kältesteuerungen: Systeme identifizieren, aktualisieren und schützen, 10. November 2026"
[10]: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "CISA – Known Exploited Vulnerabilities Catalog, abgerufen am 15. November 2026"
[11]: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk "CISA – BOD 26-04: Prioritizing Security Updates Based on Risk, US-Geltungsbereich"
[12]: https://www.edoeb.admin.ch/de/datensicherheitsverletzung-bundesverwaltungsgericht-bestaetigt-informationspflicht-der-onlineshop-betreiberin "EDÖB – Bundesverwaltungsgericht bestätigt Informationspflicht der Onlineshop-Betreiberin, 6. November 2026"
```

## Ergänzender Quellenstand zum Urteil

28. **BVGer Originalurteil A-3790/2024:** https://www.edoeb.admin.ch/dam/de/sd-web/ZjhZ9UBOprVL/Urteil%20BVGer%20A_3790_2024%20vom%208.%20April%202026%20betreffend%20Verf%C3%BCgung%20vom%2028.%20Mai%202024.pdf – 15.11.2026, 09:08:59 CET, relevante Originalpassagen mit fetch lesbar. Urteilsdatum 08.04.2026; Erwägung 5.3.2 trennt bereits erfolgte Datensicherheitsverletzung von nachträglichen technischen Massnahmen. Erwägungen 6.2–6.3 behandeln die Information und mögliche Ersatzformen im konkreten Fall. Die Rechtskraft wird hier ausschliesslich der EDÖB-Mitteilung zugeschrieben, nicht dem Urteil selbst. Keine neue allgemeine KMU-Bekanntmachungspflicht oder eigene Rechtsfreigabe. Im Artikel und Arbeitsmittel ist die EDÖB-Mitteilung als Quelle der begrenzten Fallbeschreibung zitiert; das zusätzlich geöffnete Urteil bleibt Journalquelle. [28]

## Behandlung neuer Meldungen seit 1. November und Vormerkungen

Das Prüfintervall ist **01.11.2026 bis 15.11.2026, Redaktionsgrenze 09:00 CET**; die tatsächlichen Abrufe erfolgten danach. Es wird nicht behauptet, die unversionierten Seiten hätten um 09:00 exakt denselben Wortlaut gehabt. Die Suche ergab als einschlägige Primärquellen die BACS-Heimnetzmeldung und die CISA-Resilienzmeldung. Die BACS-Übersicht führte zusätzlich die Brown-Bag-Ankündigung und die Kühlanlagenwarnung. Deren Originale wurden geöffnet, nicht bloss ihre Suchsnippets verwendet.

Die Brown-Bag-Ankündigung vom 02.11. und die US-Resilienzkampagne vom 02.11. bestätigen den bereits vorhandenen Geschäftsprozess-, Abhängigkeits- und Übungsansatz. Sie rechtfertigen keinen zusätzlichen Veranstaltungshinweis oder eine angeblich absolvierte Fachprüfung im Evergreen-Beitrag. Die Quelle zum KMU-Notfallplan belegt beim heutigen Abruf ein Download-Datum 11.11.; mangels gesicherter Vorherfassung wird daraus keine Liste angeblich neu eingeführter amtlicher Einzelanforderungen abgeleitet. Der gelesene Sicherheitsentscheid ist eine belegte Präzisierung des bestehenden sauberen Wiederanlaufs.

Die Heimnetz-Vormerkung vom 08.11. ist erledigt: Originalmeldung vom 03.11. direkt gelesen und im Rückfallabschnitt sowie im Protokoll bedingt eingearbeitet. Die Quelle betrifft private Netze. Weder wurde eine Schweizer KMU-Inzidenz daraus berechnet noch ein Heimnetz untersucht. Der Hinweis zu Kühlsteuerungen vom 10.11. ist wegen möglicher realer Geschäftsprozess- und Sicherheitsfolgen als bedingte Abhängigkeit eingearbeitet, ohne einzelne Modell-/Firmware- oder Anlagenfreigabe.

KEV-Version **2026.11.13** und die vorgemerkten WordPress-/SonicWall-Originale wurden geöffnet. Für SonicWall ist **09.11.2026** als neue Advisory-Revision dokumentiert; sie ändert Workaround/Credits, nicht eine hier geprüfte Appliance. Der Unterschied zwischen Kopfdatum 06.11. und History-Eintrag 05.11. bleibt im Journal sichtbar. WordPress-Release/Backports stammen vom 28.10.; die KEV-Aufnahme vom 03.11. ist davon getrennt. Die Produktdetails begründen keine zusätzliche wöchentliche CVE-Liste im Artikel. Stattdessen wird die erforderliche Grenze ausdrücklich aufgenommen: KEV ist weder eigener Kompromittierungsbefund noch Restorefreigabe. Die US-BOD- und Triagequellen belegen die Trennung von Patchen, Beweiserhalt und Analyse; ihre Fristen und Abläufe werden nicht als Schweizer KMU-Recht oder sofort auszuführende Forensikanweisung übernommen.

Die EDÖB-Mitteilung vom 06.11. und das Originalurteil sind als abgegrenzter Hinweis auf die getrennte Beurteilung technischer Behebung und Betroffeneninformation verwendet. Neu ist die Mitteilung, nicht das Urteilsdatum oder ein neuer DSG-Artikel. Öffentliche Bekanntmachung ist keine allgemeine KMU-Pflicht. Die vorhandenen Meldefristen und Risikoschwellen wurden nicht verändert.

Die Recherche hat keine zusätzliche allgemeine BACS-/CISA-Restoreleitlinienrevision seit 01.11. belegt. Das ist ein begrenztes Rechercheergebnis, keine Zusage über sämtliche Primärmeldungen weltweit. Nach dem nicht auslesbaren Fedlex-Änderungsabruf wurde keine Wiederholungsschleife durchgeführt. Die vorhandene amtliche XML-Alternative wurde genutzt, nicht eine URL erfunden.

## Unveränderte Abschnitte und Paketziele

Im Artikel bleiben **H1 und Kurzantwort**, «Der Startpunkt sind Geschäftsprozesse, nicht Sicherungsjobs» samt «RTO und RPO so festlegen, dass sie testbar sind», «Ein sicheres Testszenario für Ransomware definieren», «Rollen, Stellvertretungen und Offline-Unterlagen vor dem Test festlegen», «Zeit, Datenstand und Qualität messen», «Debriefing und Nachtest machen aus dem Test eine Verbesserung» und «Typische Fehler, die der Test aufdecken soll» wortgleich erhalten. Auch die ursprüngliche sechsstufige Wiederanlaufreihenfolge, die beiden vorhandenen PHP-Absätze, die bisherigen Melde-/DSG-Absätze und alle Fachprüfungs- und Kontaktpassagen sind unverändert. Nur die im Vorher-/Nachher-Protokoll genau ausgewiesenen Einfügungen, Quellen und Prüfmetadaten wurden ergänzt bzw. ersetzt.

Im Arbeitsmittel bleiben **H1**, «Zweck», «Anwendung», «1. Testauftrag und Freigabe» samt «Testszenario», «2. Geschäftsprozess und Ziele» samt Abhängigkeitstabelle, «3. Rollen, Kommunikation und Unterlagen» samt Startkontrollen, die bisherige Durchführungstabelle und technischen Kontrollpunkte, «Fachliche Abnahme», «5. Messung und Ergebnis» sowie «6. Debriefing und Massnahmen» samt Nachtestfeldern wortgleich erhalten. In «Grenzen und Eskalation» wurde nur der ausgewiesene Absatz zur Betroffeneninformation eingefügt; die drei bisherigen Absätze einschliesslich Fachmarker blieben unverändert.

Die internen Paket-Slugs `/wissen/ransomware-resistente-backups`, `/wissen/ransomware-erste-60-minuten` und `/resources/07-restore-testprotokoll` sind in den lokal vorhandenen Paketdateien definiert. Der Artikel-Slug-Verweis im Arbeitsmittel entspricht dem vorhandenen Artikel 07. Die bestehenden Service-/Kontaktziele `/unsere-dienstleistungen/risikomanagement`, `/unsere-dienstleistungen/sicherheitsanalyse` und `/kontakt` wurden unverändert erhalten. Es wurden keine neuen internen Links und keine erfundenen Slugs eingeführt. Ein lokaler Paketverweis oder eine frühere Erreichbarkeitsmessung ist kein heutiger Live-Test.

## Offene konkrete Fachfragen und Erreichbarkeitsblocker

**Erreichbarkeit:** Die Fedlex-Änderungsseite ist beim heutigen Abruf inhaltlich nicht auslesbar. Die dortigen Detailerläuterungen können nicht als aktuell verifiziert gelten. Der amtliche DSG-Text und die Chronologie sind getrennt lesbar. Das Wordtemplate war zunächst nur als Base64 erhältlich, wurde aber anschliessend erfolgreich lokal als DOCX gelesen; die technische Extraktionshürde ist gelöst, die Datierungs-/Versionsgrenze bleibt. Der ursprüngliche Wortlaut vor der sichtbaren Download-Datierung 11.11. liegt nicht als belegter Vergleich vor. Für öffentliche DKSchV-Ziele wurde heute keine Erreichbarkeitsmessung vorgenommen; deshalb wird weder Erfolg noch 403/404 oder ein aktueller CMS-Loginstatus behauptet.

**Sicherer Wiederanlauf:** Welche konkrete Fachperson bestätigt Gefahrenbeseitigung, Bereinigung von Identitäten und Persistenz sowie die Rückkehr in den Betrieb? Welche Kriterien und offenen Befunde gelten, und wie lange bzw. mit welchen Signalen wird überwacht? Diese Entscheidungen sind nicht getroffen. Das simulierte Freigabefeld darf nicht als reale Freigabe verwendet werden.

**Rückfall und Prozessabnahme:** Welche RTO/RPO-Werte, Sicherungssätze, älteren Datenstände und Behelfsprozesse sind für die tatsächliche Organisation zulässig? Wer darf stoppen, wer akzeptiert zusätzliche Datenlücken, und welche Voraussetzungen erlauben den Nachtest? Kapazität, Abhängigkeiten, Datenqualität und Wiederherstellbarkeit wurden nicht konkret getestet.

**Beweise und Forensik:** Welche Logs und flüchtigen Daten müssen in welcher Reihenfolge erhalten werden? Wer entscheidet bei konkurrierender Eindämmung, Patchen und Beweiserhalt, und wer verantwortet Sammlung, Aufbewahrung und beweisfähige Übergabe? Keine Systeme oder Logs wurden untersucht, kein Artefakt gesammelt, keine Beweiskette bestätigt.

**Homeoffice und OT:** Sind private Geräte/NAS überhaupt als Geschäftsprozessabhängigkeit zugelassen? Sind Betreiber, Exposition, Aktualisierung, Zugriff und Datenflüsse konkret geprüft? Welche Betriebsfachstelle nimmt Temperaturen, Alarme, Sicherheitsfunktionen und Wiederanlauf einer tatsächlichen Anlage ab? Keine Heimnetz-, Tenant-, Firmware-, Lieferanten- oder Produktfreigabe erfolgte.

**Rechtliche Vorfallsfragen:** BACS-Unterstellung, Ausnahmen, Angriffstatbestand und Entdeckungszeitpunkt sowie Datenschutzrollen, voraussichtlich hohes Risiko, erforderliche Betroffeneninformation und angemessene Informationsform bleiben anhand konkreter Tatsachen zu beurteilen. Quelleninhalt und allgemeine Orientierung sind keine tatsächliche Einzelfallprüfung. Der historische Fachstatus bleibt offen.

**Veröffentlichung:** Terminlich fällig seit 12.11.2026, aber Artikel weiterhin Entwurf und Arbeitsmittel weiterhin nicht freigegeben. Vor Publikation bzw. Nutzung fehlen zuständige Fachprüfungen, ausdrückliche Freigaben und ein aktueller Live-Link-/Quellenabgleich im autorisierten Veröffentlichungsprozess. Dieser Bericht enthält keine fiktive CMS-Prüfung oder Publikation.

## Referenzen

[1]: https://www.bacs.admin.ch/de/notfallkonzept "BACS Notfallkonzept"
[2]: https://www.bacs.admin.ch/de/ransomware-was-nun "BACS Ransomware"
[3]: https://www.cisa.gov/stopransomware/ransomware-guide "CISA Guide"
[4]: https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final "NIST Publikation"
[5]: https://www.bacs.admin.ch/de/meldepflicht "BACS Meldepflicht"
[6]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex DSG Webfassung"
[7]: https://www.edoeb.admin.ch/de/leitfaden-data-breach "EDÖB Leitfaden-Landingpage"
[8]: https://www.bacs.admin.ch/de/26w40-de "BACS Malwareverdacht"
[9]: https://www.bacs.admin.ch/de/warnung-php-de "BACS PHP"
[10]: https://www.bacs.admin.ch/de/26w44-de "BACS Heimnetz"
[11]: https://www.bacs.admin.ch/de/im-fokus "BACS Übersicht"
[12]: https://www.cisa.gov/news-events/news/cisa-kicks-critical-infrastructure-security-and-resilience-month-2026 "CISA Resilienzmonat"
[13]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/history "Fedlex Chronologie"
[14]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/changes "Fedlex Änderungen"
[15]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml "Fedlex vorhandene XML"
[16]: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf "NIST Original-PDF"
[17]: https://www.edoeb.admin.ch/dam/de/sd-web/T64CAUyvAMcF/1_2%20Leitfaden%20des%20ED%C3%96B%20betreffend%20die%20Meldung%20von%20Datensicherheitsverletzungen%20und%20Information%20der%20Betroffenen%20nach%20Art.%2024%20DSG_DE.pdf "EDÖB Original-PDF"
[18]: https://www.bacs.admin.ch/dam/de/sd-web/AU4cjn0YWqWM/Notfallplan_Template_KMU_DE.docx "BACS KMU-Wordtemplate"
[19]: https://www.cisa.gov/resources-tools/resources/stopransomware-guide "CISA Guide Ressourceneintrag"
[20]: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "CISA KEV JSON"
[21]: https://www.bacs.admin.ch/de/26-brownbag-cyberresilienz-de "BACS Brown-Bag-Lunches"
[22]: https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de "BACS Kühlanlagen"
[23]: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk "CISA BOD 26-04"
[24]: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk "CISA BOD Implementierung"
[25]: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014 "SonicWall Advisory"
[26]: https://wordpress.org/documentation/wordpress-version/version-7-1-4/ "WordPress Version 7.1.4"
[27]: https://www.edoeb.admin.ch/de/datensicherheitsverletzung-bundesverwaltungsgericht-bestaetigt-informationspflicht-der-onlineshop-betreiberin "EDÖB SkySale-Mitteilung"
[28]: https://www.edoeb.admin.ch/dam/de/sd-web/ZjhZ9UBOprVL/Urteil%20BVGer%20A_3790_2024%20vom%208.%20April%202026%20betreffend%20Verf%C3%BCgung%20vom%2028.%20Mai%202024.pdf "BVGer Originalurteil A-3790/2024"

## Nachtrag des lokalen Linkabgleichs

Bearbeitungszeit: 2026-11-15T09:20:58+01:00. Die Live-Zielzuordnung ist im [Zielplan](public-target-map.csv) und im [Linkänderungsprotokoll](lokaler-live-linkabgleich.json) belegt. Diese Ergänzung ersetzt nur alte lokale Markdown-Linkziele durch separat mit HTTP200 geprüfte Adressen; sie ändert keine logischen Slugs oder Freigaben.

**articles/07-backup-wiederherstellung-testen.md:** `/resources/07-restore-testprotokoll` → `https://www.dkschv.ch/wissen/resources/07-restore-testprotokoll.html`: 1 Linkvorkommen; `/unsere-dienstleistungen/sicherheitsanalyse` → `https://www.dkschv.ch/sicherheitsanalyse.html`: 1 Linkvorkommen; `/unsere-dienstleistungen/risikomanagement` → `https://www.dkschv.ch/risikomanagement.html`: 1 Linkvorkommen.

Globale Ergänzung: Alle zwölf Artikeladressen sind HTTP200, Fachfreigaben bleiben aber offen. Der Wiederherstellungsartikel lieferte trotz Login-Hinweis umfangreichen Text ohne Credentials; wirksamer serverseitiger Schutz ist nicht nachgewiesen. Webador ist nicht authentifiziert. Keine CMS-/Live-Änderung oder Veröffentlichung.
