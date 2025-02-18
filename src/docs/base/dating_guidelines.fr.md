---
title: Principes de datation
---

# Directives de datation des sources du droit suisse (SDS)

Les lignes directrices de datation permettent un enregistrement et une interrogation indépendants
de la langue et des périodes.

## 1 Trier la logique et l'édition

La logique de tri des dates ou des périodes est la suivante :

- Les dates plus anciennes sont confrontées à des dates plus récentes, p. ex. est dans les deux 
  périodes suivantes «7.–10. saec.» avant «8.–9. saec.».
- Tout ce qui pourrait être avant une date est également classé avant cela. P. ex. «18. saec.» 
  (1.1.1701–31.12.1800) avant «1800».
- Si deux dates commencent avec des périodes différentes à la même date, la datation plus détaillée
  est confrontée à l'imposition, p. ex. «6.–7. saec.» avant «6.–8. saec.» et «1300–1350» avant
  «1300–1375».
- S'il y a deux dates avec la même période, mais le calendrier sous-jacent est inconnu dans l'une
  des dates (`@calendar="unknown"`), ensuite, la datation avec un calendrier connu est d'abord,
  donc `<date calendar="julian" when="1590-01-01/>` avant
  `<date calendar="unknown" when="1590-01-01/>`.

Toutes les dates sont émises sans zéros de tête, p. ex. 1.1.1810 au lieu de 01.01.1810.

