---
datum: "08.11.2026"
status: "Redaktioneller Entwurf – nicht veröffentlicht"
zeitfenster: "01.11.2026 09:00 bis 08.11.2026 09:00 CET"
zeitzone: "Europe/Zurich"
ausgabewoche: "ISO-KW 45"
tatsaechliche_abrufe_je_befund:
  01-schweiz: "08.11.2026: Originalquellen 09:04:17–09:05:29 CET; EHRA 09:04:28, EDÖB 09:04:58, Urteil 09:05:19; Urteilspassagen lokal gelesen 09:05:38 CET."
  02-microsoft: "08.11.2026: Recherche 09:04:06–09:05:04 CET; beide verwendeten Security-Blog-Originale 09:04:30, ergänzende Originalextraktion gelesen bis 09:05:04 CET."
  03-schwachstellen: "08.11.2026: Quellenrückgaben 09:04:12–09:05:11 CET; im übermittelten Befund keine Einzelzeiten je URL."
  04-ki: "08.11.2026: Suchantworten 09:04:13 und 09:04:30; erfolgreiche Fetch-Antworten 09:04:13–09:04:46 CET."
  05-eu: "08.11.2026: Fetch-Rückgaben 09:04:12–09:05:17; letzte Suchantwort 09:05:19 CET."
turnuspflege: "Keine in KW 45; nächste Prüfung 15.11.2026, KW 46."
---

# DKSchV-Branchennews: Sonntagsausgabe

Alle Quellenabrufe erfolgten nach Redaktionsschluss; ein minutengenauer historischer Seitenstand ist nicht belegt. Die Auswahl beruht ausschliesslich auf den vorliegenden geprüften Befunden.

## SonicWall: SAML-geschützter Fernzugang kann verwundbar sein

**6. November:** CISA nahm CVE-2026-19868 in den Katalog bekannter ausgenutzter Schwachstellen auf.[1] Die SSLVPN-Lücke betrifft aktivierte SAML-Anmeldung: Gültige Zugangsdaten einer alternativen Authentifizierungsmethode können SAML-Kontrollen und möglicherweise darüber erzwungene MFA umgehen. Für die aufgeführten Gen7-/Gen8-Plattformen nennt SonicWall 7.3.4-7013 beziehungsweise 8.2.3-8015 als Mindestfixstände.[2] **KMU-Prüfpunkt:** Modell, Build, Erreichbarkeit und SAML-Konfiguration mit dem IT-Dienstleister abgleichen; verdächtige Zugänge zusätzlich untersuchen. MFA allein schliesst Betroffenheit nicht aus.

## KI-gestützte Secret-Suche bedroht Anwendungsidentitäten

**5. November:** Microsoft beschreibt ARTEX-gestützte Suchen nach Secrets in öffentlichen GitHub-Repositories und Folgeangriffe auf Entra, Azure und Microsoft 365. Auch kompromittierte Multitenant-App-Credentials von Anbietern ermöglichten Zugriffe auf nachgelagerte Kundentenants; die Angriffe begannen vor dieser Ausgabewoche.[3] **KMU-Prüfpunkt:** Exponierte Secrets widerrufen oder rotieren und historische Nutzung sowie App-Berechtigungen untersuchen. Repository-Dateien zu löschen genügt nicht; bereits ausgestellte Tokens bleiben laut Quelle bis zum Ablauf gültig. Keine Schweizer Organisation ist als betroffen belegt.

## EHRA-Imitation: Datenaktualisierung als Phishing-Köder

**6. November:** Das BACS warnt vor angeblich notwendigen Handelsregister-Datenaktualisierungen im Namen des EHRA und empfiehlt, die Phishing-Nachrichten zu löschen.[4] Für KMU-Administration ist dies ein konkretes Sensibilisierungsbeispiel. **KMU-Prüfpunkt:** Unerwartete Behördenanfragen über selbst recherchierte offizielle Kontaktwege verifizieren, nicht über Links oder Kontaktdaten aus der Nachricht.

## Erkannte Phishing-Mails können durch Ausnahmen zugestellt werden

