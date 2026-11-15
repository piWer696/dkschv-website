# Artikel 06 – Quellenprüfung und Änderungen

**Prüfdatum:** 15. November 2026, Europe/Zurich CET, ISO-KW 46. **Veröffentlichungsstatus:** Artikel «Entwurf – nicht freigegeben», Arbeitsmittel «Arbeitsvorlage – nicht freigegeben»; unverändert. Der Artikeltermin 05.11.2026 ist verstrichen, begründet aber keine Freigabe.

Artikel 06 und das zugehörige Arbeitsmittel wurden materiell ergänzt: exponierte App-Secrets und historische Nutzung, getrennte Single-Tenant-/Multitenant-Reichweite, aktuelle ConnectWise-Wiederherstellungsorientierung, Mail-Sicherheitsausnahmen und getrennte Protokollabdeckung. **21 eindeutige zitierte Originalquellen beider Dateien** sind in den relevanten Passagen auslesbar. **30 eindeutige Original-URLs insgesamt** wurden direkt mit `fetch` geöffnet, einschliesslich 9 ergänzender Journalquellen. Kein Originalabruf blieb ohne lesbaren relevanten Inhalt. Gekürzte Extraktionen und der inhaltliche Widerspruch zur Anzahl der ConnectWise-App-IDs werden unten ausdrücklich ausgewiesen. Das ist keine Zusage umfassender weltweiter Nachrichtenerfassung.

**Tatsächliche Abrufe:** Suchantwort 15.11.2026 um 09:06:09 CET; direkte Originalrückgaben zwischen **09:06:08 und 09:07:41 CET**. Ergänzende lokale Lektüre gespeicherter Originalextraktionen bis **09:08:13 CET**. Diese Zeiten stammen aus den tatsächlichen Werkzeugrückgaben, nicht aus einer behaupteten historischen Prüfung um 09:00. Der exakte Wortlaut nicht versionierter Seiten um 09:00 ist nicht rekonstruiert. Alle Abrufe erfolgten nach 09:00. Die genannten Publikations-/Änderungsdaten der Quellen sind von den heutigen Abrufzeiten zu unterscheiden.

Geprüft wurden die beiden freigegebenen lokalen Dateipfade, die Wartungsbasis, Vorwochennews, der Laufstatus vom 08.11. und der Einzelbericht vom 01.11. Nur Artikel 06, seine Vorlage und dieser Bericht wurden geändert. Es gab keine CMS-/Browseroperation, keine Verwendung von Zugangsdaten, keine Tenant- oder Protokolleinsicht und keine Konfigurationsänderung. Erreichbarkeit und allgemeiner Aussagegehalt sind keine Einzelfallprüfung und keine Fach-, Rechts-, Forensik-, Tenant-, Produkt-, Hersteller- oder Publikationsfreigabe.

## Quellenjournal je externer Originalquelle

Die Nummern dieses Journals entsprechen für [1]–[21] den Artikelreferenzen. Das Arbeitsmittel verwendet für dieselben Quellen eine eigene Nummerierung: DSG [1], EDÖB [2], Notfallkonten [3], Rollen [4], Freigaben [5], Audit [6]–[7], BACS-Cloud/Provider [8]–[9], BACS-KI/Malware [10]–[11], App-Monitoring/Storm/Widerruf [12]–[14], neue Quellen [15]–[20]. Alle 21 Artikelreferenzen und alle 20 Vorlagenreferenzen sind tatsächlich zitiert; keine ungenutzte Definition. Journalquellen [22]–[30] werden nur hier verwendet.

### Bestehende zitierte Quellen

**[1] BACS – Zusammenarbeit mit IT-Dienstleistern.** Original-URL: <https://www.bacs.admin.ch/de/empfehlungen-fuer-die-zusammenarbeit-mit-it-providern>. Abruf 15.11.2026, **09:06:08 CET**, Erfolg, ungekürzt auslesbar. Kein sichtbares Publikations-/Änderungsdatum. Bestätigt klare Zuständigkeiten für technische und organisatorische Massnahmen, nicht delegierbare Verantwortung, MFA, Monitoring, Notfallwege sowie Backup-Konzept und Restore-Tests. Einschränkung: allgemeine Behördenempfehlung, keine Prüfung des Providervertrags oder der tatsächlichen Leistungen.[1]

**[2] EDÖB – Cloud-Computing.** Original-URL: <https://www.edoeb.admin.ch/de/datenbearbeitungen-in-der-cloud>. Abruf 15.11.2026, **09:06:08 CET**, Erfolg, ungekürzt. Kein sichtbares Publikations-/Änderungsdatum. Bestätigt Cloud-Anbieter in der Regel als Auftragsbearbeiter, Verantwortung des Cloud-Nutzers, Prüfung von Weisungsbindung, Sicherheit, Unterauftrag, Ländern und Mitwirkung. Einschränkung: keine rechtliche Bewertung konkreter M365-Datenflüsse oder Verträge.[2]

**[3] Fedlex – DSG, Art. 7–9.** Original-URL: <https://www.fedlex.admin.ch/eli/cc/2022/491/de>. Abruf 15.11.2026, **09:06:08 CET**, `partial` wegen Ausgabelimit; relevante Art. 7–9 und Fassungshinweis auslesbar. Die Seite nennt **Stand 7. Juli 2025**, «in Kraft» und die entsprechenden Fassungen. Art. 7 stützt datenschutzfreundliche Voreinstellungen, Art. 8 risikoadäquate Datensicherheit, Art. 9 Vergewisserung über die Datensicherheit des Auftragsbearbeiters und vorgängige Genehmigung der Weiterübertragung. Einschränkung: Die Startseite zeigt angekündigte Wartungsarbeiten vom 13.11., 20:00 bis 15.11., 20:00; trotz dieser Warnung waren relevante Inhalte jetzt lesbar. Kein Erreichbarkeitsversprechen für spätere Abrufe. History und vorhandene amtliche XML ergänzend direkt geprüft, siehe [22]–[23]. Kein Rechtsstand-/Fachfreigabedatum geändert oder neu angelegt.[3]

**[4] Microsoft Learn – Mandatory MFA.** Original-URL: <https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication>. Abruf 15.11.2026, **09:06:10 CET**, `partial`, relevante Durchsetzungs-/Kontoabschnitte auslesbar; gespeicherter FAQ-Abschluss am 09:07:16 CET gelesen. Metadaten `ms.date` 03.04.2026, `updated_at` 06.10.2026. Bestätigt M365-Admincenter-Rollout seit Februar 2025, eigene Zugriffspolitiken, P1/P2 für Conditional Access und Security Defaults als Basisalternative. Workload Identities sind nicht von dieser MFA-Durchsetzung erfasst, für Automatisierung verwendete Benutzeridentitäten dagegen nicht pauschal ausgenommen. Einschränkung: kein Rollout-, Lizenz- oder MFA-Wirksamkeitsnachweis für einen Tenant; Aktualisierungsmetadaten allein belegen keine materielle Änderung.[4]

**[5] Microsoft Learn – Notfallkonten.** Original-URL: <https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access>. Abruf 15.11.2026, **09:06:10 CET**, `partial`, relevante Anforderungen auslesbar; Abschluss am 09:07:16 CET gelesen. Sichtbare letzte Aktualisierung **05.06.2026**. Bestätigt mindestens zwei cloudnative Konten, permanent aktive Global-Administrator-Rolle, phishing-resistente unterschiedliche Anmeldung, Monitoring und Tests mindestens alle 90 Tage. Die aktuelle Anleitung verlangt Ausnahmen von anmeldungsblockierenden/-einschränkenden Conditional-Access-Regeln; Report-only braucht keine Ausnahme. Einschränkung: keine Anleitung zu unkontrollierten MFA-Ausnahmen; praktische Funktion und sichere Arbeitsstation bleiben organisationsbezogen zu testen. Bestehende Ausnahmeformulierung im Artikel an die ausdrückliche Quellenreichweite angepasst, ohne ein neues Datum als Änderungsauslöser zu behaupten.[5]

**[6] Microsoft Learn – Entra-Rollen.** Original-URL: <https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/best-practices>. Abruf 15.11.2026, **09:06:10 CET**, Erfolg, ungekürzt. `ms.date` und `updated_at` **01.06.2026**. Stützt Least Privilege, spezifische Bereiche/Zeit, PIM, Reviews und die Richtwerte weniger als fünf Global Administrators bzw. zehn privilegierte Zuweisungen. Einschränkung: Richtwerte, keine gesetzliche Grenze; Funktionen und PIM erfordern passende Lizenzen, nicht heute geprüft.[6]

**[7] Microsoft Learn – SharePoint/OneDrive-Freigaben.** Original-URL: <https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off>. Abruf 15.11.2026, **09:06:18 CET**, Erfolg, ungekürzt. Letzte Aktualisierung **30.06.2026**. Stützt Organisations-/Site-Restriktionen, OneDrive nicht offener als SharePoint, nicht authentisierte Anyone-Links, Domains, Sicherheitsgruppen und Gastablauf. Einschränkung: Entra-B2B-Modell und Teams-/Gruppeneinstellungen wirken zusätzlich; konkrete Freigaben nicht geprüft.[7]

**[8] Microsoft Learn – Purview Audit.** Original-URL: <https://learn.microsoft.com/en-us/purview/audit-solutions-overview>. Abruf 15.11.2026, **09:06:18 CET**, Erfolg, ungekürzt. Letzte Aktualisierung **18.05.2026**. Stützt standardmässige Aktivierung bei passendem Abonnement, 180 Tage für Standard sowie lizenzabhängige Premium-Funktionen. Die Vergleichsnotiz nennt für nichtmenschliche Datensätze, etwa Dienstprinzipal-Aktionen, System- und Anwendungsereignisse, einen festen Zeitraum von einem Jahr, ohne benutzerdefinierte Aufbewahrungsrichtlinien. Einschränkung: Diese Purview-Angabe ist nicht pauschal auf Entra-Anmeldelogs oder Azure-Diagnostik übertragbar. Ergänzung dient präziser Ereignistyp-Abgrenzung; aus dem älteren Seitendatum wird keine neue Einführung im November behauptet.[8]

