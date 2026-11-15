# Newsfeld 04 – KI-Sicherheit und Agenten, 15. November 2026, ISO-KW 46

**Drei neue Meldungen sind im Newsfenster 08.11.2026 09:00 bis 15.11.2026 09:00 CET, Europe/Zurich, belegt:** Microsofts Forschung zu vergiftetem Nachtraining von Coding-Agenten vom 12. November, die gemeinsame ENISA/CERT-EU-Publikation zu KI-Codeprüfungen vom 12. November und Microsoft FORGE Labs Rust-Forschung vom 9. November. Es handelt sich um neue Veröffentlichungen, nicht automatisch um neue Vorfälle oder Patchveröffentlichungen.[1] [3] [5]

Alle Quellen wurden tatsächlich **am 15.11.2026 nach 09:00 CET** abgerufen. Suchantworten kamen um 09:05:57, 09:06:06, 09:06:15 und 09:07:15 zurück; Fetch-Rückgaben liegen zwischen 09:06:04 und 09:07:38 CET. Die Schlussabschnitte der gekürzten ENISA-Extraktion wurden um 09:07:02 und jene der Microsoft-Rust-Extraktion um 09:07:13 gelesen. Diese Zeiten sind tatsächliche Rückgabe-/Lesezeiten, keine erfundene historische Prüfung um 09:00. Publikationsdaten innerhalb der Woche sind belegt; ein minutengenauer historischer Seitenwortlaut zum Redaktionsschluss ist nicht nachgewiesen.

## 12. November – Microsoft: Vergiftetes Nachtraining kann Coding-Agenten zu schädlichen Werkzeugaufrufen bringen

**Datum und Fakt:** Microsoft Defender Research und das Microsoft AI Red Team veröffentlichten zwei Untersuchungen zu Hintertüren in nachtrainierten Modellen. Der erste Ansatz setzt vergiftete Trainingsbeispiele in einem später vom Opfer genutzten Datensatz voraus; der zweite setzt Kontrolle des Angreifers über das Modelltraining vor Verteilung eines offenen Modell-Checkpoints voraus. Nach Aktivierung durch scheinbar harmlose Anfragen oder Inhalte aus Repositories können die Modelle schädliche Werkzeugaufrufe auswählen. Eine solche Hintertür liegt im Modell und ist nicht einfach eine neue Prompt-Injection-Schwachstelle der normalen Agentensoftware.[1]

Die Forschung beschreibt auch einzelne riskante Werkzeugaufrufe in einem öffentlich verfügbaren Trainingsdatensatz. Microsoft konnte dabei weder die Absicht des Herausgebers noch einen materiellen Einfluss dieser wenigen Zeilen auf ein nachtrainiertes Modell feststellen. Die experimentellen Angriffserfolgsraten dürfen deshalb nicht als gemessene reale Angriffshäufigkeit ausgegeben werden. Die Tests mit fremden Agentenoberflächen belegen ausdrücklich keine Schwäche der Standardkonfigurationen von Claude Code oder Codex CLI; das Risiko entsteht dort beim Einsatz eines absichtlich mit einer Hintertür versehenen Modell-Checkpoints.[1]

**Fixumfang:** Dies ist eine Forschungs- und Schutzmeldung, keine neue CVE-, KEV- oder Patchmeldung. Microsoft nennt keinen universellen Fixbuild, der eine Modellhintertür entfernt. Die verlinkte Defender-Dokumentation wurde beim Hersteller geöffnet: Der Schutz hängt von Agententyp, Integration und Regeln ab. Die Standardregel für Cloud-Agenten auditiert, statt Aktionen zu blockieren. Copilot Studio und Foundry sind dort als Preview bezeichnet; nicht unterstützte Werkzeuge oder Agenten ohne erforderliche Work-IQ-MCP-Integration sind im beschriebenen Agent-365-Pfad nicht abgedeckt. Der sichtbare Dokumentstand ist 15.10.2026 und wird nicht als neue KW-46-Funktion ausgegeben.[2]

