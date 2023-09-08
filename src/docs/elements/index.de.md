# Übersicht der verwendeten Tags

## Dokumentstruktur
- [`<TEI>`](TEI.de.md)
- Textbereich: [`<text>`](text.de.md)
- Kopfbereich: [`<teiHeader>`](teiHeader.de.md)

## Tags im Textbereich

### Textkritische Auszeichnungen
- Abkürzungen und deren Auflösung: [`<abbr>`](abbr.de.md)
  [`<expan>`](expan.de.md)
- Fehler und deren Korrektur: [`<sic>`](sic.de.md) [`<corr>`](corr.de.md)
- Auswahl aus einer von zwei Varianten: [`<choice>`](choice.de.md)
- Apparateinträge mit Lemma und Lesarten: [`<app>`](app.de.md)
    [`<lem>`](lem.de.md) [`<rdg>`](rdg.de.md)
- Hinzufügungen: [`<add>`](add.de.md)
    [`<addSpan>`](addSpan.de.md)
- Tilgungen: [`<del>`](del.de.md) [`<delSpan>`](delSpan.de.md)
- Ersetzungen: [`<subst>`](subst.de.md)
- Schäden: [`<damage>`](damage.de.md)
    [`<damageSpan>`](damageSpan.de.md)
- Lücken und deren Ergänzung durch den Bearbeitenden: [`<gap>`](gap.de.md)
    [`<space>`](space.de.md) [`<supplied>`](supplied.de.md)
- Handwechsel: [`<handShift>`](handShift.de.md)
- Unsichere Lesung: [`<unclear>`](unclear.de.md)
- Ankerpunkt für hierarchieübergreifende Tags: [`<anchor>`](anchor.de.md)

### Auszeichnung der Textstruktur
- Text- und Kommentarbereich: [`<body>`](body.de.md) [`<back>`](back.de.md)
- Abschnitte: [`<div>`](div.de.md) [`<seg>`](seg.de.md)
- Absätze im Original: [`<p>`](p.de.md)
- Tabellen: [`<table>`](table.de.md) [`<row>`](row.de.md) [`<cell>`](cell.de.md)
- Listen: [`<list>`](list.de.md) [`<item>`](item.de.md)
- Graphiken: [`<figure>`](figure.de.md) [`<graphic>`](graphic.de.md)
- Umbrüche:
    - Seitenanfang: [`<pb>`](pb.de.md)
    - Spaltenanfang: [`<cb>`](cb.de.md)
    - Zeilenanfang: [`<lb>`](lb.de.md)
- Sonstige Textteile:
    - Überschriften, Titel: [`<head>`](head.de.md)
    - Unterschriften, Signaturen: [`<signed>`](signed.de.md)
    - Zitate und direkte Rede: [`<quote>`](quote.de.md) [`<q>`](q.de.md)
    - Kustoden oder Reklamanten: [`<fw>`](fw.de.md)
    - Label: [`<label>`](label.de.md)
    - Sonstiger Textblock: [`<ab>`](ab.de.md)
    - Anmerkungen, Fussnoten: [`<note>`](note.de.md)
    - Verweise, bibliographische Angaben: [`<ref>`](ref.de.md)
      [`<bibl>`](bibl.de.md) [`<listBibl>`](listBibl.de.md)
- Sprachwechsel: [`<foreign>`](foreign.de.md) [`<orig>`](orig.de.md)
- Hervorhebungen: [`<hi>`](hi.de.md)

### Inhaltliche Auszeichnung
- Datumsangaben: [`<date>`](date.de.md) [`<precision>`](precision.de.md)
- Zeitangaben: [`<time>`](time.de.md)
- Zahlen und Ziffern: [`<num>`](num.de.md)
- Masse, Gewichte, Währungen: [`<measure>`](measure.de.md)
    [`<measureGrp>`](measureGrp.de.md)
- Register:
    - Lemmata: [`<term>`](term.de.md)
    - Personen: [`<persName>`](persName.de.md)
    - Organisationen: [`<orgName>`](orgName.de.md)
    - Orte: [`<placeName>`](placeName.de.md)
    - Schlagwörter: [`<term>`](term.de.md)

## Tags im Kopfbereich

### Beschreibung der Datei
- [`<fileDesc>`](fileDesc.de.md)
- Beschreibung der Titelei:
    - Titel und Reihe: [`<titleStmt>`](titleStmt.de.md) [`<title>`](title.de.md)
        [`<publicationStmt>`](publicationStmt.de.md)
        [`<seriesStmt>`](seriesStmt.de.md)
    - Verantwortliche: [`<editor>`](editor.de.md),
      [`<publisher>`](publisher.de.md) [`<respStmt>`](respStmt.de.md)
      [`<resp>`](resp.de.md)
    - Lizenz: [`<availability>`](availability.de.md)
      [`<licence>`](licence.de.md)
- Beschreibung der Quelle: [`<sourceDesc>`](sourceDesc.de.md)
  [`<msDesc>`](msDesc.de.md)
    - Textzeugen: [`<listWit>`](listWit.de.md) [`<witness>`](witness.de.md)
    - Bibliographische Beschreibung: [`<msIdentifier>`](msIdentifier.de.md)
      [`<altIdentifier>`](altIdentifier.de.md) [`<idno>`](idno.de.md)
      [`<repository>`](repository.de.md) [`<settlement>`](settlement.de.md)
    - Beschreibung der Quelleninhalte: [`<msContents>`](msContents.de.md)
      [`<msItem>`](msItem.de.md) [`<author>`](author.de.md)
      [`<textLang>`](textLang.de.md) [`<docImprint>`](docImprint.de.md)
      [`<summary>`](summary.de.md)
    - Geschichte der Quelle: [`<history>`](history.de.md)
      [`<origin>`](origin.de.md) [`<origDate>`](origDate.de.md)
      [`<origPlace>`](origPlace.de.md)
    - Zusätzliche Angaben: [`<additional>`](additional.de.md)
    - Physische Beschreibung der Quelle: [`<physDesc>`](physDesc.de.md)
        - Bindung: [`<bindingDesc>`](bindingDesc.de.md)
        - Hände: [`<handDesc>`](handDesc.de.md) [`<handNote>`](handNote.de.md)
        - Siegel: [`<sealDesc>`](sealDesc.de.md) [`<seal>`](seal.de.md)
        - Material: [`<objectDesc>`](objectDesc.de.md)
          [`<supportDesc>`](supportDesc.de.md) [`<support>`](support.de.md)
          [`<material>`](material.de.md)
        - Umfang: [`<extent>`](extent.de.md) [`<dimensions>`](dimensions.de.md)
          [`<height>`](height.de.md) [`<width>`](width.de.md)
        - Zählung: [`<foliation>`](foliation.de.md)
        - Erhaltungszustand: [`<condition>`](condition.de.md)

### Beschreibung der Kodierung
- [`<encodingDesc>`](encodingDesc.de.md)
  [`<editorialDecl>`](editorialDecl.de.md)

### Beschreibung des Textprofils
- [`<profileDesc>`](profileDesc.de.md) [`<textClass>`](textClass.de.md)
- Schlagworte: [`<keywords>`](keywords.de.md) [`<term>`](term.de.md)
