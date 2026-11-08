---
status: Entwurf
slug: /wissen/schatten-ki-kmu
meta_title: "Schatten-KI im Schweizer KMU sicher steuern | DKSchV"
meta_description: "KI-Nutzung sichtbar machen, vertrauliche Daten schützen und klare Regeln schaffen: ein Praxisleitfaden für Schweizer KMU."
suchintention: "Informational – Schatten-KI risikobasiert steuern"
hauptkeyword: "Schatten-KI KMU"
zielgruppe: "Geschäftsleitungen und IT-Verantwortliche Schweizer KMU"
autor: "DKSchV Redaktion"
veröffentlichungsdatum: "26.11.2026"
stand: "1. November 2026"
quellenpruefung_umfang: "15 verwendete Primärquellen – alle Quellenreferenzen dieses Artikels und des zugehörigen Arbeitsmittels direkt geprüft; ergänzt um CISA- und kanadische Behördenorientierungen zu KI-Tokenverbrauch und agentischen Kontrollen"
quellenpruefung_status: "vollständig für 15/15 zitierte externe Originalquellen – am 1. November 2026 nach 09:00 Europe/Zurich erreichbar und inhaltlich abgeglichen; keine organisations-, anbieter- oder tenantbezogene Freigabe"
fachprüfung_status: "[FACHPRÜFUNG ERFORDERLICH]"
---

# Schatten-KI im Schweizer KMU: Generative KI sicher nutzen, ohne vertrauliche Daten preiszugeben

> **[FACHPRÜFUNG ERFORDERLICH]** Die Aussagen zu Personendaten, Geheimhaltung, Auftragsbearbeitung, Auslandbekanntgaben und Meldepflichten müssen vor Veröffentlichung durch Datenschutz- und Rechtsfachpersonen geprüft werden.

> **Kurzantwort:** Schatten-KI ist die nicht gesteuerte Nutzung von KI-Werkzeugen ausserhalb der festgelegten Prozesse. Ein pauschales Verbot löst das Problem selten. Wirksamer ist eine risikobasierte KI-Governance: Erfassen Sie Werkzeuge und Anwendungsfälle, ordnen Sie Daten in verständliche Klassen ein und definieren Sie erlaubte, freigabepflichtige und untersagte Nutzungen. Geben Sie nur geprüfte Werkzeuge frei und schützen Sie sie mit zentralen Identitäten, geringsten Berechtigungen, Protokollierung und Regeln gegen Datenabfluss. Wenn vertrauliche Daten bereits in einen Prompt gelangt sind, behandeln Sie dies als möglichen Sicherheitsvorfall: Nutzung stoppen, Fakten sichern, Auswirkungen beurteilen und Meldepflichten fachlich prüfen. So bleibt nützliche KI möglich, ohne die Kontrolle über Daten und Entscheidungen zu verlieren.[1] [2]

Generative KI erzeugt aus Eingaben, sogenannten **Prompts**, Text, Bilder, Code oder Zusammenfassungen. Sie kann Entwürfe strukturieren, öffentliches Wissen zusammenfassen oder Formulierungsvorschläge erstellen. Das Risiko beginnt, wenn Mitarbeitende Inhalte aus E-Mails, Kundendossiers, Personalakten, Verträgen, Quellcode oder Sitzungsnotizen in einen nicht freigegebenen Dienst kopieren.

**Schatten-KI** bezeichnet genau diese nicht sichtbare oder nicht geregelte Nutzung. Sie ist kein Beweis für Fehlverhalten einzelner Mitarbeitender. Meist zeigt sie, dass ein Arbeitsschritt Zeit kostet und eine sichere, praxistaugliche Alternative fehlt. Die Geschäftsleitung muss deshalb nicht jede KI-Idee vorweg verbieten. Sie muss entscheiden, welche Risiken akzeptabel sind, wer Ausnahmen bewilligt und wie sich diese Entscheide nachweisen lassen.

