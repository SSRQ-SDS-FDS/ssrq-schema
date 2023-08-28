# Folgendes Beispiel ist als Beispiel für p zu übernehmen

{{Sprachen}}

=== Strukturierung von Schlussformeln wie «actum», «coram consilio», «presentibus» etc. === <!--T:1-->

<!--T:2-->
* «Actum» wird abgesetzt.
* Nach «actum» folgt nach einem Komma «coram consilio», «coram senatu», «presentibus» etc.
* Punkt am Ende der Formeln.


=== Beispiele=== <!--T:3-->

<!--T:4-->
*''Beispiel 1'' (StAZH A 99.5, Nr. 136 - Editionsstück mit Digitalisat im Portal):

<!--T:5-->
[[File:StAZH_A99_5_136.gif|StAZH A 99.5, Nr. 136]]

<!--T:6-->
In der Vorlage steht «coram senatu» eingerückt auf einer neuen Zeile, dennoch wird es nicht speziell mit <[[p]]> abgesetzt, sondern mit einem Komma angefügt. Ein <[[lb]]> ist am Zeilenanfang vor «coram senatu» zu setzten, da eine Einrückung hier genauso behandelt wird, wie wenn der Text nach dem Zeilenumbruch bündig weiterfährt. 

<!--T:7-->
<pre>
<p>
 <lb/>Actum montags, den <origDate when="1671-06-19" calendar="Julian">19<hi rend="sup">ten</hi> juny anno 1671</origDate>, 
 <lb/>coram <orgName>senatu</orgName>.
</p>
<p>
 <lb/>Stattschryber 
      <choice>
       <abbr>ßt</abbr>
       <expan>scripsit</expan>
      </choice>. 
</p> 
</pre>

<!--T:8-->
Das «scripsit» wird, da auch quellennah abgesetzt, mit <[[p]]> abgesetzt. Wäre es in der Vorlage auf der gleichen Zeile wie das «coram senatu» müsste ein <[[seg]]> eingefügt werden, um einen Abschnitt in der normalisierten Fassung herbeizuführen.

<!--T:9-->
Zum Setzen des Punktes bei «Stadtschreiber scripsit» vgl. [[Interpunktion]].

# Folgendes Beispiel ist als Beispiel für seg zu übernehmen

{{Sprachen}}

<!--T:1-->
Urkunden sollten gemäss ihrem formalen Aufbau strukturiert werden (vgl. Diplomatik z. B. [http://www.hist-hh.uni-bamberg.de/hilfswiss/diplomatik.html], [http://wwws.phil.uni-passau.de/histhw/TutMA/hiwi2.html], [http://theleme.enc.sorbonne.fr/cours/diplomatique]).


=== Datierung === <!--T:2-->

<!--T:3-->
Die Datierung (Datum, Actum etc.) wird mit einem Absatz <[[seg]]> optisch abgesetzt.


<pre>
...
<seg>
Und deß zuͦ warem und vestem urkunde, so hatt der from, wys, unnser gethruwer, lieber lanndt
<lb break="no"/>vogt zuͦ Baden im Ergöw Jacob An der Rütty, des rats zuͦ Schwytz, sin eigen insigel, 
innamen unnser aller, gehennckt an disen brieff.</seg>
<seg>Der geben ist <date when-custom="1453-08-11" dating-method="julian">uff den einlifften tag ougstens, nach der gepurt 
<lb/>Christi getzalt, tusent fünffhundert viertzig und drü jare</date>. 
</seg>
</pre>
