---
titel: "QA-Bericht: Artikel und Arbeitsmittel 07 bis 12"
pruefdatum: 2026-09-20
pruefumfang: "Sechs Artikel und sechs zugehörige Arbeitsmittel"
status: "Redaktionell korrigiert; externe Fachprüfungen vor Veröffentlichung offen"
---

# QA-Bericht: Artikel und Arbeitsmittel 07 bis 12

## Gesamturteil

Die sechs Artikel und die sechs zugehörigen Arbeitsmittel wurden **vollständig gelesen, direkt überarbeitet und erneut strukturell geprüft**. Alle zwölf Dateien verfügen nun über ein einheitliches YAML-Frontmatter, eine klar ausgewiesene Suchintention beziehungsweise einen dokumentierten Zweck, Quellenstand, Autorenschaft beziehungsweise Arbeitsmittelstatus und den verbindlichen Hinweis **[FACHPRÜFUNG ERFORDERLICH]**. Die Artikel bleiben als Entwürfe gekennzeichnet. Es wird keine externe Prüfung behauptet.

Die Überarbeitung hat zeitabhängige Rechts- und Regulierungsbehauptungen mit amtlichen Primärquellen abgeglichen. Insbesondere wurden die Schweizer Cyber-Meldepflicht, die Meldefolge nach Artikel 24 DSG, die Anforderungen der Datenschutzverordnung, die BACS-Leitlinien zu Notfallkonzept, Krisenkommunikation und Lieferkette sowie NIS2 und DORA geprüft.[1] [2] [3] [4] [5] [6] [7] Der Status der NIS2-Umsetzung wurde präzisiert: Die Kommission verwies am 8. Juli 2026 vier Mitgliedstaaten wegen fehlender Notifizierung von Umsetzungsmassnahmen an den Gerichtshof; daraus folgt keine generelle Aussage über den Rechtsstand jedes EU-Mitgliedstaats.[8]

Die Endkontrolle ergab **0 Strukturfehler**. Sämtliche 21 lokalen Wissens- und Arbeitsmittelverweise verweisen auf vorhandene Dateien. Alle 39 eindeutigen Quellen-URLs wurden gegen die verlinkten Primärquellen geprüft; drei NIST-PDF-Endpunkte reagierten auf eine automatisierte `HEAD`-Abfrage mit Fehler, liessen sich jedoch über die Volltextabfrage lesen und inhaltlich validieren. Die 28 verbleibenden CMS-/Service-Links liegen ausserhalb dieses Dateipakets und müssen im Ziel-CMS vor Publikation aufgelöst werden.

## Prüfergebnis je Paar

| Nr. | Artikel und Arbeitsmittel | Redaktionelles Ergebnis | Wesentliche Korrekturen | Vor Veröffentlichung offen |
|---:|---|---|---|---|
| 07 | `07-backup-wiederherstellung-testen.md` und `07-restore-testprotokoll.md` | Korrigiert | Risikobasierten statt pauschal jährlichen Testtakt formuliert; RTO/RPO als organisationsspezifische Ziele belassen; Wiederanlauf, Offline-Unterlagen und Forensik an BACS/CISA ausgerichtet; Rechtsfolgen klar von der technischen Übung getrennt. | **[FACHPRÜFUNG ERFORDERLICH]** Technische Wiederanlaufannahmen, forensischer Ablauf und die Beurteilung eines echten Vorfalls. |
| 08 | `08-it-sicherheitscheck-kmu.md` und `08-risikoregister-vorlage.md` | Korrigiert | Suchintention ergänzt; Risikoregister konsequent als Entscheidungshilfe statt als Scan- oder Rechtsersatz eingeordnet; Vier-Wochen-Takt entfristet; Datenschutz- und Restrisikofragen als Einzelfallprüfung markiert. | **[FACHPRÜFUNG ERFORDERLICH]** DSG-Bezug, sektorale und vertragliche Anforderungen sowie organisationsspezifische Bewertungs- und Eskalationskriterien. |
| 09 | `09-schatten-ki-kmu.md` und `09-ki-nutzungsregel.md` | Korrigiert | Alle einschlägigen Rechtsaussagen mit Prüfmarkern versehen; «möglichem» durch «voraussichtlich hohem» Risiko bei der DSFA-Prüfung ersetzt; fixe Reviewfristen durch risikobasierten Review ersetzt; die nicht haltbare Zwei-Seiten-Druckzusage entfernt. | **[FACHPRÜFUNG ERFORDERLICH]** Datenflüsse, Geheimhaltung, Auftragsbearbeitung, Auslandbekanntgabe, DSFA und automatisierte Einzelentscheidungen. |
| 10 | `10-cyberangriff-kommunikation.md` und `10-holding-statement-vorlage.md` | Korrigiert | BACS-Kernbotschaften präzisiert: Sicherheits- und Verfügbarkeitsaussagen nur bei belastbarer Evidenz; Holding Statement ohne Entwarnung oder vorweggenommene Ursache; Behörden- und Betroffeneninformation vom allgemeinen Kommunikationsprozess getrennt. | **[FACHPRÜFUNG ERFORDERLICH]** EDÖB-/BACS-Meldung, Betroffeneninformation, Vertrags-, arbeits- und strafverfolgungsbezogene Aussagen im konkreten Vorfall. |
| 11 | `11-lieferantenrisiken-cybersecurity.md` und `11-lieferantenfragebogen.md` | Korrigiert | Verantwortlichkeit beim konkreten datenschutzrechtlich Verantwortlichen präzisiert; fixe jährliche Prüffrist durch risikobasiertes Intervall ersetzt; Arbeitsmittel direkt verlinkt; Fragebogen ausdrücklich ohne Freigabe- oder Sicherheitsgarantie gehalten. | **[FACHPRÜFUNG ERFORDERLICH]** Auftrags- und Unterauftragsbearbeitung, Auslandbekanntgaben, Geheimhaltung und Vertragsklauseln. |
| 12 | `12-nis2-dora-schweiz.md` und `12-nis2-dora-relevanzmatrix.md` | Korrigiert | Zeitabhängige NIS2-Aussage auf den konkret belegten Kommissionsstand vom 8. Juli 2026 begrenzt; starres 30/60/90-Tage-Schema durch Prioritätsstufen ersetzt; Matrix ausdrücklich als Erstorientierung ohne Unterstellungsentscheid oder Konformitätsbescheinigung ausgeführt. | **[FACHPRÜFUNG ERFORDERLICH]** Direkter NIS2-/DORA-Anwendungsbereich, nationales Umsetzungsrecht, EU-Vertretung und Kundenverträge. |

