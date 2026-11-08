---
titel: "QA-Bericht: Artikel und Arbeitsmittel 01–06"
stand: "20. September 2026"
prüfumfang: "6 Artikel und 6 Arbeitsmittel"
prüfstatus: "Inhaltlich und technisch bereinigt; nicht zur Veröffentlichung freigegeben"
---

# QA-Bericht: Artikel und Arbeitsmittel 01–06

## Ergebnis

Die sechs Artikel und sechs zugehörigen Arbeitsmittel wurden vollständig geöffnet, quellenbezogen geprüft und direkt in den Originaldateien überarbeitet. Alle zwölf Dateien führen nun einheitliche Frontmatter-Metadaten mit Status, Slug, Meta-Title, Meta-Description, Suchintention, Zielgruppe, Versions- beziehungsweise Quellenstand und `fachprüfung_status`. Sie sind als **„Entwurf – nicht freigegeben“** beziehungsweise **„Arbeitsvorlage – nicht freigegeben“** gekennzeichnet.

Die Schlussvalidierung ergab **keine offenen formalen Fehler**. In den zwölf Dateien stehen **109 verwendete und 109 definierte Quellenreferenzen**. Alle Quellenreferenzen verwenden das numerische Markdown-Format mit beschreibendem Titel. Die redaktionell verwendeten Zeit-, Rechts-, Statistik- und Produktangaben wurden gegen die verlinkten Primärquellen abgeglichen. Wo die Aussage zwingend eine konkrete Rechts-, Datenschutz-, Forensik- oder Tenant-Fachbeurteilung voraussetzt, ist sie ausdrücklich mit **[FACHPRÜFUNG ERFORDERLICH]** versehen. Insgesamt wurden 25 solcher Marker gesetzt.

Eine öffentliche Veröffentlichung ist erst nach den in den einzelnen Dateien markierten externen Fachprüfungen vertretbar. Dies ist kein behaupteter Prüfnachweis, sondern eine sichtbare Freigabesperre für die betroffenen Aussagen.

## Prüfungsmassstab und Quellenabgleich

Die Prüfung umfasste Struktur, Schweizer Hochdeutsch, Suchintention, E-E-A-T-Signale, Meta-Daten, interne Links, CTAs, Quellenformat und Zusagen in Arbeitsmitteln. Verifiziert wurden insbesondere die gesetzlichen Meldewege nach DSG, DSV, ISG und CSV, die BACS-Empfehlungen zur Vorfallsbehandlung und die Microsoft-Produktdokumentation zu Entra ID. Die BACS-Meldepflicht gilt seit 1. April 2025 für erfasste kritische Infrastrukturen; die Erstmeldung muss innert 24 Stunden nach Entdeckung erfolgen und fehlende Angaben sind innert 14 Tagen zu ergänzen. Eine EDÖB-Meldung nach Art. 24 DSG erfolgt dagegen bei voraussichtlich hohem Risiko so rasch als möglich; eine pauschale Schweizer 72-Stunden-Frist besteht nicht. [1] [2] [3]

Für Microsoft Entra ID wurden die zeitabhängigen Aussagen im Passkey-Beitrag besonders geprüft. Microsoft nennt für die Public Cloud den 1. September 2026 für die automatische Passkey-Aktivierung bei SMS-/Voice-aktivierten Benutzerinnen und Benutzern, den 1. Februar 2027 für die Einstellung der Microsoft-bereitgestellten SMS-/Voice-Übermittlung für die meisten Benutzergruppen und den 1. Juli 2027 für globale Administratoren und externe Benutzer. Die Herstellerdokumentation kann sich ändern; daher sind Produktfristen, Lizenzen, Tenant-Umfang und Konfiguration vor Produktivsetzung extern zu prüfen. [4]

Für Ransomware-, Backup- und Zahlungsbetrugsthemen wurden die BACS- und CISA-Primärquellen herangezogen. Sie stützen unter anderem die koordinierte Isolation betroffener Systeme, die Sicherung von Logdaten und flüchtigen Spuren, den Einsatz unabhängiger Kommunikationswege, die Wiederherstellung aus Offline-Backups sowie den unabhängigen Rückruf bei verdächtigen Zahlungsanweisungen. [5] [6] [7] [8]

## Durchgeführte Korrekturen

