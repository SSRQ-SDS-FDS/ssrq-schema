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

Für einige der angegebenen Zeichen hat es mehrere Möglichkeiten der Codierung: 
So kann beispielsweise das e caudata sowohl als einzelnes Zeichen `ę` (U+0119) kodiert werden als 
auch als Grundbuchstabe `e` (U+0065) mit einem kombinierenden Ogonek `ę` (U+0328).
Z. B. lassen sich `Ą ą Ę ę Į į Ǫ ǫ Ų ų` erzeugen, indem, wie beim e caudata, zuerst
der Grundbuchstabe eingegeben wird und anschliessend das kombinierende Ogonek.

Es können bei Bedarf auch mehrere kombinierende Zeichen mit einem Grundbuchstaben verwendet werden,
z. B. `ā̧` (= a + kombinierendes Längenzeichen + kombinierende Cedille) oder `uͦ̈` (= o + Superskript 
o + kombinierendes Trema).

Grundsätzlich gilt, dass die kombinierende Variante bevorzugt wird, weil die kombinierenden
Zeichen an alle Grundbuchstaben angehängt werden können. Ausnahme: Der Einfachheit halber können 
die deutschen Umlaute `Ä ä Ö ö Ü ü` direkt als Einzelzeichen eingegeben werden und müssen nicht 
als Grundbuchstabe mit kombinierendem Trema (U+0308) erfasst werden.

In der Tabelle wird daher bei kombinierenden Zeichen beispielhaft das `a`
verwendet, für die anderen Grundbuchstaben erfolgt die Eingabe analog.

| Beschreibung                            | Sonderzeichen         | Unicode-Codepunkt(e) |
|-----------------------------------------|-----------------------|----------------------|
| **Ligaturen**                           |                       |                      |
| A+E-Ligatur                             | `Æ`                   | U+00C6               |
| a+e-Ligatur                             | `æ`                   | U+00E6               |
| O+E-Ligatur                             | `Œ`                   | U+0152               |
| o+e-Ligatur                             | `œ`                   | U+0153               |
| s+z-Ligatur                             | `ß`                   | U+00DF               |
| **Kombinierende Diakritika**            |                       |                      |
| Buchstabe mit Gravis                    | `à`                  | Buchstabe + U+0300   |
| Buchstabe mit Akut                      | `á`                  | Buchstabe + U+0301   |
| Buchstabe mit Zirkumflex                | `â`                  | Buchstabe + U+0302   |
| Buchstabe mit Tilde                     | `ã`                  | Buchstabe + U+0303   |
| Buchstabe mit Längenzeichen             | `ā`                  | Buchstabe + U+0304   |
| Buchstabe mit Punkt                     | `ȧ`                  | Buchstabe + U+0307   |
| Buchstabe mit Trema                     | `ä`                  | Buchstabe + U+0308   |
| Buchstabe mit Haken                     | `ǎ`                  | Buchstabe + U+030C   |
| Buchstabe mit vertikalem Strich         | `a̍`                  | Buchstabe + U+030D   |
| Buchstabe mit Cedille                   | `a̧`                  | Buchstabe + U+0327   |
| Buchstabe mit Ogonek                    | `ą`                  | Buchstabe + U+0328   |
| **Kombinierende Superkripte**           |                       |                      |
| Buchstabe mit Superskript a             | `aͣ`                  | Buchstabe + U+0363   |
| Buchstabe mit Superskript e             | `aͤ`                  | Buchstabe + U+0364   |
| Buchstabe mit Superskript i             | `aͥ`                  | Buchstabe + U+0365   |
| Buchstabe mit Superskript o             | `aͦ`                  | Buchstabe + U+0366   |
| Buchstabe mit Superskript u             | `aͧ`                  | Buchstabe + U+0367   |
| Buchstabe mit Superskript v             | `aͮ`                  | Buchstabe + U+036E   |
| Buchstabe mit Superskript w             | `a`                  | Buchstabe + U+F03C   |
| **Sonstige modifizierte Buchstaben**    |                       |                      |
| i mit Strich (= eineinhalb)             | `ɨ`                   | U+0268               |
| i mit zwei Strichen                     | ``                   | U+E8A1               |
| j mit Strich                            | `ɉ`                   | U+0249               |
| j mit zwei Strichen                     | ``                   | U+E8A2               |
| q mit Strich                            | `ꝗ`                   | U+A757               |
| t mit Strich                            | `ŧ`                   | U+0167               |
| v mit Strich (= viereinhalb)            | ``                   | U+E8BB               |
| v mit diagonalem Strich                 | `ꝟ`                   | U+A75F               |
| v mit zwei Strichen                     | ``                   | U+E8BC               |
| x mit Strich oben                       | ``                   | U+E8BD               |
| x mit Strich unten  (= neuneinhalb)     | ``                   | U+E8BE               |
| x mit zwei Strichen unten               | ``                   | U+E8CE               |
| **Währungen und Einheiten**             |                       |                      |
| Florin                                  | ``                   | U+F2E8               |
| Gulden                                  | ``                   | U+F2E9               |
| h mit Strich (= Haller)                 | `ħ`                   | U+0127               |
| Helbling                                | ``                   | U+F2FB               |
| Krone                                   | ``                   | U+F2FA               |
| Krone (alternativ)                      | ``                   | U+F2FC               |
| Pfennig/Denar                           | `₰`                   | U+20B0               |
| Pfund (Währung)                         | ``                   | U+F2EA               |
| Pfund (Gewicht)                         | `℔`                   | U+2114               |
| Schilling                               | ``                   | U+F2F7               |
| Scudo                                   | ``                   | U+F2F9               |
| **Sonstige Symbole**                    |                       |                      |
| Zeigehand                               | `☞`                   | U+261E               |
| Paragraphenzeichen                      | `§`                   | U+00A7               |
| Absatzzeichen                           | `¶`                   | U+00B6               |
| Kreuz                                   | `†`                   | U+2020               |
| Doppelkreuz                             | `‡`                   | U+2021               |
| Dreifachkreuz                           | ``                   | U+F1D2               |
| Heiratssymbol                           | `⚭`                   | U+26AD               |
| Kreissymbol                             | `○`                   | U+25CB               |
| Marssymbol (Abk. für Dienstag)          | `♂`                   | U+2642               |
| Copyrightsymbol                         | `©`                   | U+00a9               |
| **Satzzeichen und dergleichen**         |                       |                      |
| Ditto Mark (in Tabellen)                | `"`                   | U+0022               |
| Punkt (Kolon)                           | `.`                   | U+002E               |
| Komma                                   | `,`                   | U+002C               |
| Semikolon                               | `;`                   | U+003B               |
| Doppelpunkt                             | `:`                   | U+003A               |
| Hochpunkt                               | `·`                   | U+00B7               |
| Apostroph                               | `’`                   | U+2019               |
| Ausrufezeichen                          | `!`                   | U+0021               |
| Fragezeichen                            | `?`                   | U+003F               |
| Auslassungszeichen                      | `…`                   | U+2026               |
| Ein Punk vor zweien                     | `⁖`                   | U+2056               |
| Ein Punkt über zweien                   | `∵`                   | U+2235               |
| Vier Punkte                             | `⁘`                   | U+2058               |
| Halbgeviertstrich                       | `–`                   | U+2013               |
| Einfache vertikale Linie                | <code>&#x007c;</code> | U+007C               |
| Doppelte vertikale Linie                | `‖`                   | U+2016               |
| Doppelter Solidus                       | `⫽`                   | U+2AFD               |
| Einfaches frz. Anführungszeichen links  | `‹`                   | U+2039               |
| Einfaches frz. Anführungszeichen rechts | `›`                   | U+203A               |
| Doppelte frz. Anführungszeichen links   | `«`                   | U+00AB               |
| Doppelte frz. Anführungszeichen rechts  | `»`                   | U+00BB               |
| Malkreuz                                | `×`                   | U+00D7               |
| Ordinalzeichen (in 1º, 2º, etc.)        | `º`                   | U+00BA               |