## Inhaltliche und quellenbezogene Qualitätssicherung

### Metadaten, Suchintention und E-E-A-T

Die sechs Artikel enthalten jetzt einheitlich **Slug, Meta-Title, Meta-Description, Hauptkeyword, Suchintention, Zielgruppe, Autor, Veröffentlichungsdatum, Quellenstand und fachlichen Prüfstatus**. Die Meta-Titel und -Beschreibungen blieben auf Suchintention und Schweizer KMU ausgerichtet. Produkt- oder Leistungszusagen wurden entfernt oder in zurückhaltende Kontakt-CTAs umformuliert. Die Arbeitsmittel erklären ihren Zweck, ihre Grenzen und ihren organisationsspezifischen Anpassungsbedarf.

Die E-E-A-T-Signale bestehen aus klarer Autorzuordnung, transparentem Entwurfs- und Quellenstand, konkreten hypothetischen Beispielen, offiziellen Primärquellen, nachvollziehbaren Begriffserklärungen sowie klarer Abgrenzung von Fachberatung. Rechts-, Datenschutz-, Forensik-, Vertrags- und EU-Regulierungsfragen sind nicht als abschliessend gelöst dargestellt.

### Rechtliche und zeitabhängige Aussagen

Die Schweizer Cyber-Meldepflicht ist auf den gesetzlichen Geltungsbereich und die Frist von 24 Stunden nach Entdeckung beschränkt. Die gesetzliche Grundlage erlaubt eine Ergänzung fehlender Angaben, sobald neue Informationen vorliegen; die BACS-Kommunikation nennt für die Vervollständigung 14 Tage.[1] [2] Die Texte vermeiden deshalb eine pauschale Pflicht für alle KMU.

Für Verletzungen der Datensicherheit wird korrekt zwischen der technischen Tatsache eines Vorfalls und der rechtlichen Meldeschwelle unterschieden. Artikel 24 DSG verlangt eine Meldung an den EDÖB so rasch als möglich, wenn ein voraussichtlich hohes Risiko für Persönlichkeit oder Grundrechte besteht. Betroffene Personen sind zu informieren, wenn dies zu ihrem Schutz erforderlich ist oder der EDÖB es verlangt.[3] Jede konkrete Schwellen- und Informationsbeurteilung ist in Artikel und Arbeitsmitteln markiert.

Die Aussagen zur Datensicherheit orientieren sich an der DSV: Schutzbedarf, Risiko und technische beziehungsweise organisatorische Massnahmen müssen bestimmt, während der Bearbeitungsdauer überprüft und bei Bedarf angepasst werden.[4] Die KI-Inhalte berücksichtigen, dass das DSG auf KI-gestützte Bearbeitungen von Personendaten direkt anwendbar ist und Transparenz über KI-Interaktion und mögliche Prompt-Verwendung wichtig ist.[5]

