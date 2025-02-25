# Aperçu des éléments utilisés

## Structure de document
- [`<TEI>`](TEI.fr.md)
- Zone de texte : [`<text>`](text.fr.md)
- Zone de tête : [`<teiHeader>`](teiHeader.fr.md)

## Éléments dans la zone de texte

### Balisage critique du texte
- Abréviations et leur résolution : [`<abbr>`](abbr.fr.md)
  [`<expan>`](expan.fr.md)
- Erreur et leur correction : [`<sic>`](sic.fr.md) [`<corr>`](corr.fr.md)
- Sélection de l'une des deux variantes : [`<choice>`](choice.fr.md)
- Entrées d'appareil avec lemme et lectures : [`<app>`](app.fr.md)
    [`<lem>`](lem.fr.md) [`<rdg>`](rdg.fr.md)
- Ajouts : [`<add>`](add.fr.md)
    [`<addSpan>`](addSpan.fr.md)
- Suppressions : [`<del>`](del.fr.md) [`<delSpan>`](delSpan.fr.md)
- Substitutions : [`<subst>`](subst.fr.md)
- Dommages : [`<damage>`](damage.fr.md)
    [`<damageSpan>`](damageSpan.fr.md)
- Lacunes et leur supplément par les éditeurs : [`<gap>`](gap.fr.md)
    [`<space>`](space.fr.md) [`<supplied>`](supplied.fr.md)
- Changement de main : [`<handShift>`](handShift.fr.md)
- Lecture incertaine : [`<unclear>`](unclear.fr.md)
- Point d'ancrage pour les balises inter-hiérarchies : [`<anchor>`](anchor.fr.md)

### Balisage de la structure du texte
- Zone de texte et zone de commentaire : [`<body>`](body.fr.md) [`<back>`](back.fr.md)
- Sections : [`<div>`](div.fr.md) [`<seg>`](seg.fr.md)
- Paragraphes dans l'original : [`<p>`](p.fr.md)
- Tableaux : [`<table>`](table.fr.md) [`<row>`](row.fr.md) [`<cell>`](cell.fr.md)
- Listes : [`<list>`](list.fr.md) [`<item>`](item.fr.md)
- Graphiques : [`<figure>`](figure.fr.md) [`<graphic>`](graphic.fr.md)
- Bouleversements :
    - Début de la page : [`<pb>`](pb.fr.md)
    - Début de la colonne : [`<cb>`](cb.fr.md)
    - Début de la ligne : [`<lb>`](lb.fr.md)
- Autres parties du texte :
    - Rubriques, titres : [`<head>`](head.fr.md)
    - Signatures: [`<signed>`](signed.fr.md)
    - Citations et discours direct : [`<quote>`](quote.fr.md) [`<q>`](q.fr.md)
    - Gardiens et plaignants : [`<fw>`](fw.fr.md)
    - Étiquettes : [`<label>`](label.fr.md)
    - Blocs anonymes : [`<ab>`](ab.fr.md)
    - Notes : [`<note>`](note.fr.md)
    - Références, informations bibliographiques : 
      [`<bibl>`](bibl.fr.md) [`<ref>`](ref.fr.md) [`<listBibl>`](listBibl.fr.md)
    - Signes de ponctuation traités en fonction de la langue : [`<pc>`](pc.fr.md)
- Changement de langue : [`<foreign>`](foreign.fr.md) [`<orig>`](orig.fr.md)
- Points forts : [`<hi>`](hi.fr.md)

### Balisage du contenu
- Dates : [`<date>`](date.fr.md) [`<precision>`](precision.fr.md)
- Temps : [`<time>`](time.fr.md)
- Nombres et chiffres : [`<num>`](num.fr.md)
- Mesures, poids, monnaies : [`<measure>`](measure.fr.md)
    [`<measureGrp>`](measureGrp.fr.md)
- Registres :
    - Lemmes ou mots-clé : [`<term>`](term.fr.md)
    - Personnes : [`<persName>`](persName.fr.md)
    - Organisations : [`<orgName>`](orgName.fr.md)
    - Lieux : [`<placeName>`](placeName.fr.md)

## Éléments dans la zone de tête

### Description du fichier
- [`<fileDesc>`](fileDesc.fr.md)
- Description de la page de titre :
    - Titre et série : [`<titleStmt>`](titleStmt.fr.md) [`<title>`](title.fr.md)
        [`<publicationStmt>`](publicationStmt.fr.md)
        [`<seriesStmt>`](seriesStmt.fr.md)
    - Responsabilité : [`<editor>`](editor.fr.md),
      [`<publisher>`](publisher.fr.md) [`<respStmt>`](respStmt.fr.md)
      [`<resp>`](resp.fr.md)
    - Licence : [`<availability>`](availability.fr.md)
      [`<licence>`](licence.fr.md)
- Description de la source : [`<sourceDesc>`](sourceDesc.fr.md)
  [`<msDesc>`](msDesc.fr.md)
    - Témoins textuels : [`<listWit>`](listWit.fr.md) [`<witness>`](witness.fr.md)
    - Description bibliographique : [`<msIdentifier>`](msIdentifier.fr.md)
      [`<altIdentifier>`](altIdentifier.fr.md) [`<idno>`](idno.fr.md)
      [`<repository>`](repository.fr.md) [`<settlement>`](settlement.fr.md)
    - Description du contenu de la source : [`<msContents>`](msContents.fr.md)
      [`<msItem>`](msItem.fr.md) [`<author>`](author.fr.md)
      [`<textLang>`](textLang.fr.md) [`<docImprint>`](docImprint.fr.md) [`<pubPlace>`](pubPlace.fr.md) [`<publisher>`](publisher.fr.md)
      [`<summary>`](summary.fr.md)
    - Histoire de la source : [`<history>`](history.fr.md)
      [`<origin>`](origin.fr.md) [`<origDate>`](origDate.fr.md)
      [`<origPlace>`](origPlace.fr.md)
      - Informations Complémentaires : [`<additional>`](additional.fr.md) [`<adminInfo>`](adminInfo.fr.md)
      [`<custodialHist>`](custodialHist.fr.md) [`<custEvent>`](custEvent.fr.md)
    - Description physique de la source : [`<physDesc>`](physDesc.fr.md)
        - Reliure : [`<bindingDesc>`](bindingDesc.fr.md)
        - Mains : [`<handDesc>`](handDesc.fr.md) [`<handNote>`](handNote.fr.md)
        - Sceaux : [`<sealDesc>`](sealDesc.fr.md) [`<seal>`](seal.fr.md)
        - Matériau : [`<objectDesc>`](objectDesc.fr.md)
          [`<supportDesc>`](supportDesc.fr.md) [`<support>`](support.fr.md)
          [`<material>`](material.fr.md)
        - Étendue : [`<extent>`](extent.fr.md) [`<dimensions>`](dimensions.fr.md)
          [`<height>`](height.fr.md) [`<width>`](width.fr.md)
        - Foliation : [`<foliation>`](foliation.fr.md)
        - État de conservation : [`<condition>`](condition.fr.md)

### Description du codage
- [`<encodingDesc>`](encodingDesc.fr.md)
  [`<editorialDecl>`](editorialDecl.fr.md)

### Description du profil du texte
- [`<profileDesc>`](profileDesc.fr.md) [`<textClass>`](textClass.fr.md)
- Mots clés: [`<keywords>`](keywords.fr.md) [`<term>`](term.fr.md)
