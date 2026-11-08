# Artikel 06 – Quellenprüfung und Änderungen

**Prüfdatum:** 1. November 2026, ISO-KW 44  
**Prüfzeit:** Die direkten Originalabrufe erfolgten am 01.11.2026 tatsächlich zwischen **09:05 und 09:07 CET (Europe/Zurich)** und damit nach dem vorgegebenen Newsfenster. Die Zeitangaben sind Abrufzeiten, keine behaupteten Abschlusszeitpunkte von Websites.  
**Geprüfter Gegenstand:**

- Artikel: `blog-paket/articles/06-microsoft-365-sicherheit-kmu.md`
- Arbeitsmittel: `blog-paket/resources/06-m365-tenant-pruefliste.md`
- Kontext: Wartungsmanifest, Prüfvormerkungen und Wochenquellenbefund vom 25.10.2026 sowie der Einzelbericht vom 18.10.2026.

> **Ergebnis:** Alle **15 eindeutigen, nach dieser Pflege in Artikel und Arbeitsmittel zitierten externen Originalquellen** waren beim direkten Abruf erreichbar und stützen die jeweils verwendeten Aussagen. Zwei neue, materielle Herstellerquellen vom 21. und 22. Oktober 2026 wurden eng abgegrenzt ergänzt: Storm-0940/ConnectWise sowie die Ursachenklärung für widerrufene Anwendungsanmeldeinformationen. Die Änderungen begründen keine Tenant-, Incident-, Forensik-, Rechts-, Hersteller- oder Publikationsfreigabe.

Die Recherche deckt die aufgeführten Originalquellen und die unten genannten Übersichten ab. Sie ist keine Zusage, alle global veröffentlichten Meldungen zu erfassen oder den exakten Wortlaut nicht versionierter Seiten zu jedem Zeitpunkt des Newsfensters historisch zu rekonstruieren. Es wurde kein Tenant geöffnet, kein Application-ID-Inventar erstellt, kein Log eingesehen, keine Lizenz geprüft und keine Konfiguration verändert.

## Quellenprüfung der zitierten Originalquellen

