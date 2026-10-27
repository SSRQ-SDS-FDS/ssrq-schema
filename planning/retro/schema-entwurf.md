# TEI-Retro: Entwurf des Metadatenprofils

Stand: 22. September 2026. **Erste technische Fassung als `TEI_Retro`-Profil
implementiert und kompiliert; das Modell bleibt bewusst auf die für die
Retrodigitalisierung verfügbaren Metadaten beschränkt.**

Grundlage ist der abgestimmte
[Integrationsplan](../../../ssrq-convert/planning/retro/README.md). Das konkrete
IDNO-Mapping für den ersten Zuger Band wird vom Nutzer erarbeitet. Dieses Profil
legt dafür keine neuen Nummern fest, sondern übernimmt das Identifier-Konzept des
Hauptschemas. Die folgende Struktur ist ein Vorschlag, keine bereits bestätigte
Detailentscheidung.

## Zweck und Form

Ein TEI-Dokument beschreibt ein Stück, das über das retrodigitalisierte
Stückverzeichnis erschlossen ist. Sein Body verweist auf die Anfangsseite im
Band-PDF. Er enthält noch keine Transkription. Titel, Datierung und Drucknachweis
sind aus dem Verzeichnis übernommen, nicht neu historisch geprüft.

Die Ausgabe besteht aus `online/<idno>.xml` und `book/<Band-PDF>.pdf` im beim
Konverteraufruf übergebenen Ordner. Ein PDF liegt einmal pro Band vor.
Im Body steht ein `pb` mit `facs`, das nur die
physische PDF-Anfangsseite enthält. Dateiname, Pfad und URL entfallen dort; editio
ermittelt das PDF über die Bandzuordnung und die Bandkonfiguration.

Arbeitsname des eigenständigen Profils: **TEI_Retro**. Es soll als weiteres ODD
neben Haupt-, Intro- und Lit-Schema versioniert werden. Kennungen, Sprachen und
geeignete Datentypen werden gemeinsam genutzt; umfangreiche Überlieferungs- und
Transkriptionsmodelle des Hauptschemas werden nicht verpflichtend übernommen.

## Vorgeschlagenes Inhaltsmodell

`1` bedeutet erforderlich, `?` optional, `+` mindestens einmal, `*` beliebig oft.
Die Typwerte in dieser Tabelle sind Vorschläge für das Retro-Profil.

| Pfad | Anzahl | Inhalt und Bedeutung |
| --- | --- | --- |
| `TEI/@xml:lang` | 1 | Sprache der Erschliessung aus `volinfo/@xml:lang` |
| `teiHeader/fileDesc/titleStmt/title` | 1 | Stücktitel aus `entry/title` |
| `titleStmt/editor` | * | Herausgeber des gedruckten Bands, soweit im Verzeichnis vorhanden |
| `titleStmt/respStmt` | * | Tatsächliche Verantwortung für die Metadatenerzeugung, soweit bekannt |
| `fileDesc/publicationStmt` | 1 | Herausgeber, elektronisches Publikationsdatum, Druckdatum und Lizenz |
| `fileDesc/seriesStmt/title` | 1 | Name der Sammlung |
| `seriesStmt/idno[not(@type)]` | 1 | Sprechende Kennung nach Hauptschema |
| `seriesStmt/idno[@type='uuid']` | 1 | UUID v4 nach Hauptschema, bei der einmaligen Konvertierung erzeugt |
| `sourceDesc/msDesc/history/origin/origDate[@type='content']` | + | Historische Datierungen des Stücks, mit Rohtext und vorhandenen strukturierten Angaben |
| `sourceDesc/msDesc/head` | + | Stücktitel aus dem Verzeichniseintrag |
| `teiHeader/encodingDesc/p` | 1 | Hinweis auf automatische Metadatenerzeugung ohne Transkription |
| `text/@type` | 1 | Fester Wert `retro` |
| `text/body/pb` | 1 | Anfangsseite des Stücks im Digitalisat |
| `pb/@type` | 1 | Fester Wert `pdf`, damit sich der PDF-Seitenkontext klar von IIIF-Faksimiles unterscheidet |
| `pb/@facs` | 1 | Positive Ganzzahl: physische PDF-Anfangsseite, ab 1 gezählt; kein Dateiname, Pfad oder URL |
| `pb/@n` | 1 | Vorschlag: gedruckte Seitenbezeichnung, z. B. `43` oder `VII` |

Die numerische Bedeutung von `pb/@facs` ist eine ausdrückliche Konvention des
Retro-Profils und muss in dessen ODD modelliert werden. Diese Werte dürfen nicht
als IIIF-Kennungen verarbeitet werden. `pb/@type` ist mit dem festen Wert `pdf`
obligatorisch. Der vorgeschlagene Dokumenttyp `text/@type="retro"` kennzeichnet
zusätzlich den gesamten Datensatz.

Die Quellnummer ist keine zweite Identität für editio. Sie darf z. B. bei
Unterstücken einen Buchstaben enthalten. Doppelte Quellenwerte dürfen nicht zu
doppelten IDNOs führen. Die Zuordnung solcher Fälle gehört ins kommende Mapping.

