# News 03 – CISA KEV und Originalhersteller · 22. November 2026

**Drei belegte Kandidaten:** VMware vCenter, Synology DSM/BeeStation und LiteLLM. Neu ist jeweils die KEV-Aufnahme; bei vCenter erschien zusätzlich ein neues Herstelleradvisory. Die Synology- und LiteLLM-Fixes sind keine Neuveröffentlichungen dieser Woche. [1] [2] [3] [4]

Newsfenster: **15. November 2026, 09:00 CET bis 22. November 2026, 09:00 CET**, Europe/Zurich, ISO-KW 47. Die Originalquellen wurden am 22. November zwischen **09:04:11 und 09:05:06 CET** abgerufen. Diese tatsächlichen Befundzeiten liegen nach Redaktionsschluss; sie garantieren keinen historischen Seitenwortlaut um 09:00. KEV liefert `dateAdded` nur als Kalendertag. Im Abruf gibt es keine Aufnahme am 15. oder 22. November, sodass die fehlende Uhrzeit keine der ausgewählten Meldungen an die Fenstergrenze rückt. [1]

Die Vorwochennachrichten vom 15. November und das Pflegemanifest wurden lokal gelesen. Die Vollpflege fand am **15. November** statt; heute wurden nur dieser Newsbericht und zugehörige Quellenbelege geschrieben. Die 24 Entwürfe und die Manifeste bleiben unverändert. Keine Browser-, Login-, CMS- oder Liveaktion. Nächste Vollpflege: **29. November 2026, KW 48**.

## 1. VMware vCenter: neue Authentifizierungsumgehung jetzt in KEV

**Ereignis:** CISA nahm **CVE-2026-123890 am 20. November 2026** in KEV auf. Der Katalog beschreibt eine Authentifizierungsumgehung im VMware Directory Service: Ein nicht authentifizierter Angreifer mit Netzwerkzugriff auf vCenter kann unbefugten Systemzugang erlangen. Eine Aufnahme in KEV bestätigt Ausnutzung in freier Wildbahn, aber nicht ihren Beginn oder ein betroffenes Schweizer Unternehmen. Das Feld zur bekannten Verwendung in Ransomware-Kampagnen steht auf `Unknown`. [1] [11]

**Herstellerstand:** Broadcom veröffentlichte VMSA-2026-0009 am **19. November** und aktualisierte es am **20. November** auf VMSA-2026-0009.1. Der Änderungsvermerk der Aktualisierung betrifft die betroffenen VMware-Tools-Versionen, nicht einen erstmals an diesem Tag veröffentlichten vCenter-Fix. Broadcom nennt für CVE-2026-123890 keinen Workaround. Die vCenter-Matrix nennt **9.1.1.0200** für 9.1.x.x, **9.0.2.0200** für 9.0.x.x und **8.0 U3m** für die 8.0-Linie. Für vCenter 7.0 verweist sie bei bestehendem Extended-Support-Vertrag an den Support; für VCF 5.x auf **5.2.5**. Diese Herstellerstände gelten für die jeweilige Matrixzeile und sind keine allgemeine Sicherheitsgarantie. [3]

**Konkrete KMU-Bedeutung:** Bei eigener oder vom IT-Dienstleister betriebener VMware-Infrastruktur sollten Produktlinie, vCenter-Version, Netzwerkreichweite und passender Updatepfad belegt werden. Das Risiko betrifft die zentrale Verwaltung, nicht nur einzelne Arbeitsplatzgeräte. Ein aktueller Patch allein belegt nicht, dass eine mögliche vorherige Kompromittierung ausgeschlossen ist. KEV markiert hier forensische Triage nach der US-Vorgabe mit `Yes`. Die KEV-Frist **23. November** ist keine aus diesen Quellen ableitbare Schweizer gesetzliche Frist. [1] [3] [10]

