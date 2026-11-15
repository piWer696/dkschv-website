# Artikel 06 – Quellenprüfung und Änderungen

**Prüfdatum:** 18. Oktober 2026, ISO-Woche 42  
**Prüfzeit:** Originalquellen ab 09:04 Europe/Zurich (Abrufe 09:04–09:06 Europe/Zurich; nach dem vorgegebenen Prüfzeitpunkt 09:00)  
**Gegenstand:**

- Artikel: `blog-paket/articles/06-microsoft-365-sicherheit-kmu.md`
- Arbeitsmittel: `blog-paket/resources/06-m365-tenant-pruefliste.md`

Der Eintrag im Wartungsmanifest wurde als verbindliche Grundlage gelesen. Manifestierte Primärquellen wurden zuerst geprüft. Zusätzlich wurden alle in Artikel und Arbeitsmittel referenzierten Originalquellen sowie die verlangten BACS-Hinweise und die Übersicht «Im Fokus» geprüft. Es wurden keine anderen Paketdateien, Manifeste, QA-Skripte oder CMS-Inhalte geändert.

> **Ergebnis:** Alle 12 eindeutigen, in Artikel und Arbeitsmittel zitierten externen Quellen waren am 18. Oktober 2026 erreichbar und stützten die jeweils verwendeten Aussagen. Der Artikel und das Arbeitsmittel bleiben Entwürfe; dies ist weder eine Fach-, Rechts-, Tenant-, Forensik- noch Publikationsfreigabe.

## Quellenprüfung

