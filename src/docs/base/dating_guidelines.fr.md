---
title: Principes de datation
---

# Directives de datation des sources du droit suisse (SDS)

Les directives de datation permettent une saisie et une consultation des dates de manière uniforme
et indépendante de la langue. 

## 1 Logique de tri

La logique de tri des dates ou des périodes est la suivante :

- Les dates plus anciennes sont indiquées avant les dates plus récentes, 
  p. ex. « VII<sup>e</sup>-X<sup>e</sup> s. » se situe avant « VIII<sup>e</sup>-IX<sup>e</sup> s. ». 
- Tout ce qui peut être antérieur à une date est indiqué avant cette dernière, 
  p. ex. « XVIII<sup>e</sup> s. » (1.1.1701–31.12.1800) avant « 1800 ». 
- Si deux périodes différentes commencent à la même date, la datation la plus
  précise est indiquée en premier, p. ex. « VI<sup>e</sup>-VII<sup>e</sup> s. »
  avant « VI<sup>e</sup>-VIII<sup>e</sup> s. » et « 1300–1350 » avant « 1300–1375 ». 
- Si deux datations correspondent à une même période, mais que le calendrier est
  inconnu pour l’une d’entre-elles (`@calendar="unknown"`), alors on indique en
  premier la date dont le calendrier est connu, donc `<date calendar="julian" when="1590-01-01/>`
  avant `<date calendar="unknown" when="1590-01-01/>`. 

Toutes les dates sont indiquées sans zéros initiaux, p. ex. 1.1.1810 au lieu de 01.01.1810.