**[9] Microsoft Learn – Audit-Aufbewahrungsrichtlinien.** Original-URL: <https://learn.microsoft.com/en-us/purview/audit-log-retention-policies>. Abruf 15.11.2026, **09:06:19 CET**, Erfolg, ungekürzt. Letzte Aktualisierung **19.06.2026**. Bestätigt Premium-Lizenzgrenzen, priorisierte benutzerdefinierte Regeln, 180 Tage für Nicht-E5-/Gastbenutzer und Nicht-Rückwirkung auf bereits festgeschriebene Datensätze. Einschränkung: keine Fristprüfung einzelner Datensätze oder Tenant-Konfiguration.[9]

**[10] BACS – Cloud Computing und Cybersicherheit.** Original-URL: <https://www.bacs.admin.ch/de/cloud-computing-und-cybersicherheit>. Abruf 15.11.2026, **09:06:19 CET**, Erfolg, ungekürzt. HTML ohne sichtbares Änderungsdatum; verlinkte Technologiebetrachtung datiert **02.05.2025**, PDF selbst nicht zusätzlich verwendet. Stützt Exportierbarkeit, Offline-Backup, dokumentierte MFA/Verschlüsselung/Zugriffsprotokollierung und Vorfallprozess. Einschränkung: allgemeine Eignungsorientierung, keine M365-Backup-Produktfreigabe.[10]

**[11] BACS – KI im Berufsalltag.** Original-URL: <https://www.bacs.admin.ch/de/csm26-s3-de>. Abruf 15.11.2026, **09:06:19 CET**, Erfolg, ungekürzt. Veröffentlicht **16.10.2026**. Stützt Prüfung/Anonymisierung sensibler Eingaben, Unternehmenskonten und Trainings-/Opt-out-Prüfung. Einschränkung: keine konkrete KI-Dienst-/Datenflussfreigabe.[11]

**[12] BACS – Malwareverdacht.** Original-URL: <https://www.bacs.admin.ch/de/26w40-de>. Abruf 15.11.2026, **09:06:19 CET**, Erfolg, ungekürzt. Veröffentlicht **06.10.2026**. Stützt Meldung geschäftlich verwendeter Geräte an IT/Arbeitgeber, fachliche Untersuchung sowie Neuaufsetzen und anschliessende Passwortwechsel bei Infektion. Einschränkung: keine Einzelfall-Forensik oder Wiederanlaufentscheidung.[12]

**[13] Microsoft Learn – App-Sicherheitsbetrieb.** Original-URL: <https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications>. Abruf 15.11.2026, **09:06:20 CET**, `partial`; relevante App-/Credential-/Berechtigungsabschnitte auslesbar, restlicher Abschluss am 09:07:15 CET gelesen. Sichtbare letzte Aktualisierung **23.10.2023**. Stützt getrennte Anwendungs-/Dienstprinzipaländerungen, Monitoring von Credentials, Owners, Consent, Rollen, Graph-/M365-/Key-Vault-Bezug und sichere Secret-Aufbewahrung. Einschränkung: produkt-/lizenzabhängige Muster, keine ausgeführten Abfragen oder bestätigten Alarme.[13]

**[14] Microsoft – Storm-0940/ConnectWise.** Original-URL: <https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/>. Abruf 15.11.2026, **09:06:20 CET**, `partial`; relevante Mitigationsabschnitte auslesbar, Abfragen/Abschluss am 09:07:15 und 09:07:41 CET gelesen. Publikation **21.10.2026**, keine neue datierte Revision sichtbar. Stützt berechtigte Anbieter-App-Zugriffe, Erhalt von Konfiguration/Beweisen, keine Erstreaktionslöschung, dringliche Eindämmung nicht wegen Exports verzögern und App-Treffer/Anmeldung nicht mit Abfluss gleichsetzen. **Konkrete Einschränkung:** «Inventory all four application IDs» steht im Text, die untersuchten Abfragelisten enthalten aber drei eindeutige IDs. Die Bildbeschreibung nennt vier Credentials, was keine vier verschiedenen App-IDs belegt. Die alte Artikel-/Vorlagenbehauptung einer abschliessenden Vierer-Liste ist damit nicht sauber gestützt und wurde nicht fortgeschrieben. Die aktuelle ConnectWise-Liste von sieben deaktivierten App-Identitäten [21] ersetzt die pauschale Begrenzung; diese sieben sind kein Nachweis, dass alle sieben missbraucht wurden.[14]

**[15] Microsoft Learn – Widerrufene App-Credentials.** Original-URL: <https://learn.microsoft.com/en-us/entra/workload-id/troubleshoot-revoked-credentials>. Abruf 15.11.2026, **09:06:26 CET**, Erfolg, ungekürzt. Letzte Aktualisierung **22.10.2026**. Bestätigt: Fehlermeldung/gefüllte `tokenRevocations` allein nennt den Aussteller nicht; Application und Service Principal mit gleicher App-ID getrennt prüfen, es können einer oder beide Objekttypen vorhanden sein. `auditDetails.issuedBy` oder korrespondierendes Auditereignis kann den Microsoft-Widerruf belegen; Berechtigungsfehler und fehlende Historie sind kein negativer Nachweis. Bereits ausgegebene Tokens können je Ressource bis 24 Stunden fortgelten; kompromittierte Credentials ersetzen und widerrufen lassen. Einschränkung: Graph-Beispiele nutzen `/beta`; keine Ausführung, kein Credential gelesen/rotiert und kein Widerruf entfernt.[15]

### Neue zitierte Quellen

**[16] Microsoft – KI-gestützte Secret-Suche.** Original-URL: <https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/>. Abruf 15.11.2026, **09:06:35 CET**, `partial`, relevante Gesamtargumentation und Mitigationsabschnitte auslesbar. Veröffentlicht **05.11.2026**, Beobachtungen seit August und App-Folgeaktivität seit mindestens 28.10.; nicht als erstmals diese Woche begonnener Angriff beschrieben. Stützt Secret-Exposition in öffentlichen Repositories, Anbieter-Multitenant-Credentials mit nachgelagerten Kundenzugriffen und getrennte Single-Tenant-Folgeangriffe. Öffentlich exponierte Credentials als kompromittiert behandeln, unverzüglich widerrufen/rotieren, historische Nutzung prüfen; Löschen allein invalidiert nichts, ausgestellte Tokens können fortgelten. Einschränkung: keine Schweizer Organisation oder unser Tenant als betroffen belegt; keine IOC-Sperren, Hunting-/Credential-Massnahmen ausgeführt oder freigegeben.[16]

**[17] Microsoft Learn – Workload Conditional Access.** Original-URL: <https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity>. Abruf 15.11.2026, **09:06:54 CET**, Erfolg, ungekürzt. Letzte Aktualisierung **24.03.2026**. Stützt Workload ID Premium für Erstellung/Änderung, direkte Zuweisung an Dienstprinzipale statt Gruppen. Nur im eigenen Tenant registrierte Single-Tenant-Dienstprinzipale erfasst; Microsoft-/Drittanbieter-SaaS, Multitenant-Apps und Managed Identities nicht erfasst. Workload Identities können keine MFA durchführen. Einschränkung: kein pauschaler Schutz für Lieferanten-Apps und keine Lizenz-/Wirksamkeitsprüfung; bestehende Regeln können laut Quelle ohne passende Lizenz weiter funktionieren, aber nicht geändert werden.[17]

**[18] Microsoft Learn – Anwendungsobjekte/Dienstprinzipale.** Original-URL: <https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals>. Abruf 15.11.2026, **09:06:54 CET**, Erfolg, ungekürzt. `ms.date` **01.10.2024**, `updated_at` **15.06.2026**. Stützt ein Anwendungsobjekt im Heimtenant und lokale Dienstprinzipale pro autorisiertem Tenant, globale App-ID versus lokale Objekt-ID. Einschränkung: allgemeines Objektmodell; Managed-Identity-Dienstprinzipale besitzen kein entsprechendes Anwendungsobjekt, nicht jede Workload ist eine gewöhnliche registrierte App. Keine App im Kundentenant inventarisiert.[18]

**[19] Microsoft Learn – Single-/Multitenant-Apps.** Original-URL: <https://learn.microsoft.com/en-us/entra/identity-platform/single-and-multi-tenant-apps>. Abruf 15.11.2026, **09:06:54 CET**, Erfolg, ungekürzt. `ms.date` **13.03.2025**, `updated_at` **15.06.2026**. Single-Tenant-Apps im Heimtenant, Multitenant-Apps in Heim-/anderen Tenants verwendbar, abhängig von Registrierung/Zielgruppe. Einschränkung: Multitenant bedeutet keinen unbeschränkten Zugriff ohne erteilte Berechtigungen; keine Architektur des Providers geprüft.[19]