**KMU-Relevanz und Prüfpunkt:** Besonders relevant für KMU, die Modelle selbst nachtrainieren, fremde Modellgewichte verwenden oder Coding-Agenten mit Dateien, Secrets und Netzverbindungen verbinden. Als allgemeine Prüfpunkte vormerken: Herkunft, Version und Hash von Trainingsdaten und Modell-Checkpoints festhalten; Werkzeuge und Zugangsdaten auf den Auftrag begrenzen; Ausführung isolieren; Aktionen mit grosser Wirkung durch eine zuständige Person prüfen lassen. Eine unauffällige Benchmarkleistung oder ein Promptfilter allein bestätigt keine sichere Modellintegrität.[1]

**Unsicherheit:** Die beschriebenen Voraussetzungen und Laborresultate belegen keinen Angriff auf ein Schweizer KMU und keine konkrete Kompromittierung. Lizenzierung, tatsächliche Schutzabdeckung, Datenbearbeitung und Wirksamkeit in einer bestimmten Umgebung bleiben offen. Die Publikationsuhrzeit ist nicht belegt.

## 12. November – ENISA/CERT-EU: KI-Codeprüfungen brauchen Isolation und menschliche Validierung

**Datum und Fakt:** Die offizielle Publikationsseite nennt 12.11.2026. Der Originalbericht beschreibt KI-gestützte Prüfungen von 27 Codebasen mit 220 potenziellen Befunden. Bis zur Publikation hatten die Codeverantwortlichen 88 davon beurteilt; 95 Prozent dieser Teilmenge wurden als echte Befunde bestätigt. Keine laufenden Anwendungen wurden getestet, und den Modellen fehlten Informationen über Produktionskonfigurationen. Die Prüfungen und die Mitteilung der Befunde an Codeverantwortliche fanden bereits vor dieser Ausgabewoche statt. Neu ist der Bericht.[3] [4]

**Fixumfang:** Vier zugewiesene CVE-IDs sind im Bericht genannt, aber keine neue Hersteller-Patchveröffentlichung im Newsfenster belegt. Daraus wird keine Fixversion abgeleitet. ENISA betont, dass vorgeschlagene Patches und Schweregrade menschlich zu validieren sind; eine vollautomatische Patchschleife kann neue Fehler einführen oder die eigentliche Ursache verfehlen.[4]

**KMU-Relevanz und Prüfpunkt:** Für KMU mit eigener Software oder Dienstleistern für KI-gestützte Codeprüfung ist die wichtigste Orientierung: Agenten in einer abgesicherten, isolierten Umgebung betreiben, Zugriff auf Systeme und Dienste begrenzen und Befunde durch Personen mit technischem Kontext prüfen lassen. Lieferanten sollen potenzielle KI-Befunde, reproduzierte Schwachstellen und bestätigte Behebungen getrennt ausweisen. Das ist keine Prüfung einer konkreten Anwendung.[4]

**Unsicherheit:** Die 95 Prozent gelten nur für die bereits beurteilten 88 Befunde, nicht für alle 220 und nicht als allgemeine Erfolgsquote. Unbeurteilte Befunde und fehlender Produktionskontext begrenzen die Aussagekraft. Der Bericht ist allgemeine Orientierung, keine Schweizer Norm oder Freigabe. Publikationsuhrzeit nicht belegt.

## 9. November – Microsoft FORGE Lab: Agentische Forschung findet Speichersicherheitsprobleme in Rust

**Datum und Fakt:** Microsoft beschreibt mehrere Probleme in den Rust-Bibliotheken `std` und `core`, darunter Fälle, in denen auch Code ohne eigene `unsafe`-Blöcke undefiniertes Verhalten auslösen kann. Ein Teil der Befunde entstand mit Unterstützung des agentischen Forschungssystems Hyenas/MDASH; Forschende reproduzierten die Fehler und bewerteten deren mögliche Sicherheitswirkung. Die drei Muster sind fehlerhafte Annahmen über ausbleibende Panics, korrekte benutzerdefinierte Implementierungen und das Verhalten des Betriebssystems. Ein Bibliotheksfehler ist laut Quelle nicht automatisch eine ausnutzbare Schwachstelle in jedem verwendenden Programm.[5]