| Nr. | Original-URL | Abruf / Erreichbarkeit | Version oder datierter Stand | Aussagegehalt für Artikel und Arbeitsmittel |
|---:|---|---|---|---|
| 1 | https://www.bacs.admin.ch/de/empfehlungen-fuer-die-zusammenarbeit-mit-it-providern | 01.11.2026, 09:05 CET; erreichbar | Kein sichtbares Publikations- oder Änderungsdatum | Das BACS verlangt klar geregelte Zuständigkeiten für technische und organisatorische Massnahmen, betont die nicht delegierbare Verantwortung und nennt unter anderem AVV, Backup-/Restore-Test, MFA, Monitoring und Notfallkontakte.[1] |
| 2 | https://www.edoeb.admin.ch/de/datenbearbeitungen-in-der-cloud | 01.11.2026, 09:05 CET; erreichbar | Kein sichtbares Publikations- oder Änderungsdatum | Der EDÖB ordnet Cloud-Anbieter in der Regel als Auftragsbearbeiter ein. Verantwortliche Cloud-Nutzer müssen datenschutzkonforme Bearbeitung und Betroffenenrechte sicherstellen sowie Weisungen, Sicherheitsmassnahmen, Unterauftragsbearbeitung, Länder und Mitwirkung prüfen.[2] |
| 3 | https://www.fedlex.admin.ch/eli/cc/2022/491/de | 01.11.2026, 09:05 CET; erreichbar | Konsolidierte Fassung gemäss amtlicher Chronologie: Berichtigung vom 07.07.2025; keine neuere Fassung in der am 01.11.2026 abgerufenen Chronologie | Art. 7 verlangt Datenschutz durch Technikgestaltung und datenschutzfreundliche Voreinstellungen; Art. 8 risikoadäquate Datensicherheit; Art. 9 die Prüfung der Datensicherheitsfähigkeit des Auftragsbearbeiters und vorgängige Genehmigung einer Weiterübertragung.[3] [4] |
| 4 | https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication | 01.11.2026, 09:05 CET; erreichbar | Direkter Abruf; der abgerufene Auszug weist kein Fussdatum aus. Letzte im Bericht vom 18.10.2026 dokumentierte Seitenaktualisierung: 03.04.2026. | Bestätigt die schrittweise MFA-Durchsetzung für Vorgänge im Microsoft-365-Admincenter seit Februar 2025, grenzt diese gegen andere Anwendungen ab und verweist für eigene Durchsetzung auf Conditional Access beziehungsweise Security Defaults. Workload Identities sind nicht Teil dieser MFA-Durchsetzung.[5] |
| 5 | https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access | 01.11.2026, 09:05 CET; erreichbar | Direkter Abruf; der abgerufene Auszug weist kein Fussdatum aus. Letzte im Bericht vom 18.10.2026 dokumentierte Seitenaktualisierung: 05.06.2026. | Bestätigt mindestens zwei cloudnative Notfallkonten, permanente aktive Global-Administrator-Rolle, phishing-resistente FIDO2- oder zertifikatsbasierte Anmeldung, Schutz der Zugangsmittel, gezielte Conditional-Access-Ausnahmen, Alarmierung und Funktionsprüfung mindestens alle 90 Tage.[6] |
| 6 | https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/best-practices | 01.11.2026, 09:05 CET; erreichbar | Letzte Aktualisierung 01.06.2026 | Stützt Least Privilege, PIM für zeitlich begrenzte Aktivierung, MFA für Admins, Access Reviews sowie die Richtwerte weniger als fünf Global Administrators und weniger als zehn privilegierte Rollenzuweisungen. Verfügbarkeit ist lizenzabhängig.[7] |
| 7 | https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off | 01.11.2026, 09:05 CET; erreichbar | Letzte Aktualisierung 30.06.2026 | Stützt Freigabestufen, nicht authentisierte «Anyone»-Links, die Restriktion einzelner Sites gegenüber der Organisation, die Begrenzung von OneDrive auf nicht offener als SharePoint sowie Domains, Sicherheitsgruppen und Gastablauf.[8] |
| 8 | https://learn.microsoft.com/en-us/purview/audit-solutions-overview | 01.11.2026, 09:05 CET; erreichbar | Letzte Aktualisierung 18.05.2026 | Bestätigt, dass Audit Standard bei Organisationen mit passendem Abonnement standardmässig aktiviert ist und grundsätzlich 180 Tage aufbewahrt. Premium erweitert Funktionen und Aufbewahrung, unter anderem abhängig von Lizenz und Ereignistyp.[9] |
| 9 | https://learn.microsoft.com/en-us/purview/audit-log-retention-policies | 01.11.2026, 09:05 CET; erreichbar | Letzte Aktualisierung 19.06.2026 | Bestätigt Audit-Premium-Aufbewahrungsrichtlinien und Lizenz-/Nicht-Rückwirkungsgrenzen. Für Entra-, Exchange-, OneDrive- und SharePoint-Ereignisse gilt die einjährige Standardrichtlinie nur unter den genannten Lizenzbedingungen; die genaue Tenant-Konfiguration bleibt offen.[10] |
| 10 | https://www.bacs.admin.ch/de/cloud-computing-und-cybersicherheit | 01.11.2026, 09:05 CET; erreichbar | HTML-Seite ohne sichtbares Änderungsdatum; verlinkte Technologiebetrachtung datiert 02.05.2025 | Stützt den BACS-Prüfprozess: Exportierbarkeit, Offline-Backup, dokumentierte MFA, Verschlüsselung, Zugriffsprotokollierung und Vorfallprozess sind in der Eignungsbeurteilung von Cloud-Diensten zu prüfen.[11] |
| 11 | https://www.bacs.admin.ch/de/csm26-s3-de | 01.11.2026, 09:05 CET; erreichbar | Veröffentlicht 16.10.2026 | Stützt die Prüfung und gegebenenfalls Anonymisierung sensibler, persönlicher oder geschäftlicher Inhalte vor KI-Eingaben, die Nutzung von Unternehmens- statt Privatkonten sowie Prüfung von Trainingsnutzung und Opt-out.[12] |
| 12 | https://www.bacs.admin.ch/de/26w40-de | 01.11.2026, 09:05 CET; erreichbar | Veröffentlicht 06.10.2026 | Stützt die eng begrenzte Vorfallnotiz: geschäftliche Geräte und zuständige IT informieren, Verdacht fachlich untersuchen lassen, bei Infektion Neuaufsetzen und nachher Passwortwechsel. Die Quelle ist keine Einzelfall-Forensik- oder Tenant-Anweisung.[13] |
| 13 | https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications | 01.11.2026, 09:06 CET; erreichbar | Direkter Abruf; kein belastbar ausgewiesenes neues Datum im abgerufenen Auszug | Stützt das Inventar und Monitoring von Anwendungs- und Dienstprinzipaländerungen: neue Anmeldeinformationen, Eigentümer, Zustimmungen, Berechtigungen und privilegierte Rollenzuweisungen ausserhalb des Änderungsprozesses. Microsoft weist darauf hin, dass Application- und Service-Principal-Updates als zwei Auditereignisse erscheinen.[14] |
| 14 | https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/ | 01.11.2026, 09:05 CET; erreichbar | Veröffentlicht 21.10.2026 | Microsoft beschreibt Storm-0940 und kompromittierte Identitäten mehrerer ConnectWise-Cloudanwendungen. Für **vier konkret genannte Application IDs** verlangt der Bericht Inventar auch in früher autorisierten Tenants, lokales Dienstprinzipal-Objekt-ID-Recording, Prüfung von Anmelde- und Auditdaten sowie Beweissicherung. Enterprise Apps sollen nicht als erste Reaktion gelöscht werden. Die eingeschränkte Anweisung, Anbindungen bis zu formellen ConnectWise-Wiederherstellungsanweisungen deaktiviert zu halten, gilt nur für diese betroffenen Anbindungen. Ein App-Treffer oder eine erfolgreiche Anmeldung beweist weder Missbrauch noch Datenzugriff oder Datenabfluss.[15] |
| 15 | https://learn.microsoft.com/en-us/entra/workload-id/troubleshoot-revoked-credentials | 01.11.2026, 09:05 CET; erreichbar | Letzte Aktualisierung 22.10.2026 | Ein Widerrufsfehler beweist nicht, dass Microsoft die Anmeldeinformation widerrufen hat. `tokenRevocations` sind für Application- und Service-Principal-Objekt derselben Application ID getrennt zu prüfen und mit Auditdaten zu korrelieren. Ein Widerruf verhindert neue Tokens, kann bei einzelnen Ressourcen bereits ausgegebene Tokens bis zu 24 Stunden fortgelten lassen. Bei bestätigter Kompromittierung empfiehlt Microsoft Ersatz/Umstellung, den Widerruf beizubehalten und zusätzlich eingebrachte Zugriffe zu entfernen.[16] |