**Unsicherheit und offene Fragen:** Keine Anlagenprüfung, kein konkreter Schweizer Vorfallnachweis, keine bestätigte Ransomware-Zuordnung. Die vier anderen CVEs im Sammeladvisory sind nicht allein durch die Aufnahme von CVE-2026-123890 ebenfalls als aktiv ausgenutzt belegt. Produktspezifische Supportberechtigung und Kompatibilität müssen im Einzelfall geklärt werden. Die Zusatz-FAQ bildet laut eigenem Stand noch die Erstfassung vom 19. November ab; für Versionen hat die neuere Advisory-Matrix Vorrang. [1] [3] [12]

**Vormerkung für den 29. November:** Artikel **08 – `/wissen/it-sicherheitscheck-kmu`**: KEV-Aufnahmedatum, Netzwerkexposition, Hersteller-Matrixzeile und verifizierten Patchstatus als getrennte Registerbelege prüfen. Artikel **11 – `/wissen/lieferantenrisiken-cybersecurity`**: Vom Dienstleister Nachweise für verwaltete vCenter-Instanzen, Zuständigkeit, Patchentscheidung und mögliche Vorfallabklärung vorsehen. Artikel **07 – `/wissen/backup-wiederherstellung-testen`** und **01 – `/wissen/ransomware-erste-60-minuten`**: Bei passender Zielarchitektur die Verwaltungsabhängigkeit und Übergabe an die Vorfalluntersuchung prüfen; nicht aus KEV automatisch einen konkreten Ransomwarefall ableiten.

**Abrufe:** KEV [1] um **09:04:11 CET**; Broadcom [3] um **09:04:29 CET**; Zusatz-FAQ [12] um **09:04:48 CET**.

## 2. Synology: ältere DSM-/BeeStation-Lücke neu als ausgenutzt priorisieren

**Ereignis:** CISA nahm **CVE-2024-10441 am 18. November 2026** in KEV auf. Synology beschreibt mögliche entfernte Codeausführung im System-Plugin-Daemon von **BeeStation OS vor 1.1-65374** sowie **DSM vor 7.2-64570-4, 7.2.1-69057-6 und 7.2.2-72806-1**. Neu ist das Priorisierungssignal für eine bekannte Lücke, nicht ein neues November-2026-Update. [1] [2]

**Herstellerstand:** Das Advisory wurde am **5. November 2024** veröffentlicht; die Kopfzeile nennt **28. März 2025** als letzte Aktualisierung und den Status `Resolved`. Der letzte Revisionseintrag trägt den 27. März 2025. Im Detailabschnitt stehen die genannten CVE-spezifischen Versionsgrenzen. Die gemeinsame Produktmatrix enthält zusätzlich Fixes für DSM 7.1 und 6.2 zu weiteren CVEs; sie wird deshalb nicht als pauschaler Nachweis verwendet, dass auch diese Linien von CVE-2024-10441 betroffen sind. [2]

**Konkrete KMU-Bedeutung:** Relevant für KMU, deren Dateiablage oder Sicherung auf Synology-Geräten beruht. Gerätetyp und Betriebssystem müssen getrennt erfasst und mit dem CVE-Detail abgeglichen werden. Ein NAS mit mehreren angeschlossenen Sicherungszielen ist nicht allein dadurch ransomware-resistent; die News ist ein Anlass, die eigene Exposition und den nachgewiesenen Firmwarestand zu priorisieren, nicht die bestehende Backup-Leitlinie neu zu datieren. [1] [2]

**Unsicherheit und offene Fragen:** Synology nennt keine konkreten Angriffsvektoren. Keine Geräteinventur oder Prüfung der Erreichbarkeit wurde durchgeführt. KEV nennt Ransomware-Kampagnennutzung `Unknown` und US-Triage `Yes`. Die KEV-Frist **21. November** wird nicht als Schweizer Frist ausgegeben. Eine frühere Ausnutzung wird durch das Einspielen eines Updates nicht rückwirkend ausgeschlossen. [1] [2] [10]