Der Locator des Eintrags ist zum Beispiel ein struktureller XPath. Er ist eine
Quellenangabe, die editio nicht ausführt. Da er sich bei Quelländerungen verschieben
kann, wird er im optionalen Prüfprotokoll an eine XML-Prüfsumme gebunden. Ein
erneuter Konverterlauf ist ein Neubau unfertiger Daten und erzeugt neue UUIDs.

## Datierungen und Unsicherheit

Die historischen Datierungen stehen in
`sourceDesc/msDesc/history/origin/origDate[@type='content']`. Das Erscheinungsjahr
des Bands und ein späteres digitales Publikationsdatum stehen als typisierte
`date`-Elemente in `publicationStmt`.

Der Entwurf sieht für strukturierte Werte die `*-custom`-Attribute des Hauptschemas
vor. Die Umbenennung ist mechanisch, keine Kalenderkonvertierung:

| Retro-XML | Vorgeschlagene TEI-Abbildung |
| --- | --- |
| `date/@when` mit vollem Datum | `origDate/@when-custom` |
| `date/@when` mit Jahr | `origDate/@from-custom` zum Jahresanfang und `@to-custom` zum Jahresende |
| `date/@when` mit Jahr und Monat | `origDate/@from-custom` am Monatsanfang und `@to-custom` am Monatsende |
| `date/@from`, `@to` | `origDate/@from-custom`, `@to-custom`; Jahresgrenzen jeweils vollständig erweitern |
| `date/@notBefore`, `@notAfter` | `origDate/@notBefore-custom`, `@notAfter-custom`; Jahresgrenzen jeweils vollständig erweitern |
| `date`-Text | Lesbare Datierung unverändert in `origDate` übernehmen |
| Mehrere `date` | Mehrere `origDate`, ursprüngliche Reihenfolge beibehalten |
| Kalender | Bei Option `fix_julian`: sicher vor 12.01.1582 `julian`, sonst `unknown` |

Ein Verzeichniseintrag kann mehrere historische Datierungen enthalten. Das
Retro-Profil begrenzt deshalb die Anzahl der `origDate`-Elemente nicht und
übernimmt auch mehrere Datierungen mit `@type="content"` in der Reihenfolge der
Quelle. Anders als im Hauptprofil geht es hier um die Übernahme der Quelldaten,
bevor sie historisch geprüft werden.

Der Hinweis in `encodingDesc/p` muss Text enthalten; leere oder ausschliesslich
aus Leerraum bestehende Absätze sind ungültig.

Die Kalenderregel nimmt keine Umrechnung des Datumswerts vor. Für einen Zeitraum,
der den 12. Januar 1582 berührt oder überschreitet, sowie für ein blosses Jahr 1582
bleibt der Kalender `unknown`. Die Retro-DTD deklariert `gregorian` als Default;
dieser Wert wird für das Retro-Profil nicht als fachlich geprüfte Kalenderangabe
übernommen.

Die Quellunsicherheit wird vollständig in das bestehende TEI-Modell übertragen.
`precision/@degree` wird auf die Kategorien des SSRQ-Schemas abgebildet:
`1` zu `high`, `0.5` zu `medium`, nicht abbildbare Werte zu `unknown`. Der Wert
`low` kommt in ZG 1.1 nicht vor, bleibt aber im Profil zulässig. Kommagetrennte Quellenwerte in `@match`
werden in eine durch Leerzeichen getrennte Liste überführt und auf die nach der
Datumsumformung vorhandenen Attribute bezogen. Beispiel:

```xml
<origDate type="content" notBefore-custom="1290-01-01"
          notAfter-custom="1310-12-31" calendar="julian">
  um 1300<precision precision="medium"
  match="@notBefore-custom @notAfter-custom"/>
</origDate>
```

Falls ein `when`-Jahres- oder Monatswert zu `from-custom` und `to-custom` wird,
verweist `@match` entsprechend auf beide Attribute. Offensichtliche Quellfehler wie
`@@notAfter` werden zu `@notAfter-custom` normalisiert und im Prüfbericht notiert.

Abgesehen von der Datierung des ausgewählten Stücks sind fehlende Daten zulässig.
Das Profil verlangt keine Archivsignaturen, Regesten oder historische Textsprachen. Es verwendet ein schlankes `msDesc` allein,
um den vorhandenen `origDate`-Datentyp des Hauptschemas ohne erfundene
Handschriftenbeschreibung nutzen zu können.

## Beispiel: erstes Stück in ZG 1.1

Das folgende XML veranschaulicht den vollständigen Aufbau. **`IDNO_AUS_MAPPING`
und `UUID_BEI_ERSTER_ERZEUGUNG` sind Platzhalter, keine zulässigen Kennungen.**
Das Beispiel ist daher absichtlich noch kein validierter Publikationsdatensatz.
Die Seitenposition 81 ist aus dem XML berechnet, noch nicht am PDF geprüft.
Der absolute Quellpfad illustriert die Herkunft in der lokalen Arbeitskopie; für
ein publiziertes Paket ist ein dauerhaft auflösbarer Quellennachweis festzulegen.