NIS2 und DORA sind voneinander sowie von Schweizer Recht getrennt. NIS2 bleibt eine Richtlinie, deren nationale Umsetzung und Durchsetzung je betroffenem Staat geprüft werden müssen. DORA enthält Anforderungen für Finanzunternehmen und für deren Management von IKT-Drittparteirisiken; eine Belieferung eines Finanzkunden macht einen Schweizer Anbieter nicht ohne Weiteres zu einem voll regulierten Finanzunternehmen.[6] [7]

### Arbeitsmittel ohne Garantieversprechen

Alle sechs Arbeitsmittel enthalten einen sichtbaren Fachprüfungsmarker und eine explizite Begrenzung. Sie bestätigen weder Rechtskonformität noch Datensicherheit, vollständige Risiken, Wiederherstellbarkeit, Verfügbarkeit oder die Rechtmässigkeit eines Einzelfalls. Die Bewertungsmatrizen und Checklisten unterstützen dokumentierte Entscheidungen; sie lösen keine automatischen Freigaben, Rechtsfolgen oder Meldepflichten aus.

### Quellen- und Linkformat

Alle geprüften Dateien verwenden die Überschrift **«Quellen»** und fortlaufende numerische Referenzdefinitionen im Format `[n]: URL "Titel"`. Der Abgleich ergab für jede Datei identische Mengen an zitierten und definierten Quellen. Die Artikel und Arbeitsmittel verlinken 21-mal auf innerhalb des Pakets vorhandene Inhalte. Die 28 Links zu Kontakt- und Dienstleistungsseiten konnten ohne CMS nicht technisch auf Erreichbarkeit geprüft werden; sie sind daher als Freigabepunkt vor dem Go-live dokumentiert.

## Verbleibende Freigabepunkte

> **[FACHPRÜFUNG ERFORDERLICH]** Die folgenden Punkte sind keine redaktionellen Restarbeiten. Sie benötigen vor öffentlicher Veröffentlichung eine echte externe oder zuständige interne Fachprüfung: die rechtliche Einordnung von Einzelfällen, Datenschutz- und Vertragsfragen, forensische Vorgehensentscheide, die konkrete technische Umsetzbarkeit sowie NIS2-/DORA-Anwendungsbereich und nationales EU-Umsetzungsrecht.

Vor dem Go-live müssen zudem die 28 CMS-/Service-Links im Zielsystem geprüft werden. Dies betrifft insbesondere `/kontakt` sowie die verlinkten Dienstleistungsseiten. Die 21 Links zu Artikeln und Arbeitsmitteln im vorliegenden Paket sind vorhanden und konsistent.

## Bearbeitete Originaldateien

| Typ | Dateien |
|---|---|
| Artikel | `articles/07-backup-wiederherstellung-testen.md`, `articles/08-it-sicherheitscheck-kmu.md`, `articles/09-schatten-ki-kmu.md`, `articles/10-cyberangriff-kommunikation.md`, `articles/11-lieferantenrisiken-cybersecurity.md`, `articles/12-nis2-dora-schweiz.md` |
| Arbeitsmittel | `resources/07-restore-testprotokoll.md`, `resources/08-risikoregister-vorlage.md`, `resources/09-ki-nutzungsregel.md`, `resources/10-holding-statement-vorlage.md`, `resources/11-lieferantenfragebogen.md`, `resources/12-nis2-dora-relevanzmatrix.md` |

## Quellen

[1]: https://www.fedlex.admin.ch/eli/oc/2024/257/de "Fedlex – Informationssicherheitsgesetz: Meldepflicht für Cyberangriffe auf kritische Infrastrukturen"
[2]: https://www.bacs.admin.ch/de/meldepflicht "BACS – Meldepflicht für Cyberangriffe auf kritische Infrastrukturen"
[3]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz, Artikel 24"
[4]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Datenschutzverordnung, Artikel 1 bis 3"
[5]: https://www.edoeb.admin.ch/de/update-geltendes-datenschutzgesetz-ist-auf-ki-direkt-anwendbar "EDÖB – Geltendes Datenschutzgesetz ist auf KI direkt anwendbar"
[6]: https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32022L2555 "EUR-Lex – Richtlinie (EU) 2022/2555 (NIS2)"
[7]: https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32022R2554 "EUR-Lex – Verordnung (EU) 2022/2554 (DORA)"
[8]: https://digital-strategy.ec.europa.eu/en/policies/nis-transposition "Europäische Kommission – NIS2-Umsetzung in EU-Mitgliedstaaten"