**Vormerkung für den 29. November:** Artikel **04 – `/wissen/ransomware-resistente-backups`**: Bei Synology-Einsatz den versions- und produktgenauen Herstellernachweis neben Trennung der Sicherungen prüfen. Artikel **07 – `/wissen/backup-wiederherstellung-testen`**: Wiederanlauf aus vertrauenswürdigem Stand und NAS-Abhängigkeit im konkreten Test berücksichtigen. Artikel **08 – `/wissen/it-sicherheitscheck-kmu`**: Aufnahme in KEV am 18. November getrennt vom alten Patchdatum dokumentieren. Artikel **11 – `/wissen/lieferantenrisiken-cybersecurity`**: Lieferantennachweis über Modell, BSM/DSM-Version und Updatezuständigkeit vormerken.

**Abrufe:** KEV [1] um **09:04:11 CET**; Synology [2] um **09:04:29 CET**. Synology nennt Publikations- und Aktualisierungszeiten in UTC+8; oben sind deren Kalendertage wiedergegeben.

## 3. LiteLLM: KEV-Aufnahme mit wichtiger Admin-Voraussetzung und Fixwiderspruch

**Ereignis:** CISA nahm **CVE-2026-40217 am 18. November 2026** in KEV auf. Das BerriAI-Advisory beschreibt einen Sandbox-Ausbruch beim Endpunkt `POST /guardrails/test_custom_code`: Präparierter Python-Code kann im Proxyprozess ausgeführt werden. Im Standard-Docker-Image läuft dieser Prozess laut Hersteller als root. **In Standardkonfigurationen ist zum Erreichen des Endpunkts eine Proxy-Admin-Zugangsinformation erforderlich.** Die kürzere KEV-Beschreibung darf nicht zu einer pauschalen Behauptung nicht authentifizierter Ausnutzung führen. [1] [4]

**Herstellerstand:** Das Advisory wurde am **7. Mai 2026** veröffentlicht; ein gesondertes Aktualisierungsdatum ist im Abruf nicht sichtbar. Die Kopfmetadaten nennen betroffene Versionen **ab 1.81.8 bis vor 1.83.10** und gepatchte Versionen **ab 1.83.10**. Der Patchabsatz sagt dagegen **1.83.11** und empfiehlt das Upgrade auf **1.83.11 oder später**. Dies wird nur als ausdrückliche Herstellerempfehlung wiedergegeben, nicht als unabhängig bestätigter universeller Fixbuild. Als Zwischenmassnahme nennt der Hersteller das Sperren dieses konkreten POST-Endpunkts am Reverse Proxy oder API-Gateway. [4]

Der verlinkte Release **v1.83.10-stable** stammt vom **27. April 2026, 17:01:01 UTC**. Sein abgerufener Text behandelt Signaturprüfung und verlinkt den Changelog; er bestätigt die CVE-Behebung nicht ausdrücklich und löst den Widerspruch zwischen 1.83.10 und 1.83.11 nicht. Auch dieser Release ist keine Nachricht der aktuellen Woche. [5]

**Konkrete KMU-Bedeutung:** Relevant für KMU und IT-Dienstleister, die LiteLLM als selbst betriebenen KI-Proxy oder Gateway einsetzen. Nicht jede Nutzung eines externen Chatdienstes ist damit betroffen. Zu prüfen sind tatsächlicher LiteLLM-Einsatz, Container-/Paketstand, Adminberechtigungen und Erreichbarkeit des Custom-Code-Endpunkts. Die Meldung zeigt zudem, warum eine als Guardrail bezeichnete Funktion selbst zur Angriffsfläche werden kann. [4]

**Unsicherheit und offene Fragen:** Fixmetadaten und Patchabsatz widersprechen sich; die genaue früheste korrigierte Version bleibt ohne zusätzlichen Herstellerbeleg offen. Keine Prüfung der eigenen Konfiguration, Secrets oder Logs. KEV belegt Ausnutzung, aber keine bestimmte lokale Angriffskette. Ransomware-Kampagnennutzung steht auf `Unknown`; die KEV-Frist **2. Dezember** ist keine Schweizer gesetzliche Frist. [1] [4] [10]

