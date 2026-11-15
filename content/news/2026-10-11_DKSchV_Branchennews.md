---
titel: "DKSchV-Branchennews"
status: "Redaktioneller Entwurf – nicht veröffentlicht"
datum: "11.10.2026"
berichtsfenster: "04.10.2026, 09:00 bis 11.10.2026, 09:00 Europe/Zurich"
recherchehinweis: "Quellenabrufe am 11.10.2026 nach 09:00. Bei nicht versionierten Webseiten ist kein minutengenauer historischer Website-Stand belegt."
zielgruppe: "Schweizer KMU"
---

# DKSchV-Branchennews – Sonntag, 11. Oktober 2026

## FortiMail: Fixes jetzt verfügbar, Cloud bereits aktualisiert

Für die aktiv ausgenutzte Schwachstelle **CVE-2026-104286** hat Fortinet am **5. Oktober** den Fixstatus aktualisiert. Anders als in der Vorwochenausgabe sind die On-Premise-Fixes nicht mehr als «angekündigt» ausgewiesen: **8.0.2**, **7.6.7** und **7.4.9**, jeweils oder höher im passenden Versionszweig. Für den betroffenen 7.2-Zweig ist die Migration auf einen abgesicherten höheren Zweig erforderlich; nicht einfach auf irgendeine ältere 7.4-Version wechseln. FortiMail Cloud wurde laut Hersteller am 5. Oktober auf 7.6.7 GA beziehungsweise 8.0.2 GA aktualisiert; die Klarstellung erschien am 7. Oktober. [1]

**Für KMU:** Betriebsmodell und Softwarestand prüfen und selbst betriebene Geräte auf den passenden Fixstand bringen. Bis dahin nennt Fortinet als Massnahmen das Deaktivieren von IBE oder das Sperren beziehungsweise Beschränken des Internetzugriffs auf Webmail. Hersteller-Logs und Kompromittierungsindikatoren prüfen. Die Cloud-Aktualisierung bestätigt weder die Sicherheit einer eigenen Appliance noch das Ausbleiben eines früheren Angriffs. [1]

## NetScaler: SAML-Konfiguration und aktuellsten Fixstand prüfen

CISA nahm **CVE-2026-88779** am **4. Oktober** neu in den Katalog bekannter aktiv ausgenutzter Schwachstellen auf. Der Speicherfehler kann einen Dienstausfall verursachen; betroffen sind NetScaler ADC/Gateway mit SAML-Service-Provider- oder SAML-Identity-Provider-Konfiguration. Die CISA-Fälligkeit vom 7. Oktober ist eine Vorgabe für US-Bundesbehörden, **keine Schweizer Rechtsfrist**. [2] [3]

Wichtig für die Aktualisierungsplanung: Citrix veröffentlichte am **8. Oktober** zusätzlich **CVE-2026-107406**, einen kritischen Speicherfehler mit möglicher Codeausführung oder Dienstausfall. Der Geltungsbereich hängt von SAML-Rolle und Build ab: Bei den zuletzt veröffentlichten Zwischenständen ist insbesondere SAML IdP betroffen; bei älteren Ständen auch SAML SP. Dieses neuere Bulletin nennt **14.1-73.46**, **13.1-64.29** und die entsprechenden FIPS-/NDcPP-Fixstände. Es wäre deshalb unzureichend, ohne Prüfung des neuen Bulletins nur einen Fix für die vorherige Lücke einzuplanen. Die neue CVE war im abgerufenen KEV-Katalog vom 8. Oktober **nicht** enthalten; daraus folgt keine Aussage, dass sie nicht ausgenutzt werden könnte. [3] [4]

**Für KMU:** Betreiberverantwortung, SAML-Rolle und Version abgleichen und gemeinsam mit dem IT-Dienstleister den neuesten geeigneten Hersteller-Fix planen. Keine pauschale Update-Anweisung ohne Prüfung von Versionszweig und Kompatibilität. [2] [4]

## BACS: Verdacht auf Schadsoftware nicht mit einem Beweis verwechseln

