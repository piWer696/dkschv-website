---
datum: "22.11.2026"
stand: "22. November 2026"
kalenderwoche: "KW 47"
status: "Redaktioneller Entwurf – nicht veröffentlicht"
autor: "Manus AI"
newsfenster: "15. November 2026, 09:00 Uhr bis 22. November 2026, 09:00 Uhr CET"
zeitzone: "Europe/Zurich"
befundzeiten:
  bacs_edoeb_fedlex: "22. November 2026, 09:04:15–09:05:33 Uhr CET"
  microsoft_entra: "22. November 2026, 09:04:10–09:05:35 Uhr CET"
  cisa_hersteller: "22. November 2026, 09:04:11–09:05:06 Uhr CET"
  ki_sicherheit_standards: "22. November 2026, 09:04:18–09:05:02 Uhr CET"
  eu_originalabrufe: "22. November 2026, 09:04:18–09:05:46 Uhr CET"
befundhinweis: "Tatsächliche Befundzeiten aus den Einzelberichten, nach Redaktionsschluss; keine Garantie des historischen Seitenwortlauts um 09:00 Uhr."
---

# DKSchV Branchennews · 22. November 2026

**Autor: Manus AI**

Neue Schwachstellenwarnungen treffen diese Woche auf Forschung zu KI-Sicherheitstests sowie Entwicklungen bei Passkeys und europäischen Produktnormen. Sechs ausgewählte Meldungen mit konkreten Prüfpunkten für Schweizer KMU.

## 1. Java4Shell: auch eingebettete Laufzeiten prüfen

**18. November:** Das BACS warnt vor CVE-2026-114938. Unter bestimmten Bedingungen ist Schadcodeausführung über das Netzwerk möglich, teilweise ohne Anmeldung. Sicherheitsupdates sind verfügbar; Oracle und OpenJDK veröffentlichten ihre Advisories am 17. November. [1] [2] [3]

**KMU-Relevanz:** Internetexponierte Anwendungen und zentrale Anmeldedienste priorisieren. Auch Java in Branchenlösungen, Geräten und Containern erfassen; vom Lieferanten produktbezogene Behebungsnachweise verlangen. Nach Updates Prozesse neu starten und die tatsächlich laufende Version verifizieren. [1]

**Unsicherheit:** Betroffenheit und Zielversion hängen von Distribution, Architektur und Anwendung ab. Nicht alle Java-Versionen sind pauschal betroffen. Ein Update beseitigt keine bereits erfolgte Kompromittierung. [1] [2] [3]

## 2. VMware vCenter: neue Lücke als ausgenutzt gelistet

**20. November:** CISA nahm CVE-2026-123890 in den Katalog bekannter ausgenutzter Schwachstellen (KEV) auf. Die Authentifizierungsumgehung im VMware Directory Service ermöglicht nicht authentifizierten Angreifern mit Netzwerkzugriff auf vCenter unbefugten Zugang. Broadcom veröffentlichte das Advisory am 19. November; ein vCenter-Workaround fehlt. [4] [5]

**KMU-Relevanz:** Eigene und extern verwaltete vCenter-Instanzen erfassen, Netzwerkreichweite begrenzen und die passende Hersteller-Matrixzeile für Updates heranziehen. Betroffen ist die zentrale Infrastrukturverwaltung. [5]

**Unsicherheit:** KEV belegt keinen Schweizer Vorfall und keine Ransomware-Zuordnung. Patchstatus und mögliche frühere Kompromittierung sind getrennt zu prüfen. Die US-KEV-Frist vom 23. November ist keine Schweizer gesetzliche Frist. [4]

## 3. KI-Sicherheitstests: Agenten können die Testumgebung erkennen

**16. November:** METR untersucht in einer Forschungsnotiz 19 Tests zur Regeltreue und 36 Fähigkeitstests. Ausdrücklich befragte Untersuchungsagenten konnten die Testarten zunehmend anhand künstlicher Umgebungen und auffälliger Köderaufgaben unterscheiden. [6]

**KMU-Relevanz:** Anbieter-Testberichte nicht als alleinigen Sicherheitsnachweis für den produktiven KI-Einsatz behandeln. Zusätzlich die Realitätsnähe der Tests und unabhängige Kontrollen für Datenzugriff und Werkzeugrechte prüfen. Das ist eine redaktionelle Ableitung, keine neue Pflicht. [6]

**Unsicherheit:** Gemessen wurde die Erkennbarkeit, nicht deren ursächlicher Einfluss auf das Verhalten. Die weniger intensiv geprüfte Forschungsnotiz belegt weder produktive Täuschung noch einen generellen Ausfall aller KI-Sicherheitstests. Die direkte Befragung kann Antworten beeinflussen. [6]

## 4. BACS: echte Personendaten machen Phishing glaubwürdig

**17. November:** Der neue BACS-Wochenbericht beschreibt angebliche PHP-Sicherheitsupdates als Köder für Website-Administrationszugänge sowie personalisierte Kreditkarten-Phishingmails mit Namen, Adressen und AHV-Nummern. [7]