### Amtlicher Rechtszugang

Die Fedlex-HTML-Seite war beim stateless Abruf inhaltlich lesbar. Unabhängig davon wurde die amtliche Chronologie direkt geöffnet und die maschinenlesbare XML-Fassung mit Art. 7–9 abgerufen.[4] [17] Der JavaScript-Hinweis in der Fedlex-Navigation wurde daher **nicht** als fehlende Rechtsfassung interpretiert. Die Chronologie weist für das DSG nach der Berichtigung mit Inkrafttreten am 07.07.2025 keine neuere Fassung aus.[4] Es wurde kein Feld `rechtsstand` ergänzt und keine rechtliche Freigabe behauptet; die verifizierte Fassung dient ausschliesslich der Quellenstützung der bestehenden allgemeinen Aussagen.

### Zusätzlich gesichtete Originalquellen und Rechercheabgrenzung seit 18. Oktober

| Original-URL | Abruf / Erreichbarkeit | Version oder Datum | Ergebnis für diese Pflege |
|---|---|---|---|
| https://www.bacs.admin.ch/de/im-fokus | 01.11.2026, 09:06 CET; erreichbar | Übersicht mit einschlägigen Einträgen bis 27.10.2026 | Geprüft wurden insbesondere die BACS-Meldungen vom 19. und 22.10.2026. Die Übersicht bestätigte keine weitere konkrete M365-/Cloud-Provider-Meldung, die eine zusätzliche Evergreen-Änderung erforderte.[18] |
| https://www.bacs.admin.ch/de/26-tb-authentifizierung-de | 01.11.2026, 09:07 CET; erreichbar | Veröffentlicht 19.10.2026 | Das BACS ordnet Authentifizierungsverfahren anhand von Sicherheitsklassen ein, versteht sich aber ausdrücklich nicht als formale Zertifizierung. Die schon präzisen Microsoft-Notfallzugangsangaben wurden nicht künstlich um eine weitere allgemeine Quelle erweitert.[19] |
| https://www.bacs.admin.ch/de/26-kmustudie-de | 01.11.2026, 09:07 CET; erreichbar | Veröffentlicht 22.10.2026 | Die Meldung unterstreicht organisatorische Lücken bei Inventarisierung, Notfallplänen, Lieferantenprüfung und Restore-Tests. Sie liefert keinen M365-spezifischen Parameter und wurde deshalb nicht als weitere Evergreen-Referenz aufgenommen.[20] |
| https://www.microsoft.com/en-us/security/blog/ | 01.11.2026, 09:06 CET; erreichbar | Übersicht mit Beiträgen bis 30.10.2026 | Übersicht nach weiteren einschlägigen Meldungen geprüft. Die Beiträge vom 28.–30.10. betrafen unter anderem CISO-Rolle, bösartige Entwicklungs-Erweiterungen und AD-CS-Intrusionswege, nicht die konkrete M365-/Entra-Konfiguration dieses Artikels. Der verpflichtend zu prüfende Beitrag vom 21.10. ist als Quelle [15] integriert.[21] |
| https://www.microsoft.com/en-us/security/blog/2026/10/19/agents-are-your-newest-insiders-security-must-move-at-their-speed/ | 01.11.2026, 09:07 CET; erreichbar | Veröffentlicht 19.10.2026 | Herstellerankündigung zu Agentenidentitäten, Dynamic Permissions und Dynamic Conditional Access. Sie formuliert sinnvolle Prinzipien, belegt aber keine allgemein verfügbare, lizenzunabhängige Standardfunktion für jedes KMU.[22] |
| https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id | 01.11.2026, 09:07 CET; erreichbar | Letzte Aktualisierung 24.06.2026 | Agent ID ist laut Seite für Entra-Kunden verfügbar; die Ausweitung der Entra-Sicherheitsfunktionen auf Agenten setzt jedoch Microsoft Agent 365 und die dort beschriebenen Lizenzen voraus. Ohne Architektur-, Lizenz- und Tenantprüfung keine Aufnahme in Artikel 06.[23] |
| https://learn.microsoft.com/en-us/purview/audit-log-activities | 01.11.2026, 09:06 CET; erreichbar | Die Seite zeigt die im Wochenbefund festgehaltenen Metadaten `ms.date` 15.10.2026 und `updated_at` 19.10.2026; der Zeitstempel allein belegt keine materielle Änderung | Bestätigt als ergänzende Referenz, dass Purview-Audit unter anderem Vorgänge zu Dienstprinzipal-Anmeldeinformationen, Delegationsberechtigungen und Entfernungen erfasst. Die bestehende Logging-Aussage bleibt durch [9], [10] und [14] ausreichend gestützt; keine zusätzliche Quellenziffer nötig.[24] |