**Fixumfang:** Der neue Forschungsbericht bündelt ältere Meldungen, bereits bearbeitete Änderungen und bei Publikation noch offene Punkte. Er ist kein pauschales neues Sicherheitsupdate. Die offizielle Rust-Veröffentlichung **1.100.0 vom 12.11.2026** und die Hersteller-Release-Notes wurden geöffnet. Sie bestätigen die Stabilisierung der Kern-Allocator-API; der dazugehörige bereits im September zusammengeführte Hersteller-PR dokumentiert verschärfte Sicherheitsbedingungen, insbesondere kein Unwinding aus Allocator-Methoden oder beim Drop. **1.100.0 wird hier nicht als universeller Mindestfixstand aller im Microsoft-Beitrag genannten Probleme behauptet.**[6] [7] [8]

**KMU-Relevanz und Prüfpunkt:** Vor allem für Softwareanbieter und KMU mit Rust-Eigenentwicklungen relevant. Bei eingesetzter Software mit dem zuständigen Hersteller klären, ob konkrete betroffene APIs und Auslösebedingungen erreicht werden und welcher Build sie behebt. KI-gestützte Schwachstellensuche ersetzt weder menschliche Reproduktion noch die anwendungsbezogene Risikobewertung. Kein pauschaler Notfallupdate-Aufruf für alle Rust-basierten Produkte.[5]

**Unsicherheit:** Microsoft nennt zwei eigene bei Publikation noch offene Meldungen sowie weitere offene verwandte Themen. Ihr heutiger Einzelstatus und die Fixmatrix sämtlicher beschriebenen Fehler wurden nicht vollständig geprüft. Der Bericht belegt weder eine aktive Ausnutzung noch Betroffenheit eines Schweizer KMU. Dass für ein einzelnes untersuchtes Szenario kein zuverlässiger Ausnutzungspfad gefunden wurde, ist keine Entwarnung für alle anderen Befunde.[5]

## Begrenzter Nichtfund bei NIST und CISA; bewusst ausgeschlossene Altmeldungen

In den gezielten Suchen und geöffneten hier aufgeführten NIST-/CISA-Quellen ist **keine zusätzliche eigenständige neue Meldung zu Agentensicherheit, Prompt Injection, KI-Datenabfluss oder KI-Sicherheitsberichten im Wochenfenster belegt**. Dies ist ein begrenzter Nichtfund, keine Vollständigkeitsbehauptung über sämtliche Publikationskanäle.

NISTs Agenteninitiative zeigt zwar «Updated November 9, 2026», wurde aber am 17.02.2026 erstellt. Ohne materiellen Änderungsbeleg zählt der neue Seitenstempel nicht als neue Nachricht. Die Agentenidentitätsgrundsätze stammen ausdrücklich vom 27.10.2026 und bleiben eine alte Vormerkung; die RFI-Auswertung stammt vom 18.05.2026.[9] [10] [11]

CISAs Tokenleitlinie ist im Original auf 22.10.2026 datiert. Die sichtbare erste Advisory-Seite zeigt im Zielzeitraum Katalogaufnahmen vom 09., 10. und 13.11., aber keinen zusätzlichen thematisch passenden Agentenbericht. Katalogaufnahme, CVE-Zuweisung, Berichtspublikation und neuer Patch sind unterschiedliche Ereignisse. Die NICCS-Kuration enthält Fremdmedien; ein neuer Suchsnippet auf dieser Seite wird nicht als neue CISA-Primärmeldung behandelt.[12] [13] [14]

Microsofts KI-gestützte Secret-Suche vom 05.11.2026 bleibt Vorwochennews. Auch die Monatsübersicht vom 05.11. und die EDÖB/BACS-Kampagne vom 16.10.2026 werden nicht künstlich neu datiert. Der November-Abschnitt in der geöffneten Microsoft-KI-Sicherheitsübersicht betrifft November 2025, nicht die aktuelle Woche.[15] [16] [17]

## Vormerkungen und bestehende Sperren

