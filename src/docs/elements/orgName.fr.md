---
title: orgName
---



# `<orgName/>` (nom d'organisation)

## Description

Signale une organisation voire une institution comme p. e. monastère, confrérie, conseil, voisinage etc. 

## Explication

Au sein du recueil des sources du droit suisse, les entités suivantes sont désignées comme organisations sont identifiées: 

- un groupe de population (p.e. juifs)
- une confrérie
- le bourgmestre et le conseil
- la citoyenneté
- la Confédération suisse ou un groupe de plusieurs cantons (p.e. les VII cantons) (quand il ne s'agit pas du lieu, mais de l'organisation) 
- une propriété
- une famille (p.e. la maison de Toggenburg, von Landenberg)
- une fête qui réunit plusieurs saints (Dix mille martyrs, Onze mille vierges, Pierre et Paul) 
- une entité politique
- une circonscription ecclésiastique / paroisse (attention: une paroisse peut aussi être une indication topographique ou une provenance géographique) 
- un couvent (Attention: un couvent peut également être le nom d'un lieu)
- une société de jeunesse
- une commission (p.e. comité de construction etc.)
- une société commerciale
- un voisinage
- une communauté d'utilisateurs
- un ordre religieux
- un conseil
- une société de tir
- une fondation
- une coopérative de taxation
- une corporation

L'éditeur de la série, ici toujours la Fondation des sources du droit, est désigné dans le [`<respStmt/>`](respStmt.md)  est distingué par[`<orgName/>`](orgName.md).

## Modèle de contenu

- **core**: [abbr](abbr.md) [add](add.md) [cb](cb.md) [choice](choice.md) [corr](corr.md) [date](date.md) [del](del.md) [foreign](foreign.md) [gap](gap.md) [head](head.md) [hi](hi.md) [label](label.md) [lb](lb.md) [measure](measure.md) [measureGrp](measureGrp.md) [note](note.md) [num](num.md) [orig](orig.md) [p](p.md) [pb](pb.md) [q](q.md) [quote](quote.md) [sic](sic.md) [term](term.md) [time](time.md) [unclear](unclear.md)
- **figures**: [figure](figure.md) [table](table.md)
- **linking**: [ab](ab.md) [anchor](anchor.md) [seg](seg.md)
- **msdescription**: [origDate](origDate.md) [origPlace](origPlace.md)
- **namesdates**: [orgName](orgName.md) [persName](persName.md) [placeName](placeName.md)
- **textcrit**: [app](app.md)
- **textstructure**: [div](div.md) [signed](signed.md)
- **transcr**: [addSpan](addSpan.md) [damage](damage.md) [damageSpan](damageSpan.md) [delSpan](delSpan.md) [fw](fw.md) [handShift](handShift.md) [space](space.md) [subst](subst.md) [supplied](supplied.md)
- Contenu de texte au choix

## Attributs

### @ref

Relier l'organisation à l'ID de la base de données des personnes et des organisations. 

*Valeurs possibles*

- Chaîne de caractères – Restriction: expression régulière `org\d{6}(\.\d{2})?`

### @role

Distinction du rôle d'une institutio dans le texte source. 

*Valeurs possibles*

- issuer – *personne/institution qui a fait un acte*
- recipient – *personne/institution qui a reçu l’acte*
- sigillant – *personne/institution qui a posé un sceau*
- testis – *personne/institution d’une liste de témoins*

## Exemples

### Exemple 1

Les institutions/fonctions sont toujours identifiées comme des organisations, mais pas les personnes. Comme indiqué ci-dessous, cela s'applique également à la désignation du maire.

```xml
<egXML xmlns:ns0="http://www.tei-c.org/ns/Examples">
    presentibus
    <lb />herr <persName ref="per001921">Bernhart von Chaam</persName>,
    <orgName ref="org002406">burgermeister, und beid
        <lb />räth
    </orgName>
</egXML>
               
```

## Sections des Guidelines de la TEI

- [13.2.2. Organizational Names](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ND.html#NDORG)