Dieser Beitrag zeigt eine umsetzbare Orientierung für Schweizer KMU. Er ersetzt keine individuelle Rechtsberatung. **[FACHPRÜFUNG ERFORDERLICH]** Personendaten, Berufs- oder Geschäftsgeheimnisse, Auslandbekanntgaben, Auftragsbearbeitung und ein möglicher Vorfall sind im konkreten Sachverhalt durch zuständige Fachpersonen zu beurteilen.

## Warum ein Verbot allein Schatten-KI nicht beendet

Ein Verbot kann für besonders kritische Daten oder nicht freigegebene Dienste notwendig sein. Ohne sichere Werkzeuge und einen kurzen Freigabeweg weichen Mitarbeitende jedoch auf private Konten, Browser-Erweiterungen oder kostenlose Dienste aus. Das Unternehmen verliert den Überblick über Datenflüsse, Verträge, Zugriffsrechte und Nachweise.

Das BACS nannte am 5. Oktober 2026 ein unbedacht in ein KI-Tool eingegebenes internes Dokument als Beispiel für Oversharing. Kombinierte Informationen können laut BACS personalisiertes Phishing, Identitätsdiebstahl oder gezielten Betrug erleichtern.[10]

Am 16. Oktober 2026 konkretisierten EDÖB und BACS in einer gemeinsamen Kampagne die Risiken generativer KI am Arbeitsplatz. Der EDÖB hebt dabei Kundinnen und Kunden, Patientinnen und Patienten sowie Mitarbeitende hervor, deren Daten in Eingaben betroffen sein können. Die Kampagne bekräftigt die Anwendung des bestehenden DSG; sie führt keine neue gesetzliche Pflicht oder Frist ein. [11]

Der passende Gegenentwurf ist **KI-Governance**: Rollen, Regeln, Freigaben und Kontrollen für die KI-Nutzung. Das freiwillige NIST AI Risk Management Framework bietet eine brauchbare Denkstruktur. Sein Profil für generative KI empfiehlt Nutzungsbedingungen, relevante Rollen sowie Kriterien für das Erfassen und Melden von Vorfällen.[4]

Für ein KMU genügt zunächst: **sehen, entscheiden, schützen, überprüfen**. Führen Sie diesen Kreislauf im [Cyber-Risikomanagement](/unsere-dienstleistungen/risikomanagement); dort gehören auch bewusst akzeptierte Restrisiken hin.

### Hypothetisches Praxisbeispiel: Der hilfreiche Prompt wird zum Datenfluss

Ein hypothetisches Schweizer Dienstleistungs-KMU möchte eine komplizierte Kundenanfrage schneller beantworten. Ein Mitarbeitender kopiert den E-Mail-Verlauf inklusive Namen, Vertragsdetails und interner Preisargumentation in ein frei zugängliches KI-Werkzeug. Die Antwort ist sprachlich gut. Niemand weiss jedoch, welches Konto verwendet wurde, ob der Inhalt gespeichert oder weiterverarbeitet werden kann und wer im Unternehmen die Nutzung bewilligt hat.

Das Problem ist nicht die Zusammenfassung als Aufgabe. Das Problem sind fehlende Regeln für Datenklasse, Werkzeug, Zweck und Freigabe. Eine sichere Alternative könnte mit einem freigegebenen Dienst, einem geschäftlich verwalteten Konto und einer vorher anonymisierten Fallbeschreibung arbeiten. Ob diese Alternative im Einzelfall datenschutz- und vertragskonform ist, hängt von Datenfluss und Vertrag ab und muss bei Personendaten fachlich geprüft werden.[2]

## DSG: Datenbearbeitung bleibt auch mit KI Datenbearbeitung

Das Schweizer Datenschutzgesetz (DSG) gilt für die Bearbeitung von Personendaten natürlicher Personen. **Bearbeiten** umfasst unter anderem das Beschaffen, Speichern, Verwenden, Verändern und Bekanntgeben. Personendaten sind Angaben, die sich auf eine bestimmte oder bestimmbare natürliche Person beziehen. Der EDÖB hält fest, dass das technologieneutral formulierte DSG auf KI-gestützte Datenbearbeitungen direkt anwendbar ist.[1] [2]

