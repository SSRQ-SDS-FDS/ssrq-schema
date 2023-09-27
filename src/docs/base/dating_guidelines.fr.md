---
title: Directives de datation
---

# Principes

- uniformiser le plus possible
- récupération selon les langues (coutumes linguistiques) : DE, FR, IT
- le style de la Circoncision (début de l\'année le 1 janvier), de
  l\'Annonciation (25 mars) ou de la Nativité (25 décembre) doit être indiqué
- *Principes spéciales pour la rétronumérisation*

- datation reprises selon le volume
- reprise de l\'entrée originale dans l\'index possible (seulement
  pour des cas problématiques)
- présentation sous forme de « index chronologique » possible
- récupération selon les langues (coutumes linguistiques) : DE, FR, IT
- le style de la Circoncision (début de l\'année le 1er janvier), de
  l\'Annonciation (25 mars) ou de la Nativité (25 décembre) doit être
  indiqué
- plusieurs tags [[date]](date.fr.md) dans l\'index sont
  possibles (pour la rétronumérisation), mais pas pour l\'édition numérique.

# Datation certaine

(avec un texte de datation certaine):

- Les dates sont normalisées selon ISO 8601 dans @when/fr ou @when (YYYY-MM-DD). Selon ISO 8601 et TEI, @when comprend
  toujours le calendrier grégorien. Depuis 2019: @when-custom avec @calendar.
- Les degrés hiérarchiques supérieurs de la datation (année, mois) sont indiqués dans @when avec un tiret ("-"). Les
  degrés inférieurs qui font par exemple défaut (le jour n'est pas connu) ne sont pas signalés de façon particulière.
- La datation selon les jours de fêtes/des saints sont résolu à l'aide du Grotefend. Sur le site web:
  [[http://www.manuscripta-mediaevalia.de/gaeste/grotefend/grotefend.htm]](http://www.manuscripta-mediaevalia.de/gaeste/grotefend/grotefend.htm)
  il existe différents outils ainsi qu'un calculateur.

## Exemples

- `<date when="2001">The year 2001</date>`
- `<date when="2001-09">September 2001</date>`
- `<date when="2001-09-11">11 Sept 01</date>`
- `<date when="--09-11">9/11</date>`
- `<date when="--09">September</date>`
- `<date when="---11">Eleventh of the month</date>`

# Datation problématique

## Plusieurs datations dans une pièce (rétronumérisation)

Il faut utiliser plusieurs éléments de datations. (L'utilisation de plusieurs éléments de datation doit être commentée
et se référer à la pièce. La datation de commentaires, de pièces similaires ou de copies ne font pas l'objet de cette
datation (éventuellement utiliser [`<note/>`](note.fr.md) dans ces cas). En générale, ces datations sont
traitées de la même façon.)

### Exemples

- `<date when="1736-11-08">1736 November 8 / 22</date>`
- `<date when="1736-11-22"/>`

## Durées de temps ou périodes

Des durées de temps ou périodes sont indiquées dans [[date]](date.fr.md) à l'aide des attributs
@from et @to. Depuis 2019: @from-custom et @to-custom avec @calendar.

### Exemples

- 1521 décembre 11 – 1544 avril
  16: `<date from-custom="1521-12-11" to-custom="1544-04-16" calendar="#julian">1521 Dezember 11 - 1544
  April 16</date>`
- 1717–1718: `<date from-custom="1717" to-custom="1718" calendar="#gregorian">1717-1718</date>`

## Des durées de temps ou périodes interrompues

- (Une explication doit être éffectuée comme sous point 1)
- Rétronumérisation : Les durées de temps ou périodes sont codées dans plusieurs tags.

### Exemples

- 1610, 1620–1635: Rétronumérisation: `<date when="1610">1610, 1620–1635</date><date from="1620" to="1635"/>`
- 1466, 25 mai et 25 juillet (Heumonat): Rétronumérisation: `<date when="1466-05-25">1466, 25. Mai und 25.
  Heumonat</date><date when="1466-07-25"/>`

## Datation ambiguë, mais qui peut être résolues

Rétronumérisation : Une indication de l'an ambiguë, p.e. "probablement 1491", est repris
avec [`<precision/>`](precision.fr.md) et les attributs @match et @degree.

`<date when="1491">wohl 1491<precision match="@when" degree="0.5"/></date>`

Des datations qui ne sont pas claires, mais qui peuvent être résolues, sont codées comme des intervalles.
À chaque fois avec @from, @to, depuis 2019 @from-custom, @to-custom avec @calendar.

<table>
<thead>
    <tr>
        <th>Exemple</th>
        <th>Valeurs @from-custom et @to-custom</th>
        <th>Période: clé</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>XVIIe siècle</td>
        <td>1601/1700</td>
        <td>siècle: 100</td>
    </tr>
    <tr>
        <td>première moitié du XVe siècle</td>
        <td>1401/1450</td>
        <td>moitié: 50</td>
    </tr>
</tbody>
</table>

`<date from-custom="1401" to-custom="1450" calendar="#julian">première moitié du XVe siècle</date>`

À chaque fois avec @notBefore, @notAfter, depuis 2019 @notBefore-custom, @notAfter-custom et
[[precision]](precision.fr.md) avec @match et @degree.

<table>
<thead>
    <tr>
        <th>Exemple</th>
        <th>Valeurs @notBefore-custom et @notAfter-custom</th>
        <th>Période: clé</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>fin du XVe siècle</td>
        <td>1475/1500</td>
        <td>fin: 25 ans</td>
    </tr>
    <tr>
        <td>env. 1510</td>
        <td>1500/1520</td>
        <td>env.: +/-10 ans</td>
    </tr>
    <tr>
        <td>ToDo</td>
        <td>1440/1460</td>
        <td>ToDo: +/-10 Jahre</td>
    </tr>
    <tr>
        <td>ToDo 1555</td>
        <td>1555-06/1555-07</td>
        <td>ToDo: +/-1 Monat</td>
    </tr>
    <tr>
        <td>fin mars</td>
        <td>03-21/03-31</td>
        <td>fin: 10 jours</td>
    </tr>
    <tr>
        <td>début juillet</td>
        <td>07-01/07-10</td>
        <td>début: 10 jours</td>
    </tr>
</tbody>
</table>

Les datations qui se réfèrent à la date originale du document (exemple en dessous, si le document a été rédigé en juin
1438):

<table>
<thead>
    <tr>
        <th>Exemple</th>
        <th>Valeurs @when et @dur</th>
        <th>Période: clé</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>il y a 5 ans</td>
        <td>when="1433" dur="P5Y"</td>
        <td></td>
    </tr>
    <tr>
        <td>il y a 3 mois</td>
        <td>when="1438-03"<br/> dur="P3M"</td>
        <td></td>
    </tr>
    <tr>
        <td>ToDo</td>
        <td>when="1437-04"<br/> dur="P1Y2M"</td>
        <td></td>
    </tr>
</tbody>
</table>

Rétronumérisation:
`<date notBefore="1500" notAfter="1520">env. 1510<precision match="@notBefore, @notAfter" degree="0.5"/></date>`<br/>
`<date notBefore="1386-07-01" notAfter="1386-07-10">1386 début juillet<precision match="@notBefore, @notAfter"
degree="0.5"/></date>`

Portail:
`<date notBefore-custom="1500" notAfter-custom="1520" calendar="#julian">env.
1510<precision match="@notBefore-custom, @notAfter-custom" degree="0.5"/></date>`<br/>
`<date notBefore-custom="1386-07-01" notAfter-custom="1386-07-10" calendar="#julian">1386 début juillet<precision
match="@notBefore-custom, @notAfter-custom" degree="0.5"/></date>`

## datation ambiguë qui ne peuvent pas être résolues

Des datations qui ne sont pas claires et qui ne peuvent pas être résolues, doivent si possible être codées commes des
intervalles (analogue à 4., le plus proche possible) :

À chaque fois avec @notBefore, @notAfter, depuis 2019 @notBefore-custom, @notAfter-custom et
[[precision]](precision.fr.md) avec @match et @degree

<table>
<thead>
    <tr>
        <th>Exemple</th>
        <th>Valeurs @notBefore-custom und @notAfter-custom</th>
        <th>Période: clé</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>avant 1688</td>
        <td>1638/1688</td>
        <td>avant: -50 ans</td>
    </tr>
    <tr>
        <td>après 1688</td>
        <td>1688/1738</td>
        <td>après: +50 ans</td>
    </tr>
    <tr>
        <td>autour de 1500, sans date</td>
        <td>1490/1510</td>
        <td>autour: +/-10 ans</td>
    </tr>
    <tr>
        <td>1730 (après le 20 novembre)</td>
        <td>1730-11-21/1730-12-31</td>
        <td>jusqu'à la fin de l'année</td>
    </tr>
</tbody>
</table>

Des datations *post quem* ne doivent pas être mises en question, mais la date indiquée pour le début et la fin.

`<date notBefore-custom="1730-11-21" notAfter-custom="1730-12-31" calendar="#gregorian">1730
après le 20 novembre<precision match="@notAfter-custom" degree="0.5"/></date>`

## "falsification" / changement de date

En général, on part de la conclusion de l'éditeur (surtout dans le regeste – une éventuelle datation divergente est de
toute façon indiquée dans le texte et doit être signalée).

## Style nouveau / style ancien

**Règles générales:**

1. En général, la datation est faite selon le style nouveau. Si un document n'est pas issu d'une instance publique qui
   date manifestement selon le style ancien (p.e. les chancelleries de Zurich et de Berne), on peut conclure en cas
   d'une date non commentée qu'il s'agit du nouveau style.
2. Les datations selon le style ancien ou selon les deux styles sont saisies dans une annotation critique, mais pas dans
   le regeste.
3. En cas de doute sur le style de la datation, il faut laisser un commenter dans une annotation critique.

**Règles spéciales pour la rétronumérisation:**

Tant la date grégorienne que la date julienne doivent être saisies dans l'index selon le style ISO. Si les deux
datations sont données, on attribue aux deux les valeurs correspondantes "Julian" ou "Gregorian" dans
l'attribut @calendar. Si dans l'index n'apparaît qu'une sorte de datation elle n'est pas spécialement
signalée, mais supposée grégorienne.

`<date from="1588-09-03" to="1588-09-20" calendar="Julian">Zwischen 3. und 20. September 1588</date>`<br/>
`<date when="1588-09-13" to="1588-10-30" calendar="Gregorian">Zwischen 13. und 30. September 1588</date>`

Voir également l'article Calendriers dans le DHS:
[[http://www.hls-dhs-dss.ch/textes/f/F12812.php]](http://www.hls-dhs-dss.ch/textes/f/F12812.php)

Pour une conversion automatique du style ancien dans le style nouveau:
[[http://www.manuscripta-mediaevalia.de/gaeste/grotefend/grotefend.htm]](http://www.manuscripta-mediaevalia.de/gaeste/grotefend/grotefend.htm)
(Calculateur)

**Edition numérique:**

Calendrier julien (style ancien)

La date indiqueé dans la pièce éditée voire le texte de datation est laissé tel quel. La normalisation et la
signalisation des dates ou des périodes se fait avec les attributs nécessaires selon le style ISO, c'est-à-dire selon le
calendrier grégorien voire le style nouveau. En outre, il faut ajouter la valeur "Julian" dans l'attribut @calendar.

`<date from="1588-09-13" to="1588-09-30" calendar="julian">Zwischen 3. und 20 September 1588</date>`

### Changement du calendrier

Lucerne: le jour du changement: le 12 janvier 1584 ancien style = 22 janvier 1584 style nouveau (StALU RP 39, fol. 7r.)

## Style de début de l'année

Les différents styles de début de l'année (Circoncision (1er janvier), Annonciation (25 mars) ou Nativité (25 décembre))
doivent être annotés dans [`<date/>`](date.fr.md) à l'aide de @calendar.

**Style de l'Annonciation**

Le style de l'Annonciation est établi dans le diocèse de Lausanne et à Fribourg dès le début jusqu'à la deuxième moitié
du XVe siècle, en cas du diocèse de Lausanne jusqu'à la première moitié du XVIe.

Dans SDS FR I/2/6 le style de l'Annonciation apparaît sous forme de n. st. (= nouveau style), mais la date est résolue
selon le calendrier moderne.

> Exemple : 5. Ordonnance au sujet des voies de fait.
> [[http://www.ssrq-sds-fds.ch/online/FR_I_2_6/index.html#p_5]](http://www.ssrq-sds-fds.ch/online/FR_I_2_6/index.html#p_5)
> 1364 (n. st.) février 4.
> Dans la source on trouve la datation suivante : ... le quatre jour
> du mois de février en l’ans Notre Seigneur courant 1363 ...

Comme le 4 février se trouve dans la période entre le 1er janvier (ou entre le 25 décembre) et le 25 mars
(= Annonciation), l'éditrice a correctement repris le 4 février 1363 comme le 4 février 1364.

# Dates fixes et délais

Des dates fixes (délais de pâturage, saison de chasse restreinte etc.) sont également indiquées avec
[[date]](date.fr.md) et @when. Pour signaler qu'il s'agit d'une date fixe ou d'un délai, il faut ajouter
dans @type la valeur "deadline".

Par exemple pour une date fixe :
> wellind und doch nit länger dann bis `<date type="deadline" when="--04-16">zuͦ mittem aprellen</date>`

Un délai de grâce pour les poissons du 3 janvier au 4 mars :

`<date from="--01-03" to="--03-04"/>`

Des jours de fête sans date fixe, p.e. le carême de mercredi des Cendres à vendredi saint, sont résolus avec la
taxonomie.