**Vormerkung für den 29. November:** Artikel **09 – `/wissen/schatten-ki-kmu`**: Für selbst betriebene KI-Gateways Werkzeug-/Adminrechte und Ausführungsisolation konkretisieren, sofern das Produkt in der Zielarchitektur vorkommt. Artikel **11 – `/wissen/lieferantenrisiken-cybersecurity`**: Vom Anbieter den tatsächlich verwendeten Gatewaystand und einen CVE-spezifischen Fixbeleg verlangen. Artikel **08 – `/wissen/it-sicherheitscheck-kmu`**: Den Versionswiderspruch als offenen Befund erhalten; nicht vorzeitig `behoben` setzen. Den Herstellerabsatz und die Fixmetadaten bei der Vollpflege erneut abgleichen.

**Abrufe:** KEV [1] um **09:04:11 CET**; BerriAI-Advisory [4] um **09:04:29 CET**; Release [5] um **09:05:04 CET**.

## Deduplikation und fortbestehende Vormerkungen

Der vollständige KEV-Abruf trägt **catalogVersion 2026.11.20**, **dateReleased 20. November 2026, 17:48:39.1516 UTC** und enthält neun `dateAdded`-Einträge seit dem 15. November: einen am 17., vier am 18. und vier am 20. November. Die drei oben ausgewählten Kandidaten sind nicht Gegenstand der Vorwochennachrichten. Die übrigen sechs Einträge betreffen Puppet Enterprise, Apache Axis, REDCap, Apache Roller, SAP NetWeaver und Cisco Expressway. Sie werden hier nicht zu zusätzlichen Nachrichten ausgearbeitet; daraus folgt keine Bestätigung ihrer Hersteller-Fixstände. Das ist eine begrenzte Auswahl, keine Vollprüfung aller neun Produkte. [1]

**Danfoss bleibt eine offene Vorwochenfrage, keine neue News:** Das CCB-Advisory nennt weiterhin **12. November 2026** als Veröffentlichung und letzte Aktualisierung. Es betrifft sechs zusätzliche Lücken im AK-SM800A bis einschliesslich 5.3.2. Der Hinweis zum fehlenden Patch bezieht sich ausdrücklich auf den damaligen Veröffentlichungsstand. Die erneut gelesene Danfoss-Seite nennt ein Paket **5.3.x vom Oktober 2026**, während die verlinkte Readme auf **SM800A-5.1.1.spk** führt. Keiner dieser Abrufe liefert einen spezifischen Behebungsnachweis für die sechs neuen CCB-Lücken. Es wird weder ein sicherer Fixbuild noch eine pauschale Entwarnung behauptet. [6] [7] [8]

Für **Artikel 07, 08 und 11** am 29. November vormerken: Modell-/Firmwarebeleg, sicheren Fernwartungsweg und Herstellerbeleg zu genau diesen sechs Lücken prüfen. Internetexposition und notwendige Überwachung mit Anlagenfachpersonen beurteilen. Das CCB warnt ausdrücklich, dass Firmwareupdate, geänderte Standardpasswörter und Strict Session Control allein exponierte Steuerungen nicht absichern. Nicht aus der alten Aussage `kein Patch damals` eine ohne erneuten Beleg aktuelle globale Patchlage machen. [6]

**SonicWall-Workaround ist alt:** SNWLID-2026-0014 nennt die Erstpublikation am **6. November** und die letzte Aktualisierung am **9. November**; die Revision 1.1 datiert die Workaround-Ergänzung ebenfalls auf den 9. November. Für CVE-2026-19868 beschreibt sie bei SAML-Nutzung und vorerst unmöglichem Upgrade das Deaktivieren oder Löschen aktiver LDAP-, RADIUS- und TACACS+-Authentifizierungsserver. Dieser Hinweis liegt vor dem Fenster und wird nicht als neue Meldung ausgegeben. Die Kopfzeile und der erste Revisionseintrag weichen beim Erstpublikationsdatum um einen Tag ab; der entscheidende Workaround-Termin ist eindeutig. [9]