```xml
<TEI xmlns="http://www.tei-c.org/ns/1.0" xml:lang="de">
  <teiHeader>
    <fileDesc>
      <titleStmt>
        <title>Grund- und Territorialherren. Stadt und Amt</title>
         <editor>
               <persName>Eugen Gruber</persName>
            </editor>
            <respStmt>
               <persName>Eugen Gruber</persName>
               <resp>Transkription</resp>
            </respStmt>
            <respStmt>
               <persName>Bastian Politycki</persName>
               <resp>XML-Codierung der Transkription</resp>
            </respStmt>
      </titleStmt>
      <publicationStmt>
            <publisher>SSRQ-SDS-FDS</publisher>
            <!-- current date -->
            <date type="electronic" when-custom="2026-09-22"/>
            <!-- date from xml-toc -->
            <date type="print" from-custom="1971-01-01" to-custom="1971-12-31"/>
            <availability>
               <licence target="https://creativecommons.org/licenses/by-nc-sa/4.0/"
                  >Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA
                  4.0)</licence>
            </availability>
         </publicationStmt>
      <seriesStmt>
        <title>Sammlung Schweizerischer Rechtsquellen</title>
        <idno>IDNO_AUS_MAPPING</idno>
        <idno type="uuid">UUID_BEI_ERSTER_ERZEUGUNG</idno>
      </seriesStmt>
      <sourceDesc>
        <msDesc>
          <!-- title of entry without closing dot! -->
          <head>Schenkung des Hofs Cham an das Kloster Zürich</head>
          <history>
            <origin>
              <origDate type="content" when-custom="0858-04-16" calendar="julian">858 April 16</origDate>
            </origin>
          </history>
        </msDesc>
      </sourceDesc>
    </fileDesc>
    <encodingDesc>
      <p>Metadaten aus dem retrodigitalisierten Stückverzeichnis automatisch
        übernommen. Der Text des Stücks ist nicht als Transkription erfasst.</p>
    </encodingDesc>
  </teiHeader>
  <text type="retro">
    <body>
      <pb type="pdf" n="43" facs="81"/>
    </body>
  </text>
</TEI>
```

Für editio ergeben sich klare Zugriffspfade: Bandtitel aus `titleStmt/title`,
Herausgeber aus `titleStmt/editor` und historische Datierung aus
`msDesc/history/origin/origDate`. Der alte Extraktionszweig bleibt für die
vollständigen Editionen bestehen.

## Vorgesehene Prüfregeln

1. Genau eine sprechende IDNO und genau eine UUID; Syntax entsprechend Hauptschema.
   Die Detailprüfung übernimmt dessen Regeln, statt ein abweichendes Regex-Muster
   für Retro einzuführen. Der XML-Dateiname ist ausserhalb von RNG zu prüfen.
2. Genau ein `pb type="pdf"` im Body. `@facs` enthält genau eine positive Ganzzahl als
   physische PDF-Anfangsseite, keinen Dateinamen oder URL; keine Endseitenheuristik.
   Das zum Stück gehörende Band-PDF wird ausserhalb des Seitenverweises zugeordnet.
3. Physische Seitenposition (`@facs`) und Druckseite (`@n`) bleiben verschiedene
   Werte.
4. Datierungsattribute und Unsicherheitsreferenzen sind syntaktisch konsistent.
   Fehlende Datierung ist zulässig; überlieferte Widersprüche werden gemeldet.
5. Keine Transkription im Retro-Body. Wenn später ein Volltext vorliegt, erfolgt
   eine kontrollierte Überführung ins Hauptprofil bei Erhalt von IDNO und UUID.
6. Konverterprüfungen zusätzlich zur Schema-Validierung: PDF existiert, Seitenzahl
   im gültigen Bereich, Quellenzuordnung stimmt, Kennungen im Zielbestand eindeutig.

## Übergang zur technischen Schemafassung

Nach Besprechung dieses Inhaltsmodells wird ein `retro.odd.xml` mit den nötigen
Retro-Elementdefinitionen angelegt und als eigenes Profil registriert. Die
bestehenden Definitionen werden gezielt wiederverwendet: beispielsweise bringt
`date.xml` zusätzliche Inhaltsmodelle und Kontextregeln mit, die nicht pauschal in
das Minimalprofil passen.

Die erste technische Fassung muss gegen das vorhandene ODD-Werkzeug geprüft, zu
RNG/Schematron kompiliert und mit positiven/negativen Beispielen getestet werden.
Wichtige Fälle: fehlendes Datum, mehrere Daten, unsichere Datierung, Quellen-Titel
mit Hochstellung, gleiche Anfangsseite verschiedener Stücke, ungültige Kennung,
fehlendes `pb`, fehlendes oder nichtnumerisches `@facs`, ein Dateipfad statt
einer Seitenposition sowie Seitenposition null.

Nicht vorweggenommen werden: die vom Nutzer kommende konkrete IDNO-Zuordnung und
die technische Anbindung der PDF-Scans in editio.
