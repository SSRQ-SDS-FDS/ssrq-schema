---
title: Directives de datation
---

# Principes

- uniformiser le plus possible
- récupération selon les langues (coutumes linguistiques) : DE, FR, IT
- le style de la Circoncision (début de l\'année le 1 janvier), de
  l\'Annonciation (25 mars) ou de la Nativité (25 décembre) doit être
  indiqué

*Principes spéciales pour la rétronumérisation*

- datation reprises selon le volume
- reprise de l\'entrée originale dans l\'index possible (seulement
  pour des cas problématiques)
- présentation sous forme de « index chronologique » possible
- récupération selon les langues (coutumes linguistiques) : DE, FR, IT
- le style de la Circoncision (début de l\'année le 1er janvier), de
  l\'Annonciation (25 mars) ou de la Nativité (25 décembre) doit être
  indiqué
- plusieurs tags \<[date](date/fr "wikilink")\> dans l\'index sont
  possibles (pour la rétronumérisation), mais pas pour l\'édition
  numérique.

= Datation certaine =
(avec un texte de datation certaine) :

• Les dates sont normalisées selon ISO 8601 dans [[@when/fr|@when]] (YYYY-MM-DD). Selon ISO 8601 et TEI, @when comprend
toujours le calendrier grégorien. Depuis 2019 : [[@when-custom/fr|@when-custom]]
avec [[@datingMethod/fr|@datingMethod]].

• Les degrés hiérarchiques supérieurs de la datation (année, mois) sont indiqués dans @when avec un tiret ("-"). Les
degrés inférieurs qui font par exemple défaut (le jour n'est pas connu) ne sont pas signalés de façon particulière.

• La datation selon les jours de fêtes/des saints sont résolu à l'aide du Grotefend. Sur le site
web : http://www.manuscripta-mediaevalia.de/gaeste/grotefend/grotefend.htm il existe différents outils ainsi qu'un
calculateur (Rechner).

Exemples :

<font size="3"><pre><date when="2001">The year 2001</date>
<date when="2001-09">September 2001</date>
<date when="2001-09-11">11 Sept 01</date>
<date when="--09-11">9/11</date>
<date when="--09">September</date>
<date when="---11">Eleventh of the month</date></pre></font>

Selon :  [http://www.tei-c.org/release/doc/tei-p5-doc/en/html/CO.html#CONADA  TEI] (18.01.2011)

= Datation problématique =
(texte de datation)

== 1. Plusieurs datations dans une pièce (rétronumérisation)==

Il faut utiliser plusieurs éléments de datations. (L'utilisation de plusieurs éléments de datation doit être commentée
et se référer à la pièce. La datation de commentaires, de pièces similaires ou de copies ne font pas l'objet de cette
datation (éventuellement utiliser <[[note/fr|note]]> dans ces cas). En générale, ces datations sont traitées de la même
façon.)


<pre><date when="1736-11-08">1736 November 8 / 22</date>
<date when="1736-11-22"/></pre>

== 2. Durées de temps ou périodes ==

Des durées de temps ou périodes sont indiquées dans <[[date/fr|date]]> à l'aide des attributs [[@from/fr|@from]]
et [[@to/fr|@to]]. Depuis 2019 : [[@from-custom/fr|@from-custom]] et [[@to-custom/fr|@to-custom]]
avec [[@datingMethod/fr|@datingMethod]].

1521 décembre 11 – 1544 avril 16:
<font size="3"><pre><date from-custom="1521-12-11" to-custom="1544-04-16" datingMethod="#julian">1521 Dezember 11 - 1544
April 16</date></pre></font>

1717–1718
<font size="3"><pre><date from-custom="1717" to-custom="1718" datingMethod="#gregorian">1717-1718</date></pre></font>

== 3. Des durées de temps ou périodes interrompues ==

(Une explication doit être éffectuée comme sous point 1)
Rétronumérisation : Les durées de temps ou périodes sont codées dans plusieurs tags :

1610, 1620–1635:
<font size="3"><pre>Rétronumérisation :<date when="1610">1610,
1620–1635</date><date from="1620" to="1635"/></pre></font>

1466, 25 mai et 25 juillet (Heumonat):
<font size="3"><pre>Rétronumérisation :<date when="1466-05-25">1466, 25. Mai und 25.
Heumonat</date><date when="1466-07-25"/></pre></font>

== 4. Datation ambiguë, mais qui peut être résolues ==

Rétronumérisation : Une indication de l'an ambiguë, p.e. "probablement 1491", est repris
avec <[[precision/fr|precision]] et les attribut [[@match/fr|@match]] et [[@degree/fr|@degree]].

<pre><date when="1491">wohl 1491<precision match="@when" degree="0.5"/></date></pre>


Des datations qui ne sont pas claires, mais qui peuvent être résolues, sont codées comme des intervalles.

''à chaque fois avec [[@from/fr|@from]], [[@to/fr|@to]], depuis
2019 [[@from-custom/fr|@from-custom]], [[@to-custom/fr|@to-custom]] avec [[@datingMethod/fr|@datingMethod]]''

{| border="1" cellpadding="5" cellspacing="0"
|-
|Exemple
|Valeurs<br/>@from-custom & @to-custom
|Période:<br/> clé
|-
|XVIIe siècle.
|1601/1700
|siècle : 100
|-
|première moitié du XVe siècle
|1401/1450
|moitié : 50
|-
|}

<font size="3"><pre><date from-custom="1401" to-custom="1450" datingMethod="#julian">première moitié du XVe
siècle</date></pre></font>

'' à chaque fois avec @notBefore, @notAfter, depuis
2019 [[@notBefore-custom/fr|@notBefore-custom]], [[@notAfter-custom/fr|@notAfter-custom]]
et <[[precision/fr|precision]] [[@match/fr|@match]][[@degree/fr|@degree]]>''

{| border="1" cellpadding="5" cellspacing="0"
|-
|Exemple
|Valeurs<br/>@notBefore-custom & @notAfter-custom
|Période:<br/> clé
|-
|fin du XVe siècle
|1475/1500
|fin: 25 ans
|-
|env. 1510
|1500/1520
|env.: +/-10 ans
|-
|fin mars
|03-21/03-31
|fin: 10 jours
|-
|début juillet
|07-01/07-10
|début: 10 jours
|-
|}

Les datations qui se réfèrent à la date originale du document (exemple en dessous, si le document a été rédigé en juin
1438):
{| border="1" cellpadding="5" cellspacing="0"
|-
|Exemple
|Valeurs <br/>@when & @dur<br/>
|-
|il y a 5 ans
|when="1433"<br/> dur="P5Y"
|-
|il y a 3 mois
|when="1438-03"<br/> dur="P3M"
|-
|vor 1 Jahre und 2 Monaten
|when="1437-04"<br/> dur="P1Y2M"
|-

|}

<font size="3"><pre>Rétronumérisation : <date notBefore="1500" notAfter="1520">env.
1510<precision match="@notBefore, @notAfter" degree="0.5"/></date>
<date notBefore="1386-07-01" notAfter="1386-07-10">1386 début juillet<precision match="@notBefore, @notAfter"
degree="0.5"/></date></pre></font>

<font size="3"><pre>Portail : <date notBefore-custom="1500" notAfter-custom="1520" datingMethod="#julian">env.
1510<precision match="@notBefore-custom, @notAfter-custom" degree="0.5"/></date>
<date notBefore-custom="1386-07-01" notAfter-custom="1386-07-10" datingMethod="#julian">1386 début juillet<precision
match="@notBefore-custom, @notAfter-custom"
degree="0.5"/></date></pre></font>

== 5. datation ambiguë qui ne peuvent pas être résolues ==

Des datations qui ne sont pas claires et qui ne peuvent pas être résolues, doivent si possible être codées commes des
intervalles (analogue à 4., le plus proche possible) :

'' à chaque fois avec [[@notBefore/fr|@notBevore]], [[@notAfter/fr|@notAfter]],
depuis [[@notBefor-custom/fr|@notBefore-custom]], [[@notAfter-custom/fr|@notAfter-custom]]
et <[[precision/fr|precision]] [[@match/fr|@match]][[@degree/fr|@degree]]>''

{| border="1" cellpadding="5" cellspacing="0"
|-
|Exemple
|Valeurs<br/>@notBefore-custom & @notAfter-custom
|Période:<br/> clé
|-
|avant 1688
|1638/1688
|avant : -50 ans
|-
|après 1688
|1688/1738
|après : +50 ans
|-
|autour de 1500, sans date
|1490/1510
|autour : +/-10 ans
|-
|1730 [après le 20 novembre]
|1730-11-21/1730-12-31
|jusqu'à la fin de l'année
|}

Des datations ''post quem'' ne doivent pas être mises en question, mais la date indiquée pour le début et la fin.

<font size="3"><pre><date notBefore-custom="1730-11-21" notAfter-custom="1730-12-31" datingMethod="#gregorian">1730
[après le 20 novembre]<precision match="@notAfter-custom" degree="0.5"/></date></pre></font>

== 6. "falsification" / changement de date ==

En général on part de la conclusion de l'éditeur (surtout dans le regeste – une éventuelle datation divergente est de
toute façon indiquée dans le texte et doit être signalée).

== 7. Style nouveau / style ancien ==

'' Règles générales : ''

1. En général, la datation est faite selon le style nouveau. Si un document n'est pas issu d'une instance publique qui
   date manifestement selon le style ancien (p.e. les chancelleries de Zurich et de Berne), on peut conclure en cas
   d'une date non commentée qu'il s'agit du nouveau style.

2. Les datation selon le style ancien ou selon les deux styles sont saisies dans une annotation critique, mais pas dans
   le regeste.

3. En cas de doute sur le style de la datation, il faut laisser un commenter dans une annotation critique.

'' Edition numérique : ''

Calendrier julien (style ancien)

La date indiqueé dans la pièce éditée voire le texte de datation est laissé tel quel. La normalisation et la
signalisation des dates ou des périodes se fait avec les attributs nécessaires selon le style ISO, c'est-à-dire selon le
calendrier grégorien voire le style nouveau. En outre, il faut ajouter la valeur "Julian" dans l'attribut @calendar.

<font size="3"><pre><date from="1588-09-13" to="1588-09-30" calendar="Julian">Zwischen 3. und 20 September
1588</date></pre></font>

'' Règles spéciales pour la rétronumérisation '' :

Tant la date grégorienne que la date julienne doivent être saisies dans l'index selon le style ISO. Si les deux
datations sont données, on attribue aux deux les valeurs correspondantes "Julian" ou "Gregorian" dans
l'attribut [[@calendar/fr|@calendar]]. Si dans l'index n'apparaît qu'une sorte de datation elle n'est pas spécialement
signalée, mais supposée grégorienne.

<font size="3"><pre><date from="1588-09-03" to="1588-09-20" calendar="Julian">Zwischen 3. und 20. September 1588</date>
<date when="1588-09-13" to="1588-10-30" calendar="Gregorian">Zwischen 13. und 30. September 1588</date></pre></font>

Voir également l'article Calendriers dans le DHS :http://www.hls-dhs-dss.ch/textes/f/F12812.php

Pour une conversion automatique du style ancien dans le style
nouveau : http://www.manuscripta-mediaevalia.de/gaeste/grotefend/grotefend.htm (Rechner)

=== Changement du calendrier ===

Lucerne: le jour du changement: le 12 janvier 1584 ancien style = 22 janvier 1584 style nouveau<ref>StALU RP 39, fol.
7r.</ref>

'''Références'''
<references />

== 8. Style de début de l'année ==

Les différents styles de début de l'année [Circoncision (1er janvier), Annonciation (25 mars) ou Nativité (25 décembre)]
doivent être annotés dans <date> à l'aide de [[@calendar/fr|@calendar]].

''' Style de l'Annonciation '''

Le style de l'Annonciation est établi dans le diocèse de Lausanne et à Fribourg dès le début jusqu'à la deuxième moitié
du XVe siècle, en cas du diocèse de Lausanne jusqu'à la première moitié du XVIe.

Dans SDS FR I/2/6 le style de l'Annonciation apparaît sous forme de n. st. (= nouveau style), mais la date est résolue
selon le calendrier moderne.

Exemple :

5. Ordonnance au sujet des voies de fait. http://www.ssrq-sds-fds.ch/online/FR_I_2_6/index.html#p_5
   1364 (n. st.) février 4.
   Dans la source on trouve la datation suivante : ... le quatre jour
   du mois de février en l’ans Notre Seigneur courant 1363 ...

Comme le 4 février se trouve dans la période entre le 1er janvier (ou entre le 25 décembre) et le 25 mars (=
Annonciation), l'éditrice a correctement repris le 4 février 1363 comme le 4 février 1364.

= Dates fixes et délais =

Des dates fixes (délais de pâturage, saison de chasse restreinte etc.) sont également indiquées avec <[[date/fr|date]]>
et [[@when/fr|@when]]. Pour signaler qu'il s'agit d'une date fixe ou d'un délai, il faut ajouter dans [[@type/fr|@type]]
la valeur "deadline".

Par exemple pour une date fixe :<pre>wellind und doch nit
länger dann bis <date type="deadline" when="--04-16">zuͦ mittem aprellen</date>
</pre>


Un délai de grâce pour les poissons du 3 janvier au 4 mars :

<pre>
<date from="--01-03" to="--03-04"></date>
</pre>


Des jours de fête sans date fixe, p.e. le carême de mercredi des Cendres à vendredi saint, sont résolus avec la
taxonomie.