Beim ersten Versuch wurde die nicht einschlägige URL `https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/remove-application-credentials` am 01.11.2026 um 09:05 CET per stateless Abruf technisch ohne extrahierbaren Inhalt zurückgegeben. Das war **kein** Nachweis einer fehlenden Rechts- oder Produktfunktion und wurde nicht zitiert. Der vom Prüfvormerkungsbefund dokumentierte, direkt erreichbare Herstellerpfad `https://learn.microsoft.com/en-us/entra/workload-id/troubleshoot-revoked-credentials` wurde stattdessen vollständig geöffnet und ist als Quelle [16] verwendet.

Die Recherche führte zu keiner belastbaren weiteren Originalmeldung vom 25.10. bis 01.11.2026, die eine zusätzliche M365-Konfigurationsaussage oder einen wöchentlichen CVE-Einschub in diesen Evergreen-Artikel rechtfertigte. Die neue BACS-KMU-Studie und die BACS-Authentifizierungsorientierung sind kontextlich passend, ändern aber nicht die bereits belegten Konfigurationskontrollen.

## Änderungen am Artikel

### Metadaten und sichtbarer Stand

| Element | Vorher | Nachher | Grund |
|---|---|---|---|
| `status` | `Entwurf – nicht freigegeben` | Unverändert | Keine Fach- oder Publikationsfreigabe. |
| `slug` | `/wissen/microsoft-365-sicherheit-kmu` | Unverändert | Ursprünglichen Slug erhalten. |
| `veröffentlichungsdatum` | `05.11.2026` | Unverändert | Ursprüngliches Datum erhalten; es ist keine Freigabe. |
| `fachprüfung_status` und sämtliche bestehenden Fachmarker | Vorhanden | Erhalten; ein neuer sachbezogener Fachmarker im Incident-Abschnitt ergänzt | Die Fach- und Legalabgrenzungen bleiben ausdrücklich offen. |
| `meta_title`, `meta_description` | Bestehende Importfelder | Unverändert; keine Vorschlagsfelder angelegt | Keine konkrete belegte SEO-Korrektur erforderlich. |
| `stand` | `18. Oktober 2026` | `1. November 2026` | Genaues Datum der Quellenpflege. |
| `quellenpruefung_umfang` | 12 Referenzen beider Dateien plus BACS «Im Fokus» bis 18.10.2026 | 15 zitierte Originalquellen beider Dateien sowie die direkt gesichteten BACS-/Microsoft-Übersichten und einschlägigen Learn-Seiten vom 18.10. bis 01.11.2026; keine Tenant-, App-ID-, Log-, Lizenz-, CMS- oder Live-Linkprüfung | Tatsächlich geprüfte Reichweite präzisiert. |
| `quellenpruefung_status` | Vollständig für referenzierte Quellen, ohne Fach-, Rechts-, Tenant- oder Publikationsfreigabe | Vollständig für 15 zitierte Originalquellen und die definierten Übersichten, ergänzt um Ausschluss von Forensik- und Herstellerfreigabe | Tatsächliche Reichweite und Grenzen präzisiert. |
| Sichtbarer Hinweis unter H1 | Nicht vorhanden | `Stand: 1. November 2026. Die Quellenprüfung bestätigt allgemeine Hersteller- und Behördenaussagen, nicht die Einstellungen, Lizenzen oder Protokolle eines konkreten Tenants.` | Sichtbaren Stand an Frontmatter und Quellenprüfung angeglichen. |
| `rechtsstand`, `fachlich_geprueft_am` | Nicht vorhanden | Nicht angelegt | Die amtliche Fassung ist für die zitierten Artikel verifiziert, aber diese Quellenprüfung ist keine Rechts- oder Fachfreigabe. |