Das bedeutet nicht, dass KI generell verboten wäre. Für die konkrete Nutzung sind insbesondere Zweckbindung, Verhältnismässigkeit, Transparenz, Richtigkeit sowie die Löschung oder Anonymisierung nicht mehr benötigter Daten relevant. Der Verantwortliche muss Datenbearbeitungen von der Planung an datenschutzgerecht gestalten und durch Voreinstellungen auf das notwendige Mindestmass begrenzen. Verantwortliche und Auftragsbearbeiter müssen zudem eine dem Risiko angemessene Datensicherheit gewährleisten.[2]

Bei generativer KI ist Transparenz besonders wichtig. Betroffene Personen müssen erkennen können, ob sie mit KI interagieren; der EDÖB nennt zudem die Frage, wie Prompt-Daten verwendet werden könnten.[3] Wenn ein System ausschliesslich automatisiert eine Entscheidung trifft, die für eine Person rechtliche Folgen hat oder sie erheblich beeinträchtigt, greifen zusätzliche Informations- und Überprüfungsrechte nach Artikel 21 DSG.[2] Lassen Sie Anwendungsfälle in Personal, Kredit, Versicherung, Gesundheit, Zugang oder vergleichbar folgenreichen Bereichen deshalb vor der Freigabe fachlich bewerten.

Eine Übermittlung an einen KI-Anbieter kann eine **Bekanntgabe ins Ausland** sein. Nach Artikel 16 DSG ist sie bei angemessenem Schutz zulässig; fehlt dieser, verlangt das Gesetz grundsätzlich geeignete Garantien, etwa anerkannte Standarddatenschutzklauseln. Bei Auftragsbearbeitung muss der Verantwortliche zudem prüfen, ob der Dienstleister die Datensicherheit gewährleisten kann; Unterauftragsbearbeitung braucht die vorgängige Genehmigung.[2] **[FACHPRÜFUNG ERFORDERLICH]** Datenorte, Empfänger, Vertrag, Unterauftragsbearbeiter und Rechtsgrundlage lassen sich nicht aus einem Produktnamen ableiten.

Bei Datenbearbeitungen mit voraussichtlich hohem Risiko ist vorab eine Datenschutz-Folgenabschätzung (DSFA) erforderlich. Sie beschreibt die geplante Bearbeitung, bewertet die Risiken für Persönlichkeit und Grundrechte und hält Schutzmassnahmen fest. Neue Technologien sind dabei ein ausdrücklich relevantes Kriterium.[2]

## Inventar und Datenklassen: Erst sichtbar machen, dann freigeben

Beginnen Sie nicht mit einer langen Liste verbotener Tools. Erstellen Sie ein **KI-Inventar**: eine zentrale, lebende Übersicht über alle bekannten KI-Werkzeuge, eingebetteten KI-Funktionen in Fachanwendungen, Agenten mit Toolzugriff und geplanten Anwendungsfälle. Das Inventar verbindet die technische Sicht mit dem Geschäftsprozess.[4] [15]

Erfassen Sie mindestens Werkzeug und Anbieter, Eigentümer, Zweck, Datenklassen, Kontotyp, Datenflüsse und Datenorte soweit bekannt, Vertragsunterlagen, Freigabestatus sowie Reviewdatum. Bei Agenten gehören eigene Identität, zugelassene Tools sowie Umfang und Laufzeit der Rechte dazu. Halten Sie auch fest, ob Ausgaben extern verwendet werden oder Entscheidungen beeinflussen.[15]

Kombinieren Sie das Inventar mit vier einfachen **Datenklassen**. Sie sind ein Steuerungsmittel, keine rechtliche Ersatzprüfung:

| Datenklasse | Beispiele | Grundregel für Prompts |
|---|---|---|
| **Öffentlich** | bereits publizierte Website-Inhalte, öffentliche Gesetzestexte | In freigegebenen Werkzeugen zulässig, Quellen und Ergebnisse prüfen. |
| **Intern** | nicht publizierte Arbeitsentwürfe, interne Prozessbeschreibungen | Nur in dafür freigegebenen Werkzeugen und für einen klaren Zweck. |
| **Vertraulich** | Kundenbezug, Vertragsentwürfe, Preise, Personalinformationen, nicht publizierter Quellcode | Nicht in allgemeine oder private KI-Konten eingeben; nur nach dokumentierter Freigabe und Schutzprüfung. |
| **Besonders schützenswert oder geheim** | Gesundheitsdaten, Straf- oder Sozialhilfedaten, Passwörter, private Schlüssel, Zugangstoken, Berufs- und Geschäftsgeheimnisse | Nicht in generative KI-Prompts eingeben, solange kein ausdrücklich geprüfter Anwendungsfall mit geeigneten Kontrollen freigegeben wurde. |

Die Kategorien ersetzen nicht die gesetzliche Definition. Besonders schützenswerte Personendaten sind im DSG abschliessend beschrieben, zum Beispiel Gesundheits-, biometrische und Daten über strafrechtliche Verfolgungen oder Sanktionen.[2] Ihre interne Klasse «vertraulich» kann und soll darüber hinaus Vertrags- und Geschäftsinteressen abbilden.

## Freigaben nach Risiko statt nach Hype

Ordnen Sie jeden Anwendungsfall einer von drei Freigabestufen zu. Die Stufe ergibt sich nicht allein aus dem verwendeten Modell. Massgeblich sind Datenklasse, Zweck, Reichweite, Empfängerkreis, mögliche Auswirkungen falscher Antworten und die Schutzmassnahmen des konkreten Dienstes.

### Erlaubt: risikoarme Unterstützung mit klaren Grenzen

Erlaubt sind etwa Ideensammlungen, Übersetzungsentwürfe oder Zusammenfassungen von bereits öffentlichen, nicht personenbezogenen Inhalten in einem inventarisierten und freigegebenen Werkzeug. Auch hier bleiben Mitarbeitende verantwortlich: Sie prüfen Fakten, Quellen, Urheberrechte, Vertraulichkeit und die Eignung des Ergebnisses vor Verwendung. Ein KI-Ergebnis ist keine Freigabe für eine externe Aussage.

### Freigabepflichtig: Daten, Entscheide oder neue Schnittstellen

Freigabepflichtig sind Anwendungsfälle mit internen oder vertraulichen Daten, Personendaten, Kundenkommunikation, Codezugriff, Uploads, Schnittstellen zu Fachsystemen, Agenten mit Toolzugriff oder erheblicher Auswirkung auf Personen und Geschäftsentscheide. Die Fachfreigabe dokumentiert Zweck, Datenklasse, Datenfluss, Anbieterrolle, Vertragsgrundlage, Schutzmassnahmen, menschliche Kontrolle und Reviewtermin. Kann ein hohes Risiko entstehen, prüfen Sie die DSFA-Pflicht vor der Nutzung.[2]

Bei Agenten sind nicht nur Prompt und Ausgabe, sondern auch die eigene Identität, einzelne Toolrechte und mögliche externe Wirkungen freizugeben. Geben Sie pro Agent nur die für den dokumentierten Zweck erforderlichen Rechte, Ressourcen und gegebenenfalls begrenzten Laufzeiten frei. Entscheide darüber, wann eine menschliche Freigabe erforderlich ist, dürfen nicht dem Agenten selbst überlassen werden. Vor folgenreichen oder schwer rückgängig zu machenden Aktionen, etwa dem Löschen wichtiger Datensätze, einer externen Datenübermittlung oder einer kritischen Systemänderung, braucht es einen von der zuständigen Stelle festgelegten und tatsächlich ausgeführten menschlichen Freigabepunkt. Dies ist eine produktneutrale Kontrollvorgabe, keine Funktions- oder Sicherheitszusage für ein bestimmtes KI-Angebot.[15]