**[20] Microsoft – Q3-Mail-Bedrohungsbericht.** Original-URL: <https://www.microsoft.com/en-us/security/blog/2026/11/05/email-threat-landscape-q3-2026-trends-and-insights/>. Abruf 15.11.2026, **09:06:35 CET**, `partial`; relevanter Abschnitt «Spoofed sender domains» auslesbar, Empfehlungen lokal am 09:07:41 CET gelesen. Veröffentlicht **05.11.2026**, Daten Juli–September 2026. Stützt den Einfluss tenant-/benutzerseitiger Overrides auf Zustellungen erkannter schädlicher Nachrichten mit vorgetäuschten Geschäftsservice-Absendern. Einschränkung: 63 Prozent im September beziehen sich auf Nachrichten mit erfasstem Sicherheitsresultat im untersuchten Geschäftsservice-Spoofing-Bestand, nicht auf alle Nachrichten; keine Öffnungen, Kontoübernahmen oder Schweizer KMU-Inzidenz belegt. Diese Zahl wurde bewusst nicht in den Evergreen-Volltext aufgenommen; dort nur belegter Kontrollbedarf.[20]

**[21] ConnectWise Trust Center – Cloud Backup und App-Liste.** Original-URL: <https://www.connectwise.com/company/trust/advisories>. Abruf 15.11.2026, **09:07:41 CET**, `partial` wegen sehr langer Seite. Aktuelle Cloud-Backup-Abschnitte aus der gespeicherten Originalextraktion am 09:08:05–09:08:13 CET gelesen. Cloud-Backup-Update **04.11.2026, 18:55 UTC**; historische App-Liste nennt sieben am **17.10., 07:00 UTC** deaktivierte Identitäten. Bestätigt Backups/Restores für erneut autorisierte M365-Tenants, neue App, erfolgreiche Snapshots gesondert prüfen, Lücke dokumentieren, alte Apps nicht ohne ausdrückliche Anleitung reaktivieren; Billing/Platform-Dashboard/Zusatzbenachrichtigungen noch nicht vollständig. Einschränkung: Wiederautorisierung, Anbieter-Mitigation und Serviceverfügbarkeit belegen weder bereinigten Tenant noch erfolgreiche Kundensicherung. Die Seite enthält ältere Updates und teils pauschalere FAQ-Aussagen; der konkrete datierte Wiederherstellungsabschnitt wurde verwendet. Die aktuell oben stehende ScreenConnect-Meldung vom 13.11. ist ein anderer Produkt-/Vorfallbezug, kein Beleg über Cloud Backup.[21]

### Ergänzende Rechts- und Nachrichtenquellen, nur im Journal

**[22] Fedlex – DSG-Chronologie.** Original-URL: <https://www.fedlex.admin.ch/eli/cc/2022/491/de/history>. Abruf 15.11.2026, **09:06:41 CET**, Erfolg, Chronologietabelle ungekürzt auslesbar; JavaScript-Hinweis am Ende ändert dies nicht. Neueste gelistete Fassung **07.07.2025**, Berichtigung vom 02.07.2025; keine jüngere konsolidierte Fassung in dieser heute gelesenen Chronologie. Einschränkung: Quellenstand, keine umfassende rechtliche Prüfung aller DSG-/DSV- oder sektorspezifischen Fragen.[22]

**[23] Fedlex – vorhandene amtliche DSG-XML.** Original-URL: <https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml>. Diese URL war bereits im Einzelbericht vom 01.11. und in der heute geöffneten Fedlex-Fassungsliste vorhanden; keine URL konstruiert. Abruf 15.11.2026, **09:06:36 CET**, `partial`, Fassung **7. Juli 2025** und Art. 7–9 inhaltlich auslesbar. Stützt bestehende allgemeine Rechtsaussagen. Einschränkung: nur relevante Artikel ausgewertet, keine Rechts-/Fachfreigabe; neue Quellenprüfung nicht als historische Fachprüfung eingetragen.[23]

**[24] BACS – Im Fokus.** Original-URL: <https://www.bacs.admin.ch/de/im-fokus>. Abruf 15.11.2026, **09:06:35 CET**, `partial`, aktuelle Einträge bis **10.11.2026** und seit 01.11. lesbar. Übersicht nennt Black-Friday-/Paket-Phishing, Kühlsteuerungen, ESTV-/EHRA-Phishing, Heimnetzwerke und Cyberresilienz-Veranstaltungen. Einschränkung: Übersichtssichtung, keine Vollprüfung jeder dort verlinkten Meldung; keine weitere daraus abgeleitete M365-Einstellung. Kein globaler Nichtfund behauptet.[24]

**[25] Microsoft Security Blog – Übersicht.** Original-URL: <https://www.microsoft.com/en-us/security/blog/>. Abruf 15.11.2026, **09:06:34 CET**, Erfolg, ungekürzt; aktuelle Einträge bis **13.11.2026**. Diente der Einordnung und Auswahl weiterer einschlägiger Originalmeldungen [28]–[30]. Themen wie Linux/Rust-/Modellforschung liefern aus der Übersicht keinen konkreten M365-Tenant-Parameter. Einschränkung: keine Garantie sämtlicher Meldungen seit 01.11.; nicht allein auf Snippets gestützte neue Aussagen.[25]

**[26] NVD – CVE-2026-109469.** Original-URL: <https://nvd.nist.gov/vuln/detail/CVE-2026-109469>. Abruf 15.11.2026, **09:06:35 CET**, Erfolg, ungekürzt. NVD publiziert/geändert **06.11.2026**, «Exclusively Hosted Service», Microsoft als CNA, noch «Awaiting Enrichment». Diente zum Original-MS​​RC-Verweis [27]. Einschränkung: NVD-Publikation am 06.11. ist nicht MSRC-Erstpublikation und der CVSS-Wert ist Microsoft-CNA, keine eigenständige NVD-Bewertung; kein Kundenpatch daraus abgeleitet.[26]

**[27] MSRC – CVE-2026-109469.** Original-URL: <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-109469>. Abruf 15.11.2026, **09:06:54 CET**, Erfolg, ungekürzt. **Revision 1.0 vom 05.11.2026**. FAQ bestätigt vollständige Mitigation durch Microsoft und ausdrücklich keine Kundenaktion für diesen Cloud-Dienst. Einschränkung: kein Kundenpatch und keine pauschale Sicherheitsfreigabe für Entra-/M365-Tenants. Deshalb kein patchpflichtiger Kontrollpunkt oder wöchentlicher CVE-Einschub im Artikel/Arbeitsmittel.[27]

**[28] Microsoft – November-Produktübersicht.** Original-URL: <https://www.microsoft.com/en-us/security/blog/2026/11/05/whats-new-in-microsoft-security-november-2026/>. Abruf 15.11.2026, **09:06:54 CET**, Erfolg, ungekürzt. Publikation **05.11.2026**. Beschreibt unter anderem Agentenrechte, MXC, Intune Endpoint Privilege Management und Defender-Funktionen; MXC-Integrationen teils zukünftig, SQL-Aussage ausdrücklich Azure Government. Einschränkung: Herstellerübersicht, keine KMU-/Schweiz-/Lizenz-/Tenant-Eignungsfreigabe. Keine neue Produktpflicht in Artikel 06.[28]

**[29] Microsoft – SCKit/ScreenConnect.** Original-URL: <https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/>. Abruf 15.11.2026, **09:06:55 CET**, `partial`, relevante Architektur-/Mitigationsabschnitte auslesbar. Publikation **13.11.2026**, Herstellerberichte seit 11.11. Beschreibt Drittanbieter-Erweiterungen, unzulässige Remote-Clients, Techniker-Sitzungen und getrennte Client-/Server-Angriffsflächen; Einstieg noch unter Untersuchung. Einschränkung: von Cloud-Backup-App-Identitäten getrennt; kein Beleg, jedes ConnectWise-Produkt sei kompromittiert. Keine klientenspezifische Patchanweisung in diese allgemeine Tenant-Prüfliste übernommen; konkrete Fernwartungsprüfung bleibt Provider-Fachfrage. Der aktuelle ConnectWise-Abschnitt bestätigt die eigene ScreenConnect-Reichweite.[29] [21]

**[30] Microsoft – ARTEX/Finanzsektor.** Original-URL: <https://www.microsoft.com/en-us/security/blog/2026/11/06/artex-abuse-expands-as-cybercriminals-target-financial-sector/>. Abruf 15.11.2026, **09:06:55 CET**, Erfolg, ungekürzt. Publikation **06.11.2026**, Storm-3358-Aktivität seit Oktober, vorwiegend Südostasien plus einzelne globale Finanzorganisationen. Stützt schnelle automatisierte Angriffsabläufe und verhaltensbezogene statt nur statische IOC-Betrachtung. Einschränkung: keine Schweizer KMU-Betroffenheit oder neue M365-Standardeinstellung belegt; nicht als zusätzliche Evergreen-Referenz eingefügt.[30]

## Änderungsentscheid und konkrete Einschränkungen

Die Microsoft-Vormerkungen vom 05.11. sind direkt belegt und eingearbeitet.[16] [20] Der neue Secret-Unterabschnitt unterscheidet Anbieter-Multitenant-Credentials, lokale Dienstprinzipale und Single-Tenant-Folgezugriffe ausdrücklich.[17] [18] [19] Er gibt keine eigene Tenant-Freigabe und ordnet mit dieser Quellenpflege keine Deaktivierung, Rotation, Widerrufsentfernung oder IOC-Sperre an.

Der direkte Herstellerabgleich korrigiert einen **materiellen veralteten Wiederherstellungszustand**: Die historische Aussage «bis zu formellen Wiederherstellungsanweisungen deaktiviert halten» durfte nicht suggerieren, es lägen noch keine Anweisungen vor. ConnectWise beschreibt neue App-/Reautorisierungswege und verlangt weiterhin getrennte Untersuchung und Snapshot-Nachweise; alte deaktivierte Apps bleiben ohne ausdrückliche Anweisung deaktiviert.[21] Auch die vorbestehende angeblich abschliessende Vierer-ID-Grenze ist nicht gestützt: Microsofts Prosa, Bild und Abfragelisten sind nicht konsistent. Die sieben vendor-seitig deaktivierten IDs des aktuellen ConnectWise-Inventars werden nur als zu prüfender Herstellerbestand verwendet, nicht als sieben bestätigte Missbrauchsfälle.[14] [21]