### Inhaltliche Passagen

| Betroffene Passage | Vorher | Nachher | Belegte Änderung |
|---|---|---|---|
| Überschrift Abschnitt 2 | `Adminrollen auf das notwendige Mass begrenzen` | `Adminrollen, Enterprise Apps und Workload Identities steuern` | Der Gegenstand umfasst nun bewusst auch nichtmenschliche Identitäten und Anwendungen. |
| Nach Absatz zu PIM | Nur allgemeiner Hinweis zu PIM, separaten Admin-Konten und manuellen Reviews | Neuer Absatz zum Inventar von Enterprise Apps/Dienstprinzipalen: Eigentümer, Zweck, Hersteller-/Providerbezug, Berechtigungen, Genehmigung, Lebenszyklus, Application ID und lokale Dienstprinzipal-Objekt-ID; Monitoring von Credential-, Owner-, Consent-, Berechtigungs- und Rollenzuweisungsänderungen ausserhalb des Änderungsprozesses | Microsofts Sicherheitsleitfaden belegt genau diese Überwachung; die Ergänzung setzt keine konkrete App-Berechtigung voraus.[14] |
| Neuer Unterabschnitt `Herstellerintegrationen und widerrufene Anmeldeinformationen ohne vorschnelles Löschen` | Nicht vorhanden | Eng begrenzter Storm-0940-Hinweis: bei den vier genannten ConnectWise-Application-IDs nur nach Application ID prüfen, frühere Autorisierungen und Dienstprinzipal-Objekt-ID erfassen, Herstelleranweisung zur Deaktivierung nur für diese Anbindungen; App-Treffer/Anmeldung sind kein Missbrauchs- oder Abflussnachweis | Der Microsoft-Bericht vom 21.10.2026 verlangt diese auf vier IDs begrenzte Untersuchung. Keine pauschale ConnectWise- oder Enterprise-App-Aussage.[15] |
| Gleicher Unterabschnitt, Beweissicherung | Kein konkreter App-Incident-Hinweis | Vor irreversiblen Änderungen Konfiguration, Entra-Anmelde-/Auditdaten, Purview-Auditdaten und gegebenenfalls SIEM sichern; Enterprise Apps nicht als Erstreaktion löschen; erst nach Beweissicherung durch berechtigte Fachstelle bestätigte unbefugte Credentials, Grants, Owners, Assignments oder Identitäten entfernen. Dringliche Eindämmung nicht wegen Exporten verzögern. | Unmittelbare Herstelleranweisung, ausdrücklich ohne eigene Deaktivierungs-, Lösch- oder Rotationsanweisung.[15] |
| Gleicher Unterabschnitt, Widerruf | Nicht vorhanden | Widerrufsfehler nicht als Microsoft-Widerruf gleichsetzen; Application- und Service-Principal-Objekt getrennt mit gleicher Application ID sowie Auditereignis prüfen; bereits ausgestellte Tokens können je Ressource bis zu 24 Stunden fortgelten. Bei bestätigter Kompromittierung Ersatz und Workload-Umstellung, kompromittierte Anmeldeinformation bleibt widerrufen. | Direkte Learn-Anleitung vom 22.10.2026. Neuer Fachmarker grenzt Verdachtsbeurteilung, Beweissicherung, Eindämmung und Integrationserholung ab.[16] |
| 30-Tage-Plan, Tage 1–7 | Inventar von «Konten, Gäste, Apps, Adminrollen» | Präzisiert zu Enterprise Apps und Dienstprinzipalen mit Application ID | Das Inventar wird prüfbar und an die neue Passage angepasst.[14] [15] |
| 30-Tage-Plan, Tage 15–21 | Test von Suchabfragen für Adminrollen, Anmeldungen und Freigaben | Test ergänzt um Änderungen an Anwendungsanmeldeinformationen und Zustimmungen | Audit- und Monitoringbezug konsistent ergänzt.[14] [24] |
| Quellen | [1]–[12] | [1]–[15], neue verwendete Quellen [13]–[15] | Jede neue externe Quelle wird durch passende Inline-Zitate tatsächlich verwendet. |