**5. November:** Microsofts neue Q3-Auswertung zeigt: Im September bestanden Overrides bei 63 Prozent der Nachrichten mit erfasstem Sicherheitsresultat im untersuchten Geschäftsservice-Spoofing-Bestand – nicht bei allen E-Mails. Die Zahlen belegen weder Öffnungen noch kompromittierte Konten.[5] **KMU-Prüfpunkt:** Breite Absenderfreigaben und Sicherheitsausnahmen fachlich prüfen, nicht unkontrolliert entfernen. Zahlungs- und Kontoänderungen unabhängig bestätigen. Die Daten sind keine gemessene Schweizer KMU-Inzidenz.

## Datenpanne: Technische Behebung ersetzt Information nicht automatisch

**6. November:** Der EDÖB publizierte zum Fall SkySale/apfelkiste.ch: Das Bundesverwaltungsgericht bestätigte die angeordnete Betroffeneninformation; das Urteil vom 8. April 2026 ist laut Behörde rechtskräftig. Neu ist die Mitteilung, nicht der Vorfall oder das DSG.[6] Das Urteil begründet keine allgemeine Pflicht zur öffentlichen Bekanntmachung; diese wird als mögliche Ersatzform im konkreten Fall behandelt.[7] **KMU-Prüfpunkt:** Technische Eindämmung und Informationsbedarf getrennt beurteilen; Adressaten und Informationsform rechtlich prüfen lassen.

## WordPress: KEV-Aufnahme für Upgrade-Schwachstelle

**3. November:** Neu im KEV ist CVE-2026-119977, eine nicht authentifizierte Codeausführung während vollständiger Core-Upgrades.[1] Der Fix 7.1.4 stammt bereits vom 28. Oktober; liniengenaue Backports sind dokumentiert.[8] **KMU-Prüfpunkt:** Mit dem Hoster die tatsächlich installierte Linie und ihren Fixstand bestätigen. Nicht pauschal jede Version unter 7.1.4 als verwundbar behandeln. Bei Auffälligkeiten frühere Upgradefenster untersuchen: Ein Update beseitigt nicht automatisch eine bereits erfolgte Kompromittierung.

## Vormerkung für 15. November · KW 46

 Keine zusätzliche eigenständige KI- oder EU-Regelwerksneuigkeit ist im begrenzten Lauf belegt. Die nächste Turnusprüfung umfasst Herstellerstände und KEV-Revisionen, App-Identitäten und Sicherheitsausnahmen sowie die getrennte Rechtsprüfung zur Betroffeneninformation. Artikel zu Schatten-KI bleiben ohne neue Freigabe.

 **Betriebsstatus:** Der lokale KW44-Metadatenabgleich ist nachgeholt; der Paketvalidator meldet 0 Fehler und 0 Warnungen. Webador zeigt weiterhin den Login. Der heutige HTTP-Linkchecker erhielt 403, nicht einen neuen 404-Nachweis. Keine Live-Änderung, kein geschützter Import und keine Veröffentlichung. Die genauen Sperren stehen im [Laufstatus](2026-11-08_DKSchV_Laufstatus.md).

 ## References

[1]: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "CISA: Known Exploited Vulnerabilities Catalog"
[2]: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014 "SonicWall: Advisory SNWLID-2026-0014"
[3]: https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/ "Microsoft: Threat actors use agentic AI tooling to find and abuse exposed secrets"
[4]: https://www.bacs.admin.ch/de/warnung-ehra-de "BACS: Warnung vor Phishing mit angeblicher EHRA-Datenaktualisierung"
[5]: https://www.microsoft.com/en-us/security/blog/2026/11/05/email-threat-landscape-q3-2026-trends-and-insights/ "Microsoft: Email threat landscape Q3 2026 – trends and insights"
[6]: https://www.edoeb.admin.ch/de/datensicherheitsverletzung-bundesverwaltungsgericht-bestaetigt-informationspflicht-der-onlineshop-betreiberin "EDÖB: Bundesverwaltungsgericht bestätigt Informationspflicht der Onlineshop-Betreiberin"
[7]: https://www.edoeb.admin.ch/dam/de/sd-web/ZjhZ9UBOprVL/Urteil%20BVGer%20A_3790_2024%20vom%208.%20April%202026%20betreffend%20Verf%C3%BCgung%20vom%2028.%20Mai%202024.pdf "Bundesverwaltungsgericht: Urteil A-3790/2024 vom 8. April 2026"
[8]: https://wordpress.org/documentation/wordpress-version/version-7-1-4/ "WordPress: Version 7.1.4 und Backports"