Der Source-Status ist deshalb konkret: **kein technisch nicht auslesbarer Quellenblocker bei den 30 dokumentierten Original-URLs**, aber eine offengelegte inhaltliche Quellenabweichung und keine Fachfreigabe. Die mit `partial` bezeichneten Abrufe waren wegen Ausgabelimit gekürzt, nicht leere oder fehlgeschlagene Quellen. Es wurde keine erfolglose URL durch eine erfundene Ersatz-URL oder eine Wiederholungsschleife kaschiert. Für zusätzliche nicht geprüfte Unterlinks wird ausdrücklich kein Erfolg behauptet.

Der Artikelstand und beide Frontmatter-Felder `stand` lauten exakt **15. November 2026**. Beim Arbeitsmittel bestand zuvor kein `stand`; es wurde ergänzt. Die Arbeitsmittelversion wurde wegen der materiellen Ergänzungen von **Stand 1. November 2026** auf **Stand 15. November 2026** erhöht und mit der sichtbaren Version abgeglichen; keine numerische Versionsreihe erfunden. `rechtsstand` und `fachlich_geprüft_am` bzw. `fachlich_geprueft_am` waren in diesen Dateien nicht vorhanden und wurden nicht angelegt. `fachprüfung_status` blieb exakt unverändert.

## Exakte Änderungen am Artikel und Arbeitsmittel

### Artikel – Frontmatter: quellenpruefung_umfang

**Vorher:**

```text
quellenpruefung_umfang: "Alle 15 eindeutigen, nach dieser Pflege in Artikel und zugehörigem Arbeitsmittel zitierten externen Originalquellen; zusätzlich BACS «Im Fokus», Microsoft Security Blog und einschlägige Microsoft-Learn-Referenzen vom 18.10. bis 01.11.2026. Keine Tenant-, App-ID-, Log-, Lizenz-, CMS- oder Live-Linkprüfung."
```

**Nachher:**

```text
quellenpruefung_umfang: "21 eindeutige zitierte externe Originalquellen beider Dateien; insgesamt 30 direkte Original-URLs einschliesslich DSG-History/XML, BACS-/Microsoft-Übersichten und relevanter Primärmeldungen seit 01.11.2026. Tatsächliche Abrufe am 15.11.2026 nach 09:00 CET; Einzelstatus im Quellenjournal. Keine Tenant-, App-ID-, Log-, Lizenz-, CMS-, Browser- oder Live-Linkprüfung."
```

### Artikel – Frontmatter: quellenpruefung_status

**Vorher:**

```text
quellenpruefung_status: "Vollständig für die 15 zitierten externen Originalquellen und die im Umfang genannten Übersichten; keine Fach-, Rechts-, Tenant-, Forensik-, Herstellerfreigabe- oder Publikationsfreigabe."
```

**Nachher:**

```text
quellenpruefung_status: "21 von 21 zitierten Originalquellen in den relevanten Passagen auslesbar; 30 von 30 dokumentierten Original-URLs mit relevantem Inhalt, teilweise gekürzte Extraktionen. Kein nicht auslesbarer Quellenblocker; Microsofts widersprüchliche App-ID-Anzahl im Journal offengelegt und nicht übernommen. Keine Fach-, Rechts-, Tenant-, Forensik-, Produkt-, Hersteller- oder Publikationsfreigabe."
```

### Artikel – Frontmatter: stand

**Vorher:**

```text
stand: "1. November 2026"
```

**Nachher:**

```text
stand: "15. November 2026"
```

### Artikel – Sichtbarer Stand

**Vorher:**

```text
> **Stand:** 1. November 2026.
```

**Nachher:**

```text
> **Stand:** 15. November 2026.
```

### Arbeitsmittel – Frontmatter: quellenpruefung_umfang

**Vorher:**

```text
quellenpruefung_umfang: "Alle 15 eindeutigen, nach dieser Pflege in Arbeitsmittel und zugehörigem Artikel zitierten externen Originalquellen; zusätzlich BACS «Im Fokus», Microsoft Security Blog und einschlägige Microsoft-Learn-Referenzen vom 18.10. bis 01.11.2026. Keine Tenant-, App-ID-, Log-, Lizenz-, CMS- oder Live-Linkprüfung."
```

**Nachher:**

```text
quellenpruefung_umfang: "21 eindeutige zitierte externe Originalquellen beider Dateien; insgesamt 30 direkte Original-URLs einschliesslich DSG-History/XML, BACS-/Microsoft-Übersichten und relevanter Primärmeldungen seit 01.11.2026. Tatsächliche Abrufe am 15.11.2026 nach 09:00 CET; Einzelstatus im Quellenjournal. Keine Tenant-, App-ID-, Log-, Lizenz-, CMS-, Browser- oder Live-Linkprüfung."
```

### Arbeitsmittel – Frontmatter: quellenpruefung_status

**Vorher:**

```text
quellenpruefung_status: "Vollständig für die 15 zitierten externen Originalquellen und die im Umfang genannten Übersichten; keine Fach-, Rechts-, Tenant-, Forensik-, Herstellerfreigabe- oder Publikationsfreigabe."
```

**Nachher:**

```text
quellenpruefung_status: "21 von 21 zitierten Originalquellen in den relevanten Passagen auslesbar; 30 von 30 dokumentierten Original-URLs mit relevantem Inhalt, teilweise gekürzte Extraktionen. Kein nicht auslesbarer Quellenblocker; Microsofts widersprüchliche App-ID-Anzahl im Journal offengelegt und nicht übernommen. Keine Fach-, Rechts-, Tenant-, Forensik-, Produkt-, Hersteller- oder Publikationsfreigabe."
```

### Arbeitsmittel – Frontmatter: version und neu stand

**Vorher:**

```text
version: "Stand 1. November 2026"
```

**Nachher:**

```text
version: "Stand 15. November 2026"
stand: "15. November 2026"
```

### Arbeitsmittel – Sichtbare Version

**Vorher:**

```text
> **Version:** Stand 1. November 2026.
```

**Nachher:**

```text
> **Version:** Stand 15. November 2026.
```

### Artikel – 1. Identitäten zuerst: neuer Absatz zur MFA-Reichweite

**Vorher:**

```text
Bei der Umsetzung genügt es nicht, eine Regel einzuschalten.
```

**Nachher:**

```text
Diese MFA-Durchsetzung erfasst keine Workload Identities wie Dienstprinzipale oder Managed Identities. Solche nichtmenschlichen Identitäten können selbst keine MFA durchführen. Ein Benutzerkonto, das für Automatisierung eingesetzt wird, ist hingegen nicht automatisch ausgenommen. App-Anmeldeinformationen und Berechtigungen benötigen deshalb eigene Kontrollen; Benutzer-MFA schliesst diesen Angriffsweg nicht.[4] [17]

Bei der Umsetzung genügt es nicht, eine Regel einzuschalten.
```

### Artikel – 1. Notfallzugänge: Conditional-Access-Ausnahmen

**Vorher:**

```text
Ein solcher Zugang ist kein Freipass. Dokumentieren Sie, wer die Zugangsmittel in einem gesicherten Verfahren verwenden darf, wie eine Nutzung freigegeben wird und welche Nachprüfung danach erfolgt. Schliessen Sie diese Konten nur von Conditional-Access-Regeln aus, wenn sie sonst im Notfall blockiert wären. Die Ausnahme muss eng dokumentiert sein und die Anmeldung muss einen Alarm auslösen.[5]
```

**Nachher:**

```text
Ein solcher Zugang ist kein Freipass. Dokumentieren Sie, wer die Zugangsmittel in einem gesicherten Verfahren verwenden darf, wie eine Nutzung freigegeben wird und welche Nachprüfung danach erfolgt. Microsoft empfiehlt, Notfallkonten von Conditional-Access-Regeln auszunehmen, die eine Anmeldung blockieren oder einschränken; reine Report-only-Regeln benötigen diese Ausnahme nicht. Die Ausnahme ersetzt weder die phishing-resistente Anmeldung noch Überwachung und Tests. Dokumentieren Sie ihren Geltungsbereich und stellen Sie sicher, dass jede Anmeldung einen Alarm auslöst.[5]
```

### Artikel – 2. Adminrollen: Inventar und Objekttypen

**Vorher:**

```text
Eine **Enterprise App** beziehungsweise ein Dienstprinzipal (Service Principal) kann Berechtigungen erhalten und als Workload Identity ohne interaktive Benutzeranmeldung auf Dienste zugreifen. Führen Sie deshalb neben Konten und Adminrollen ein Inventar dieser Anwendungen: Eigentümer, Geschäftszweck, Hersteller- oder Providerbezug, Berechtigungen, Genehmigung, Lebenszyklus sowie die Application ID. Halten Sie bei wichtigen Integrationen zusätzlich die tenant-spezifische Objekt-ID des Dienstprinzipals fest. Überwachen Sie insbesondere neue Anmeldeinformationen, neue Eigentümer, Zustimmungen, Berechtigungen und Rollenzuweisungen ausserhalb des vorgesehenen Änderungsprozesses.[13]
```

**Nachher:**

