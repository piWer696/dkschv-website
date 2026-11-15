---
titel: "QA-Befund Microsoft-News"
datum: "01.11.2026"
berichtsfenster: "25.10.2026, 09:00 CET bis 01.11.2026, 09:00 CET, Europe/Zurich"
abrufstand: "01.11.2026, ca. 09:04–09:06 CET"
---

# Microsoft-News – QA-Befund vom 1. November 2026

Für das Nachrichtenfenster sind **zwei** neue, unmittelbar relevante Meldungen belastbar belegt. Die Auswahl ist keine Vollständigkeitszusage. Alle unten referenzierten Originalseiten wurden nach Ende des Fensters stateless abgerufen, tatsächlich am **01.11.2026 zwischen ca. 09:04 und 09:06 CET**. Die Abrufe belegen den dann sichtbaren Stand, nicht den minutengenauen historischen Wortlaut um 09:00 CET.

## Für das Newsfeld verwertbare Meldungen

### Microsoft Entra: eigener Telefonieanbieter für SMS und Voice ist ab 30.10. allgemein verfügbar

Microsofts am **30.10.2026** aktualisierte FAQ bezeichnet «Choose Your Own Telephony Provider» als ab diesem Datum **allgemein verfügbar** für Microsoft-Entra-ID-Workforce-Tenants in **global Azure**. Als auswählbare Anbieter nennt die FAQ Soprano, Telesign und Infobip. Die Lösung kann SMS und Voice über den gewählten Anbieter zustellen; unterschiedliche Anbieter je Kanal sind laut FAQ möglich. [1]

Die ebenfalls am 30.10. aktualisierte Einrichtungsanleitung konkretisiert, dass der Betrieb einen Workforce-Tenant, ein Azure-Abonnement mit gültiger Zahlungsmethode, einen über Microsoft Security Store bezogenen Anbieter und Berechtigungen für App-Registrierung, Azure-Ressourcen sowie die Authentifizierungsmethodenrichtlinie erfordert. Microsoft sieht zuerst einen Evaluationsmodus und danach eine schrittweise Verkehrsverlagerung vor. [2]

**Relevanz:** Dies ist der tatsächliche Herstellerbeleg, der die bisher nur angekündigte Konfigurationsmöglichkeit ersetzt. Er ist für die Einordnung des MFA-/Passkey-Themas relevant, aber keine Aufforderung zu einer Tenant-Änderung.

**Geltungsgrenzen und Unsicherheit:** Die Verfügbarkeit gilt nach der FAQ nur für Workforce-Tenants in global Azure, nicht für Microsoft Entra External ID oder Azure AD B2C. Regionale Abdeckung, Preise, Providervertrag, Azure-Kosten und die produktive Funktionsfähigkeit müssen je Anbieter und Tenant geprüft werden. Es wurde kein Kundentenant, keine Lizenz, kein Providervertrag und keine Zustellstrecke geprüft. Die ältere Übersichtsseite vom 23.09.2026 sagt noch, die Konfiguration sei «noch nicht» verfügbar und nennt nur eine Private Preview mit Soprano und Telesign; sie ist deshalb kein tragfähiger Nachweis für den Stand nach dem 30.10. Die neueren FAQ- und Einrichtungsseiten sind hier die spezifischeren Herstellerquellen. [1] [2] [3]

### Microsoft Security: Teams-Hilfesupport-Betrug als Einstieg in AD-CS-Zertifikatsmissbrauch

Microsoft Security Research veröffentlichte am **30.10.2026** die Untersuchung zweier menschlich gesteuerter Intrusionen. In beiden Fällen gaben sich Angreifer in Microsoft Teams als IT- oder Help-Desk-Personal aus und brachten Nutzer vor allem über Quick Assist dazu, interaktiven Fernzugriff zu genehmigen. Danach untersuchten sie Active Directory Certificate Services und missbrauchten entweder eine für ESC1 anfällige Zertifikatvorlage oder leiteten bei ESC8 NTLM-Authentisierung an AD-CS-Web-Enrollment weiter. [4]

Der Bericht grenzt ausdrücklich ab: Die Aktivität nutzte **keine Schwachstelle in Microsoft Teams**, sondern Social Engineering sowie unsichere oder zu weit gefasste AD-CS-Konfigurationen. Microsoft weist zudem darauf hin, dass ein für ein privilegiertes Benutzer- oder Computerkonto erlangtes Authentisierungszertifikat einen dauerhaften Zugangspfad schaffen kann; ein Passwort-Reset oder die Neuinstallation des zuerst betroffenen Geräts widerrufen ein ausgestelltes Zertifikat nicht automatisch. [4]

**Relevanz:** Die Meldung verbindet Teams-basierte Identitätstäuschung mit on-premises AD-CS- und privilegierten Identitätsrisiken. Sie ist damit eine substanzielle Identitätsmeldung, keine neue Entra-Produktfunktion und keine Aussage über eine konkrete Microsoft-365-Organisation.

**Geltungsgrenzen und Unsicherheit:** Der Herstellerbericht beschreibt zwei untersuchte Intrusionen und allgemeine Erkennungs-/Untersuchungshinweise. Er belegt weder eine kompromittierte eigene Teams-, Microsoft-365- oder Entra-Umgebung noch die Ausnutzbarkeit jeder AD-CS-Installation. Konkrete Alarmdaten, Zertifikatvorlagen, Berechtigungen, Ausschlüsse aus automatischer Eindämmung sowie Incident-Response-Schritte erfordern eine fachliche und umgebungsspezifische Prüfung. [4]