| Prüffeld | Korrektur und Ergebnis |
|---|---|
| **Struktur und Metadaten** | Fehlende beziehungsweise uneinheitliche Metadaten wurden in allen zwölf Dateien als YAML-Frontmatter vereinheitlicht. Doppelte, im Textkörper sichtbare Metadatenblöcke in Artikel 03 und 05 wurden entfernt. |
| **Suchintention und E-E-A-T** | Jede Datei enthält nun eine explizite Suchintention. Hypothetische Fälle bleiben als solche gekennzeichnet. Allgemeine Orientierung, Quellenstand, Autorenschaft und konkrete Abgrenzungen zur Einzelfallberatung sind sichtbar. |
| **Rechts- und Meldeangaben** | EDÖB- und BACS-Meldewege wurden klar getrennt. Die unzutreffende Verknüpfung von Ransomware mit automatischer Meldepflicht wurde vermieden. Fristen und Kriterien wurden anhand von BACS, EDÖB und Erlassen formuliert. [1] [2] [3] |
| **Produktspezifische Aussagen** | Microsoft-Entra-Termine, Benutzergruppen, Passkey-Registrierung, Conditional Access, TAP, Notfallkonten und Audit-Aufbewahrung wurden am Herstellertext gespiegelt. Pauschale Tenant-Zusagen wurden entfernt oder als prüfpflichtig markiert. [4] [9] [10] |
| **Unbelegte oder zu starke Aussagen** | Spekulative BEC-Zuordnungen wurden als Arbeitshypothese eingeordnet. Das vorzeitige Behaupten einer kompromittierten Partnermailbox wurde entfernt. CTAs versprechen keine Auditergebnisse, Wiederherstellbarkeit oder Sicherheitswirkung mehr. |
| **Arbeitsmittel und Garantien** | Alle sechs Vorlagen enthalten ausdrückliche Grenzen. Keine Vorlage verspricht nun eine rechtzeitige oder rechtlich ausreichende Meldung, erfolgreiche Wiederherstellung, unterbruchsfreie Anmeldung, Betrugsverhinderung oder Tenant-Sicherheit. |
| **Interne Links und CTA** | Artikel verlinken die passenden Arbeitsmittel unter `/resources/01-…` bis `/resources/06-…`; ein fehlerhafter relativer Ressourcenlink in Artikel 04 wurde korrigiert. CTAs wurden sachlich und ohne Leistungszusage formuliert. |
| **Quellenformat** | Quellenüberschriften wurden einheitlich deutschsprachig als „Quellen“ geführt. Jede genutzte Referenz ist definiert; ungenutzte Portalquelle in Artikel 01 wurde entfernt. |
| **Sprachqualität** | Schreibweise, Terminologie und Satzbau wurden auf Schweizer Hochdeutsch vereinheitlicht, insbesondere bei „E-Mail“, „so rasch als möglich“, „innert“, „Meldepflicht“, „Auftragsbearbeiter“ und „Fachprüfung“. |

## Dateispezifisches Ergebnis