```text
Eine **Enterprise App** ist die im Tenant verwaltete lokale Anwendungsidentität, der Dienstprinzipal (Service Principal). Das zugehörige Anwendungsobjekt liegt im Heimtenant der App; eine Multitenant-App kann eigene Dienstprinzipale in mehreren Kundentenants haben. Eine Single-Tenant-App ist dagegen auf ihren Heimtenant beschränkt. Application ID, Objekt-ID des Anwendungsobjekts und tenant-spezifische Dienstprinzipal-Objekt-ID sind nicht austauschbar.[18] [19] Führen Sie neben Konten und Adminrollen ein Inventar dieser Anwendungen: Eigentümer, Geschäftszweck, Hersteller- oder Providerbezug, Heimtenant, Single-Tenant- oder Multitenant-Typ, Berechtigungen, Genehmigung, Lebenszyklus sowie die Application ID und lokale Dienstprinzipal-Objekt-ID. Überwachen Sie insbesondere neue Anmeldeinformationen, neue Eigentümer, Zustimmungen, Berechtigungen und Rollenzuweisungen ausserhalb des vorgesehenen Änderungsprozesses.[13]
```

### Artikel – 2. Neuer Unterabschnitt: Exponierte App-Secrets und Reichweite von Zugriffskontrollen

**Vorher:**

```text
### Herstellerintegrationen und widerrufene Anmeldeinformationen ohne vorschnelles Löschen
```

**Nachher:**

```text
### Exponierte App-Secrets und Reichweite von Zugriffskontrollen

Microsoft berichtete am 5. November 2026 über KI-gestützte Suchen nach **Secrets**, also geheimen Zugangsmitteln wie Client-Secrets oder API-Schlüsseln, in öffentlichen GitHub-Repositories. Der Bericht beschreibt sowohl kompromittierte Anbieter-Credentials einer Multitenant-App mit Zugriff auf bereits angebundene Kundentenants als auch Folgezugriffe über Single-Tenant-Apps innerhalb einer Zielorganisation. Die tatsächliche Reichweite hängt von Autorisierungen und Ressourcenrechten ab; ein lokaler Dienstprinzipal macht eine Anbieter-App nicht zur Single-Tenant-App. Die Meldung belegt keine Betroffenheit Ihres Unternehmens.[16] [18] [19]

Legen Sie mit Entwicklung und Provider fest, wo Anmeldeinformationen gespeichert werden, wer ihren Lebenszyklus verantwortet und wie Secret-Exposition erkannt und eskaliert wird. Microsoft verlangt, öffentlich exponierte Zugangsmittel als kompromittiert zu behandeln, sie unverzüglich zu widerrufen oder zu rotieren und ihre historische Nutzung zu untersuchen. Das Löschen einer Datei oder eines Repository-Eintrags invalidiert weder das Secret noch Kopien in Versionshistorien oder Caches. Bereits ausgestellte Tokens können bis zum Ablauf weiter gelten; der Widerruf allein ist kein Nachweis, dass jeder Zugriff beendet ist.[16] [15] Diese Herstellerempfehlung ist keine mit dieser Quellenpflege ausgeführte Credential- oder Vorfallmassnahme; die konkrete Umsetzung gehört zu den berechtigten Fachstellen und in den Notfallprozess.

Verwechseln Sie eine Benutzer-Zugriffsregel nicht mit **Conditional Access für Workload Identities**. Microsoft verlangt für die Erstellung oder Änderung solcher Regeln Workload ID Premium. Die Regel muss dem Dienstprinzipal direkt zugewiesen sein; eine Zuweisung über eine Gruppe greift für ihn nicht. Erfasst werden im eigenen Tenant registrierte Single-Tenant-Dienstprinzipale, nicht Microsoft- oder Drittanbieter-SaaS, Multitenant-Apps oder Managed Identities. Eine solche Regel ist daher kein pauschaler Schutz für Lieferantenintegrationen. Dokumentieren Sie je App die anwendbare Kontrolle und deren Lücke, bevor Sie eine Abdeckung als erfüllt bewerten.[17]

### Herstellerintegrationen und widerrufene Anmeldeinformationen ohne vorschnelles Löschen
```

### Artikel – 2. Herstellerintegrationen: aktuelle App-Liste statt Vierer-Begrenzung

**Vorher:**

```text
Microsoft berichtete am 21. Oktober 2026, dass Storm-0940 kompromittierte Identitäten mehrerer ConnectWise-Cloudanwendungen für Zugriffe über bereits berechtigte Anwendungen nutzte. Die spezifische Herstelleranweisung, die betroffenen Anbindungen bis zu formellen Wiederherstellungsanweisungen von ConnectWise deaktiviert zu halten, gilt nur für die vier im Bericht genannten Application IDs – nicht pauschal für jedes ConnectWise-Produkt oder jede Enterprise App. Wenn eine dieser Application IDs aktuell oder früher autorisiert war, soll die zuständige, hierzu berechtigte Incident-Response-Fachstelle die aktuelle und frühere Autorisierung nach Application ID statt nach Anzeigename abklären und die lokale Dienstprinzipal-Objekt-ID festhalten. Das Vorhandensein einer solchen Anwendung oder eine erfolgreiche Anmeldung belegt für sich weder einen Missbrauch noch Datenzugriff oder Datenabfluss.[14]
```

**Nachher:**

```text
Microsoft berichtete am 21. Oktober 2026, dass Storm-0940 kompromittierte Identitäten mehrerer ConnectWise-Cloudanwendungen für Zugriffe über bereits berechtigte Anwendungen nutzte.[14] Für das Inventar betroffener Anbindungen ist die aktuelle ConnectWise-Liste nach Application ID massgeblich: Sie nennt sieben am 17. Oktober deaktivierte App-Identitäten und weist darauf hin, dass eine herstellerseitige Aktion keine lokal gespeicherte Änderung in jedem Kundentenant belegt. Die Anweisungen gelten nicht pauschal für jedes ConnectWise-Produkt oder jede Enterprise App. War eine gelistete Application ID aktuell oder früher autorisiert, soll die berechtigte Incident-Response-Fachstelle dies nach Application ID statt Anzeigename abklären und die lokale Dienstprinzipal-Objekt-ID festhalten.[21] Das Vorhandensein einer solchen Anwendung oder eine erfolgreiche Anmeldung belegt für sich weder einen Missbrauch noch Datenzugriff oder Datenabfluss.[14]
```

### Artikel – 2. Herstellerintegrationen: neuer Wiederherstellungsstand

**Vorher:**

```text
Ein Fehler für eine widerrufene Client-Anmeldeinformation
```

**Nachher:**

```text
ConnectWise hat seit dem 28. Oktober eine schrittweise Wiederherstellung über die neue App «ConnectWise Cloud Backup for M365» beschrieben. Das Update vom 4. November bestätigt Backup- und Restore-Funktionen für erneut autorisierte M365-Tenants, aber noch nicht sämtliche Zusatzfunktionen. Bereits deaktivierte alte Apps sollen ohne ausdrückliche Herstelleranweisung nicht wieder aktiviert werden. Erneute Autorisierung ersetzt weder die Untersuchung des Tenants noch den Nachweis neuer erfolgreicher Backup-Snapshots. Erfassen Sie die Sicherungslücke zwischen letztem erfolgreichem Snapshot vor der Unterbrechung und erstem erfolgreichen Snapshot danach; Serviceverfügbarkeit ist keine Wiederherstellungs- oder Sicherheitsfreigabe für Ihren Tenant.[21]

Ein Fehler für eine widerrufene Client-Anmeldeinformation
```

### Artikel – 2. Widerruf: Objekttypen und Herkunftsnachweis

**Vorher:**

```text
Prüfen Sie bei einer fachlich begründeten Untersuchung die Widerrufseinträge am Application- **und** Service-Principal-Objekt mit derselben Application ID sowie das zugehörige Entra-Auditereignis.
```

**Nachher:**

```text
Prüfen Sie bei einer fachlich begründeten Untersuchung die Widerrufseinträge am Application- **und** Service-Principal-Objekt mit derselben Application ID; der Tenant kann nur einen dieser Objekttypen oder beide enthalten. Eine Berechtigungsfehlermeldung ist kein Nachweis fehlender Widerrufe. Microsoft nennt als Herkunftsnachweis entweder den passenden Aussteller in `auditDetails.issuedBy` oder das korrespondierende Entra-Auditereignis; fehlende Audit-Historie allein klärt die Herkunft nicht.
```

### Artikel – 4. Logging: neuer Absatz zu nichtmenschlichen Ereignissen und getrennten Logquellen

**Vorher:**

```text
Verlassen Sie sich deshalb nicht auf eine angenommene Aufbewahrungsfrist.
```

**Nachher:**

```text
Die Auditübersicht unterscheidet davon Datensätze nichtmenschlicher Entitäten, etwa Dienstprinzipal-Aktionen und Anwendungsaktivitäten: Sie nennt dafür einen festen Zeitraum von einem Jahr, auf den benutzerdefinierte Aufbewahrungsrichtlinien nicht anwendbar sind.[8] Erfassen Sie den Ereignistyp deshalb separat. Eine Purview-Aufbewahrungsangabe darf nicht pauschal als Frist für alle Entra-Anmeldeprotokolle oder Azure-Ressourcenlogs übernommen werden; verfügbare Quellen und tatsächliche Abdeckung sind getrennt nachzuweisen.[13] [21]

Verlassen Sie sich deshalb nicht auf eine angenommene Aufbewahrungsfrist.
```

### Artikel – 6. Provider-Governance: neuer Absatz zu Mail-Sicherheitsausnahmen

**Vorher:**

```text
**[FACHPRÜFUNG ERFORDERLICH]** Die datenschutzrechtliche Tragfähigkeit
```

**Nachher:**