Interne relative Slugs und alle bisherigen inhaltlichen Abschnitte blieben erhalten. Der Artikel enthält nach der Erweiterung weiterhin deutlich mehr als 1'400 Wörter. Es wurde kein wöchentlicher CVE-Einschub vorgenommen.

## Änderungen am Arbeitsmittel

### Metadaten und sichtbare Version

| Element | Vorher | Nachher | Grund |
|---|---|---|---|
| `status`, `slug`, `titel`, `bezug`, `fachprüfung_status` | Vorhanden | Unverändert | Ursprünglichen Status, Slug und Fachmarker erhalten. |
| Meta-Title und Meta-Description | Bestehende Importfelder | Unverändert; keine Vorschlagsfelder angelegt | Keine belegte Meta-Korrektur nötig. |
| `version` | `Stand 18. Oktober 2026` | `Stand 1. November 2026` | Konsistent zum aktuellen Artikelstand. |
| `quellenpruefung_umfang` | 12 Referenzen beider Dateien plus BACS «Im Fokus» bis 18.10.2026 | Auf 15 zitierte Originalquellen plus tatsächlich gesichtete Übersichten/Learn-Referenzen im Zeitraum erweitert, mit ausdrücklichem Ausschluss von Tenant-, App-ID-, Log-, Lizenz-, CMS- und Live-Linkprüfung | Tatsächlich geprüfte Reichweite präzisiert. |
| `quellenpruefung_status` | Vollständig für referenzierte Quellen, ohne Fach-, Rechts-, Tenant- oder Publikationsfreigabe | Vollständig für 15 zitierte Originalquellen und die definierten Übersichten; ergänzt um keine Forensik- oder Herstellerfreigabe | Tatsächliche Grenze präzisiert. |
| Sichtbarer Versionshinweis | Nicht vorhanden | `Version: Stand 1. November 2026. Die Vorlage ist eine Arbeitsgrundlage; ihr Ausfüllen belegt keine Tenant-, Fach-, Rechts- oder Veröffentlichungsfreigabe.` | Sichtbare Version konsistent zu Frontmatter aktualisiert. |

### Inhaltliche Passagen