### Untersagt: Ungesteuerte Offenlegung und Hochrisiko-Automatisierung

Untersagt sind mindestens private oder nicht freigegebene Konten für vertrauliche Inhalte, das Eingeben von Zugangsdaten oder Geheimnissen sowie der Upload von besonders schützenswerten Daten ohne geprüften und ausdrücklich bewilligten Prozess. Untersagen Sie ebenfalls Agenten mit ungeprüften, zu weit reichenden oder dauerhaft privilegierten Toolrechten sowie Entscheide mit erheblichen Folgen ausschliesslich durch ein KI-System, wenn die erforderliche Prüfung, Transparenz und menschliche Überprüfung nicht sichergestellt sind.[2] [15] Diese Regeln müssen im Alltag sichtbar sein: als kurze Prompt-Regel, in der Einführungsinformation und im Freigabeformular.

## Schutzmassnahmen: Aus einer Regel wird erst mit Kontrollen ein Schutz

Die Datenschutzverordnung verlangt, Schutzbedarf und Risiko zu bestimmen und geeignete technische sowie organisatorische Massnahmen festzulegen. Ihre Ziele sind Vertraulichkeit, Verfügbarkeit, Integrität und Nachvollziehbarkeit. Zugriff darf nur erhalten, wer ihn für die Aufgabe braucht; Verletzungen sollen rasch erkannt und ihre Folgen gemindert werden können.[5]

Setzen Sie deshalb freigegebene KI-Werkzeuge möglichst über zentral verwaltete Geschäftskonten ein. Erzwingen Sie Mehrfaktor-Authentisierung, beschränken Sie administrative Rollen und überprüfen Sie Berechtigungen regelmässig. Trennen Sie Test- und Produktivzugänge. Regeln Sie, wer neue KI-Funktionen in bestehenden Cloud-Diensten aktivieren darf. Solche Grundkontrollen gehören auch in eine [Sicherheitsanalyse](/unsere-dienstleistungen/sicherheitsanalyse), weil KI sonst eine zusätzliche, unkontrollierte Schnittstelle im vorhandenen Cloud- und Identitätsbestand schafft.

Das BACS empfiehlt seit dem 16. Oktober zusätzlich ausdrücklich, wenn möglich geschäftliche Business- oder Enterprise-Zugänge statt privater Konten zu verwenden sowie Trainingsnutzung und vorhandene Opt-out-Möglichkeiten zu prüfen. Eine einzelne Einstellung oder ein Business-Tarif ist jedoch keine pauschale Datenschutzfreigabe; der konkrete Dienst, seine Datenflüsse und Vertragsbedingungen bleiben zu beurteilen. [12]

Ergänzen Sie technische Kontrollen durch einen kurzen **Prompt-Standard**: keine Passwörter, Schlüssel oder Tokens; keine vollständigen Dossiers oder Personalakten; nur nötige, möglichst anonymisierte Angaben; keine Uploads aus Gewohnheit; Ausgabe vor Weitergabe fachlich prüfen. **Datenverlustprävention (DLP)** bezeichnet Kontrollen, die das unberechtigte Weitergeben sensibler Inhalte erkennen, warnen oder verhindern sollen. Eignung und Verfügbarkeit von DLP, Protokollierung sowie Browser- oder Netzwerkkontrollen sind für Ihre Umgebung zu prüfen. CISA betont robuste Datensicherheit, Risikomanagement, Monitoring und Erkennung über den KI-Lebenszyklus.[6]

Für freigegebene KI- und Agentenabläufe ist auch der Verbrauch eine Betriebsfrage. CISA verweist seit dem 22. Oktober 2026 auf eine gemeinsame Behördenorientierung, nach der lange Eingaben, wiederholte Verarbeitung, Connector-Daten und mehrstufige Abläufe Kosten, Leistungsfähigkeit, Quoten und Verfügbarkeit beeinträchtigen können. Legen Sie daher risikogerecht Verbrauchsbudgets, Warnschwellen, Monitoring und bei kritischen Prozessen einen getesteten Ausweichablauf fest. Begrenzen Sie Endlosschleifen und unnötige Ausgaben, ohne dadurch den fachlich nötigen Kontext zu unterschlagen. Kosten- und Verfügbarkeitskontrollen ersetzen weder Datenminimierung noch die Prüfung von Toolrechten, Personendaten, Geheimhaltung, Datenflüssen oder zulässigen Eingaben.[13] [14]

