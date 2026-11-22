# News 03 – gesicherte Belegauszüge

Die Zeiten sind tatsächliche Rückgabezeiten der Originalquellenabrufe am 22. November 2026 in Europe/Zurich, CET. Es handelt sich um Auszüge der Fetch-Rückgaben, nicht um revisionssichere historische Seitenkopien. Alle Quellen wurden ohne Browser, Anmeldung, Zustimmung oder Produktdownload gelesen. Der vollständige KEV-JSON-Abruf ist separat als `cisa-kev-2026-11-22-090411-cet.json` gespeichert.

## Synology – 09:04:29 CET

URL: https://www.synology.com/en-global/security/advisory/Synology_SA_24_20

Titel: Synology-SA-24:20 DSM PWN2OWN 2024

Wörtliche Auszüge:

> Publish Time: 2024-11-05 15:15:05 UTC+8
>
> Last Updated: 2025-03-28 09:15:30 UTC+8
>
> Status Resolved
>
> Improper encoding or escaping of output vulnerability in the system plugin daemon in Synology BeeStation OS (BSM) before 1.1-65374 and Synology DiskStation Manager (DSM) before 7.2-64570-4, 7.2.1-69057-6 and 7.2.2-72806-1 allows remote attackers to execute arbitrary code via unspecified vectors.

Die Produktmatrix nennt zusätzlich DSM-7.1- und DSM-6.2-Fixes, bezieht sich aber auf mehrere CVEs. Diese werden nicht als CVE-2024-10441-spezifische Betroffenheit übernommen. Die Kopfzeile nennt den 28. März 2025 als letzte Aktualisierung, während der letzte Revisionseintrag auf den 27. März 2025 datiert ist.

## Broadcom – 09:04:29 CET

URL: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39495

Titel: VMSA-2026-0009.1: VMware vCenter, Tools, and SDDC Manager updates address multiple vulnerabilities

Wörtliche Auszüge:

> Initial Publication Date 19 November 2026
>
> Last Updated 20 November 2026
>
> A malicious actor with network access to vCenter may exploit this issue to bypass authentication and gain unauthorized access to the system.
>
> Workarounds: None
>
> 2026-11-20 VMSA-2026-0009.1 Updated advisory to clarify the impacted VMware Tools versions.

Matrix 3a für CVE-2026-123890: vCenter 9.1.x.x → 9.1.1.0200; vCenter 9.0.x.x → 9.0.2.0200; vCenter 8.0 → 8.0 U3m; vCenter 7.0 → Kontakt zum Broadcom-Support bei Extended-Support-Vertrag; VCF 5.x → 5.2.5. Keine Übertragung dieser Stände auf ESX, Tools oder SDDC Manager.

Zusatz-FAQ abgerufen 09:04:48 CET: https://brcm.tech/vmsa-2026-0009-qna

> This document reflects VMSA-2026-0009, the initial advisory, published November 19, 2026.
>
> The VMSA will always be the source of truth for which products and versions are affected and the proper patches to keep your organization secure.

Der FAQ-Stand bildet noch die Erstfassung ab; die neuere Advisory-Matrix hat Vorrang. Die FAQ wird nicht als Fixbeleg für die am 20. November präzisierte Tools-Betroffenheit verwendet.

## BerriAI LiteLLM – 09:04:29 CET

URL: https://github.com/BerriAI/litellm/security/advisories/GHSA-wxxx-gvqv-xp7p

Titel: Sandbox escape in custom-code guardrail

Wörtliche Auszüge:

> jaydns published GHSA-wxxx-gvqv-xp7p May 7, 2026
>
> Affected versions >= 1.81.8, < 1.83.10
>
> Patched versions >= 1.83.10
>
> The POST /guardrails/test_custom_code endpoint runs user-supplied Python inside a hand-rolled sandbox. The sandbox can be escaped using bytecode-level techniques, allowing arbitrary code execution in the proxy process — which runs as root in the default Docker image.
>
> Reaching the endpoint requires a proxy-admin credential in default configurations.
>
> Fixed in 1.83.11. The hand-rolled sandbox has been replaced with RestrictedPython. Upgrade to 1.83.11 or later.
>
> If upgrading is not immediately possible, block POST /guardrails/test_custom_code at your reverse proxy or API gateway.