```text
Prüfen Sie Sicherheitsausnahmen auch im E-Mail-Schutz. Microsofts Q3-Bericht vom 5. November zeigt, dass tenant- oder benutzerseitige Overrides als schädlich erkannte Nachrichten mit vorgetäuschten Geschäftsservice-Absendern dennoch zur Zustellung bringen können. Das ist weder ein Nachweis geöffneter Nachrichten noch kompromittierter Konten in Ihrem KMU.[20] Führen Sie deshalb ein Register breiter Absenderfreigaben und anderer Schutz-Overrides mit Zweck, genehmigender Stelle, Reichweite, Ablauf oder Review-Termin und tatsächlich beobachteter Wirkung. Lassen Sie Ausnahmen mit dem Provider kontrolliert prüfen; eine pauschale Entfernung ohne Abklärung der betroffenen Geschäftsabläufe ist keine Empfehlung dieses Artikels.

**[FACHPRÜFUNG ERFORDERLICH]** Die datenschutzrechtliche Tragfähigkeit
```

### Artikel – Typische Fehler: neuer Secret-Fehler

**Vorher:**

```text
**«Der Provider ist Global Administrator, das ist einfacher.»**
```

**Nachher:**

```text
**«Das Secret wurde aus dem Repository gelöscht, also ist der Zugang geschlossen.»** Löschen invalidiert kein Zugangsmittel. Zuständige Fachstellen müssen exponierte Credentials und deren historische Nutzung nach Herstelleranweisung behandeln; bereits ausgestellte Tokens und weitere eingerichtete Zugriffe sind gesondert zu beurteilen.[16] [15]

**«Der Provider ist Global Administrator, das ist einfacher.»**
```

### Artikel – 30-Tage-Plan, Tage 1–7: Inventar

**Vorher:**

```text
Enterprise Apps und Dienstprinzipale mit Application ID, Adminrollen, externe Freigabestufen
```

**Nachher:**

```text
Enterprise Apps und Dienstprinzipale mit Application ID, lokaler Objekt-ID, Heimtenant und Single-Tenant-/Multitenant-Typ, Adminrollen, externe Freigabestufen
```

### Artikel – 30-Tage-Plan, Tage 1–7: Secret- und Ausnahmeregister

**Vorher:**

```text
Kennzeichnen Sie kritische Geschäftsprozesse und Datenbereiche.
```

**Nachher:**

```text
Erfassen Sie Secret-Verantwortung und Sicherheitsausnahmen, aber keine Secret-Werte in der Prüfliste.[16] [17] [18] [19] Kennzeichnen Sie kritische Geschäftsprozesse und Datenbereiche.
```

### Artikel – 30-Tage-Plan, Tage 15–21: Logabdeckung und Mail-Ausnahmen

**Vorher:**

```text
Bestimmen Sie, welche Ereignisse an wen eskaliert werden.[7] [8] [13]
```

**Nachher:**

```text
Dokumentieren Sie die getrennte Logabdeckung für Benutzer und Anwendungen und lassen Sie E-Mail-Sicherheitsausnahmen kontrolliert überprüfen. Bestimmen Sie, welche Ereignisse an wen eskaliert werden.[7] [8] [13] [20]
```

### Artikel – 30-Tage-Plan, Tage 22–30: Snapshots und Sicherungslücke

**Vorher:**

```text
Überführen Sie verbleibende Lücken mit Eigentümer und Termin in Ihr Risikoregister.
```

**Nachher:**

```text
Wenn eine unterbrochene Backup-Integration erneut autorisiert wurde, verlangen Sie getrennt den Nachweis neuer erfolgreicher Snapshots und eine Dokumentation der Sicherungslücke; die Autorisierung allein genügt nicht.[21] Überführen Sie verbleibende Lücken mit Eigentümer und Termin in Ihr Risikoregister.
```

### Artikel – Quellen: neue tatsächlich zitierte Referenzen [16]–[21]

**Vorher:**

```text
Keine Referenzen [16]–[21].
```

**Nachher:**

```text
[16]: https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/ "Microsoft Security Blog – Threat actors use agentic AI tooling to find and abuse exposed secrets, 5. November 2026"
[17]: https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity "Microsoft Learn – Conditional Access for workload identities"
[18]: https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals "Microsoft Learn – Apps and service principals in Microsoft Entra ID"
[19]: https://learn.microsoft.com/en-us/entra/identity-platform/single-and-multi-tenant-apps "Microsoft Learn – Single and multitenant apps in Microsoft Entra ID"
[20]: https://www.microsoft.com/en-us/security/blog/2026/11/05/email-threat-landscape-q3-2026-trends-and-insights/ "Microsoft Security Blog – Email threat landscape: Q3 2026 trends and insights, 5. November 2026"
[21]: https://www.connectwise.com/company/trust/advisories "ConnectWise Trust Center – Cloud Backup: Wiederherstellungsupdate vom 4. November 2026 und App-Identitäten"

```

### Arbeitsmittel – B. Administratorrechte: B6

**Vorher:**

```text
| B6 | Kritisch | Enterprise Apps, Dienstprinzipale und andere Workload Identities sind mit Eigentümer, Zweck, Hersteller- oder Providerbezug, Application ID, Berechtigungen, Genehmigung und Lebenszyklus inventarisiert. |  |  |  |  |
```

**Nachher:**

```text
| B6 | Kritisch | Enterprise Apps, Dienstprinzipale und andere Workload Identities sind mit Eigentümer, Zweck, Hersteller- oder Providerbezug, Heimtenant, Single-Tenant-/Multitenant-Typ, Application ID, lokaler Dienstprinzipal-Objekt-ID, Berechtigungen, Genehmigung und Lebenszyklus inventarisiert. |  |  |  |  |
```

### Arbeitsmittel – B. Administratorrechte: neue B9–B10

**Vorher:**

```text
| B8 | Optimierend | Der Tenant nutzt Gruppen, klar abgegrenzte Bereiche oder andere Mechanismen, um Verwaltungsrechte strukturiert zu delegieren. |  |  |  |  |
```

**Nachher:**

```text
| B8 | Optimierend | Der Tenant nutzt Gruppen, klar abgegrenzte Bereiche oder andere Mechanismen, um Verwaltungsrechte strukturiert zu delegieren. |  |  |  |  |
| B9 | Kritisch | Speicherung, Lebenszyklus, Eigentümer und Erkennung exponierter App-Secrets sind geregelt; öffentlich exponierte Credentials werden nach Herstelleranweisung durch berechtigte Fachstellen behandelt und ihre historische Nutzung untersucht. Keine Secret-Werte werden in dieser Vorlage erfasst. |  |  |  |  |
| B10 | Wichtig | Je Workload Identity sind anwendbare Zugriffskontrollen, Lizenzvoraussetzungen und nicht abgedeckte Integrationen dokumentiert. Workload-Conditional-Access-Abdeckung wird nicht aus Benutzer-MFA oder einer Gruppenzuweisung abgeleitet. |  |  |  |  |
```

### Arbeitsmittel – B. Prüfnotiz B6–B7: Objekttypen und aktuelle App-Liste

**Vorher:**

```text
**Prüfnotiz zu B6–B7:** Anwendungen und Dienstprinzipale können weitreichende Berechtigungen erhalten. Microsoft empfiehlt, neue Anmeldeinformationen, neue Eigentümer, Zustimmungen, Berechtigungen und privilegierte Rollenzuweisungen ausserhalb des vorgesehenen Änderungsprozesses zu überwachen.[12] Der Herstellerbericht zu Storm-0940 vom 21. Oktober 2026 verlangt bei den **vier dort konkret genannten ConnectWise-Application-IDs**, nicht bloss beim Anzeigenamen, ein Inventar in aktuell und früher autorisierten Tenants. Die eingeschränkte Anweisung, diese betroffenen Anbindungen bis zu formellen Wiederherstellungsanweisungen von ConnectWise deaktiviert zu halten, gilt nicht pauschal für andere ConnectWise-Produkte oder Anwendungen. Enterprise Apps sollen nicht als erste Reaktion gelöscht werden: Verfügbare Konfiguration und Beweise sind vor irreversiblen Änderungen zu sichern; dringliche Eindämmung darf nicht auf Exporte warten.[13]
```

**Nachher:**

```text
**Prüfnotiz zu B6–B7:** Anwendungen und Dienstprinzipale können weitreichende Berechtigungen erhalten. Microsoft empfiehlt, neue Anmeldeinformationen, neue Eigentümer, Zustimmungen, Berechtigungen und privilegierte Rollenzuweisungen ausserhalb des vorgesehenen Änderungsprozesses zu überwachen.[12] Das Anwendungsobjekt liegt im Heimtenant, der Dienstprinzipal ist die lokale Repräsentation; bei Multitenant-Apps existieren lokale Dienstprinzipale in mehreren autorisierten Tenants.[17] [18] Beim Storm-0940-/Cloud-Backup-Bezug ist die aktuelle ConnectWise-Liste nach Application ID massgeblich: Sie nennt sieben am 17. Oktober deaktivierte App-Identitäten, nicht einen pauschalen Produktnamen. Herstellerseitige Deaktivierung belegt keine separate lokale Änderung in jedem Kundentenant.[20] Prüfen Sie aktuelle und frühere Autorisierungen nach Application ID. Ein App-Treffer oder eine erfolgreiche Anmeldung ist kein Nachweis für Missbrauch, Datenzugriff oder Abfluss. Enterprise Apps sollen nicht als erste Reaktion gelöscht werden: Verfügbare Konfiguration und Beweise sind vor irreversiblen Änderungen zu sichern; dringliche Eindämmung darf nicht auf Exporte warten.[13]
```

### Arbeitsmittel – B. Widerrufsnotiz: vorhandene Objekte und Herkunft

**Vorher:**

```text
Prüfen Sie bei einer fachlich begründeten Untersuchung die `tokenRevocations` am Application- und Service-Principal-Objekt mit derselben Application ID sowie das passende Entra-Auditereignis.
```

**Nachher:**