Definieren Sie Nachweise für den Freigabestatus: Vertragsunterlagen, Datenflüsse, Konfiguration, Rollen, Schulungsnachweis und Reviewdatum. Protokollierung soll im Vorfall zeigen, welches Konto welches Werkzeug für welchen freigegebenen Zweck nutzte. Für besonders schützenswerte Daten in grossem Umfang oder Profiling mit hohem Risiko kann die DSV eine weitergehende Protokollierung verlangen.[5]

## Wenn vertrauliche Daten bereits in einen Prompt gelangt sind

Behandeln Sie die Meldung «Ich habe etwas Falsches eingegeben» ruhig und ohne Schuldzuweisung. Nur dann erreicht sie die zuständige Stelle früh genug. Aktivieren Sie Ihre [IT-Notfallplanung](/unsere-dienstleistungen/notfallplanung). Die ausführliche rechtlich-operative Einordnung bietet der Beitrag [Datenpanne in der Schweiz: EDÖB oder BACS?](/wissen/datenpanne-melden-schweiz); die interne Kontaktliste bleibt getrennt von der öffentlich sichtbaren [Kontaktseite](/kontakt).

1. **Nutzung stoppen und Zugang begrenzen.** Verhindern Sie weitere Eingaben oder Freigaben im betroffenen Konto. Ändern oder sperren Sie Zugangsdaten, Tokens oder Schlüssel, falls solche offengelegt wurden. Löschen Sie keine Belege vorschnell.
2. **Fakten sichern.** Dokumentieren Sie Zeitpunkt, Konto, Werkzeug, Prompt oder Upload, Datenklasse, betroffene Personen oder Systeme, erzeugte Ausgabe und bereits getroffene Massnahmen. Sichern Sie verfügbare Protokolle und Screenshots nach Ihrem Beweissicherungsprozess.
3. **Umfang und Datenfluss klären.** Prüfen Sie, welche Daten offengelegt wurden, ob sie gespeichert, exportiert oder durch weitere Empfänger verarbeitet werden konnten und welche Vertrags- oder Dienstinformation dafür relevant ist. Fordern Sie bei Bedarf Unterstützung des Anbieters nach den vereinbarten Wegen an.
4. **Risiko beurteilen und eskalieren.** Bewerten Sie technische, geschäftliche und datenschutzrechtliche Folgen. Eine Verletzung der Datensicherheit liegt nach DSG vor, wenn Personendaten unbeabsichtigt oder widerrechtlich verloren gehen, verändert werden oder Unbefugten offengelegt beziehungsweise zugänglich gemacht werden.[2]
5. **Melden, informieren, nacharbeiten.** Führt die Verletzung voraussichtlich zu einem hohen Risiko für Persönlichkeit oder Grundrechte, meldet der Verantwortliche sie dem EDÖB so rasch wie möglich. Betroffene Personen sind zu informieren, wenn dies zu ihrem Schutz erforderlich ist oder der EDÖB es verlangt. Betreiber kritischer Infrastrukturen können zusätzlich einer BACS-Meldepflicht unterliegen.[7] [8]

> **[FACHPRÜFUNG ERFORDERLICH]** Ob ein konkreter Prompt-Vorfall eine meldepflichtige Datensicherheitsverletzung ist, welche Personen zu informieren sind, ob eine BACS-Meldepflicht besteht und welche Ausland- oder Vertragsfragen folgen, ist durch Datenschutz- und gegebenenfalls Rechtsfachpersonen zu beurteilen. Es gibt im Schweizer DSG keine pauschale, für alle Fälle geltende 72-Stunden-Frist.[2] [8]

