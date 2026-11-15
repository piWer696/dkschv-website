# DKSchV-Blogautomation – Stand 15. November 2026, KW46

**Lokal erledigt:** Zwölf Artikel und zwölf Arbeitsmittel auf den tatsächlichen Quellenprüfstand 15. November 2026 gepflegt, Einzelberichte geschrieben, Metadaten und CMS-Importmanifest synchronisiert, alte Markdown-Linkziele in 14 Dateien auf verifizierte Live-Adressen korrigiert. [Paketvalidator](../reviews/2026-11-15/validator-ergebnis.txt): **0 Fehler, 0 Warnungen**. SEO-Felder, Slugs, Termine, ursprüngliche Fachmarker und historische Fach-/Rechtsfelder bleiben erhalten; materielle Arbeitsmittelrevisionen sind sichtbar abgeglichen.

Die [Sonntagsnews](../news/2026-11-15_DKSchV_Branchennews.md) priorisieren sechs aktuelle Themen: Outlook/Chromium, Kühlsteuerungen, ScreenConnect, vergiftetes Modellnachtraining, KI-Codeprüfung und KI-Fakeshops. Quellenzeit, Änderungen und sämtliche zwölf artikelweisen Blocker stehen im [Pflegebericht KW46](../reviews/2026-11-15/DKSchV_Pflegebericht_KW46.md).

## Aktuelle Live- und Schutzblocker

**CMS-Zugang nicht authentifiziert:** Der [Webador-Test](../reviews/2026-11-15/cms-zugangsstatus.md) vom 15.11. gegen 09:05 CET leitete auf den Login um. Gespeicherte Anmeldereferenzen sind in dieser Umgebung nicht zugreifbar. Die My-Browser-Einstellung ist aktiviert, aber keine verbundene Webador-Sitzung wurde genutzt. Aktuelles Hosting/CMS und die Zuordnung der neuen öffentlichen `.html`-Darstellung zum historischen Projekt DKSchV Pro sind nicht verifiziert.

**Öffentliche Bereitstellung entdeckt, nicht von diesem Lauf ausgeführt:** Alle zwölf Artikeladressen sind HTTP200. Der ursprüngliche Paket-Linktest liefert15×404 für alte Ressourcen-/Servicepfade; die [verlinkten neuen Ziele](../reviews/2026-11-15/public-target-map.csv) liefern200. Die tatsächlichen Zieladressen sind im lokalen Importmanifest getrennt erfasst. Ressourcen-Slugs bleiben logische Paket-IDs.

**Serverseitiger Schutz nicht nachgewiesen:** Der Wiederherstellungsartikel liefert trotz «Kunden-Login erforderlich» rund 22.200 Zeichen Text ohne Credentials. Der [strukturierte Abrufbefund](../reviews/2026-11-15/public-article-exposure.json) bestätigt umfangreiche Fachabschnitte in der Antwort. Die öffentliche Darstellung enthält weiterhin eine Fachprüfungswarnung. Artikel 08–12 sind bereits HTTP200, obwohl ihre geplanten Termine noch nicht erreicht sind. Eine Freigabe oder Herkunft dieser Bereitstellung wird nicht behauptet.

**Fach- und Quellenblocker:** Alle Einzelfall-Fachmarker bleiben offen. Nicht auslesbare Zusatzansichten und der kanadische generische HTTP403-Abruf bleiben artikelbezogen dokumentiert. Lokale Validierung, allgemeine Behördenempfehlungen, ein200-Status und ein verstrichener Termin ersetzen keine tatsächliche Fachfreigabe.

**Live-Synchronisierung BLOCKIERT:** Kein Editor geändert, kein geschützter Import gestartet, kein Beitrag veröffentlicht. Normale Webador-Änderungen würden sofort live gehen. Für spätere Änderungen sind der passende CMS-/Hostingzugang, Quellen- und Linkprüfung, alle zuständigen Fachfreigaben und die gewünschte serverseitige Zugangspolitik erforderlich.

## Aktiver Takt

Der am 15.11. rein lesend geprüfte Zeitplan **«DKSchV News und Blogpflege»** ist aktiv: sonntags 09:00, Zeitzone Europe/Zurich. Branchennews wöchentlich, zusätzliche Vollpflege in jeder geraden ISO-Woche. **Nächste News:** 22.11.2026, KW47. **Nächste Vollpflege:** 29.11.2026, KW48. Kein neuer Zeitplan und keine Änderung der Konfiguration.

Historisch wurden am 20.09. ein interaktiver Webador-Login und eine passwortgeschützte Testseite bestätigt. Der spätere Übernahmeversuch vom 25.10. war vom Benutzer als nicht ladend gemeldet worden. Diese Befunde beweisen weder einen heutigen Login noch eine wirksame Schutzkonfiguration der inzwischen anders dargestellten öffentlichen Inhalte.

**Live-Änderungsprotokoll dieses Laufs:** Keine Einträge. Entwürfe, Quellenjournal, Linkzuordnung und lokale QA sind aktualisiert; die öffentliche Bereitstellung wurde weder freigegeben noch verändert.
