# Sonderzeichen

Alle Sonderzeichen werden in Unicode kodiert, ihre Darstellung erfolgt mithilfe
der SSRQ-Schrift Lexia Fontes für die lateinische Schrift sowie der Libertinus
Serif für die griechische und die hebräische Schrift.

## Akzente und Diakritika

### Allgemeine Regeln

=== "Deutsche Texte"

    Diakritische Zeichen und übergeschriebene Buchstaben der 
    deutschen Texte werden buchstabengetreu wiedergegeben.
    
    Distinktionszeichen über `u`, die in deutschen Texten einer Verwechslung 
    mit `n` vorbeugen sollen, werden nicht wiedergegeben.

=== "Lateinische Texte"

    e caudata (`ę`) wird vom gewöhnlichen `e` unterschieden.

    Die Gelehrten des 17. und 18. Jahrhunderts neigten aufgrund von 
    Hyperkorrekturen dazu, die Diphthongierung zu bevorzugen.

    Wenn ein mittelalterliches Original erhalten ist, sollte die Schreibweise des
    Ausgangstextes beibehalten werden, d. h. das `ę`, das in späteren Kopien
    wahrscheinlich als `æ` geschrieben wurde, sollte wiedergegeben werden.
    Wenn nur die spätere Abschrift existiert, sollte man sich an die Schreibweise
    dieser Abschrift halten und den Diphthong getreu wiedergeben.

=== "Französische und italienische Texte"

    Die diakritischen Zeichen des Französischen und Italienischen werden gemäss
    dem modernen Gebrauch verwendet, sofern keine Ausnahmen vorliegen.

    Bei der Akzentsetzung sollte in einem Textkorpus ein kohärentes System 
    angewendet werden, das sich so weit wie möglich an den graphischen und 
    typographischen Gepflogenheiten der jeweiligen Zeit orientiert.

### Sonderregeln für französische Texte

=== "Mittelalterliche Hss."

    Bei mittelalterlichen französischen Handschriften sollten keine Akzente
    hinzugefügt werden, ausser wenn dadurch homophone Verwechslungen aufgrund
    des atonalen und des tonischen `e` vermieden werden können. So erhalten
    Endsilben auf `-e` oder `-es` einen Akzent.

    Beispiele:  
    afrz. `aprés` meint frz. `après` (nach)  
    afrz. `apres` steht für frz. `âpres` (bitter)  
    afrz. `leve` meint frz. `lève`,  
    während afrz. `levé` das Partizip des Verbs afrz. `lever` (hochheben) ist
    
    Der Artikel afrz. `des` wird immer unverändert transkribiert, also `des`
    und nicht `dés`.

=== "Hss. 16. Jh."

    Für französische Texte des 16. Jhs. (bis ca. 1580) gelten die Standards,
    die für die Edition mittelalterlicher französischer Texte festgelegt wurden.
    Es wird nur der Akzent auf dem Buchstaben `e` verwendet, um zwischen
    tonischem und atonischem `e` zu unterscheiden.
    
    Beispiele:  
    mfrz. `né`, `tombé`, `vous avés`, `aprés`, `procés`
    
    Endungen auf `-ee` werden nicht betont.
    
    Beispiele:  
    mfrz. `nee`, `armee`

=== "Hss. 17. Jh."

    Bei der Bearbeitung von französischen Handschriften aus dem 17. Jh.
    (bis ca. 1715) können Akzente in grösserem Umfang verwendet werden.
    Insbesondere werden die Endungen auf `-ée` betont.

    Beispiele:  
    frz. `née`, `armée`
    
    Der Akzent auf den Buchstaben `a`, `e` und `u` in einsilbigen Präpositionen
    und Adverbien wird verwendet, um sie von homographen Wörtern zu 
    unterscheiden.
    
    Beispiele:  
    frz. `à`, `là`, `dès`, `lès`, `où`
    
    Dagegen wird der Buchstabe `e` innerhalb eines Wortes nicht betont.
    
    Beispiele:  
    frz. `maniere`, `pere`, `present`

=== "Hss. 18. Jh."
    
    Auf französische Handschriften des 18. Jahrhunderts wird der heutige
    Sprachgebrauch angewendet.

### Bestimmte Diakritika in französischen Texten

=== "Trema"

    Grundsätzlich sollte ein Trema, wenn es in Wörtern vorkommt, die heute ohne 
    Trema geschrieben werden, entfernt werden. Dasselbe gilt für `ÿ` (vgl. 
    [Normalisierung](normalization.de.md)).

    Beispiele:  
    frz. `queüe`, `veü`

    In mittelalterlichen literarischen Texten kann das Trema eine phonetische 
    Funktion haben, in diesem Fall wird es beibehalten.

=== "Cedille (`ç`)"

    Dem `c`, das einen phonetischen Wert als /s/ hat, soll eine Cedille 
    hinzugefügt werden.
    
    Beispiele:  
    `François` und nicht `Francois`  
    `il sçait` und nicht `il scait`