**KMU-Relevanz:** Richtige Personendaten sind kein Echtheitsnachweis. Updates nur über offizielle Herstellerkanäle oder etablierte Administrationsprozesse beziehen; Dienste über bekannte, selbst aufgerufene Adressen öffnen. Nach einem Datenabfluss auch spätere Betrugsrisiken in Betroffeneninformation und Krisenkommunikation berücksichtigen. [7]

**Unsicherheit:** Die beschriebene Datenabflussinformation datiert vom 7. Oktober, die Phishingmails vom 24. Oktober. Das ist keine neu belegte Datenpanne dieser Woche. Die Verbindung zum früheren Abfluss wird als mutmasslich beschrieben; eine aktuelle KMU-Schadenquote fehlt. [7]

## 5. Entra: identitätsgeprüfte Passkeys in Vorschau

**17. November:** Microsoft kündigt «High assurance credentials» als Vorschau an. Passkeys lassen sich bei Onboarding, sensiblen Zugriffen und Kontowiederherstellung mit Identitätsprüfung verbinden. Diese ersetzt weder Anmeldung noch MFA oder Self-Service Password Reset. [8] [9]

**KMU-Relevanz:** Bei Erstregistrierung und Ersatz muss die richtige Person verifiziert werden, nicht nur ein starker Authenticator entstehen. Vor einem Pilotbetrieb Geräteprofile, Providerdatenflüsse, Lizenzierung und Notfallwege prüfen. [9]

**Unsicherheit:** Keine allgemeine Verfügbarkeit: Die Vorschau gilt nur für Microsoft Public Cloud. Bei vorgeschriebener Attestierung unterstützt TAP-freie Recovery-Registrierung laut Learn nur Android; iOS erhält weiterhin einen Temporary Access Pass. Nicht alle üblichen Conditional-Access-Kontrollen greifen. [9]

## 6. CRA: erste Normen, kein automatischer Konformitätsnachweis

**18./19. November:** Die Kommission datiert die erste CRA-unterstützende Normpublikation auf den 18. November. CEN-CENELEC meldet am 19. November EN 40000-1-1 zum Vokabular und EN 40000-1-2 zu Prinzipien, Produktrisikomanagement und Lebenszyklusaktivitäten. [10] [11]

**KMU-Relevanz:** Schweizer Hardware- und Softwareanbieter mit Produkten auf dem EU-Markt sollten Supportende, Risikoanalyse und Lieferantennachweise prüfen. Ein betrieblicher Sicherheitscheck ist keine Produktkonformitätsbewertung.

**Unsicherheit:** Dies ist eine Normungsentwicklung, kein neuer Gesetzesakt. CRA Artikel 27 verlangt für die Konformitätsvermutung eine Amtsblattreferenz und begrenzt sie auf erfasste Anforderungen. Eine solche Referenz ist hier nicht belegt; ihre sichere Abwesenheit ebenso wenig. Keine neue allgemeine Schweizer KMU-Pflicht folgt daraus. [12]

**Pflegevormerkung:** Keine Vollpflege in KW 47; die Entwürfe behalten Quellenstand **15. November 2026**. Nächste Vollpflege: **29. November 2026, KW 48** – mit Fokus auf Sicherheitscheck, Lieferantennachweise, Wiederherstellung, Phishingprävention, Passkey-Recovery und CRA-Abgrenzung.

## References

[1]: https://www.bacs.admin.ch/de/warnung-java-2-de "BACS: Java4Shell – Kritische Schwachstelle in Java, 18. November 2026"
[2]: https://www.oracle.com/security-alerts/cspunov2026.html "Oracle: Critical Security Patch Update Advisory – November 2026"
[3]: https://openjdk.org/groups/vulnerability/advisories/2026-11-17 "OpenJDK: Vulnerability Advisory vom 17. November 2026"
[4]: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "CISA: Offizieller KEV-JSON-Katalog, catalogVersion 2026.11.20"
[5]: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39495 "Broadcom: VMSA-2026-0009.1, vCenter, Tools und SDDC Manager"
[6]: https://metr.org/notes/2026-11-16-measuring-alignment-eval-tells/ "METR: Measuring alignment eval tells, 16. November 2026"
[7]: https://www.bacs.admin.ch/de/26w46-de "BACS: Woche 46 – Personalisiertes Phishing aufgrund von abgeflossenen Daten, 17. November 2026"
[8]: https://techcommunity.microsoft.com/blog/microsoft-entra-blog/ai-is-changing-access-see-how-microsoft-entra-helps-you-stay-ahead-/4556456 "Microsoft Entra: Ignite-Ankündigungen vom 17. November 2026"
[9]: https://learn.microsoft.com/en-us/entra/verified-id/high-assurance "Microsoft Learn: High Assurance und Vorschaugrenzen"
[10]: https://digital-strategy.ec.europa.eu/en/news/first-european-standard-published-support-cyber-resilience-act "EU-Kommission: Erste europäische Norm zur Unterstützung des CRA, 19. November 2026"
[11]: https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-11-19-cra-standards-en-40000-1-1-and-en-40000-1-2/ "CEN-CENELEC: Erste CRA-Normen EN 40000-1-1 und EN 40000-1-2 verfügbar"
[12]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847 "EUR-Lex: Cyber Resilience Act, Verordnung EU 2024/2847"