Für **Artikel 08 und 11** am 29. November nur bei tatsächlichem SonicWall-Einsatz Konfiguration, passende Gen7-/Gen8-Updatezeile und betriebliche Abhängigkeiten prüfen. Keine pauschale Abschaltungsempfehlung und keine Änderung am Microsoft-365-Passkey-Artikel aus einer Firewallmeldung ableiten.

**Abrufe der Nachkontrollen:** CCB [6] **09:04:44 CET**; Danfoss-Softwareseite [7] **09:04:45 CET**; Danfoss-Readme [8] **09:05:06 CET**; SonicWall [9] **09:05:04 CET**. CISA-Katalogseite [11] **09:04:46 CET** und BOD 26-04 [10] **09:05:06 CET** wurden zur Einordnung von KEV und US-Fristen gelesen. Keine verlässlich datierte neue Danfoss- oder SonicWall-Änderung innerhalb des Fensters aus diesen Abrufen belegt.

## Gesicherte Belege und Grenzen

Der [vollständige KEV-Originalabruf](news03-evidence/cisa-kev-2026-11-22-090411-cet.json) und die [Hersteller- und Behördenauszüge mit Abrufzeiten](news03-evidence/originalquellen-auszuege.md) liegen im eigenen QA-Unterordner. Die Auszüge dokumentieren den tatsächlich gelesenen Stand; sie sind keine historische Wortlautgarantie. Keine wesentliche Quelle war unlesbar. Materiell offen bleiben der LiteLLM-Versionswiderspruch, die Danfoss-CVE-/Fixzuordnung und alle organisationsspezifischen Inventar-, Expositions- und Vorfallfragen. Heute keine Artikelpflege oder Fachfreigabe.

## References

[1]: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "CISA: Offizieller KEV-JSON-Katalog, catalogVersion 2026.11.20"
[2]: https://www.synology.com/en-global/security/advisory/Synology_SA_24_20 "Synology: SA-24:20 DSM und BeeStation, CVE-2024-10441"
[3]: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39495 "Broadcom: VMSA-2026-0009.1, vCenter, Tools und SDDC Manager"
[4]: https://github.com/BerriAI/litellm/security/advisories/GHSA-wxxx-gvqv-xp7p "BerriAI: Sandbox escape in custom-code guardrail, CVE-2026-40217"
[5]: https://github.com/BerriAI/litellm/releases/tag/v1.83.10-stable "BerriAI: LiteLLM Release v1.83.10-stable, 27. April 2026"
[6]: https://ccb.belgium.be/advisories/warning-six-new-danfoss-vulnerabilities-refrigeration-controllers-risk-immediate-action "CCB: Sechs neue Danfoss-Lücken, Stand 12. November 2026"
[7]: https://www.danfoss.com/en-us/service-and-support/downloads/dcs/adap-kool-software/ak-sm-800a/ "Danfoss: AK-SM 800A Softwareseite, Paketbezeichnung 5.3.x"
[8]: https://www.danfoss.com/en/service-and-support/downloads/dcs/adap-kool-software/ak-sm-800a/license-agreement/ "Danfoss: AK-SM 800A Readme und verlinkter Paketstand 5.1.1"
[9]: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014 "SonicWall PSIRT: SonicOS-Advisory mit Workaround-Revision vom 9. November 2026"
[10]: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk "CISA: BOD 26-04 und Geltungsbereich für US-Bundesbehörden"
[11]: https://www.cisa.gov/known-exploited-vulnerabilities-catalog "CISA: KEV-Katalog und Verwendung zur Schwachstellenpriorisierung"
[12]: https://brcm.tech/vmsa-2026-0009-qna "Broadcom: VMSA-2026-0009 Questions and Answers, Stand der Erstfassung"