=== "Apostroph"

    Um die Bedeutung eines Textes zu verdeutlichen und ihn verständlicher zu 
    machen, ist das Hinzufügen von Apostrophen unerlässlich. Beispielsweise muss
    die Schreibweise `se` für `c’est` mit `s’e` wiedergegeben werden. Da das 
    Pronomen der dritten Person Singular und Plural oft auf `i` reduziert wird, 
    muss ihm ein Apostroph vorangestellt werden, wenn es mit einem Relativpronomen 
    oder einer Konjunktion verbunden ist, damit `qui` nicht mit `qu’il` 
    verwechselt wird.

    Beispiel:  
    ```Item ledit detenu a dit et confesé que illiaz quattre ans qu’i 
    deroba une boiste avec l’estuy.```

    Das oben genannte Beispiel zeigt auch, dass ein Apostroph hinzugefügt werden
    sollte, um den bestimmten Artikel, der mit einem Substantiv verbunden sein 
    könnte, zu trennen.

    Beispiel:  
    `l’estuy` und nicht `lestuy`

    Wenn die Kombination `quil` als relative Präposition fungiert, sollte sie so 
    transkribiert werden.

    Beispiel:  
    ```Item for celuy quil allat querir le maistre d’ovre```

## Ligaturen

In Drucken werden Ligaturen in Einzelbuchstaben aufgelöst und auch in 
handschriftlichen Texten wird auf die Verwendung von Ligaturen in der
Regel verzichtet.

Ausnahmen: Eigene Zeichen können für die Ligaturen `Æ`, `æ`,
`Œ`, `œ` und `ß` verwendet werden.

Zum Beispiel kann anstelle von e caudata (`ę`) in einer späteren Kopie durch
Hyperkorrektur die Schreibweise `æ` entstehen.

Der Bearbeitende muss sich darüber im Klaren sein, dass `æ` und `ae` in der 
digitalen Textverarbeitung nicht denselben Wert haben und nicht als 
identisches Graphem erkannt werden.

Sonstige Ligaturen, die vor allem typographischen Charakter haben, 
werden nicht mit eigenen Unicodezeichen kodiert, sondern einfach nur durch die 
beiden aufeinanderfolgenden Grundbuchstaben, also:
`ff`, `fi`, `fl`, `ffi`, `ffl` und nicht `ﬀ`, `ﬁ`, `ﬂ`, `ﬃ`, `ﬄ`.

## Brüche

In Unicode gibt es zwar eine Reihe von speziellen Bruchzeichen, die für
die häufigsten Brüche gedacht sind, diese sollten jedoch nicht verwendet
werden, weil sie nicht alle in den Texten vorkommenden Fälle abdecken.
Stattdessen sollten Brüche mit dem Tag [`<num>`](num.de.md)
kodiert werden:

Beispiele:  
`<num value="0.5">1/2</num>` und nicht `½`  
`<num value="0.75">3/4</num>` und nicht `¾`

## Code-Tabelle für Sonderzeichen

Die unten stehende Tabelle zeigt, wie die einzelnen Zeichen kodiert werden sollten.

Dabei gilt, dass es für einige der angegebenen Zeichen mehrere Möglichkeiten
der Codierung gibt. So kann beispielsweise das e caudata sowohl als einzelnes
Zeichen `ę` (U+0119) kodiert werden als auch als Grundbuchstabe
`e` (U+0065) mit einem kombinierenden Ogonek `ę` (U+0328).

Grundsätzlich wird die kombinierende Variante bevorzugt, weil die kombinierenden
Zeichen an alle Grundbuchstaben angehängt werden können.
Z. B. lassen sich `Ą ą Ę ę Į į Ǫ ǫ Ų ų` erzeugen, indem, wie beim e caudata, zuerst
der Grundbuchstabe eingegeben wird und anschliessend das kombinierende Ogonek.
In der Tabelle wird daher bei kombinierenden Zeichen beispielhaft das `a`
verwendet, für die anderen Grundbuchstaben erfolgt die Eingabe analog.

Ausnahme: Der Einfachheit halber können die deutschen Umlaute `Ä ä Ö ö Ü ü`
direkt als Einzelzeichen eingegeben werden und müssen nicht als Grundbuchstabe mit 
kombinierendem Trema (U+0308) erfasst werden. 