| Datei | Ergebnis der Korrektur | Verbleibende Freigabevoraussetzung |
|---|---|---|
| `articles/01-ransomware-erste-60-minuten.md` | Akutablauf, Backups, Polizei-, BACS- und EDÖB-Einordnung präzisiert; nicht mehr benötigte Portalquelle entfernt; CTA ohne Leistungsversprechen. | Externe Prüfung der konkreten forensischen Vorgehensweise, BACS-Unterstellung, DSG-Risikobewertung und Lösegeld-/Sanktionsfragen. |
| `articles/02-ceo-betrug-business-email-compromise.md` | CEO-Betrug und BEC vorsichtiger abgegrenzt; die Diagnose einer kompromittierten Mailbox nicht mehr als Schlussfolgerung aus einer einzelnen Nachricht dargestellt; Zahlungsprozess und CTA bereinigt. | Datenschutzrechtliche Prüfung bei konkretem Mailbox- oder Personendatenvorfall. |
| `articles/03-datenpanne-melden-schweiz.md` | Doppelte Metadaten entfernt; EDÖB-/BACS-Entscheidung sauber getrennt; 72-Stunden-Verwechslung eingeordnet; Arbeitsmittel korrekt verlinkt. | Externe Datenschutz-, sektor- und gegebenenfalls aufsichtsrechtliche Prüfung jedes konkreten Meldefalls. |
| `articles/04-ransomware-resistente-backups.md` | Relativer Ressourcenlink korrigiert; RPO/RTO ausdrücklich als Ziele statt Zusagen eingeordnet; rechtliche Speicher- und Aufbewahrungsfragen markiert; CTA ohne Wiederherstellbarkeitsgarantie. | Fachliche Architekturprüfung sowie fachjuristische Prüfung von Aufbewahrung, Löschung und Datenschutzbezug. |
| `articles/05-microsoft-365-mfa-passkeys.md` | Doppelte Metadaten entfernt; zeitlich zu enge Überschrift neutralisiert; aktuelle Microsoft-Termine und Benutzergruppen präzisiert; Notfallkonto-Aussage auf Herstellerempfehlung beschränkt. | Microsoft-Entra-Fachprüfung von Public-Cloud-Geltung, Fristen, Lizenzen, Tenant-Einstellungen und Produktivrollout. |
| `articles/06-microsoft-365-sicherheit-kmu.md` | Sicherheits- und Audit-Aussagen risikobasiert formuliert; CTA ohne Massnahmenplan-Zusage; Datenschutzhinweise und Provider-Governance als prüfpflichtig markiert. | Tenant-Fachprüfung sowie Datenschutz-/Rechtsprüfung von Auftragsbearbeitung und Auslandbekanntgaben. |
| `resources/01-60-minuten-checkliste.md` | Einheitliche Metadaten und klare Haftungsgrenzen ergänzt; keine Aussage über Schadensvermeidung, Angreiferfreiheit oder sichere Wiederherstellung. | Vor produktiver Verwendung Fachprüfung für organisationsspezifische Notfall-, Melde- und Forensikwege. |
| `resources/02-zahlungspruefprotokoll.md` | Metadaten ergänzt; Kontoübernahme als technisch abzuklärender Verdacht eingeordnet; keine Betrugs- oder Schadensverhinderung zugesagt. | Fachprüfung, falls ein konkreter Personendaten- oder Rechtsfall ausgelöst wird. |
| `resources/03-datenpanne-entscheidungsbaum.md` | Metadaten ergänzt; die Vorlage entscheidet ausdrücklich keine Meldepflicht; alle rechtlich relevanten Entscheide sichtbar mit Prüfmarker versehen. | Datenschutz-, aufsichts- und sektorrechtliche Fachprüfung konkreter Meldungen und Kommunikation. |
| `resources/04-backup-selbstcheck.md` | Metadaten ergänzt; keine Backup-, Ransomware- oder Wiederherstellbarkeitsgarantie; rechtliche Aufbewahrungsfragen markiert. | Architektur- und bei Bedarf fachjuristische Prüfung der konkreten Sicherungs- und Aufbewahrungsregel. |
| `resources/05-passkey-rollout-checkliste.md` | Metadaten ergänzt; Microsoft-Termingruppen präzisiert; Produktivsetzung explizit gesperrt, bis Herstellerstand und Tenant geprüft sind. | Microsoft-Entra-Fachprüfung von Produktstand, Tenant, Lizenz und Wiederherstellungsprozess. |
| `resources/06-m365-tenant-pruefliste.md` | Metadaten ergänzt; klar als Bestandsaufnahme statt Audit, Zertifizierung oder Sicherheitszusage abgegrenzt. | Tenant-Test sowie Datenschutz-/Rechtsprüfung bei Cloud- und Providerdatenflüssen. |

## Verbleibende Blocker vor der Veröffentlichung

Die Dateien sind redaktionell bereinigt, aber nicht pauschal veröffentlichungsreif. Folgende Punkte sind in den Originaldateien mit **[FACHPRÜFUNG ERFORDERLICH]** markiert und bleiben echte Freigabeblocker:

1. **Recht und Datenschutz:** Die Einstufung eines konkreten Vorfalls, das voraussichtlich hohe Risiko nach Art. 24 DSG, EDÖB-Meldung, Information Betroffener, BACS-Unterstellung, sektorspezifische Pflichten, Auftragsbearbeitung, Auslandbekanntgaben, Aufbewahrung und Löschkonzepte sind Einzelfallfragen.
2. **Forensik und Incident Response:** Isolierung, Beweissicherung, Systembereinigung, Wiederanlauf und Umgang mit Lösegeld müssen im konkreten Vorfall durch geeignete Fachpersonen beurteilt werden.
3. **Microsoft Entra ID:** Öffentliche Produkt-, Termin-, Lizenz- und Konfigurationsaussagen müssen vor Publikation sowie vor jedem Rollout gegen die aktuelle Microsoft-Learn-Dokumentation und den betroffenen Tenant geprüft werden.
4. **Backup und Wiederherstellung:** Architektur, Schutzfristen, Rechte, RPO/RTO und Restore-Tests benötigen eine organisationsspezifische technische Beurteilung. Ein Arbeitsmittel oder ein einzelner Test ersetzt diese nicht.

## Schlussvalidierung

Die finale automatisierte Prüfung bestätigte für alle zwölf Dateien vollständige Pflichtmetadaten, eine veröffentlichungsgesperrte Statusangabe, einen H1-Titel, gültige Quellenreferenzen, konsistente interne Links und keine verbliebenen unqualifizierten Garantieformulierungen. Die folgende Tabelle fasst die Referenzprüfung zusammen.

| Datei | Genutzte / definierte Quellen | Fachprüfungsmarker | Fehler | Warnungen |
|---|---:|---:|---:|---:|
| Artikel 01 | 9 / 9 | 3 | 0 | 0 |
| Artikel 02 | 11 / 11 | 1 | 0 | 0 |
| Artikel 03 | 10 / 10 | 3 | 0 | 0 |
| Artikel 04 | 14 / 14 | 1 | 0 | 0 |
| Artikel 05 | 13 / 13 | 2 | 0 | 0 |
| Artikel 06 | 10 / 10 | 2 | 0 | 0 |
| Arbeitsmittel 01 | 7 / 7 | 1 | 0 | 0 |
| Arbeitsmittel 02 | 4 / 4 | 1 | 0 | 0 |
| Arbeitsmittel 03 | 8 / 8 | 5 | 0 | 0 |
| Arbeitsmittel 04 | 7 / 7 | 1 | 0 | 0 |
| Arbeitsmittel 05 | 7 / 7 | 3 | 0 | 0 |
| Arbeitsmittel 06 | 9 / 9 | 2 | 0 | 0 |
| **Gesamt** | **109 / 109** | **25** | **0** | **0** |

Die Abruf- und Validierungsartefakte liegen zur Nachvollziehbarkeit im aufgabenspezifischen Arbeitsordner unter `/home/ubuntu/jobs/eb75c13b82f0_a12/`; sie sind keine Bestandteile des zu veröffentlichenden Blog-Pakets.

## Quellen

[1]: https://www.bacs.admin.ch/de/informationen-zur-meldepflicht "BACS – Informationen zur Meldepflicht für Cyberangriffe auf kritische Infrastrukturen"
[2]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz (DSG), insbesondere Art. 5 und 24"
[3]: https://www.edoeb.admin.ch/dam/de/sd-web/T64CAUyvAMcF/1_2%20Leitfaden%20des%20ED%C3%96B%20betreffend%20die%20Meldung%20von%20Datensicherheitsverletzungen%20und%20Information%20der%20Betroffenen%20nach%20Art.%2024%20DSG_DE.pdf "EDÖB – Leitfaden zur Meldung von Datensicherheitsverletzungen und Information der Betroffenen nach Art. 24 DSG"
[4]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement "Microsoft Learn – Passkeys by default and retirement of Microsoft-provided SMS and voice authentication"
[5]: https://www.bacs.admin.ch/de/ransomware-was-nun "BACS – Ransomware: Was nun?"
[6]: https://www.cisa.gov/stopransomware/ive-been-hit-ransomware "CISA – I've Been Hit By Ransomware! Response Checklist"
[7]: https://www.cisa.gov/stopransomware/ransomware-guide "CISA – StopRansomware Guide"
[8]: https://www.bacs.admin.ch/de/business-email-compromise-de "BACS – Business E-Mail Compromise (Rechnungsmanipulationsbetrug)"
[9]: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access "Microsoft Learn – Manage emergency access accounts in Microsoft Entra ID"
[10]: https://learn.microsoft.com/en-us/purview/audit-log-retention-policies "Microsoft Learn – Manage audit log retention policies"