Das BACS empfiehlt bei Datenabfluss, den Schaden zu begrenzen, die Sicherheitslücke zu finden und zu schliessen sowie weitere Abflüsse zu verhindern. Fehlt das nötige Fachwissen, soll spezialisierte Unterstützung beigezogen werden.[9]

## In 30 Tagen zu einer tragfähigen KI-Nutzungsregel

**Tage 1–7: Eigentum und Transparenz schaffen.** Benennen Sie geschäftliche, IT-, Datenschutz- und Fachverantwortung. Starten Sie das Inventar mit den meistgenutzten Werkzeugen und wichtigsten Anwendungsfällen. Fragen Sie gezielt nach eingebetteten KI-Funktionen.

**Tage 8–14: Daten und Risiken entscheiden.** Beschliessen Sie die vier Datenklassen und die drei Freigabestufen. Prüfen Sie besonders die Anwendungsfälle mit Personen-, Kunden-, Personal- oder vertraulichen Daten. Legen Sie fest, welche Fragen zwingend in eine Fachprüfung und welche ins Risikoregister gehören.

**Tage 15–21: Sichere Nutzung ermöglichen.** Wählen Sie freigegebene Konten und Werkzeuge aus, richten Sie Identitäts- und Berechtigungskontrollen ein und legen Sie für Agenten Toolumfang, minimale Rechte, menschliche Freigabepunkte und Entzug nach Ende der Aufgabe fest.[15] Veröffentlichen Sie die kurze KI-Nutzungsregel. Schulen Sie anhand echter Arbeitssituationen, nicht nur mit abstrakten Verboten. Das druckbare [Arbeitsmittel KI-Nutzungsregel, Version 1.3](/resources/09-ki-nutzungsregel) hilft bei der Einführung.

**Tage 22–30: Vorfall und Review testen.** Spielen Sie einen Prompt-Vorfall durch: Wer nimmt die Meldung an? Wo werden Fakten gesichert? Wer beurteilt Datenfluss und Meldepflicht? Welche Nachweise sind verfügbar? Testen Sie bei kritischen KI-Abläufen zusätzlich eine Verbrauchswarnung und den Ausweichablauf bei fehlender KI-Verfügbarkeit.[13] [14] Überführen Sie offene Punkte mit Eigentümer und Termin in das Risikoregister. Legen Sie einen risikobasierten Reviewtermin fest und überprüfen Sie die Regel bei wesentlichen Tool-, Vertrags- oder Datenflussänderungen.

## Typische Fehler

**«KI ist nur ein Browser-Tool.»** KI-Funktionen stecken auch in Suchdiensten, Office-Anwendungen, Kundenplattformen und Entwicklerwerkzeugen. Erfassen Sie Funktion und Datenfluss, nicht nur den Markennamen. Für zentrale Konten und Berechtigungen hilft auch der Praxis-Check [Microsoft 365 sicher konfigurieren](/wissen/microsoft-365-sicherheit-kmu).

**«Anonymisiert» wird mit «Namen entfernt» verwechselt.** Eine Fallbeschreibung kann trotz entfernten Namens durch Kombination von Details re-identifizierbar sein. Prüfen Sie, ob die Angaben wirklich nicht mehr einer Person zugeordnet werden können.

**«Der Anbieter speichert nicht für Training, also ist alles erlaubt.»** Eine einzelne Einstellung beantwortet nicht Zweck, Auftragsbearbeitung, Datenorte, Unterauftragsbearbeitung, Berechtigungen, Aufbewahrung, Ausgaben und Meldewege. Prüfen Sie den konkreten Einsatz.

**«Budgetwarnungen ersetzen den Datenschutz.»** Verbrauchslimits, Kostenbudgets und Ausweichabläufe helfen, Verfügbarkeit und Betrieb zu steuern. Sie bewerten aber weder die Zulässigkeit einer Eingabe noch Datenklasse, Geheimhaltung, Empfänger oder Toolrechte.[13] [14]