| Beschreibung                            | Zeichen               | Unicode-Codepunkt(e) |
|-----------------------------------------|-----------------------|----------------------|
| **Ligaturen**                           |                       |                      |
| A+E-Ligatur                             | `Æ`                   | U+00C6               |
| a+e-Ligatur                             | `æ`                   | U+00E6               |
| O+E-Ligatur                             | `Œ`                   | U+0152               |
| o+e-Ligatur                             | `œ`                   | U+0153               |
| s+z-Ligatur                             | `ß`                   | U+00DF               |
| **Kombinierende Diakritika**            |                       |                      |
| Buchstabe mit Gravis                    | `à`                  | a + U+0300           |
| Buchstabe mit Akut                      | `á`                  | a + U+0301           |
| Buchstabe mit Zirkumflex                | `â`                  | a + U+0302           |
| Buchstabe mit Tilde                     | `ã`                  | a + U+0303           |
| Buchstabe mit Längenzeichen             | `ā`                  | a + U+0304           |
| Buchstabe mit Punkt                     | `ȧ`                  | a + U+0307           |
| Buchstabe mit Trema                     | `ä`                  | a + U+0308           |
| Buchstabe mit Haken                     | `ǎ`                  | a + U+030C           |
| Buchstabe mit vertikalem Strich         | `a̍`                  | a + U+030D           |
| Buchstabe mit Cedille                   | `a̧`                  | a + U+0327           |
| Buchstabe mit Ogonek                    | `ą`                  | a + U+0328           |
| **Kombinierende Superkripte**           |                       |                      |
| Buchstabe mit Superskript a             | `aͣ`                  | a + U+0363           |
| Buchstabe mit Superskript e             | `aͤ`                  | a + U+0364           |
| Buchstabe mit Superskript i             | `aͥ`                  | a + U+0365           |
| Buchstabe mit Superskript o             | `aͦ`                  | a + U+0366           |
| Buchstabe mit Superskript u             | `aͧ`                  | a + U+0367           |
| Buchstabe mit Superskript v             | `aͮ`                  | a + U+036E           |
| Buchstabe mit Superskript w             | `a`                  | a + U+F03C           |
| **Sonstige modifizierte Buchstaben**    |                       |                      |
| h mit Strich                            | `ħ`                   | U+0127               |
| i mit Strich                            | `Ɉ`                   | U+0248               |
| i mit zwei Strichen                     | ``                   | U+E8A1               |
| j mit Strich                            | `ɉ`                   | U+0249               |
| j mit zwei Strichen                     | ``                   | U+E8A1               |
| q mit Strich                            | `ꝗ`                   | U+A757               |
| t mit Strich                            | `ŧ`                   | U+0167               |
| v mit Strich                            | ``                   | U+E8BB               |
| v mit diagonalem Strich                 | `ꝟ`                   | U+A75F               |
| v mit zwei Strichen                     | ``                   | U+E8BC               |
| x mit Strich oben                       | ``                   | U+E8BD               |
| x mit Strich unten                      | ``                   | U+E8BE               |
| x mit zwei Strichen unten               | ``                   | U+E8CE               |
| **Währungen und Einheiten**             |                       |                      |
| Floren                                  | ``                   | U+F2E8               |
| Groschen                                | ``                   | U+F2E9               |
| Helbling                                | ``                   | U+F2FB               |
| Krone                                   | ``                   | U+F2FA               |
| Pfennig                                 | `₰`                   | U+20B0               |
| Pfund (Währung)                         | ``                   | U+F2EA               |
| Pfund (Gewicht)                         | `℔`                   | U+2114               |
| Schilling                               | ``                   | U+F2F7               |
| Scudi                                   | ``                   | U+F2F9               |
| **Sonstige Symbole**                    |                       |                      |
| Zeigehand                               | `☛`                   | U+261B               |
| Paragraphenzeichen                      | `§`                   | U+00A7               |
| Absatzzeichen                           | `¶`                   | U+00B6               |
| Copyrightzeichen                        | `©`                   | U+00A9               |
| Kreuz                                   | `†`                   | U+2020               |
| Doppelkreuz                             | `‡`                   | U+2021               |
| Dreifachkreuz                           | ``                   | U+F1D2               |
| **Satzzeichen**                         |                       |                      |
| Halbgeviertstrich                       | `–`                   | U+2013               |
| Hochpunkt                               | `·`                   | U+00B7               |
| Auslassungszeichen                      | `…`                   | U+2026               |
| Ein Punk vor zweien                     | `⁖`                   | U+2056               |
| Ein Punkt über zweien                   | `∵`                   | U+2235               |
| Vier Punkte                             | `⁘`                   | U+2058               |
| Einfache vertikale Linie                | <code>&#x007c;</code> | U+007C               |
| Doppelte vertikale Linie                | `‖`                   | U+2016               |
| Doppelter Solidus                       | `⫽`                   | U+2AFD               |
| Apostroph                               | `’`                   | U+2019               |
| Einfaches dt. Anführungszeichen links   | `‚`                   | U+201A               |
| Einfaches dt. Anführungszeichen rechts  | `‘`                   | U+2018               |
| Doppelte dt. Anführungszeichen links    | `„`                   | U+201E               |
| Doppelte dt. Anführungszeichen rechts   | `“`                   | U+201C               |
| Einfaches frz. Anführungszeichen links  | `‹`                   | U+2039               |
| Einfaches frz. Anführungszeichen rechts | `›`                   | U+203A               |
| Doppelte frz. Anführungszeichen links   | `«`                   | U+00AB               |
| Doppelte frz. Anführungszeichen rechts  | `»`                   | U+00BB               |