Für Artikel 09 «Schatten-KI» und Artikel 11 «Lieferantenrisiken» vormerken: Herkunft von Trainingsdaten und Modellen, Werkzeugrechte, unabhängige Schutzkontrollen und Datenflüsse mit den bestehenden Kontrollen abgleichen. Für Artikel 08 «IT-Sicherheitscheck» potenzielle KI-Befunde von fachlich bestätigten Ergebnissen und verifizierten Behebungen trennen. Die ältere NIST-Vormerkung vom 27.10. ist bei der vorgesehenen Artikelpflege als Vorschlag, nicht als Schweizer Norm, einzuordnen.

Die drei Meldungen liefern allgemeine Orientierung. Erreichbarkeit und gelesener Inhalt sind keine tatsächliche Einzelfallprüfung. Es erfolgten **keine CMS-/Browseroperationen, kein Zugriff auf Zugangsdaten, keine Artikeländerungen und keine Änderungen globaler Manifeste**. Fach-, Rechts-, Forensik-, Tenant- und Produktfreigaben bleiben ausgeschlossen. Offene KI-Anbieter-/Datenschutz- und Architekturprüfungen aus der Wartungsbasis und dem Vorwochenlaufstatus bleiben unverändert.

## Quellenprotokoll: Datum, Original-URL, Aussage und Einschränkung

Alle nachfolgenden Abrufzeiten sind tatsächliche Fetch-Rückgaben vom **15.11.2026 in CET**. Die Original-URLs stehen in den nummerierten Referenzen.

**[1] Microsoft – Trained to betray.** Publiziert 12.11.2026; Abruf 09:07:23. Aussage: Zwei Untersuchungen zu vergifteten Nachtrainingsdaten beziehungsweise Modell-Checkpoints und daraus folgenden Werkzeugaufrufen. Einschränkung: experimentelle Angriffsvoraussetzungen; Absicht und Wirkung einzelner öffentlich gefundener Datensatzzeilen ungeklärt; keine Standardprodukt-Schwachstelle nachgewiesen. Inline-Rückgabe gekürzt, alle verwendeten Abschnitte einschliesslich Einschränkungen und Schutzempfehlungen lesbar.

**[2] Microsoft Learn – Agenten-Echtzeitschutz.** Sichtbarer Stand 15.10.2026; Abruf 09:07:38. Aussage: Unterstützungsumfang, Preview-Pfade, erforderliche Integration und Audit-Standardregel. Einschränkung: keine neue Veröffentlichung im Newsfenster, keine konkrete Lizenz-/Tenant-/Wirksamkeitsprüfung.

**[3] ENISA – Publikationsseite Code Review.** Publiziert 12.11.2026; Abruf 09:06:13. Aussage: Datum, Zweck und Originaldownload. Einschränkung: Publikationsuhrzeit fehlt; Zusammenfassung allein ersetzt den Bericht nicht.

**[4] ENISA/CERT-EU – Original-PDF.** Dokumentdatum November 2026, Publikationstag durch [3]; Abruf 09:06:27, Schlussabschnitte gelesen 09:07:02. Aussage: 27 Codebasen, 220 potenzielle Befunde, 88 beurteilt, 95 Prozent bestätigte Teilmenge, vier CVE-IDs, keine Live-Tests, Isolation und menschliche Validierung. Einschränkung: laufende Beurteilung und fehlender Produktionskontext; keine neue Patchmatrix. Gekürzte Inline-Rückgabe durch die gespeicherte vollständige Extraktion für relevante Schlussabschnitte ergänzt.

**[5] Microsoft – FORGE Lab und Rust.** Publiziert 09.11.2026; Abruf 09:07:02, Schlussabschnitte gelesen 09:07:13. Aussage: Agentisch unterstützte Forschung, reproduzierte Bibliotheksfehler, unterschiedliche Fehler-/Fixstadien und anwendungsabhängige Wirkung. Einschränkung: kein universeller Fixbuild oder Angriffsnachweis; offene Einzelstände nicht vollständig nachgeprüft. Gekürzte Rückgabe gezielt durch Schlussabschnitte der vollständigen Extraktion ergänzt.