## 2 Datations claires
- Les datations claires sont normalisées, conformément à la norme [ISO 8601](https://de.wikipedia.org/wiki/ISO_8601), dans les balises 
  [`<date>`](date.fr.md), [`<origDate>`](origDate.fr.md) et [`<custEvent>`](custEvent.fr.md) avec l’attribut
  `@when-custom` et selon le format : `YYYY-MM-DD`, soit quatre chiffres pour l’année,
  deux pour le mois et deux pour le jour.
  Si nécessaire, les dates sont complétées par des zéros initiaux.
- Selon ISO 8601 et TEI, l’utilisation de l’attribut `@when` suppose toujours l’utilisation 
  du [calendrier grégorien](https://hls-dhs-dss.ch/de/articles/012812/2018-01-15/), ce qui n’est pas toujours le cas avec les SDS.
  C’est pourquoi nous utilisons l’attribut général `@when-custom` combiné avec `@calendar`
  à la place de `@when` pour spécifier le calendrier.
  Si le calendrier utilisé est inconnu, `calendar="unknown"` est utilisé.  
  Exemples :

    ```
    <date when-custom="2001-09-11" calendar="gregorian">11 Sept 2001</date>
    ```

    ```
    <date when-custom="1001-09-11" calendar="julian">11 Sept 1001</date>
    ```

    ```
    <date when-custom="1601-09-11" calendar="unknown">11 Sept 1601</date>
    ```

- Lorsque des indications de dates (hiérarchiquement plus élevées) manquent
  (p. ex., l’année manquante, mois manquant) elles sont spécifiées dans `@when-custom`
  avec un trait d’union ("-").  
  Exemples :

    ```xml
    <date when-custom="--09-11">11.9.</date>
    ```

    ```xml
    <date when-custom="---11">Onze jours d’un mois</date>
    ```

- Lorsque que des indications de dates (hiérarchiquement inférieures) manquent
  (p. ex. le jour manquant), elles ne sont pas attribuées avec `@when-custom`,
  mais comme une période avec `@from-custom` et `@to-custom`.  
  Exemple :
  `<date from-custom="1001-09-01" to-custom="1001-09-30" calendar="julian">Septembre 1001</date>`
- Les datations basées sur des jours saints ou des fêtes liturgiques sont résolues à l’aide
  de la version HTML du [Grotefend](http://www.manuscripta-mediaevalia.de/gaeste/grotefend/grotefend.htm).
  Il existe également divers outils, comme des calculateurs de calendriers.

## 3 Datations non claires

### 3.1 Plusieurs datations dans une même source

Si une source contient plusieurs dates, tout doit être balisé individuellement.
Si une datation n’est pas sûre, elle doit être indiquée sous la forme d’une période.  
Exemple :

```
<date from-custom="1736-11-08" to-custom="1736-11-22 calendar="unknown">8./22. novembre 1736</date>
```

### 3.2 Périodes

#### 3.2.1 Périodes continues

Les périodes sont indiquées avec les balises `@from-custom`, `@to-custom` et `@calendar`, 
à l’intérieur des balises [`<date>`](date.fr.md), [`<origDate>`](origDate.fr.md)> et 
[`<custEvent>`](custEvent.fr.md).  
Exemples :

```
<date from-custom="1521-12-11" to-custom="1544-04-16"
      calendar="julian">11. Decembre 1521 - 16. Avril 1544</date>
```

```
<date from-custom="1717-01-01" to-custom="1718-12-31"
      calendar="gregorian">1717-1718</date>
```

#### 3.2.2 Datations non claires qui peuvent être attribuées

Les indications d’années qui ne sont pas sûres, p. ex. « probablement 1491 »,
sont indiquées à l’aide de la balise [`<precision>`](precision.fr.md).  
Exemple :

```
<date from-custom="1491-01-01" to-custom="1491-12-31" calendar="julian">wohl 1491
    <precision match="@from-custom @to-custom" precision="medium"/>
</date>
```

Les datations qui ne sont pas sûres, mais qui peuvent être attribuées,
sont indiquées comme des périodes avec `@from-custom`, `@to-custom`, `@calendar` et 
[`<precision>`](precision.fr.md).

| Exemple                                    | Valeurs `@from-custom` et `@to-custom` | Durée      |
|--------------------------------------------|----------------------------------------|------------|
| XV<sup>e</sup> s.                          | 1401-01-01/1500-12-31                  | 100 ans    |
| 1<sup>re</sup> moitié du XV<sup>e</sup> s. | 1401-01-01/1450-12-31                  | 50 ans     |
| 2<sup>e</sup> moitié du XV<sup>e</sup> s.  | 1451-01-01/1500-12-31                  | 50 ans     |
| Début XV<sup>e</sup> s.                    | 1401-01-01/1425-12-31                  | 25 ans     |
| Fin XV<sup>e</sup> s.                      | 1475-01-01/1500-12-31                  | 25 ans     |
| Env. 1510                                  | 1500-01-01/1520-12-31                  | +/-10 ans  |
| Milieu du XV<sup>e</sup> s.                | 1440-01-01/1460-12-31                  | +/-10 ans  |
| Moitié de 1555                             | 1555-06-01/1555-07-31                  | +/-1 mois  |
| Début mars                                 | --03-01/--03-10                        | 10 jours   |
| Mi-février                                 | --04-09/--04-19                        | +- 5 jours |
| Mi-mars                                    | --03-10/--03-20                        | +- 5 jours |
| Fin mars                                   | --03-22/--03-31                        | 10 jours   |

#### 3.2.3 Datations non claires qui ne peuvent pas être attribuées

Les dates qui ne sont pas claires et ne peuvent pas être attribuées doivent être indiquées aussi
précisément que possible en tant que périodes avec `@notBefore-custom`, ` @notAfter-custom` et
[`<precision>`](precision.fr.md).

| Exemple                     | Valeurs `@notBefore-custom` et `@notAfter-custom` | Durée                      |
|-----------------------------|---------------------------------------------------|----------------------------|
| avant 1700                  | 1675-01-01/1699-12-31                             | -25 ans                    |
| après 1700                  | 1701-01-01/1725-12-31                             | +25 ans                    |
| autour de 1700              | 1690-01-01/1710-12-31                             | +/-10 ans                  |
| probablement 1700 ou 1700 ? | 1700-01-01/1700-12-31                             | 1 an                       |
| avant le 20. novembre 1700  | 1700-01-01/1700-11-19                             | depuis le début de l’année |
| après le 20. novembre 1700  | 1700-11-21/1700-12-31                             | jusqu’à la fin de l’année  |
| avant octobre 1700          | 1700-07-01/1700-09-30                             | -3 mois                    |
| après octobre 1700          | 1700-11-01/1701-01-31                             | +3 mois                    |

#### 3.2.4 Datations _post quem_ et _ante quem_

Les datations _post quem_ ne reçoivent pas de balise [`<precision>`](precision.fr.md),
mais la date de fin ou de début calculée.

Lorsqu’il s’agit de fonctions officielles, dont seule la date de la fin de la fonction est connue,
on estime le début du mandat à 10 ans auparavant. La valeur de `@notAfter-custom` est sûre,
mais pas la valeur de `@notBefore-custom`, c’est pourquoi une [`<precision>`](precision.fr.md)
est indiquée.  
Exemple :

```
<date notBefore-custom="1489-01-01" notAfter-custom="1499-12-31"
      calendar="julian">[Amtszeit] bis 1499
    <precision match="@notBefore-custom" precision="medium"/>
</date>
```

Les mêmes règles s’appliquent, à l’inverse, pour les datations _ante quem_.

## 4 « Falsifications » / Modifications de la datation

Lorsqu’un « faux » est édité, c’est la date de la falsification qui fait foi,
et non celle indiquée dans la source. Un commentaire explicatif est alors nécessaire.

Si la date mentionnée dans le regeste diffère de celle figurant dans la source,
un commentaire est obligatoire.

## 5 Nouveau style / ancien style
Pour la période qui suit la [réforme du calendrier](http://www.hls-dhs-dss.ch/textes/d/D12812.php),
c’est-à-dire l’époque durant laquelle le calendrier julien (ancien style)
et le calendrier grégorien (nouveau style) ont été utilisés,
les réglementations suivantes s’appliquent : 

1. Les dates mentionnées dans les sources sont conservées telles quelles.
   Elles ne sont pas converties au nouveau style.
   Dans les balises (`@when-custom`, `@from-custom`, `@to-custom` etc.),
   la date est indiquée en fonction du calendrier utilisé dans la source.  
   Exemple : 
    ```
    <date from-custom="1588-09-03" to-custom="1588-09-20"
          calendar="julian">Zwischen 3. und 20. September 1588</date>
    ```
2. Si une source spécifie une date dans les deux styles (double datation),
   la date est mentionnée dans les balises selon le nouveau style. Exemple : 
    ```
    <date when-custom="1590-10-25"
          calendar="gregorian">25/15. octobris anno 90</date>
    ```
3. Si un document a été produit par une autorité qui n’utilise pas l’ancien style
   (p. ex., les chancelleries de Zurich et Berne), et qu’aucune indication contraire
   n’est donnée, une datation selon le nouveau style est supposée.
4. Si l’on ne peut pas déterminer le calendrier utilisé, et que l’attribution au
   nouveau style est mise en doute de façon justifiée, on indique dans `@calendar`
   la valeur `unknown`. Il est alors recommandé d’ajouter une note explicative
   avec [`<note>`](note.fr.md).  
  Exemple :
    ```
    <date from-custom="1588-09-03" to-custom="1588-09-20"
          calendar="unknown">Zwischen 3. und 20. September 1588</date>
    <note>Es finden sich keine Informationen zum Kalenderwechsel.</note>
    ```
5. Dans les paratextes éditoriaux (p. ex., introductions, commentaires etc.),
   les éditeurs doivent utiliser le nouveau style, sauf s’ils souhaitent souligner
   explicitement l’utilisation de l’ancien style.  
   Exemple : 
   ```
    am <date when-custom="1588-09-03" calendar="julian">3. September 1588</date>
    <note>Der Verkauf des Landguts XY an die Familie Soundso wurde nicht,
    wie in der Quelle steht, am <date when-custom="1588-09-03" calendar="julian">
    3. September 1588</date>, sondern bereits <date from-custom="1587-01-01"
    to-custom="1587-12-31 calendar="gregorian">1587</date> abgeschlossen.
    Dies geht aus XYZ hervor, vgl. <bibl><ref>Hinz 1962, S. 63.</ref></bibl>
    </note>
   ```

Les sept cantons catholiques – à l’exception d’Obwald et Nidwald – sont passés au nouveau 
style le 12/22 janvier 1584. Obwald et Nidwald ont adopté le nouveau calendrier
un mois plus tard.

À Lucerne, le changement a lieu le 12 janvier 1584 (ancien style) = 22 janvier 1584
(nouveau style) (StALU RP 39, fol. 7r).

Dans le bailliage commun de Thurgovie, l’adoption du nouveau style en 1584 a conduit à
des tensions entre Zurich et les cinq cantons catholiques de Suisse centrale. 
Le 6 mars 1585, la Diète de Baden imposa la célébration des fêtes religieuses selon 
le nouveau calendrier ; toutefois, les protestants purent continuer à célébrer Noël, 
la Saint Etienne, le Nouvel An, Pâques, l’Ascension et la Pentecôte selon l’ancien style.

À Appenzell, l’introduction du calendrier grégorien a conduit à la résistance des 
Rhodes-Extérieures. Les Rhodes-Intérieures ont accepté le nouveau style en 1584 et
les Rhodes-Extérieures durant la période de la République helvétique, à Noël 1798.

Dans le Valais, la transition a eu lieu le 1/11 mars 1656. Le bas Valais l’avait
toutefois déjà adopté en 1622.

Les cantons protestants de Zurich, Berne, Bâle et Schaffhouse, ainsi que les zones
catholiques de Glaris, Neuchâtel et Genève ont adopté le nouveau calendrier le 1/12 
janvier 1701, la ville de Saint-Gall en 1724 et finalement la partie protestante de
Glaris durant la République helvétique le 4 juillet 1798.

Aux Grisons, le style grégorien fut introduit dans les communes catholiques en 1623/1624. 
Dans les communes mixtes, les catholiques utilisèrent le nouveau calendrier à partir 
du milieu du XVII<sup>e</sup> siècle, tandis que les protestants ne l’adoptèrent que
dans la seconde moitié du XVIII<sup>e</sup> siècle. Dans les communes protestantes, 
le changement eut lieu entre 1783 (Haute-Engadine et Bergell) et 1812 (Schiers et Grüsch).

À Genève, le changement de calendrier eut lieu le 13 décembre 1700 
([SDS GE 4, Nr. 2947](https://www.ssrq-sds-fds.ch/online/GE_4/index.html#p_672)).

## 6 Les styles de début d’année

Les styles de début d’année différant de celui usuel de la Circoncision (début de
l’année le 1er janvier) comme le style de l’Annonciation (début de l’année le 25 mars) 
et le style de la Nativité (début de l’année le 25 décembre) doivent être indiqués 
dans [`<date>`](date.fr.md), [`<origDate>`](origDate.fr.md) et [`<custEvent>`](custEvent.fr.md)
avec l’attribut `@calendar`.

Le style de l’Annonciation est en vigueur dans le diocèse de Lausanne et à Fribourg
depuis le début du XV<sup>e</sup> siècle, jusqu’à la seconde moitié du XV<sup>e</sup>
siècle et ailleurs dans le diocèse de Lausanne jusqu’à la première moitié du
XVI<sup>e</sup> siècle.

Dans l’édition [SDS FR I 2 6](http://www.ssrq-sds-fds.ch/online/FR_I_2_6/index.html#p_5),
le style de l’Annonciation est indiqué par la mention « n. st. » (=nouveau style),
mais la date est résolue selon le calendrier moderne.  
Exemple :
```
 Ordonnance au sujet des voies de fait. 1364 (n. st.) février 4. –
 La datation suivante est dans la source :
 « ... <date calendar="julian_annunciation" when-custom="1364-02-04">lo quar jor
 dou moys de febrier, in l’ant de Nostre Segnour corant per
 mil CCC et sexante et troys</date> ... »
```

Le 4 février se situant entre le 1er janvier (ou éventuellement le 25 décembre)
et le 25 mars (= fête de l’Annonciation), l’éditeur du texte modifie à juste
titre le « 4 février 1363 » comme le « 4 février 1364 ».