Der BACS-Wochenrückblick vom **6. Oktober** ergänzt die Vorwochenwarnung zu Infektionswegen um konkrete Hinweise für den Verdachtsfall. Ein langsames Gerät allein beweist keine Infektion. Unbekannte Erweiterungen, veränderte Einstellungen, auffällige Anmeldungen oder mehrere ungewöhnliche Beobachtungen rechtfertigen jedoch eine Untersuchung. Auch macOS ist betroffen; ein Virenscanner garantiert keinen vollständigen Schutz. [5]

**Für KMU:** Echte Sicherheitswarnungen prüfen, bei Geschäftsgeräten die IT informieren und eine Fachperson beiziehen. BACS empfiehlt bei bestätigter Infektion Neuaufsetzen und anschliessende Passwortwechsel. Das ist **kein Auftrag zum eigenmächtigen Reset** eines möglicherweise beweisrelevanten Geschäftsgeräts: Untersuchung, Sicherung und Wiederanlauf mit der zuständigen IT beziehungsweise Incident Response abstimmen. [5]

## KI und Oversharing: internen Dokumenten klare Grenzen setzen

Der BACS-Folgebeitrag vom **5. Oktober** nennt ein unbedacht in ein KI-Tool eingegebenes internes Dokument neben öffentlich geteilten Fotos oder Bordkarten als Beispiel für Oversharing. Kombinierte Informationen können personalisiertes Phishing, Identitätsdiebstahl und Betrug erleichtern. Das ist ein neuer Awareness-Beitrag der bestehenden Kampagne, **keine neue KI-Regulierung**. [6]

**Für KMU:** Vor KI-Eingaben klären, welche Dokumente und Datenkategorien im freigegebenen Dienst zulässig sind. Vertrauliche Unterlagen nicht ungeprüft hochladen. Im übrigen geprüften NIST-/CISA-KI- sowie Microsoft- und EU-Regulierungsfeld wurde keine weitere belastbare neue Wochenmeldung aufgenommen; das ist keine Vollständigkeitszusage.

## Redaktioneller Status

**ISO-Woche 41: keine vollständige Blogpflege heute.** Die zwölf Artikel und zwölf Arbeitsmittel bleiben auf dem Quellenstand ihrer letzten gezielten Prüfung vom **4. Oktober**; alle Fachprüfungsmarker sind erhalten. Für den nächsten Review am **18. Oktober (KW 42)** sind die neuen BACS-Hinweise zu Erstreaktion/Wiederherstellung und Oversharing vorgemerkt.

**Keine Veröffentlichung oder CMS-Änderung:** Für diesen Lauf ist kein authentifizierter Webador-Zugang verifiziert. Die bereits terminierten Artikel 01 und 02 bleiben nicht freigegeben; ihre vorgesehenen URLs liefern am 11. Oktober HTTP 404. Technische Paketprüfung: **0 Fehler, 0 Warnungen**, jedoch keine Fachfreigabe.

## Quellen

[1]: https://fortiguard.fortinet.com/psirt/FG-IR-26-175 "Fortinet PSIRT FG-IR-26-175 – Solution update 05.10.2026 und FortiMail Cloud clarification 07.10.2026"
[2]: https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697174 "Citrix – NetScaler Security Bulletin zu CVE-2026-88779"
[3]: https://www.cisa.gov/known-exploited-vulnerabilities-catalog "CISA – Known Exploited Vulnerabilities Catalog; Datensatzstand 08.10.2026"
[4]: https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697191 "Citrix – NetScaler Security Bulletin zu CVE-2026-107406, veröffentlicht 08.10.2026"
[5]: https://www.bacs.admin.ch/de/26w40-de "BACS – Woche 40: Mythen zu Schadsoftware und Massnahmen bei Verdacht auf eine Infektion, 06.10.2026"
[6]: https://www.bacs.admin.ch/de/csm26-s2-de "BACS – Cyber Security Month 2026: Oversharing – Wie viel geben wir über uns preis?, 05.10.2026"
