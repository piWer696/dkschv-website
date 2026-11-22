# DKSchV CMS-Zugangsstatus – 22. November 2026

**Rein lesender Browsertest am 22. November 2026 um 09:04 CET, Europe/Zurich:** Der Sandbox-Browser wurde auf `https://www.webador.de/v2/website/6004383/pages` geführt und auf `https://www.webador.de/anmelden?redirect=/v2/website/6004383/pages` umgeleitet. Kein authentifizierter Projekteditor wurde geöffnet. Der [gespeicherte Seitentext](../../../../page_texts/www.webador.de_anmelden_redirect__v2_website_6004383_pages.md) liegt ausserhalb des Lieferpakets; das beobachtete Ergebnis ist hier vollständig beschrieben.

Die lesende Konfigurationsprüfung ergab keinen passenden Webador-Eintrag. My Browser ist als Einstellung aktiviert, aber für diese Ausführung nicht als verbundene Sitzung verwendet; der lokale Browser bleibt übersprungen. Gespeicherte Anmeldereferenzen sind in dieser Ausführungsumgebung nicht zugreifbar. Das ist keine Aussage darüber, ob der Benutzer andernorts Zugangsdaten hinterlegt hat.

**Live-Synchronisierung: blockiert.** Keine Anmeldung eingereicht, keine Browserübernahme angefordert, keine Konfiguration geändert, kein geschützter Import gestartet und kein Beitrag veröffentlicht oder im Editor geändert. Die bereits vorhandenen öffentlichen Seiten belegen keine Fachfreigabe oder heutige Editorberechtigung. Ihre Zuordnung zum historischen Webador-Projekt und das tatsächliche zuständige Hosting-/CMS-Ziel sind weiterhin nicht verifiziert.

## Öffentliche Erreichbarkeit und Schutz

Der [Pfadtest](public-link-check.csv) und die [Live-Zielzuordnung](public-target-map.csv) liefen am 22. November von 09:04:03 bis 09:04:42 CET. Der Pfadtest umfasst nach den lokalen Linkkorrekturen vom 15. November **25 Ziele: 13 HTTP 200 und 12 HTTP 404**. Die geringere Zielzahl gegenüber der Vorwoche ist keine neue Website-Reparatur, sondern folgt aus dem aktuellen lokalen Prüfumfang. Alle zwölf Artikel-Slugs sind HTTP 200, die zwölf ursprünglichen logischen Ressourcen-Slugs unter `/resources/` HTTP 404. Die 13. erfolgreiche Adresse des Pfadtests ist `/kontakt`.

Getrennt geprüft wurden die tatsächlich auf den Artikelseiten verlinkten zwölf Ressourcen unter `/wissen/resources/<Dateiname>.html` und drei Serviceziele im Website-Root: **15 HTTP 200**. Ein HTTP-Status bestätigt weder fachliche Richtigkeit noch Freigabe, Zugangsschutz oder einen erfolgreichen CMS-Import.

Der [normale GET ohne Credentials](public-article-exposure.json) auf `https://www.dkschv.ch/wissen/backup-wiederherstellung-testen` um 09:04:49 CET liefert HTTP 200 und rund **26.800 Zeichen** lesbaren Text. Enthalten sind weiterhin Kunden-Login-/Mandantenhinweise, eine Fachprüfungswarnung sowie Wiederherstellungs- und Forensikmerkmale. Es wurden 16 Abschnittsüberschriften und 15 externe Links gezählt; die Linkzahl ist kein Quellenvalidierungsergebnis. Ein wirksamer serverseitiger Schutz für diesen ausgelieferten Inhalt ist damit weiterhin nicht nachgewiesen. Keine Sperre wurde umgangen; keine Passwortwerte, Zugangsdaten oder Skriptgeheimnisse wurden untersucht oder gespeichert.

Die Antwort nennt `Last-Modified: Sun, 15 Nov 2026 09:54:05 GMT`. Das unterscheidet sich vom Header der Vorwoche und deutet auf eine spätere Bereitstellung hin, identifiziert aber weder Änderung, Autor noch Deployment-Verantwortung. Die erfassten Textmerkmale enthalten Datumsverweise auf den 1. und 15. November; daraus folgt keine vollständige lokale/live Inhaltsgleichheit. Der heutige Lauf hat keine Live-Änderung vorgenommen.

**Termine und Freigaben:** Artikel 01–08 sind terminlich fällig; Artikel 08 seit 19. November. Artikel 09–12 sind noch nicht fällig, aber ebenfalls unter den geprüften Slugs erreichbar. Alle zwölf lokalen Artikel samt Ressourcen bleiben nicht freigegebene Entwürfe mit offenen Fachmarkern. Die aktuelle öffentliche Erreichbarkeit ist keine Zustimmung zu deren Bereitstellung.

**Live-Änderungsprotokoll:** Keine erfolgreichen Live-Änderungen in diesem Lauf.
