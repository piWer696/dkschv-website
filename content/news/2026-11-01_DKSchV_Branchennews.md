---
titel: "DKSchV Branchennews KW 44"
datum: "01.11.2026"
status: "Redaktioneller Entwurf – nicht veröffentlicht"
zeitfenster: "25.10.2026, 09:00–01.11.2026, 09:00 CET"
tatsaechliche_abrufe: "01.11.2026, ca. 09:04–09:06 CET; alle hier verwendeten Originalquellen wurden nach 09:00 CET abgerufen"
---

# DKSchV Branchennews KW 44

**Redaktioneller Entwurf – nicht veröffentlicht.** Diese Auswahl priorisiert sechs belegte Entwicklungen für Schweizer KMU. Sie ist keine Vollständigkeits-, Betroffenheits-, Rechts- oder Freigabeaussage. Eine KEV-Aufnahme, eine Behördenmeldung oder ein Herstellerbericht belegt keinen Vorfall in der eigenen Umgebung.

## 1. PHP: Neue KEV-Aufnahme für zwei bereits behobene RCE-Lücken

CISA nahm CVE-2026-109618 und CVE-2026-109619 am 26. Oktober in den Katalog bekannter aktiv ausgenutzter Schwachstellen auf. PHP nennt für die betroffenen Web-Betriebsarten die bereinigten Releases 8.5.12, 8.4.27, 8.3.36 und 8.2.35; Distributionen können Fixes zurückportieren. Betreibende sollten deshalb Internet-exponierte PHP-Instanzen und eingebettete Komponenten erfassen und den tatsächlichen Paket- oder Hosting-Fixstand bestätigen lassen. Ein Update allein schliesst eine frühere Kompromittierung nicht aus. [1] [2]

## 2. Selbst betriebenes GitLab: KEV-Aufnahme einer Server-RCE

Für CVE-2026-97229 meldete CISA am 29. Oktober aktive Ausnutzung und nahm die Schwachstelle in KEV auf. GitLab nennt für selbst betriebene CE/EE-Installationen die korrigierten Linien 19.2.8, 19.3.5 und 19.4.2; GitLab.com und GitLab Dedicated waren laut Hersteller bereits gepatcht. Relevant ist somit insbesondere die bestätigte Version und Erreichbarkeit einer eigenen Instanz, nicht eine pauschale Aussage zu jeder GitLab-Nutzung. [1] [3]

## 3. Ivanti Connect Secure: Zwei weitere KEV-Einträge in einer Angriffskette

CISA ergänzte am 30. Oktober CVE-2026-111357 und CVE-2026-118527 und verknüpft beide mit CVE-2026-104935. Ivanti berichtet für die beschriebene Kette über Ausnutzung bei einer begrenzten Zahl Kunden und nennt 25.1.1.3 sowie 22.8R2.6 als bereinigte Versionen für die zwei neuen CVEs. Organisationen mit Connect Secure sollten Produktlinie, Hardware-/Softwarepfad, externe Erreichbarkeit und Herstellerfix gegen die konkrete Instanz abgleichen. [1] [4]

## 4. BACS: Gekaperte WhatsApp-Konten über gefälschte Abstimmungen

Das BACS berichtete am 27. Oktober über mehr als 50 Oktober-Meldungen zu gestohlenen oder manipulierten WhatsApp-Konten. Über kompromittierte Kontakte führen gefälschte Abstimmungen zur Eingabe eines Registrierungscodes oder zum QR-Scan für ein verknüpftes Fremdgerät. Für geschäftliche Kommunikation gilt: ungewöhnliche Anfragen über einen unabhängig bekannten Kanal prüfen, keine Verifizierungscodes weitergeben und keine QR-Codes unbekannter Webseiten scannen. Die Meldung schafft keine neue gesetzliche Meldepflicht. [5]

## 5. Microsoft: Help-Desk-Imitation als Weg zu AD-CS-Missbrauch

Microsoft beschrieb am 30. Oktober zwei untersuchte Intrusionen, bei denen sich Angreifer in Teams als Help Desk ausgaben, Fernzugriff bestätigen liessen und anschliessend unsichere AD-CS-Konfigurationen über ESC1 oder ESC8 ausnutzten. Laut Microsoft lag keine Teams-Schwachstelle vor. Das ist ein Anlass, Hilfeanfragen und privilegierte Fernzugriffe über etablierte Kanäle zu verifizieren sowie AD-CS-Konfigurationen fachlich zu überprüfen; es belegt keine Kompromittierung einer eigenen Microsoft-365-, Teams- oder Entra-Umgebung. [6]

## 6. KI-Sicherheit: NIST skizziert Agentenidentität und begrenzte Toolrechte

NIST veröffentlichte am 27. Oktober vorgeschlagene Gestaltungsgrundsätze für KI-Agenten: getrennte Agentenidentitäten, aufgabengebundene und zeitlich begrenzte Rechte, laufende Kontrolle von Tool-, API- und Ressourcenzugriffen sowie eine von der Modelllogik getrennte Berechtigungsentscheidung. Damit sollen nicht vertrauenswürdige Inhalte oder Prompt Injection keine Credentials manipulieren oder Rechte erweitern. Es handelt sich um freiwillige technische Orientierung, nicht um einen verbindlichen Standard oder eine Schweizer Rechtsvorgabe. [7]

## Redaktionelle Einordnung

Im geprüften Fenster ist keine neue materielle Änderung der einschlägigen Schweizer DSG-, DSV- oder ISG-Rechtsstände belegt. Für den nächsten News-Lauf am **8. November 2026** sollten vor allem neue Behörden-, Hersteller- und Rechtsmeldungen gegen diese Abgrenzung geprüft werden. Dieser Entwurf ist nicht veröffentlicht und enthält keine Produkt-, Lizenz-, Tenant-, Patch- oder Meldefristfreigabe.

## Quellen

[1]: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json "CISA – Catalog of Known Exploited Vulnerabilities JSON"
[2]: https://www.php.net/archive/2026.php "PHP – News Archive 2026"
[3]: https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/ "GitLab – Critical Patch Release 19.4.2, 19.3.5, 19.2.8"
[4]: https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935?language=en_US "Ivanti – Security Advisory Ivanti Connect Secure CVE-2026-104935"
[5]: https://www.bacs.admin.ch/de/26w43-de "BACS – Woche 43: Betrüger kapern erneut WhatsApp-Konten mit gefälschten Abstimmungen, 27.10.2026"
[6]: https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/ "Microsoft Security – From help desk impersonation to AD CS abuse, 30.10.2026"
[7]: https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems "NIST – Design Tenets for Agent Identity Management Systems, 27.10.2026"