**«Die KI hat entschieden.»** Verantwortung für geschäftliche Entscheide bleibt beim Unternehmen. Definieren Sie, wann eine qualifizierte Person Ergebnisse prüft, korrigiert oder verwirft.

> **Nächster Schritt:** [Kontaktieren Sie DKSchV](/kontakt), wenn Sie Ihre KI-Nutzungsregel und offene organisatorische Fragen besprechen möchten. Rechtliche Einzelfragen bleiben einer Fachprüfung vorbehalten.

## Fazit

Sichere KI-Nutzung entsteht nicht durch perfekte Voraussicht, sondern durch einen belastbaren Regelkreis. Ein Inventar zeigt, wo KI bereits wirkt. Datenklassen machen Prompt-Entscheide im Alltag verständlich. Risikobasierte Freigaben ermöglichen nützliche Anwendungen, ohne sensible Fälle zu verharmlosen. Identitäten, Berechtigungen, Protokolle und ein geübter Vorfallablauf machen die Regel überprüfbar.

Damit wird Schatten-KI von einem blinden Fleck zu einem führbaren Risiko. Die Regel bleibt wirksam, wenn Sie sie nach neuen Werkzeugen, geänderten Datenflüssen und realen Vorfällen anpassen.

## Quellen

[1]: https://www.edoeb.admin.ch/de/update-geltendes-datenschutzgesetz-ist-auf-ki-direkt-anwendbar "EDÖB – Update: Geltendes Datenschutzgesetz ist auf KI direkt anwendbar"
[2]: https://www.fedlex.admin.ch/eli/cc/2022/491/de "Fedlex – Bundesgesetz über den Datenschutz (DSG), insbesondere Art. 5–9, 16, 19, 21, 22 und 24"
[3]: https://www.edoeb.admin.ch/de/datenschutztag-2026 "EDÖB – Datenschutztag 2026: Einsatz generativer KI und Herausforderungen für den Datenschutz"
[4]: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf "NIST – Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile"
[5]: https://www.fedlex.admin.ch/eli/cc/2022/568/de "Fedlex – Verordnung über den Datenschutz (DSV), insbesondere Art. 1–4"
[6]: https://www.cisa.gov/news-events/alerts/2025/05/22/new-best-practices-guide-securing-ai-data-released "CISA – AI Data Security: Best Practices for Securing Data Used to Train and Operate AI Systems"
[7]: https://www.edoeb.admin.ch/de/databreach "EDÖB – DataBreach: Meldung von Datensicherheitsverletzungen und Information der Betroffenen"
[8]: https://www.bacs.admin.ch/de/infos-unternehmen-behoerden "BACS – Informationen für Unternehmen und Behörden zu Cybervorfällen und Meldepflicht"
[9]: https://www.bacs.admin.ch/de/datenabfluss-behoerden "BACS – Datenabfluss: Was nun?"
[10]: https://www.bacs.admin.ch/de/csm26-s2-de "BACS – Cyber Security Month 2026: Oversharing – Wie viel geben wir über uns preis?"
[11]: https://www.edoeb.admin.ch/de/csm-generative-ki-arbeitsplatz-datenschutzherausforderungen "EDÖB – Generative KI am Arbeitsplatz: gemeinsame Kampagne vom 16.10.2026"
[12]: https://www.bacs.admin.ch/de/csm26-s3-de "BACS – KI im Berufsalltag: Chancen nutzen, Daten schützen, 16.10.2026"
[13]: https://www.cisa.gov/resources-tools/resources/managing-ai-token-consumption-operational-resilience "CISA – Managing AI Token Consumption for Operational Resilience, 22.10.2026"
[14]: https://www.cyber.gc.ca/en/guidance/managing-ai-token-consumption-operational-resilience-itsm00125 "Canadian Centre for Cyber Security – Managing AI token consumption for operational resilience"
[15]: https://www.cyber.gc.ca/en/guidance/careful-adoption-agentic-ai "Canadian Centre for Cyber Security – Careful adoption of agentic AI"