| Betroffene Passage | Vorher | Nachher | Belegte Änderung |
|---|---|---|---|
| B6 | «Neue Anwendungen, Service Principals und weitreichende Berechtigungen» mit Eigentümer, Zweck und Freigabeprozess | Präzisiert als vollständiges Inventar von Enterprise Apps, Dienstprinzipalen und Workload Identities: Eigentümer, Zweck, Hersteller-/Providerbezug, Application ID, Berechtigungen, Genehmigung und Lebenszyklus | Nachweisorientierter Inventar-Kontrollpunkt gemäss Microsoft-App-Monitoring.[14] |
| B7/B8 | B7 war Delegation über Gruppen/abgegrenzte Bereiche | Neuer B7-Kontrollpunkt für begründete Untersuchungshinweise zu Herstellerintegrationen: aktuelle/frühere Autorisierung nach Application ID, lokale Dienstprinzipal-Objekt-ID, verfügbare Logs und Konfiguration vor irreversiblen Änderungen sichern oder Lücke dokumentieren. Bisheriges B7 als B8 erhalten. | Auf das tatsächliche Storm-0940-Vorgehen beschränkt; keine generelle Incident- oder Deaktivierungsanweisung.[15] |
| Neue Prüfnotiz B6–B7 | Nicht vorhanden | Beschreibt Monitoring relevanter Änderungen, die vier spezifischen ConnectWise-IDs, den begrenzten Geltungsbereich der Hersteller-Deaktivierungsanweisung und die Beweissicherung vor Löschen. | Hersteller- und Learn-Aussagen ohne Ausweitung auf andere Apps oder Produkte.[14] [15] |
| Neue Prüfnotiz zu widerrufenen Anmeldeinformationen | Nicht vorhanden | Getrennte Prüfung der `tokenRevocations` beider Objekttypen, Korrelation mit Auditereignis und 24-Stunden-Grenze für einzelne bereits ausgestellte Tokens; neuer Fachmarker, der keine App-Deaktivierung, Löschung, Rotation oder Reaktivierung anordnet. | Direkte Learn-Anleitung vom 22.10.2026.[16] |
| D3 | Suche nach Adminrollenänderung, externer Freigabe und verdächtiger Anmeldung | Test ergänzt um Änderung an Anwendungsanmeldeinformationen oder Zustimmungen | Kontrollpunkt passt zur erweiterten App-Governance.[14] [24] |
| D5 | Sicherheitsrelevante Protokolle im Vorfall sichern | Ergänzt um Konfigurationen und weitere verfügbare Beweise vor irreversiblen Änderungen | Beweissicherung konkretisiert, ohne Forensikverfahren vorzuschreiben.[15] |
| Quellen | [1]–[11] | [1]–[14], neue tatsächlich verwendete Quellen [12]–[14] | Nummerierung und Inline-Zitate sind konsistent. |

## Erhaltene Grenzen, genaue Blocker und Live-Status

1. **Tenant- und App-Prüfung offen.** Es wurden keine Microsoft-365-Tenants, Enterprise Apps, Dienstprinzipale, Application IDs, Object IDs, Berechtigungen, Zustimmungen, Anmeldeprotokolle, Purview-Auditdaten, SIEM-Daten, Conditional-Access-Richtlinien, Notfallkonten oder Lizenzen geprüft. Ein Checklistenpunkt mit Status «erfüllt» benötigt einen organisationsspezifischen Nachweis.

2. **Storm-0940 bleibt eine eingeschränkte Herstelleranweisung.** Es wurde weder festgestellt, dass eine ConnectWise-Integration vorhanden ist, noch dass eines der vier im Herstellerbericht genannten Application IDs autorisiert war. Die Deaktivierungsanweisung wurde nicht verallgemeinert und nicht ausgeführt. Ein App-Treffer oder eine erfolgreiche Anmeldung ist laut Hersteller kein hinreichender Missbrauchs-, Datenzugriffs- oder Datenabflussnachweis.[15]

3. **Beweissicherung, Eindämmung und Wiederherstellung verlangen Fachentscheid.** Es wurde keine App deaktiviert oder gelöscht, keine Anmeldeinformation rotiert oder widerrufen, kein Widerruf entfernt und kein Zugriff wiederhergestellt. Der neue Fachmarker bleibt offen. Die konkreten Rollen, Freigaben, zeitkritischen Eindämmungsschritte und forensischen Anforderungen sind mit dem Notfallprozess und dazu berechtigten Fachstellen zu bestimmen.[15] [16]

4. **Rechts- und Datenschutzprüfung offen.** Die DSG-Artikel 7–9 wurden amtlich verifiziert.[3] [4] Die konkrete Zulässigkeit von Auftragsbearbeitung, Unterauftragsbearbeitung, Weisungen, Vertragsbedingungen, Datenbearbeitungsorten, Auslandbekanntgaben, Personendaten und KI-Datenflüssen ist weiterhin **[FACHPRÜFUNG ERFORDERLICH]**. Die EDÖB-Cloud-Information ist eine Orientierung, keine Einzelfallbeurteilung.[2]

5. **Keine Liveänderung.** Es gab keinen CMS-Zugriff, keine Browserbedienung, keinen Import und keine Veröffentlichung. Im Laufstatus vom 25.10.2026 sind die geplanten öffentlichen Artikel- und Arbeitsmittelziele weiterhin als HTTP 404 dokumentiert; die internen relativen Slugs wurden deshalb unverändert gelassen. Vor einem Go-live sind Fachfreigabe, tatsächliche Ziel-URLs, CMS-Zugriff und aktueller Quellenstand erneut zu prüfen.

6. **Keine Vollständigkeitszusage.** Die Quellenprüfung ist vollständig für die 15 zitierten Originalquellen und die ausdrücklich dokumentierten Übersichten. Sie ersetzt keine Garantie über nicht gefundene, nachträglich geänderte oder nicht versionierte Inhalte.