Die Kopfmetadaten nennen 1.83.10, der Patchabsatz 1.83.11. Keine eigenständige Auflösung dieses Widerspruchs durch Annahmen; Empfehlung als Herstellerempfehlung attribuieren. Kein sichtbares Aktualisierungsdatum im Advisory.

Release abgerufen 09:05:04 CET: https://github.com/BerriAI/litellm/releases/tag/v1.83.10-stable

> Published: 2026-04-27T17:01:01Z

Die Release-Rückgabe erläutert Cosign-Signaturen und verlinkt einen Changelog. Sie bestätigt in ihrem Text nicht ausdrücklich die CVE-spezifische Behebung und löst den Versionswiderspruch nicht.

## CCB Danfoss – 09:04:44 CET

URL: https://ccb.belgium.be/advisories/warning-six-new-danfoss-vulnerabilities-refrigeration-controllers-risk-immediate-action

Titel: Warning: Six New Danfoss Vulnerabilities - Refrigeration Controllers at Risk - Immediate Action Required!

Wörtliche Auszüge:

> Published : 12/11/2026
>
> Last update: 12/11/2026
>
> Affected versions: All up to and including 5.3.2
>
> CVE identifiers were pending at the time of publication, and coordinated disclosure with Danfoss was ongoing. No patches were available at that time.
>
> Updating firmware, changing default passwords, and enabling strict session control are insufficient on their own to secure internet-exposed controllers.

Die Aussagen zum fehlenden Patch beziehen sich auf den Stand der damaligen Warnung, nicht auf eine unabhängig bestätigte universelle Patchlage am 22. November.

## Danfoss – Softwareseite 09:04:45 CET; Readme 09:05:06 CET

URLs:

https://www.danfoss.com/en-us/service-and-support/downloads/dcs/adap-kool-software/ak-sm-800a/

https://www.danfoss.com/en/service-and-support/downloads/dcs/adap-kool-software/ak-sm-800a/license-agreement/

Belegauszüge:

> AK-SM 800A 5.3.x.spk (October 2026).

Die Readme trägt den Titel `AK-SM 800A software package Release 5.0.x Important readme`, erläutert zusätzliche R5.1.x-Hinweise und verlinkt unter `Ok (Proceed to download software package 5.x)` das Ziel `https://sm800a.danfoss.com/sw_shared/SM800A-5.1.1.spk`. Das Ziel wurde nicht angeklickt oder heruntergeladen. Beide Seiten enthalten im Abruf keinen konkreten Behebungsnachweis für die sechs im CCB-Hinweis genannten neuen Schwachstellen und kein verlässlich datiertes neues Release im Newsfenster.

## SonicWall – 09:05:04 CET

URL: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0014

Titel: SonicWall SonicOS Affected By Multiple Vulnerabilities

Wörtliche Auszüge:

> First Published 2026-11-06
>
> Last Updated 2026-11-09
>
> If SAML authentication is in use and upgrading the firmware is not possible, disable or delete any active LDAP, RADIUS, and TACACS+ authentication server configured on the firewall.
>
> Version 1.1 Date 09-Nov-2026 Description The Workaround section has been updated for “CVE-2026-19868 - SSLVPN Authentication Enforcement Vulnerability via Alternate Authentication Methods,” and the names in the Credit(s) section have been updated as requested by the external researcher.

Der erste Revisionseintrag nennt den 5. November, die Kopfzeile den 6. November als Erstpublikation. Der für die Deduplikation wesentliche Workaround-Eintrag ist eindeutig auf den 9. November datiert.

## CISA – Katalogseite 09:04:46 CET; BOD 26-04 09:05:06 CET

URLs:

https://www.cisa.gov/known-exploited-vulnerabilities-catalog

https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk

Wörtliche Auszüge:

> CISA maintains the authoritative source of vulnerabilities that have been exploited in the wild. Organizations should use the KEV catalog as an input to their vulnerability management prioritization framework.
>
> This directive refers to the systems to which it applies as “Federal Civilian Executive Branch” systems, and to agencies operating those systems as “Federal Civilian Executive Branch” agencies.
>
> Unless directed by the governing procurement contract, this Directive does not apply to contractors.

Der KEV-Katalog ist ein Priorisierungssignal; die darin genannten US-Fristen werden nicht als Schweizer gesetzliche Fristen dargestellt.