**[6] Rust Release Team – Announcing Rust 1.100.0.** Publiziert 12.11.2026; Abruf 09:07:22. Aussage: tatsächliche neue Version und Kern-Allocator-Stabilisierung. Einschränkung: nicht als universeller Sicherheitsfix aller in [5] erwähnten Fehler verwendet.

**[7] rust-lang/rust – Allocator-PR 156882.** Erstellt 24.05.2026, Zusammenführung im September, letzter sichtbarer Update 29.09.2026; Abruf 09:07:13. Aussage: Sicherheitsbedingungen des stabilisierten Allocator-Traits, unter anderem kein Unwinding aus Methoden oder Drop. Einschränkung: älterer Entwicklungs-/Designbeleg, keine neue Wochenmeldung; inline gekürzt, relevante Bedingungen lesbar.

**[8] rust-lang/rust – Release 1.100.0.** Originalmetadatum Published 12.11.2026 18:19:42 UTC; Abruf 09:07:38. Aussage: bestätigte Veröffentlichung und enthaltene Allocator-Stabilisierung. Einschränkung: keine vollständige Zuordnung aller Microsoft-Forschungsbefunde zu Fixversionen.

**[9] NIST – SI Agent Standards Initiative.** Erstellt 17.02.2026, aktualisiert 09.11.2026; Abruf 09:06:04. Aussage: Initiative für freiwillige Standards, Protokolle und Identitätsforschung. Einschränkung: materieller Änderungsvergleich fehlt; Aktualisierungsdatum allein ist keine neue Sachmeldung.

**[10] NIST – Design Tenets for Agent Identity Management Systems.** Publiziert 27.10.2026; Abruf 09:07:23. Aussage: zehn vorgeschlagene Identitäts-/Autorisierungsgrundsätze. Einschränkung: Altbestand, kein Schweizer Standard und keine neue KW-46-Meldung; neue Nutzerkommentare ändern das Publikationsdatum nicht.

**[11] NIST – RFI-Auswertung zu Agentensicherheit.** Publiziert 18.05.2026; Abruf 09:06:26. Aussage: Auswertung von Stellungnahmen. Einschränkung: alt; automatische Zitier-Abrufdaten sind keine Publikationsdaten. Sichtbare Created-/Updated-Metadaten sind widersprüchlich, die ausgewiesene Publikation liegt dennoch klar ausserhalb des Fensters.

**[12] CISA – Managing AI Token Consumption.** Publiziert 22.10.2026; Abruf 09:06:26. Aussage: Tokenverbrauch, Verfügbarkeit und Denial-of-Wallet/-Tokens. Einschränkung: alte Orientierung, keine neue Meldung.

**[13] CISA – Cybersecurity Alerts & Advisories.** Dynamische Liste; Abruf 09:06:13. Aussage: erste Seite mit Katalogaufnahmen vom 09., 10. und 13.11.2026. Einschränkung: begrenzte Liste, keine vollständige Ressourcenprüfung und keine Hersteller-Patchbelege.

**[14] CISA NICCS – News-Kuration.** Dynamische Liste; Abruf 09:06:15. Aussage: Links zu Fremdmedien und älteren CISA-Ressourcen. Einschränkung: Suchsnippet und geöffneter Text zeigen unterschiedlichen aktuellen Umfang; keine neue CISA-Originalforschung daraus abgeleitet. Rückgabe gekürzt, nicht für den Nachweis eines umfassenden Nichtfunds verwendet.

**[15] Microsoft – Agentische Secret-Suche.** Publiziert 05.11.2026; Abruf 09:07:23. Aussage: Originaldatum und KI-gestützte Suche nach exponierten Secrets. Einschränkung: Vorwoche, hier keine neue Meldung; ausgewählte Extraktionsabschnitte für Datierung/Abgrenzung verwendet.

**[16] EDÖB/BACS – Generative KI am Arbeitsplatz.** Publiziert 16.10.2026; Abruf 09:07:13. Aussage: Sensibilisierung zu Datenschutz- und Informationssicherheitsrisiken. Einschränkung: alter Kontext, keine Rechtsänderung oder Einzelfallprüfung.