```text
Prüfen Sie bei einer fachlich begründeten Untersuchung die `tokenRevocations` am Application- und Service-Principal-Objekt mit derselben Application ID; es kann nur einer dieser Objekttypen oder beide im Tenant vorhanden sein. Berechtigungsfehler belegen keine fehlenden Widerrufe. Microsoft nennt entweder den passenden Aussteller in `auditDetails.issuedBy` oder das korrespondierende Entra-Auditereignis als Herkunftsnachweis; fehlende Audit-Historie klärt die Herkunft allein nicht.
```

### Arbeitsmittel – B. Neue Prüfnotiz B9–B10

**Vorher:**

```text
### C. Externe Zusammenarbeit und Freigaben
```

**Nachher:**

```text
**Prüfnotiz zu B9–B10:** Microsofts Bericht vom 5. November 2026 beschreibt KI-gestützte Secret-Suche und sowohl Anbieter-Credentials einer Multitenant-App mit nachgelagerten Kundenzugriffen als auch Folgezugriffe über Single-Tenant-Apps. Löschen des Repository-Inhalts invalidiert kein Secret. Öffentlich exponierte Credentials sind laut Hersteller als kompromittiert zu behandeln, unverzüglich zu widerrufen oder zu rotieren und auf historische Nutzung zu untersuchen; bereits ausgestellte Tokens können weiter gelten.[15] Das ist keine mit dieser Vorlage ausgeführte Vorfallmassnahme. Conditional Access für Workload Identities verlangt für Erstellung oder Änderung Workload ID Premium und eine direkte Dienstprinzipal-Zuweisung. Erfasst werden im eigenen Tenant registrierte Single-Tenant-Dienstprinzipale; Multitenant-/Drittanbieter-SaaS und Managed Identities sind nicht erfasst. Eine Gruppenzuweisung gilt nicht für enthaltene Dienstprinzipale. Benutzer-MFA deckt diese nichtmenschlichen Identitäten nicht ab.[16]

### C. Externe Zusammenarbeit und Freigaben
```

### Arbeitsmittel – D. Prüfnotiz D2: nichtmenschliche Datensätze und getrennte Logfristen

**Vorher:**

```text
Prüfen Sie die tatsächliche Verfügbarkeit und Aufbewahrung in Ihrem Tenant.[6] [7]
```

**Nachher:**

```text
Die Auditübersicht nennt für Datensätze nichtmenschlicher Entitäten wie Dienstprinzipal-Aktionen und Anwendungsaktivitäten einen festen Zeitraum von einem Jahr; benutzerdefinierte Aufbewahrungsrichtlinien gelten dafür nicht.[6] Prüfen Sie Ereignistyp, tatsächliche Verfügbarkeit und Aufbewahrung in Ihrem Tenant getrennt; Purview-Fristen sind keine pauschalen Fristen für Entra-Anmeldelogs oder Azure-Ressourcenlogs.[7] [12]
```

### Arbeitsmittel – E. Neuer Kontrollpunkt E7

**Vorher:**

```text
| E6 | Optimierend | Die Wiederanlaufreihenfolge ist mit Geschäftsleitung, Fachbereichen und dem Notfallplan abgestimmt. |  |  |  |  |
```

**Nachher:**

```text
| E6 | Optimierend | Die Wiederanlaufreihenfolge ist mit Geschäftsleitung, Fachbereichen und dem Notfallplan abgestimmt. |  |  |  |  |
| E7 | Wichtig | Nach unterbrochenen oder erneut autorisierten Backup-Integrationen sind erfolgreiche neue Snapshots, die Sicherungslücke und weiterhin fehlende Funktionen getrennt nachgewiesen; Wiederautorisierung gilt nicht als Sicherheits- oder Restore-Freigabe. |  |  |  |  |
```

### Arbeitsmittel – E. Neue Prüfnotiz E7 zur Wiederherstellung

**Vorher:**

```text
**Prüfnotiz zum Vorfallbezug:**
```

**Nachher:**

```text
**Prüfnotiz zu E7:** ConnectWise beschreibt seit dem 28. Oktober 2026 die Wiederherstellung über die neue App «ConnectWise Cloud Backup for M365». Das Update vom 4. November bestätigt Backups und Restores für erneut autorisierte Tenants, aber noch nicht sämtliche Zusatzfunktionen. Alte deaktivierte Apps sollen ohne ausdrückliche Anweisung nicht wieder aktiviert werden. Erneute Autorisierung ersetzt weder Tenant-Untersuchung noch neue erfolgreiche Snapshots. Erfassen Sie die Lücke zwischen letztem erfolgreichem Snapshot vor der Unterbrechung und erstem danach.[20] Diese Vorlage ordnet keine Wiederautorisierung an.

**Prüfnotiz zum Vorfallbezug:**
```

### Arbeitsmittel – F. Neuer Kontrollpunkt F7

**Vorher:**

```text
| F6 | Optimierend | Die vereinbarten Leistungen und Nachweise werden periodisch kontrolliert und Abweichungen nachverfolgt. |  |  |  |  |
```

**Nachher:**

```text
| F6 | Optimierend | Die vereinbarten Leistungen und Nachweise werden periodisch kontrolliert und Abweichungen nachverfolgt. |  |  |  |  |
| F7 | Wichtig | Breite Absenderfreigaben und E-Mail-Schutz-Overrides sind mit Zweck, Genehmigung, Reichweite, Ablauf oder Review-Termin und beobachteter Wirkung dokumentiert; Änderungen erfolgen kontrolliert nach Prüfung der Geschäftsabläufe. |  |  |  |  |
```

### Arbeitsmittel – F. Neue Prüfnotiz F7 zu Sicherheitsausnahmen

**Vorher:**

```text
## Priorisierte Massnahmenliste
```

**Nachher:**

```text
**Prüfnotiz zu F7:** Microsofts Q3-Bericht vom 5. November 2026 beschreibt Zustellungen erkannter schädlicher Nachrichten mit vorgetäuschten Geschäftsservice-Absendern durch tenant- oder benutzerseitige Ausnahmen. Das belegt keine geöffneten Nachrichten oder kompromittierten Konten in Ihrem Unternehmen.[19] Die Vorlage verlangt ein überprüfbares Ausnahmeregister, keine unkontrollierte Entfernung sämtlicher Freigaben.

## Priorisierte Massnahmenliste
```

### Arbeitsmittel – Quellen: neue tatsächlich zitierte Referenzen [15]–[20]

**Vorher:**

```text
Keine Referenzen [15]–[20].
```

**Nachher:**

```text
[15]: https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/ "Microsoft Security Blog – Threat actors use agentic AI tooling to find and abuse exposed secrets, 5. November 2026"
[16]: https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity "Microsoft Learn – Conditional Access for workload identities"
[17]: https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals "Microsoft Learn – Apps and service principals in Microsoft Entra ID"
[18]: https://learn.microsoft.com/en-us/entra/identity-platform/single-and-multi-tenant-apps "Microsoft Learn – Single and multitenant apps in Microsoft Entra ID"
[19]: https://www.microsoft.com/en-us/security/blog/2026/11/05/email-threat-landscape-q3-2026-trends-and-insights/ "Microsoft Security Blog – Email threat landscape: Q3 2026 trends and insights, 5. November 2026"
[20]: https://www.connectwise.com/company/trust/advisories "ConnectWise Trust Center – Cloud Backup: Wiederherstellungsupdate vom 4. November 2026 und App-Identitäten"

```


## Unveränderte Abschnitte und erhaltene Paketziele

Im Artikel bleiben H1, Kurzantwort, Einführung und der allgemeine Disclaimer, «Cloud und Provider ändern die Verantwortung nicht» einschliesslich hypothetischem Praxisbeispiel, die allgemeinen Konto-/MFA-/Pilotabsätze, der erste Notfallkontenabsatz, Rollen-/PIM-Richtwerte und Rollenfragen, die Beweissicherungsabgrenzung, Abschnitt 3 «Externe Freigaben gezielt statt pauschal öffnen», Abschnitt 5 «Backup-Verantwortung: Wiederherstellung konkret definieren», die bisherigen Provider-/Datenschutzabsätze und internen Ziele, sämtliche vorbestehenden typischen Fehler, Tage 8–14, nächster Schritt und Fazit erhalten. Ergänzungen erfolgen nur in den oben exakt bezeichneten Abschnitten; keine Kürzung oder Ersetzung des Volltexts.

Im Arbeitsmittel bleiben Zweck, Anwendung, Stammdaten, A1–A7 samt Prüfnotiz A6, B1–B5, B7–B8 und Prüfnotiz B2, sämtliche C-Punkte/Notizen, D1–D6, E1–E6 samt bestehenden Backup-/Vorfallnotizen, F1–F6 samt Rechtsnotiz F5, die priorisierte Massnahmenliste, Grenzen und Fachprüfung erhalten. Neue B9–B10, E7 und F7 sowie zugehörige Notizen wurden ergänzt; bestehende Kontrollpunktnummern nicht umnummeriert.

**Unveränderliche Felder:** Slugs, Meta-Titel, Meta-Beschreibungen, Veröffentlichungsdatum 05.11.2026, Autor, Titel-/Bezugfelder, Entwurfs-/Vorlagenstatus und Fachstatus sind erhalten. Alle **fünf Original-FACHPRÜFUNG-Marker je Datei** sind wortgleich erhalten. Keine neue Fachprüfung datiert. Die lokalen Kontrollen vor dem Schreiben bestätigten **defined = cited** und mehr als 1'400 Wörter in beiden Volltexten; nach dieser Pflege 3'591 Artikelwörter und 2'730 Vorlagenwörter vor dem Quellenabschnitt, nach einfachem Leerraum-Zähler inklusive Metadaten/Tabellen. Es wurde kein globales QA-Skript geändert oder ausgeführt und kein globales Validatorergebnis behauptet.