## Metadaten-, Status- und Referenzkontrolle

- Artikel-Slug `/wissen/microsoft-365-sicherheit-kmu`, Arbeitsmittel-Slug `/resources/06-m365-tenant-pruefliste`, Artikel-Veröffentlichungsdatum `05.11.2026`, Entwurfsstatus und `fachprüfung_status` sind erhalten.
- Die bisherigen sichtbaren **[FACHPRÜFUNG ERFORDERLICH]**-Marker bleiben bestehen. Der neue Fachmarker steht unmittelbar an der neuen Incident-/Herstellerintegrationspassage.
- `meta_title` und `meta_description` beider Dateien wurden nicht verändert; es wurden keine `meta_title_vorschlag`- oder `meta_description_vorschlag`-Felder angelegt.
- Der sichtbare Artikelstand und die sichtbare Arbeitsmittelversion sind jeweils auf **1. November 2026** angeglichen.
- Der Quellenprüfstatus entspricht dem tatsächlich geprüften Umfang. `fachlich_geprueft_am` wurde nicht angelegt. Die Artikel-Frontmatter enthält weiterhin kein `rechtsstand`; keine Rechtsfreigabe wird daraus abgeleitet.
- Alle externen URLs in den Quellenabschnitten sind numerisch zitiert und definiert. URLs mit Klammern wurden nicht eingefügt; damit ist keine URL-Klammer-Encodierung erforderlich.

## Quellen

[1]: https://www.bacs.admin.ch/de/empfehlungen-fuer-die-zusammenarbeit-mit-it-providern "BACS – Zusammenarbeit mit IT-Dienstleistern"
[2]: https://www.edoeb.admin.ch/de/datenbearbeitungen-in-der-cloud "EDÖB – Cloud-Computing"
[3]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Datenschutzgesetz DSG"
[4]: https://www.fedlex.admin.ch/eli/cc/2022/491/de/history "Fedlex – Chronologie DSG"
[5]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication "Microsoft Learn – Mandatory multifactor authentication"
[6]: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access "Microsoft Learn – Manage emergency access accounts"
[7]: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/best-practices "Microsoft Learn – Best practices for Microsoft Entra roles"
[8]: https://learn.microsoft.com/en-us/sharepoint/turn-external-sharing-on-or-off "Microsoft Learn – Manage sharing settings for SharePoint and OneDrive"
[9]: https://learn.microsoft.com/en-us/purview/audit-solutions-overview "Microsoft Learn – Auditing solutions in Microsoft Purview"
[10]: https://learn.microsoft.com/en-us/purview/audit-log-retention-policies "Microsoft Learn – Audit log retention policies"
[11]: https://www.bacs.admin.ch/de/cloud-computing-und-cybersicherheit "BACS – Cloud Computing und Cybersicherheit"
[12]: https://www.bacs.admin.ch/de/csm26-s3-de "BACS – KI im Berufsalltag"
[13]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40 Malwareverdacht"
[14]: https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications "Microsoft Learn – Security operations guide for applications"
[15]: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/ "Microsoft Security Blog – Storm-0940 ConnectWise supply-chain compromise"
[16]: https://learn.microsoft.com/en-us/entra/workload-id/troubleshoot-revoked-credentials "Microsoft Learn – Troubleshoot revoked application credentials"
[17]: https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2022/491/20250707/de/xml/fedlex-data-admin-ch-eli-cc-2022-491-20250707-de-xml-1.xml "Fedlex – DSG XML-Fassung 7. Juli 2025"
[18]: https://www.bacs.admin.ch/de/im-fokus "BACS – Im Fokus"
[19]: https://www.bacs.admin.ch/de/26-tb-authentifizierung-de "BACS – Sicher authentifizieren"
[20]: https://www.bacs.admin.ch/de/26-kmustudie-de "BACS – KMU Cybersicherheit 2026"
[21]: https://www.microsoft.com/en-us/security/blog/ "Microsoft Security Blog – Übersicht"
[22]: https://www.microsoft.com/en-us/security/blog/2026/10/19/agents-are-your-newest-insiders-security-must-move-at-their-speed/ "Microsoft Security Blog – Agents are your newest insiders"
[23]: https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id "Microsoft Learn – What is Microsoft Entra Agent ID"
[24]: https://learn.microsoft.com/en-us/purview/audit-log-activities "Microsoft Learn – Audit log activities"