## 2 Datations claires
- La datation claire est selon [ISO 8601](https://de.wikipedia.org/wiki/ISO_8601) dans 
  [`<date>`](date.fr.md) ou [`<origDate>`](origDate.fr.md) avec l'attribut `@when-custom`
  normalisé : `YYYY-MM-DD`, i. e. informations annuelles à quatre chiffres, informations mensuelles
  à double chiffre, informations quotidiennes à double chiffre qui peuvent être remplies de zéros
  de premier plan.
- Selon ISO 8601 et TEI, le
  [calendrier grégorien](https://hls-dhs-dss.ch/de/articles/012812/2018-01-15/) est toujours
  signifié lors de l'utilisation de l'attribut `@when`, ce qui n'est pas toujours le cas avec le SDS.
  C'est pourquoi nous utilisons l'attribut le plus général `@when-custom` en combinaison avec
  `@calendar` au lieu de `@when` pour spécifier le calendrier. Si le calendrier utilisé est inconnu,
  `calendar="unknown"` est utilisé.  
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

- Hiérarchiquement, des espaces vides (p. ex., l'année manquante, mois manquant) sont spécifiés 
  dans `@when-custom` avec un trait d'union ("-").  
  Exemples :

    ```xml
    <date when-custom="--09-11">11.9.</date>
    ```

    ```xml
    <date when-custom="---11">Onze jours d'un mois</date>
    ```

- Les espaces vides subordonnés hiérarchiquement (p. ex. le jour manquant), en revanche, ne sont
  pas attribués avec `@when-custom`, mais comme une période de temps avec `@from-custom` et
  `@to-custom`.
  Exemple :
  `<date from-custom="1001-09-01" to-custom="1001-09-30" calendar="julian">Septembre 1001</date>`
- Les dates après les jours sacrés ou festifs sont dissous à l'aide de la version HTML du
  [Grotefend](http://www.manuscripta-mediaevalia.de/gaeste/grotefend/grotefend.htm).
  Il y a aussi diverse aide, comme un calculateur de calendrier.

## 3 Datations non claires

### 3.1 Plusieurs datations dans une source

Si une source contient plusieurs dates, tout doit être attribué individuellement.
Si la datation d'une pièce n'est pas sûre, la datation sous la forme d'une période doit être
spécifiée.
Exemple :

```
<date from-custom="1736-11-08" to-custom="1736-11-22 calendar="unknown">8./22. novembre 1736</date>
```

### 3.2 Périodes

#### 3.2.1 Périodes continues

Les périodes sont utilisées avec les attributs `@from-custom` et `@to-custom` avec `@calendar` dans
[`<date>`](date.fr.md) ou [`<origDate>`](origDate.fr.md).
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

Les informations annuelles dangereuses, p. ex. «probablement 1491», sont attribuées
avec [`<precision>`](precision.fr.md).
Exemple :

```
<date from-custom="1491-01-01" to-custom="1491-12-31" calendar="julian">wohl 1491
    <precision match="@from-custom @to-custom" precision="medium"/>
</date>
```

Les datations qui ne sont pas claires, mais qui peuvent être attribuées, sont utilisées 
comme périodes avec `@from-custom` et `@to-custom` avec `@calendar` et 
[`<precision>`](precision.fr.md ).

| Exemple           | Valeurs `@from-custom` et `@to-custom` | Période      |
|-------------------|----------------------------------------|--------------|
| 15. Jh.           | 1401-01-01/1500-12-31                  | 100 Années   |
| 1. moitié 15. Jh. | 1401-01-01/1450-12-31                  | 50 Années    |
| 2. moitié 15. Jh. | 1451-01-01/1500-12-31                  | 50 Années    |
| Début 15. Jh.     | 1401-01-01/1425-12-31                  | 25 Années    |
| Fin 15. Jh.       | 1475-01-01/1500-12-31                  | 25 Années    |
| Ca. 1510          | 1500-01-01/1520-12-31                  | +/-10 Années |
| Centre 15. Jh.    | 1440-01-01/1460-12-31                  | +/-10 Années |
| Centre 1555       | 1555-06-01/1555-07-31                  | +/-1 Mois    |
| Début mars        | --03-01/--03-10                        | 10 Jours     |
| Milieu de février | --04-09/--04-19                        | +- 5 Jours   |
| Milieu de mars    | --03-10/--03-20                        | +- 5 Jours   |
| Fin mars          | --03-22/--03-31                        | 10 Jours     |

#### 3.2.3 Datations non claires qui ne peuvent pas être attribuées

Les dates qui ne sont pas claires et ne peuvent pas être attribuées doivent être attribuées aussi
précisément que possible en tant que périodes avec `@notBefore-custom`und` @notAfter-custom` et
[`<precision>`](precision.fr.md).

| Exemple                    | Valeurs `@notBefore-custom` et `@notAfter-custom` | Période                 |
|----------------------------|---------------------------------------------------|-------------------------|
| avant 1700                 | 1675-01-01/1699-12-31                             | -25 Années              |
| après 1700                 | 1701-01-01/1725-12-31                             | +25 Années              |
| autour 1700                | 1690-01-01/1710-12-31                             | +/-10 Années            |
| probablement 1700 ou 1700? | 1700-01-01/1700-12-31                             | 1 Année                 |
| avant 20. Novembre 1700    | 1700-01-01/1700-11-19                             | Dès le début de l'année |
| après 20. Novembre 1700    | 1700-11-21/1700-12-31                             | À la fin de l'année     |
| avant Octobre 1700         | 1700-07-01/1700-09-30                             | -3 Mois                 |
| après Octobre 1700         | 1700-11-01/1701-01-31                             | +3 Mois                 |

#### 3.2.4 Datations _post quem_ et _ante quem_

Datations _post quem_ n'obtenir pas [`<precision>`](precision.fr.md),
cependant, la fin ou la date de début calculée.

S'il n'y a que lorsque quelqu'un était au pouvoir, nous nous attendons à -10 ans pour le début
du bureau.
Le contenu de `@notAfter-custom` est certain, mais pas le contenu dans `@notBefore-custom`, c'est 
pourquoi il reçoit un [`<precision>`](precision.fr.md).
Exemple :

```
<date notBefore-custom="1489-01-01" notAfter-custom="1499-12-31"
      calendar="julian">[Amtszeit] bis 1499
    <precision match="@notBefore-custom" precision="medium"/>
</date>
```

La même chose s'applique, à l'inverse, pour datations _ante quem_.

## 4 «Faux» / Modifications de la datation

Si un faux est modifié, la date de falsification est pertinente et non la datation dans le texte
source. Un commentaire explicatif est nécessaire.

Si une datation dans le regeste s'écarte d'une datation dans le texte source, un commentaire
est obligatoire.

## 5 Nouveau style / ancien style
Pour le temps après la [réforme du calendrier](http://www.hls-dhs-dss.ch/textes/d/D12812.php),
i. e. le moment où le calendrier julien (ancien style) et le calendrier grégorien (nouveau style)
ont été utilisés, les réglementations suivantes s'appliquent :
1. Les données survenant dans les sources sont laissées comme elles sont dans la source.
   Vous ne serez pas réécrit au nouveau style. La date est utilisée dans les attributs
   (`@when-custom`, `@from-custom`, `@to-custom` etc.) après le calendrier utilisé dans la source.
   Exemple :
    ```
    <date from-custom="1588-09-03" to-custom="1588-09-20"
          calendar="julian">Zwischen 3. und 20. September 1588</date>
    ```
2. Si une source spécifie une date dans les deux styles (double datation), la date est utilisée
   dans les attributs en fonction du nouveau style.
   Exemple:
    ```
    <date when-custom="1590-10-25"
          calendar="gregorian">25/15. octobris anno 90</date>
    ```
3. Si un document ne vient pas d'une autorité qui remonte à l'ancien style (p. ex., les cabinets
   d'avocats de Zurich et Bern), si une date non éminente, une datation selon un nouveau style est
   supposée.
4. Lorsqu'il n'est pas certain dans lequel le style était daté et justifié des doutes sur une
   datation selon un nouveau style, cela est enregistré dans `@calendar` avec la valeur `unknown`.
   Une note avec [`<note>`](note.fr.md) est utile dans ces cas.
   Exemple:
    ```
    <date from-custom="1588-09-03" to-custom="1588-09-20"
          calendar="unknown">Zwischen 3. und 20. September 1588</date>
    <note>Es finden sich keine Informationen zum Kalenderwechsel.</note>
    ```
5. Dans les paratextes éditoriaux (par exemple, introductions, commentaires, etc.),
   les éditeurs doit utiliser le nouveau style, sauf si vous souhaitez souligner explicitement
   l'utilisation de l'ancien style.
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

Les sept lieux catholiques sont allés - à l'exception d'Ob- et Nidwalden - le 12/22. Janvier 1584
au nouveau style. Obwalden et Nidwalden ont accepté le nouveau calendrier un mois plus tard.

À Lucerne était le jour du changement le 12 janvier 1584 ancien style = 22 janvier 1584 nouveau
style (StALU RP 39, fol. 7r).

Dans la communauté de Thurgau, l'utilisation du nouveau style en 1584 a conduit à des tensions
entre Zurich et les cinq emplacements intérieurs. Le 6 mars 1585, le Statut de Baden Day a fait la
célébration des festivals de l'église selon le nouveau calendrier; Cependant, les évangéliques ont
été autorisés à célébrer Noël, Stephanstag, le Nouvel An, Pâques, l'ascension et la Pentecôte à
l'ancien.

À Appenzellerland, l'introduction du calendrier grégorien a conduit à la résistance du rhoden
extérieur. Innerrhoden a accepté le nouveau style en 1584, Rhoden extérieur hors des Helvetics, 
à Noël 1798.

Dans le Valais, la transition a eu lieu le 1/11. Mars 1656. Le nouveau style était arrivé dans la
sous-zone de l'Unterwallis en 1622.

L'évangélique repost Zurich, Bern, Bâle et Schaffhausen, ainsi que catholique-Glarus, Neuchâtel et
Genève sur 1/12. Janvier 1701 au nouveau calendrier. La ville de St. Gallen a suivi en 1724.
Le réformé Glarus a pris le nouveau style à Helvetik le 4 juillet 1798.

Le style grégorien dans les communautés catholiques a été introduit en grégorien à Graubünden
en 1623/1624. Dans les communautés de parité, les catholiques ont suivi le nouveau calendrier du
milieu du XVIIe siècle, le réformé uniquement de la seconde moitié du XVIIIe siècle. Dans les
communautés protestantes, la transition entre 1783 (Oberengadin et Bergell) et 1812 (Schiers et
Grüsch) a eu lieu.

Le changement de calendrier a eu lieu à Genève le 13 décembre 1700 ([SDS GE 4, Nr. 2947](https://www.ssrq-sds-fds.ch/online/GE_4/index.html#p_672)).

## 6 Styles annuels

Les styles du début habituel de l'année, le _style du circumcision_ (début de l'année le 1er
janvier), le _style d'annuntiation_ (début de l'année le 25 mars) et le _style de natal_ (début de
l'année le 25 décembre) sont expliqué in [`<date>`](date.fr.md) et [`<origDate>`](origdate.fr.md)
avec l'attribute `@calendar`.

Le style de rendez-vous s'applique dans le diocèse de Lausanne et à Freiburg depuis le début à la 
seconde moitié du XVe siècle, sinon dans le diocèse de Lausanne jusqu'au 1er moitié du XVIe siècle.

Dans [SDS FR I/2/6](http://www.ssrq-sds-fds.ch/online/FR_I_2_6/index.html#p_5), le style d'annonce avec «n. st.» (= «style nouveau»), mais la date est
dissoute selon le calendrier moderne.
Exemple :
```
 Ordonnance au sujet des voies de fait. 1364 (n. st.) février 4. –
 La datation suivante est dans la source:
 «... <date calendar="julian_annunciation" when-custom="1363-02-04">lo quar jor
 dou moys de febrier, in l’ant de Nostre Segnour corant per
 mil CCC et sexante et troys</date> ...»
```

Parce que le 4 février est maintenant entre le 1er janvier (ou tout au plus le 25 décembre) et le
25 mars (= Annuntiation Mariä), l'éditeur modifie à juste titre le «4. Février 1363» comme le
«4. Février 1364».