Die vorhandenen internen Artikel-/Ressourcenlinks bleiben unverändert: `/wissen/microsoft-365-mfa-passkeys`, `/wissen/ransomware-resistente-backups`, `/wissen/backup-wiederherstellung-testen`, `/resources/06-m365-tenant-pruefliste` und der Vorlagenbezug `/wissen/microsoft-365-sicherheit-kmu` sind lokal in den Paketdateien als Slugs vorhanden. Auch die originalen Paket-Service-/Kontaktziele `/unsere-dienstleistungen/notfallplanung`, `/unsere-dienstleistungen/risikomanagement`, `/unsere-dienstleistungen/sicherheitsanalyse` und `/kontakt` bleiben erhalten. Keine neuen internen Ziele angelegt; **kein aktueller öffentlicher Linktest**. Der historische Laufstatus vom 08.11. meldete 403 im Linkchecker, nicht einen neuen 404-Nachweis; dieser historische Wert wird nicht als heutiger Status wiederholt.

## Offene konkrete Fachfragen und Veröffentlichungsblocker

**Tenant-/App-Identitäten:** Welche Application IDs, Heimtenants, lokalen Dienstprinzipale, aktuellen/früheren Consent-Grants und Ressourcenrechte sind tatsächlich vorhanden? Wer verantwortet jede Integration und deren Credentials? Welche nichtmenschlichen Identitäten sind durch welche technische Kontrolle tatsächlich abgedeckt, und ist Workload ID Premium vorhanden? Keine dieser Fragen wurde durch Quellenabruf beantwortet.[13] [17] [18] [19]

**Secret-/Incident-Bezug:** Liegen tatsächlich exponierte Secrets oder Verdachtsindikatoren vor? Wie weit reicht verfügbare Historie, und welche App-, Entra-, Azure-, M365- und Ressourcendaten sind zu sichern? Welche berechtigte Fachstelle trifft zeitkritische Eindämmungs-, Credential-/Token-, Beweissicherungs- und Wiederherstellungsentscheide? Fehlende Historie, Fehlercodes und erfolgreiche Anmeldung sind für sich keine abschliessende Betroffenheits-/Abflussprüfung.[14] [15] [16]

**Provider-Wiederherstellung:** Falls ConnectWise Cloud Backup eingesetzt wird: Galt eine gelistete App-Autorisierung, wurde über den ausdrücklich vorgesehenen neuen Weg reautorisiert, und sind tatsächliche neue Snapshots, Sicherungslücke, Restore-Abdeckung und fehlende Zusatzfunktionen dokumentiert? Die jetzige Erreichbarkeit der Herstelleranleitung ist kein erfolgreicher Kunden-Restore.[21] Eine allenfalls eingesetzte ScreenConnect-Fernwartung ist separat auf Produkt, Erweiterungen, Technikerclients und mögliche Vorfälle durch zuständige Fachstellen zu prüfen, ohne Cloud-Backup-App-IDs damit gleichzusetzen.[29]

**Sicherheitsausnahmen und Logging:** Welche Mail-Overrides/Absenderfreigaben gelten tatsächlich, wem gehören sie, sind Zweck und Review-Termin dokumentiert, und welche Wirkung ist nachgewiesen? Welche Benutzer-/nichtmenschlichen Ereignistypen, Lizenzen, Suchrechte, Aufbewahrung und Eskalationswege sind wirksam? Keine Mail zugestellt/geöffnet, kein Override entfernt und kein Audit-/Anmeldelog getestet.[8] [9] [20]

**Recht/Datenschutz:** Konkrete Verantwortlichen-/Auftragsbearbeiterrollen, Verträge, Unterauftragsgenehmigungen, Personendaten, Bearbeitungsorte, Auslandbekanntgaben und KI-Datenflüsse bleiben fachlich offen. Art. 7–9 wurden nur als allgemeine Quellenstützung gelesen; weder materielle Rechtsänderung noch Einzelfallkonformität wird daraus behauptet.[2] [3] [22] [23]

**Publikation:** Beide Dateien bleiben lokal nicht freigegeben. Kein CMS geöffnet, kein Browser verwendet, kein Login versucht, kein geschützter Import, keine Veröffentlichung und keine Konfiguration geändert. Eine aktuelle Authentifizierung oder fehlende Authentifizierung wurde heute nicht getestet; der Nutzer hat solche Operationen ausgeschlossen. Vor einer gesondert autorisierten Veröffentlichung bleiben Fachfreigabe, tatsächliche öffentliche Ziele, aktueller Quellenstand und berechtigte Publikationsentscheidung offen. Keine Produkt-/Tenant-Sicherheitsgarantie.

## Quellen

[1]: https://www.bacs.admin.ch/de/empfehlungen-fuer-die-zusammenarbeit-mit-it-providern "BACS – Zusammenarbeit mit IT-Dienstleistern"
[2]: https://www.edoeb.admin.ch/de/datenbearbeitungen-in-der-cloud "EDÖB – Cloud-Computing"
[3]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – DSG Art. 7–9"
[4]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication "Microsoft Learn – Mandatory MFA"
[5]: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access "Microsoft Learn – Notfallkonten"
[6]: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/best-practices "Microsoft Learn – Entra-Rollen"
[7]: https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off "Microsoft Learn – SharePoint und OneDrive Sharing"
[8]: https://learn.microsoft.com/en-us/purview/audit-solutions-overview "Microsoft Learn – Purview Audit"
[9]: https://learn.microsoft.com/en-us/purview/audit-log-retention-policies "Microsoft Learn – Audit-Aufbewahrungsrichtlinien"
[10]: https://www.bacs.admin.ch/de/cloud-computing-und-cybersicherheit "BACS – Cloud Computing und Cybersicherheit"
[11]: https://www.bacs.admin.ch/de/csm26-s3-de "BACS – KI im Berufsalltag, 16. Oktober 2026"
[12]: https://www.bacs.admin.ch/de/26w40-de "BACS – Malwareverdacht, 6. Oktober 2026"
[13]: https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications "Microsoft Learn – App-Sicherheitsbetrieb"
[14]: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/ "Microsoft – Storm-0940 ConnectWise"
[15]: https://learn.microsoft.com/en-us/entra/workload-id/troubleshoot-revoked-credentials "Microsoft Learn – Widerrufene App-Credentials"
[16]: https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/ "Microsoft – KI-gestützte Secret-Suche, 5. November 2026"
[17]: https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity "Microsoft Learn – Conditional Access for workload identities"
[18]: https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals "Microsoft Learn – Anwendungsobjekte und Dienstprinzipale"
[19]: https://learn.microsoft.com/en-us/entra/identity-platform/single-and-multi-tenant-apps "Microsoft Learn – Single und Multitenant Apps"
[20]: https://www.microsoft.com/en-us/security/blog/2026/11/05/email-threat-landscape-q3-2026-trends-and-insights/ "Microsoft – Q3-Mail-Bedrohungsbericht, 5. November 2026"
[21]: https://www.connectwise.com/company/trust/advisories "ConnectWise Trust Center – Cloud Backup und App-Identitäten"
[22]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/history "Fedlex – DSG-Chronologie"
[23]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml "Fedlex – Amtliche DSG-XML, 7. Juli 2025"
[24]: https://www.bacs.admin.ch/de/im-fokus "BACS – Im Fokus"
[25]: https://www.microsoft.com/en-us/security/blog/ "Microsoft Security Blog – Übersicht"
[26]: https://nvd.nist.gov/vuln/detail/CVE-2026-109469 "NVD – CVE-2026-109469"
[27]: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-109469 "MSRC – CVE-2026-109469, Cloud-Mitigation"
[28]: https://www.microsoft.com/en-us/security/blog/2026/11/05/whats-new-in-microsoft-security-november-2026/ "Microsoft – November-Produktübersicht"
[29]: https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/ "Microsoft – SCKit und ScreenConnect, 13. November 2026"
[30]: https://www.microsoft.com/en-us/security/blog/2026/11/06/artex-abuse-expands-as-cybercriminals-target-financial-sector/ "Microsoft – ARTEX im Finanzsektor, 6. November 2026"

## Nachtrag des lokalen Linkabgleichs

Bearbeitungszeit: 2026-11-15T09:20:58+01:00. Die Live-Zielzuordnung ist im [Zielplan](public-target-map.csv) und im [Linkänderungsprotokoll](lokaler-live-linkabgleich.json) belegt. Diese Ergänzung ersetzt nur alte lokale Markdown-Linkziele durch separat mit HTTP200 geprüfte Adressen; sie ändert keine logischen Slugs oder Freigaben.

**articles/06-microsoft-365-sicherheit-kmu.md:** `/resources/06-m365-tenant-pruefliste` → `https://www.dkschv.ch/wissen/resources/06-m365-tenant-pruefliste.html`: 2 Linkvorkommen; `/unsere-dienstleistungen/sicherheitsanalyse` → `https://www.dkschv.ch/sicherheitsanalyse.html`: 1 Linkvorkommen; `/unsere-dienstleistungen/risikomanagement` → `https://www.dkschv.ch/risikomanagement.html`: 1 Linkvorkommen; `/unsere-dienstleistungen/notfallplanung` → `https://www.dkschv.ch/notfallplanung.html`: 1 Linkvorkommen.

Globale Ergänzung: Alle zwölf Artikeladressen sind HTTP200, Fachfreigaben bleiben aber offen. Der Wiederherstellungsartikel lieferte trotz Login-Hinweis umfangreichen Text ohne Credentials; wirksamer serverseitiger Schutz ist nicht nachgewiesen. Webador ist nicht authentifiziert. Keine CMS-/Live-Änderung oder Veröffentlichung.