## Griechische und hebräische Schrift

Passagen in griechischer und hebräischer Schrift werden ebenfalls direkt in Unicode kodiert.
Hierbei gilt, dass die griechischen Akzente, Spiritus sowie *iota subscriptum* bzw. 
*adscriptum* und die hebräischen Vokalisierungszeichen mit kombinierenden Zeichen dargestellt
werden sollen.
Als Beispiele hierfür dienen das gr. Alpha und das hebr. Alef.

| Beschreibung                                          | Sonderzeichen | Unicode-Codepunkt(e)                 |
|-------------------------------------------------------|---------------|--------------------------------------|
| **Griechische Buchstaben**                            |               |                                      |
| Alpha                                                 | `Α`, `α`      | U+0391, U+03B1                       |
| Beta                                                  | `Β`, `β`      | U+0392, U+03B2                       |
| Gamma                                                 | `Γ`, `γ`      | U+0393, U+03B3                       |
| Delta                                                 | `Δ`, `δ`      | U+0394, U+03B4                       |
| Epsilon                                               | `Ε`, `ε`      | U+0395, U+03B5                       |
| Zeta                                                  | `Ζ`, `ζ`      | U+0396, U+03B6                       |
| Eta                                                   | `Η`, `η`      | U+0397, U+03B7                       |
| Theta                                                 | `Θ`, `θ`      | U+0398, U+03B8                       |
| Iota                                                  | `Ι`, `ι`      | U+0399, U+03B9                       |
| Kappa                                                 | `Κ`, `κ`      | U+039A, U+03BA                       |
| Lambda                                                | `Λ`, `λ`      | U+039B, U+03BB                       |
| My                                                    | `Μ`, `μ`      | U+039C, U+03BC                       |
| Ny                                                    | `Ν`, `ν`      | U+039D, U+03BD                       |
| Xi                                                    | `Ξ`, `ξ`      | U+039E, U+03BE                       |
| Omikron                                               | `Ο`, `ο`      | U+039F, U+03BF                       |
| Pi                                                    | `Π`, `π`      | U+03A0, U+03C0                       |
| Rho                                                   | `Ρ`, `ρ`      | U+03A1, U+03C1                       |
| Sigma                                                 | `Σ`, `ς`, `σ` | U+03A3, U+03C2, U+03C3               |
| Tau                                                   | `Τ`, `τ`      | U+03A4, U+03C4                       |
| Ypsilon                                               | `Υ`, `υ`      | U+03A5, U+03C5                       |
| Phi                                                   | `Φ`, `φ`      | U+03A6, U+03C6                       |
| Chi                                                   | `Χ`, `χ`      | U+03A7, U+03C7                       |
| Psi                                                   | `Ψ`, `ψ`      | U+03A8, U+03C8                       |
| Omega                                                 | `Ω`, `ω`      | U+03A9, U+03C9                       |
| **Griechische Diakritika**                            |               |                                      |
| Buchstabe mit Gravis                                  | `ὰ`          | Buchstabe + U+0300                   |
| Buchstabe mit Akut                                    | `ά`          | Buchstabe + U+0301                   |
| Buchstabe mit Zirkumflex                              | `ᾶ`          | Buchstabe + U+0342                   |
| Buchstabe mit *spiritus lenis*                        | `ἀ`          | Buchstabe + U+0313                   |
| Buchstabe mit *spiritus asper*                        | `ἁ`          | Buchstabe + U+0314                   |
| Buchstabe mit *iota sub- bzw. adscriptum*             | `ᾳ`          | Buchstabe + U+0345                   |
| Buchstabe mit Spiritus und Akzent                     | `ἅ`         | Buchstabe + U+0314 + U+0301          |
| Buchstabe mit Spiritus, Akzent und *iota subscriptum* | `ᾅ`        | Buchstabe + U+0314 + U+0301 + U+0345 |
| **Hebräische Buchstaben**                             |               |                                      |
| Alef                                                  | `א`           | U+05D0                               |
| Bet                                                   | `ב`           | U+05D1                               |
| Gimel                                                 | `ג`           | U+05D2                               |
| Dalet                                                 | `ד`           | U+05D3                               |
| He                                                    | `ה`           | U+05D4                               |
| Waw                                                   | `ו`           | U+05D5                               |
| Sajin                                                 | `ז`           | U+05D6                               |
| Chet                                                  | `ח`           | U+05D7                               |
| Tet                                                   | `ט`           | U+05D8                               |
| Jud                                                   | `י`           | U+05D9                               |
| Kaf                                                   | `כ`, `ך`      | U+05DA, U+05DB                       |
| Lamed                                                 | `ל`           | U+05DC                               |
| Mem                                                   | `מ`, `ם`      | U+05DD, U+05DE                       |
| Nun                                                   | `נ`, `ן`      | U+05DF, U+05E0                       |
| Samech                                                | `ס`           | U+05E1                               |
| Ajin                                                  | `ע`           | U+05E2                               |
| Pe                                                    | `פ`, `ף`      | U+05E3, U+05E4                       |
| Zade                                                  | `צ`, `ץ`      | U+05E5, U+05E6                       |
| Kuf                                                   | `ק`           | U+05E7                               |
| Resch                                                 | `ר`           | U+05E8                               |
| Sin, Schin                                            | `ש`           | U+05E9                               |
| Taw                                                   | `ת`           | U+05EA                               |
| **Hebräische Diakritika**                             |               |                                      |
| Buchstabe mit Schwa                                   | `אְ`          | Buchstabe + U+05B0                   |
| Buchstabe mit Schwa und Seggol                        | `אֱ`          | Buchstabe + U+05B1                   |
| Buchstabe mit Schwa und Patach                        | `אֲ`          | Buchstabe + U+05B2                   |
| Buchstabe mit Schwa und Qamäz                         | `אֳ`          | Buchstabe + U+05B3                   |
| Buchstabe mit Chiriq                                  | `אִ`          | Buchstabe + U+05B4                   |
| Buchstabe mit Sere                                    | `אֵ`          | Buchstabe + U+05B5                   |
| Buchstabe mit Seggol                                  | `אֶ`          | Buchstabe + U+05B6                   |
| Buchstabe mit Patach                                  | `אַ`          | Buchstabe + U+05B7                   |
| Buchstabe mit Qamäz                                   | `אַָ`         | Buchstabe + U+05B8                   |
| Buchstabe mit Choläm                                  | `אֹ`          | Buchstabe + U+05B9                   |
| Buchstabe mit Qubbuz                                  | `אֻ`          | Buchstabe + U+05BB                   |