| Nr. | Originalquelle | Datierter Quellenstand, soweit belegt | Abruf / Erreichbarkeit | Prüfungsergebnis |
|---:|---|---|---|---|
| 1 | [BACS – Zusammenarbeit mit IT-Dienstleistern](https://www.bacs.admin.ch/de/empfehlungen-fuer-die-zusammenarbeit-mit-it-providern) | Kein sichtbares Publikations- oder Änderungsdatum | 18.10.2026, ab 09:04; erreichbar | Stützt klare Zuständigkeiten, nicht delegierbare Verantwortung, MFA, Monitoring, Notfallkontakt, 3-2-1 und Wiederherstellungstest. |
| 2 | [EDÖB – Cloud-Computing](https://www.edoeb.admin.ch/de/datenbearbeitungen-in-der-cloud) | Kein sichtbares Publikations- oder Änderungsdatum | 18.10.2026, ab 09:05; erreichbar | Stützt die Regelrolle als Auftragsbearbeiter, die Verantwortung des Cloud-Nutzers sowie die Prüffragen zu Weisung, Sicherheit, Unterauftragsbearbeitung, Bearbeitungsländern und Mitwirkung. |
| 3 | [Fedlex – DSG, geltender Text](https://www.fedlex.admin.ch/eli/cc/2022/491/de) | **Stand am 7. Juli 2025**, in Kraft seit 01.09.2023; amtliche Chronologie zuletzt: Berichtigung vom 07.07.2025 | 18.10.2026, ab 09:05; erreichbar | Art. 7 bis 9 wurden auf der amtlichen HTML-Seite sowie über die amtliche [XML-Fassung](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml) und [Chronologie](https://www.fedlex.admin.ch/eli/cc/2022/491/de/history) bestätigt. Art. 7 betrifft Datenschutz durch Technikgestaltung/Voreinstellungen, Art. 8 risikoadäquate Datensicherheit, Art. 9 Auftragsbearbeitung und vorgängige Genehmigung einer Weiterübertragung. Keine neuere DSG-Fassung war auf der amtlichen Chronologie ausgewiesen. |
| 4 | [Microsoft Learn – Mandatory multifactor authentication for Azure and admin portals](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication) | **Last updated 03.04.2026** | 18.10.2026, ab 09:05; erreichbar | Bestätigt die seit Februar 2025 schrittweise MFA-Durchsetzung für administrative Vorgänge im Microsoft-365-Admincenter, den begrenzten Geltungsbereich sowie Conditional Access P1/P2 und Security Defaults als Alternative. |
| 5 | [Microsoft Learn – Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access) | **Last updated 05.06.2026** | 18.10.2026, ab 09:05; erreichbar | Bestätigt mindestens zwei cloudnative Notfallkonten, dauerhafte aktive Global-Administrator-Rolle, phishing-resistente Anmeldung mit Passkey FIDO2 oder zertifikatbasierter Authentisierung, Ausschluss von blockierenden Conditional-Access-Regeln, Überwachung und Test mindestens alle 90 Tage. |
| 6 | [Microsoft Learn – Best practices for Microsoft Entra roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/best-practices) | **Last updated 01.06.2026** | 18.10.2026, ab 09:05; erreichbar | Bestätigt Least Privilege, PIM für zeitlich begrenzte Aktivierung, weniger als fünf Global Administrators sowie weniger als zehn privilegierte Rollenzuweisungen als Richtwerte und die Lizenzabhängigkeit von PIM. |
| 7 | [Microsoft Learn – Manage sharing settings for SharePoint and OneDrive in Microsoft 365](https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off) | **Last updated 30.06.2026** | 18.10.2026, ab 09:05; erreichbar | Bestätigt Freigabestufen, nicht authentisierte «Jeder»-Links, die Beschränkung von Sites auf gleich oder restriktiver als die Organisation und OneDrive auf nicht offener als SharePoint; bestätigt Domains, Sicherheitsgruppen und Gastablauf. |
| 8 | [Microsoft Learn – Learn about auditing solutions in Microsoft Purview](https://learn.microsoft.com/en-us/purview/audit-solutions-overview) | **Last updated 18.05.2026** | 18.10.2026, ab 09:05; erreichbar | Bestätigt aktiviertes Audit Standard bei passendem Abonnement, 180 Tage Standardaufbewahrung, Audit Premium mit längeren Aufbewahrungsoptionen und Lizenzbezug. |
| 9 | [Microsoft Learn – Manage audit log retention policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) | **Last updated 19.06.2026** | 18.10.2026, ab 09:05; erreichbar | Bestätigt Audit-Premium-Aufbewahrungsrichtlinien bis zehn Jahre sowie die Lizenz- und Nicht-Rückwirkungsgrenzen. |
| 10 | [BACS – Cloud Computing und Cybersicherheit](https://www.bacs.admin.ch/de/cloud-computing-und-cybersicherheit) | Verweis auf Technologiebetrachtung vom **02.05.2025**; kein sichtbares Datum der HTML-Seite | 18.10.2026, ab 09:05; erreichbar | Bestätigt Exportierbarkeit sowie Offline-Backup als Anforderung im BACS-Prüfprozess und verweist auf MFA, Verschlüsselung und Zugriffsprotokollierung. |
| 11 | [BACS – KI im Berufsalltag: Chancen nutzen, Daten schützen](https://www.bacs.admin.ch/de/csm26-s3-de) | Veröffentlicht **16.10.2026** | 18.10.2026, ab 09:05; erreichbar | Neue, einschlägige BACS-Quelle: Vor KI-Eingaben sensible oder persönliche Daten prüfen und anonymisieren; wenn möglich Unternehmens- statt Privatkonten verwenden, Trainingsnutzung und Opt-out prüfen. |
| 12 | [BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion](https://www.bacs.admin.ch/de/26w40-de) | Veröffentlicht **06.10.2026** | 18.10.2026, ab 09:05; erreichbar | Verlangte Quelle. Für geschäftlich verwendete Geräte: zuständige IT informieren, Untersuchung durch Fachperson; bei bestätigter Infektion nennt BACS Neuaufsetzen und anschliessende Passwortwechsel. Kein pauschaler Forensik- oder Tenant-Handlungsauftrag daraus abgeleitet. |

### Zusätzlich verlangte und beobachtete BACS-Quellen

| Quelle | Datierter Quellenstand | Abruf / Erreichbarkeit | Einordnung für Artikel 06 |
|---|---|---|---|
| [BACS – Cyber Security Month 2026: «Oversharing»](https://www.bacs.admin.ch/de/csm26-s2-de) | Veröffentlicht **05.10.2026** | 18.10.2026, ab 09:05; erreichbar | Verlangt einbezogen. Sie nennt unter anderem ein unbedacht in ein KI-Tool eingegebenes internes Dokument. Die konkretere, neuere BACS-Quelle vom 16.10.2026 wurde deshalb als Referenz [11] verwendet; die Meldung vom 05.10.2026 wird nicht ungenutzt in Artikel oder Arbeitsmittel referenziert. |
| [BACS – Im Fokus](https://www.bacs.admin.ch/de/im-fokus) | Übersicht bei Abruf bis **15.10.2026**; einschlägig: 06.10.2026 und 05.10.2026; der Eintrag vom 16.10.2026 war über die direkte Original-URL erreichbar | 18.10.2026, ab 09:06; erreichbar | Neuere Einträge bis 15.10.2026 betrafen insbesondere Online-Shops und internationale Termine und erforderten keine Änderung. Der direkte Beitrag vom 16.10.2026 war für externe Zusammenarbeit/Datenfreigaben einschlägig und wurde ergänzt. |

**Erreichbarkeit aller Referenzen:** `all_references_verified=true`. Es gibt keine nicht erreichbare oder nur per Snippet bewertete Quelle. Fedlex wurde trotz JavaScript-Hinweis über die amtliche History- und XML-Ressource geprüft; es wurde keine unbelegte Rechtsfassung oder Freigabe erfunden.

## Änderungen am Artikel

### Metadaten und Struktur

| Element | Vorher | Nachher |
|---|---|---|
| `status`, `slug`, Veröffentlichungsdatum, `fachprüfung_status` | Unverändert | Unverändert; Entwurfsstatus und alle bestehenden Fachprüfungsmarker erhalten. |
| `stand` | `4. Oktober 2026` | `18. Oktober 2026` – ausschliesslich Datum dieser Quellenprüfung. |
| `quellenpruefung_umfang` | Nicht vorhanden | Ergänzt: alle externen Quellenreferenzen beider Dateien und BACS «Im Fokus» bis 18.10.2026; keine Tenant- oder Live-Linkprüfung. |
| `quellenpruefung_status` | Nicht vorhanden | Ergänzt: vollständig für referenzierte Quellen, keine Fach-, Rechts-, Tenant- oder Publikationsfreigabe. |
| Meta-Title und Meta-Description | `Microsoft 365 sicher konfigurieren: KMU-Check | DKSchV` beziehungsweise bestehende Beschreibung | **Unverändert**, da die Ergänzungen keine Anpassung der Suchmetadaten verlangen. |
| H1, Kurzantwort, Gliederung und interne relative Links | Vorhanden | Erhalten. Keine künftige DKSchV-URL als live geprüft oder behauptet. |

### Inhaltliche Änderungen

| Betroffener Abschnitt | Vorher | Nachher und Grund |
|---|---|---|
| **1. Identitäten zuerst: Konten, MFA und Wiederherstellung** | MFA-Durchsetzung seit Februar 2025 für Anmeldungen im Microsoft-365-Admincenter. | Präzisiert auf Konten, die dort administrative Vorgänge durchführen. Das entspricht dem aktuellen Microsoft-Geltungsbereich in Quelle [4]. |
| **Notfallzugänge schützen – und trotzdem testbar halten** | «starke und von den normalen Admin-Konten unterschiedliche Authentisierung». | Mit Passkey FIDO2 oder zertifikatbasierter, phishing-resistenter Anmeldung konkretisiert; Überwachung und mindestens 90-tägiger Test bleiben belegt. Quelle [5] wurde 05.06.2026 aktualisiert. |
| **3. Externe Freigaben gezielt statt pauschal öffnen** | Kein spezifischer KI-Eingabehinweis. | Neuer, klar begrenzter Absatz zu internen Inhalten, Personendaten und Geschäftsgeheimnissen in KI-Tools; BACS-Empfehlungen vom 16.10.2026 als neue Quelle [11]. Konkrete Datenflüsse und Einstellungen bleiben ausdrücklich fachprüfungspflichtig. |
| **5. Backup-Verantwortung: Wiederherstellung konkret definieren** | Wiederherstellungsprobe ohne aktuelle Abgrenzung zum Malwareverdacht. | Neuer Absatz zur Abgrenzung: BACS-Quelle vom 06.10.2026 nennt Fachuntersuchung und bei bestätigter Infektion Neuaufsetzen/Passwortwechsel. Keine organisationsspezifische forensische oder Wiederanlaufanweisung; Quelle [12]. |
| **Quellen** | Quellen [1] bis [10]. | Neue, tatsächlich im Text verwendete Primärquellen [11] BACS KI im Berufsalltag und [12] BACS Woche 40. Keine ungenutzte Referenz ergänzt. |

Der Artikel umfasst nach der Änderung **mehr als 1'400 Wörter**. Schweizer Schreibweise ohne ß bleibt erhalten.

## Änderungen am Arbeitsmittel

### Metadaten und Struktur

| Element | Vorher | Nachher |
|---|---|---|
| `status`, `slug`, `titel`, `bezug`, `fachprüfung_status` | Unverändert | Unverändert; Arbeitsvorlage und Fachprüfungsmarker bleiben erhalten. |
| `version` | `Stand 4. Oktober 2026` | `Stand 18. Oktober 2026` – konsistent mit dem Quellenprüfdatum des Artikels. |
| `quellenpruefung_umfang` | Nicht vorhanden | Ergänzt, identisch in der Reichweite zum Artikel. |
| `quellenpruefung_status` | Nicht vorhanden | Ergänzt, identisch in der Einschränkung zum Artikel. |
| Meta-Title und Meta-Description | Bestehende Angaben | **Unverändert**, weil der Kontrollpunkt die bestehende Einordnung ergänzt, aber den Gegenstand der Vorlage nicht verändert. |

### Inhaltliche Änderungen

| Betroffener Abschnitt | Vorher | Nachher und Grund |
|---|---|---|
| **A. Identitäten und Anmeldung – Prüfnotiz A6** | Allgemeine starke, abweichende Authentisierung. | Phishing-resistente Anmeldung mit Passkey FIDO2 oder zertifikatbasierter Authentisierung konkretisiert; Überwachung und mindestens 90-tägiger Test ergänzt. Quelle [3]. |
| **C. Externe Zusammenarbeit und Freigaben – Kontrollpunkt C7** | Kein KI-spezifischer Kontrollpunkt. | Neuer Kontrollpunkt zur Regelung von Eingaben in KI-Tools, Prüfung sensibler Inhalte und gegebenenfalls Anonymisierung. Grundlage: BACS vom 16.10.2026, Quelle [10]. |
| **C. Externe Zusammenarbeit und Freigaben – Prüfnotiz C7** | Nicht vorhanden. | Neue Prüfnotiz mit BACS-Empfehlungen zu Unternehmens- statt Privatkonten, Trainingsnutzung und Opt-out; konkrete Zulässigkeit, Datenflüsse und Einstellungen sind ausdrücklich als **[FACHPRÜFUNG ERFORDERLICH]** abgegrenzt. |
| **E. Wiederherstellung und Backup-Verantwortung – Prüfnotiz zum Vorfallbezug** | Nicht vorhanden. | Neue, begrenzte BACS-Notiz zu Malwareverdacht auf Geschäftsgeräten. Sie ist ausdrücklich kein Ersatz für eine organisationsspezifische forensische oder Wiederanlaufentscheidung. Quelle [11]. |
| **Quellen** | Quellen [1] bis [9]. | Neue, verwendete Quellen [10] BACS KI im Berufsalltag und [11] BACS Woche 40. |

## Metadaten, Link- und Statuskontrolle

- **Original-Slug Artikel:** `/wissen/microsoft-365-sicherheit-kmu` – erhalten.
- **Original-Slug Arbeitsmittel:** `/resources/06-m365-tenant-pruefliste` – erhalten.
- **Veröffentlichungsdatum Artikel:** `05.11.2026` – erhalten.
- **Interne relative Paketlinks:** erhalten; keine Zielseite wurde als live geprüft oder als live dargestellt.
- **Externe Quellenlinks:** alle zitierten Links erreichbar und in den Quellenabschnitten numerisch definiert.
- **Entwurfsstatus:** Artikel `Entwurf – nicht freigegeben`, Arbeitsmittel `Arbeitsvorlage – nicht freigegeben` – erhalten.
- **Fachprüfungsmarker:** alle vorher bestehenden Marker erhalten; weitere Marker nur dort ergänzt, wo die neue KI-Aussage konkrete Datenflüsse/Einstellungen berühren könnte.
- **Nicht gesetzt oder geändert:** `rechtsstand`, `fachlich_geprueft_am` und jede Freigabeangabe. Eine Quellenprüfung ersetzt keine juristische oder fachliche Prüfung.

## Offene Fach- und Publikationsblocker

1. **Tenant-Prüfung offen:** Lizenzierung, aktivierte Richtlinien, Notfallkonten, Rollen, Audit-Aufbewahrung, Freigaben, Apps, Logs, Backup-Abdeckung und Wiederherstellbarkeit wurden nicht in einem konkreten Tenant geprüft.
2. **Fachprüfung offen:** Die datenschutzrechtliche Tragfähigkeit von Auftragsbearbeitung, Unterauftragsbearbeitung, Datenbearbeitungsorten, Auslandbekanntgaben sowie KI-Datenflüssen ist je konkretem Sachverhalt zu beurteilen. Die neue Frage lautet: *Welche Daten dürfen im konkret freigegebenen Microsoft-365- oder KI-Dienst verarbeitet werden, welche Trainings-/Weiterverwendungsoptionen, Auftragsbearbeitungen und Auslanddatenflüsse gelten und welche technischen Einstellungen belegen dies?*
3. **Vorfall/Forensik offen:** Die BACS-Meldung vom 06.10.2026 ersetzt keinen organisationsspezifischen Entscheid über Beweissicherung, Untersuchung, Isolation, Neuaufsetzen oder Wiederanlauf.
4. **Publikation blockiert:** Alle Entwurfs- und Fachprüfungsmarker bleiben offen. Ein Veröffentlichungsdatum, die lokale Quellenprüfung oder diese Dokumentation sind keine Freigabe. Vor Go-live sind ein tatsächlich freigegebener Inhalt, ein aktueller Fachentscheid, ein authentifizierter CMS-Zugang und die öffentlichen Zielseiten erneut zu prüfen.