## Nicht als neue Microsoft-News aufgenommen

Der neue Security-Blogbeitrag vom **28.10.2026** zur CISO-Rolle im agentischen Umfeld ist eine allgemeine Branchen- und Handlungseinordnung. Er enthält keine konkret datierte neue Microsoft-365-/Entra-Funktionsfreigabe und wird deshalb nicht als eigene Produkt- oder Bedrohungsmeldung gezählt. [5]

Der Microsoft-Threat-Intelligence-Bericht vom **29.10.2026** über den KI-Einsatz nordkoreanischer Akteure enthält zwar unter anderem Hinweise auf Defender for Office 365 und das Beschränken von Device Code Flow in Entra. Sein Schwerpunkt ist jedoch die allgemeine KI-Nutzung staatlicher Akteure, nicht eine neue M365-/Entra- oder Identitätsfunktion. Er wird angesichts der Begrenzung auf höchstens drei und der nur indirekten Zuordnung nicht aufgenommen. [6]

Der Bericht zur manipulierten Claude-Code-Erweiterung vom **30.10.2026** betrifft laut Microsoft eine zeitlich begrenzte Verteilung im Cursor Marketplace; Microsoft Visual Studio Marketplace und npm `@anthropic-ai/claude-code` seien nicht betroffen. Der Bezug zu Microsoft 365 oder Entra ist nicht unmittelbar genug für dieses Newsfeld. [7]

Der bereits in den Vorwochennews behandelte Microsoft-Bericht zu Storm-0940 und kompromittierten ConnectWise-Anwendungsidentitäten datiert vom **21.10.2026** und liegt vor dem Nachrichtenfenster. Er wird nicht unverändert als neue Meldung wiederholt. [8]

## Quellenreichweite und Prüfung

Die Microsoft-Entra-Übersichtsseite «What’s new» wurde geöffnet, enthielt im sichtbaren aktuellen Abschnitt jedoch Monatsabschnitte nur bis Juni 2026. Aus ihrem fehlenden Oktober-Eintrag kann daher keine Aussage über das Nichtbestehen späterer Änderungen abgeleitet werden. [9]

Die Microsoft-Security-Blog-Archivseite für Entra wurde geöffnet. Sie wies im einschlägigen Bereich den Beitrag vom 28.10. und anschliessend den bereits bekannten ConnectWise-Beitrag vom 21.10. aus. Neuere, thematisch anders klassifizierte Security-Blogbeiträge wurden zusätzlich direkt geöffnet und einzeln abgegrenzt. Das Archiv ist keine lückenlose, ausschliessliche Indexierung aller Sicherheitsbeiträge mit mittelbarem Identitätsbezug. [10]

Die öffentlich zugängliche MSRC Security Update Guide-Übersicht wurde geöffnet. Der stateless Abruf lieferte im relevanten Auszug unter anderem Release-Daten vom 13. und 22.10.2026, aber keinen belastbaren neuen, zwischen dem 25.10. und 01.11. datierten M365-/Entra-/Identitätseintrag. Wegen der dynamischen Filter-/Auszugdarstellung ist dies kein Vollständigkeitsnachweis über das gesamte MSRC-Angebot. [11]

Die Microsoft-Developer-Changelog-Seite wurde ebenfalls geöffnet, lieferte stateless aber nur eine JavaScript-Ladehülle («Loading…», «No updates found.»). Diese technische Leere wird nicht als fehlende Rechts- oder Produktfassung und nicht als Gegenbeleg zur aktuellen Learn-FAQ gewertet.

Der Befund ersetzt keine Sicherheits-, Fach-, Rechts- oder Tenantfreigabe. Es wurden keine Konten, Richtlinien, Apps, Provider, Lizenzen oder Telefoneinstellungen verändert.

## References

[1]: https://learn.microsoft.com/en-us/entra/identity/authentication/phone-providers-faq "Microsoft Learn – Frequently asked questions about Choose Your Own Telephony Provider, last updated 30.10.2026"
[2]: https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-set-up-sms-voice-api "Microsoft Learn – Set up SMS and voice, last updated 30.10.2026"
[3]: https://learn.microsoft.com/en-us/entra/identity/authentication/concept-phone-providers "Microsoft Learn – Choose a telephony provider for SMS and voice authentication, last updated 23.09.2026"
[4]: https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/ "Microsoft Security – From help desk impersonation to AD CS abuse, 30.10.2026"
[5]: https://www.microsoft.com/en-us/security/blog/2026/10/28/the-cisos-evolving-role-protecting-and-defending-in-the-agentic-era/ "Microsoft Security – The CISO’s evolving role, 28.10.2026"
[6]: https://www.microsoft.com/en-us/security/blog/2026/10/29/tracking-ai-adoption-in-north-korean-threat-actor-tradecraft/ "Microsoft Security – Tracking AI adoption in North Korean threat actor tradecraft, 29.10.2026"
[7]: https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/ "Microsoft Security – Malicious Claude Code-branded Cursor extension, 30.10.2026"
[8]: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/ "Microsoft Security – Storm-0940 ConnectWise supply-chain compromise, 21.10.2026"
[9]: https://learn.microsoft.com/en-us/entra/fundamentals/whats-new "Microsoft Learn – Microsoft Entra releases and announcements"
[10]: https://www.microsoft.com/en-us/security/blog/product/microsoft-entra/ "Microsoft Security Blog – Microsoft Entra archive"
[11]: https://msrc.microsoft.com/update-guide/vulnerability "Microsoft Security Response Center – Security Update Guide"