**[17] Microsoft Learn – What's new in Microsoft AI security.** Sichtbarer Stand 06.05.2026; Abruf 09:06:04. Aussage: jüngster inhaltlicher Abschnitt April 2026; November-Abschnitt ist 2025. Einschränkung: begrenzte Übersicht, nicht Nachweis fehlender Neuigkeit auf anderen Microsoft-Kanälen.

**[18] Microsoft – Themenübersicht AI and agents.** Dynamische Übersicht; Abruf 09:06:26. Aussage: führt zum datierten FORGE-Original vom 09.11.; Monatsübersicht vom 05.11. Einschränkung: nicht alleiniger Kernbeleg und erfasst nicht alle Originalbeiträge; der Beitrag [1] wurde zusätzlich über verlinkten verwandten Inhalt gefunden.

**[19] ENISA – Publikationsübersicht.** Dynamische Übersicht; Abruf 09:06:04. Aussage: Code-Review-Bericht vom 12.11. Einschränkung: Beim allgemeinen Unionsbericht stehen sichtbare Datumsangaben 09./10.11. nebeneinander; er wurde hier nicht als weitere KI-Meldung aufgenommen.

## References

[1]: https://www.microsoft.com/en-us/security/blog/2026/11/12/trained-to-betray-how-post-training-supply-chain-attacks-hijack-coding-agents/ "Microsoft: Trained to betray – How post-training supply chain attacks hijack coding agents"
[2]: https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-real-time-protection "Microsoft Learn: Protect AI agents in real time using Microsoft Defender"
[3]: https://www.enisa.europa.eu/publications/joint-advisory-on-the-use-of-frontier-ai-models-for-code-review "ENISA: Joint Advisory on the Use of Frontier AI Models for Code Review"
[4]: https://www.enisa.europa.eu/sites/default/files/2026-11/ENISA_CERTEU_JOINTREPORT_Final.pdf "ENISA und CERT-EU: Originalbericht zu KI-gestützter Codeprüfung"
[5]: https://www.microsoft.com/en-us/security/blog/2026/11/09/forge-lab-uses-agentic-tools-to-identify-memory-safety-issues-in-rust/ "Microsoft: FORGE Lab uses agentic tools to identify memory safety issues in Rust"
[6]: https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/ "Rust Release Team: Announcing Rust 1.100.0"
[7]: https://github.com/rust-lang/rust/pull/156882 "Rust-Herstellerrepository: Stabilisierung des Allocator-Traits"
[8]: https://github.com/rust-lang/rust/releases/tag/1.100.0 "Rust-Herstellerrepository: Release 1.100.0"
[9]: https://www.nist.gov/super-intelligence/si-agent-standards-initiative "NIST: SI Agent Standards Initiative"
[10]: https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems "NIST: Design Tenets for Agent Identity Management Systems"
[11]: https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-considerations-ai "NIST: RFI-Auswertung zu Sicherheitsfragen bei KI-Agenten"
[12]: https://www.cisa.gov/resources-tools/resources/managing-ai-token-consumption-operational-resilience "CISA: Managing AI Token Consumption for Operational Resilience"
[13]: https://www.cisa.gov/news-events/cybersecurity-advisories "CISA: Cybersecurity Alerts and Advisories"
[14]: https://niccs.cisa.gov/news-events/news "CISA NICCS: Kuratierte News"
[15]: https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/ "Microsoft: Threat actors use agentic AI tooling to find and abuse exposed secrets"
[16]: https://www.edoeb.admin.ch/de/csm-generative-ki-arbeitsplatz-datenschutzherausforderungen "EDÖB und BACS: Generative KI am Arbeitsplatz – Datenschutzherausforderungen"
[17]: https://learn.microsoft.com/en-us/security/security-for-ai/whats-new "Microsoft Learn: What's new in Microsoft AI security"
[18]: https://www.microsoft.com/en-us/security/blog/topic/ai-and-machine-learning/ "Microsoft Security Blog: AI and agents"
[19]: https://www.enisa.europa.eu/publications "ENISA: Publikationsübersicht"
