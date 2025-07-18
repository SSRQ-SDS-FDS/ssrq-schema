# Caractères spéciaux

Tous les caractères spéciaux sont codés en Unicode et sont représentés à l’aide de la police 
SDS Lexia Fontes pour l’écriture latine et du Libertinus Serif pour les écritures grecque
et hébraïque.

## Accents et diacritica

### Règles générales

=== "Textes allemands"

    Les caractères diacritiques et les lettres de textes allemands sont reproduits fidèlement.
    
    Les signes de distinction sur `u`, qui sont censés empêcher la confusion avec `n` dans les
    textes allemands, ne sont pas reproduits.

=== "Textes latins"

    Une distinction est faite entre l’e caudata (`ę`) et le `e` ordinaire.

    En raison des hyper corrections, les chercheurs des XVIIe et XVIIIe siècles avaient
    tendance à préférer la diphtongation.

    Si un original médiéval est préservé, l’orthographe du texte de départ doit être conservée,
    i. e. `ę`, qui a probablement été écrit en copies ultérieurs en tant que `æ`, devrait
    être reproduit.
    Si seulement la copie ultérieure existe, il faut adhérer à l’orthographe de cette copie et
    reproduire fidèlement la diphtongue.

=== "Textes français et italiens"

    Les signes diacritiques du français et de l’italien sont utilisés en fonction de l’usage
    moderne, à condition qu’il n’y ait aucune exception.

    Lors de la définition de l’accent, un système cohérent doit être utilisé dans un corpus
    de texte, qui est basé sur les coutumes graphiques et typographiques du temps respectif
    autant que possible.

### Règles spéciales pour les textes français

=== "Manuscrits médiévaux"

    Dans le cas des manuscrits français médiévaux, aucun accente ne doit être ajouté, sauf si
    les homophones peuvent être évités en raison de la `e` atonale et tonique.
    De cette façon, les syllabes de fin reçoivent un accent sur `-e` ou `-es`.

    Exemples :  
    afr. `aprés` représente fr. `après` (nach)  
    afr. `apres` représente fr. `âpres` (bitter)  
    afr. `leve` représente fr. `lève`,  
    alors que afr. `levé` est le participe du verbe afr. `lever`
    
    L’article afr. `des` est toujours transcrit inchangé, donc `des` et pas `dés`.

=== "Mss. XVIe siècle"

    Pour les textes français du XVIe siècle (jusqu’à environ 1580), les normes qui ont été fixées
    pour l’édition des textes français médiévaux s’appliquent.
    Seul l’accent sur la lettre `e` est utilisé pour faire la distinction entre `e` tonique
    et atonique.
    
    Exemples :  
    mfr. `né`, `tombé`, `vous avés`, `aprés`, `procés`
    
    Les terminaisons sur `-ee` ne sont pas soulignées.
    
    Exemples :  
    mfr. `nee`, `armee`

=== "Mss. XVIIe siècle"

    Lors du traitement des manuscrits français du XVIIe siècle (jusqu’à environ 1715), les
    accents peuvent être utilisés dans une plus grande mesure.
    En particulier, les fins sur `-ée` sont soulignées.

    Exemples :  
    fr. `née`, `armée`
    
    L’accent sur les lettres `a`, `e` et `u` dans les prépositions et les adverbes monosyllabiques
    est utilisé pour les distinguer des mots homographes.
    
    Exemples :  
    fr. `à`, `là`, `dès`, `lès`, `où`
    
    En revanche, la lettre `e` n’est pas soulignée en un seul mot.
    
    Exemples :  
    fr. `maniere`, `pere`, `present`

=== "Mss. XVIIIe siècle"
    
    L’utilisation de la langue d’aujourd’hui est appliquée aux manuscrits français du
    XVIIIe siècle.

### Certains diacritica dans les textes français

=== "Trema"

    Fondamentalement, un trema devrait être supprimé dans des mots qui sont écrits aujourd’hui
    sans trema. Il en va de même pour `ÿ` (voir [normalisation](normalization.fr.md)).

    Exemples :  
    fr. `queüe`, `veü`

    Dans les textes littéraires médiévaux, le Trema peut avoir une fonction phonétique, dans ce
    cas, il est conservé.

=== "Cedille (`ç`)"

    Le `c`, qui a une valeur phonétique comme /s/, doit être ajouté une cedille.
    
    Exemples :  
    `François` et pas `Francois`  
    `il sçait` et pas `il scait`

=== "Apostrophe"

    Afin de clarifier le sens d’un texte et de le rendre plus compréhensible, l’ajout 
    d’apostrophène est essentiel.

    P. ex., l’orthographe `se` pour `c’est` avec `s’e` doit être reproduite.

    Puisque le pronom à la troisième personne du singulier et du pluriel est souvent réduit 
    à `i`, il doit être précédé d’une apostrophe lorsqu’il est combiné avec un pronom relatif
    ou une conjonction afin que `qui` ne soit pas confondu avec `qu’il`.

    Exemple :  
    ```Item ledit detenu a dit et confesé que illiaz quattre ans qu’i 
    deroba une boiste avec l’estuy.```

    L’exemple mentionné ci-dessus montre également qu’une apostrophe doit être ajoutée
    pour séparer l’article spécifique qui pourrait être connecté à un nom.

    Exemple :  
    `l’estuy` et pas `lestuy`

    Si la combinaison `Quil` agit comme une préposition relative, elle doit être transcrite.

    Exemple :  
    ```Item for celuy quil allat querir le maistre d’ovre```

## Ligatures

Dans l’impression, les ligatures sont dissoutes dans des lettres individuelles et également dans
des textes manuscrits, l’utilisation de ligatures est généralement dispensée.

Exceptions : les propres signes peuvent être utilisés pour les ligatures `Æ`, `æ`,
`Œ`, `œ` et `ß`

Par exemple, au lieu d’e caudata (`ę`), l’orthographe `æ` peut survenir dans une copie ultérieure
par hyper correction.

L’éditeur doit être conscient que les `æ` et `ae` dans le traitement de texte numérique n’ont pas
la même valeur et ne sont pas reconnus comme un graphème identique.

D’autres ligatures qui ont principalement un caractère typographique ne sont pas codées avec leurs
propres unicodmarks, mais simplement par les deux lettres de terrain consécutives, c’est-à-dire :
`ff`, `fi`, `fl`, `ffi`, `ffl` et pas `ﬀ`, `ﬁ`, `ﬂ`, `ﬃ`, `ﬄ`.

## Fractures

Bien qu’Unicode comporte un certain nombre de symboles de fractions spéciaux destinés aux fractions
les plus courantes, ceux-ci ne doivent pas être utilisés car ils ne couvrent pas tous les cas qui
apparaissent dans le texte.
Au lieu de cela, les fractures doivent être codées avec [`<num>`](num.fr.md).

Exemples :  
`<num value="0.5">1/2</num>` et pas `½`  
`<num value="0.75">3/4</num>` et pas `¾`

## Tableau de code pour les caractères spéciaux

Le tableau ci-dessous montre comment les caractères individuels doivent être codés.

Pour certains des caractères spécifiés, il a plusieurs options de codage :
P. ex., l’e caudata peut être codé sous la forme d’un seul caractère `ę` (U+0119)
ou sous la forme d’une lettre de base `e` (U+0065) avec un Ogonek combinant `ę` (U+0328).
P. ex., `Ą ą Ę ę Į į Ǫ ǫ Ų ų` peut être généré en entrant d’abord la lettre de base puis en
Ogonek combinant, comme avec l’e caudata.

Si nécessaire, plusieurs personnages combinés avec une lettre terrestre peuvent également
être utilisés, p. Ex. `ā̧` (= a + Macron combinant + Cedille combinante) oder `uͦ̈` (= o + superscrit 
o + trema combinant).

Fondamentalement, la variante de combinaison est préférée car les caractères de combinaison peuvent
être attachés à tous les registres terrestres. Exception : 
Par souci de simplicité, les umlauts allemands `Ä ä Ö ö Ü ü` peuvent être entrés directement sous
forme de signes individuels et n’ont pas à être enregistrés comme une lettre terrestre avec un
trema combinant (U+0308).

Dans le tableau, le `a` est utilisé comme exemple dans la combinaison des caractères, l’entrée est
analogue aux autres lettres.

| Description                            | Caractère spécial     | Unicode         |
|----------------------------------------|-----------------------|-----------------|
| **Ligatures**                          |                       |                 |
| A+E-ligature                           | `Æ`                   | U+00C6          |
| a+e-ligature                           | `æ`                   | U+00E6          |
| O+E-ligature                           | `Œ`                   | U+0152          |
| o+e-ligature                           | `œ`                   | U+0153          |
| s+z-ligature                           | `ß`                   | U+00DF          |
| **Diacritica combinants**              |                       |                 |
| Lettre avec accent grave               | `à`                  | Lettre + U+0300 |
| Lettre avec accent aigu                | `á`                  | Lettre + U+0301 |
| Lettre avec circonflexe                | `â`                  | Lettre + U+0302 |
| Lettre avec tilde                      | `ã`                  | Lettre + U+0303 |
| Lettre avec macron                     | `ā`                  | Lettre + U+0304 |
| Lettre avec point                      | `ȧ`                  | Lettre + U+0307 |
| Lettre avec trema                      | `ä`                  | Lettre + U+0308 |
| Lettre avec caron                      | `ǎ`                  | Lettre + U+030C |
| Lettre avec ligne verticale            | `a̍`                  | Lettre + U+030D |
| Lettre avec cedille                    | `a̧`                  | Lettre + U+0327 |
| Lettre avec ogonek                     | `ą`                  | Lettre + U+0328 |
| ** Lettres écrites dessus**            |                       |                 |
| Lettre avec a dessus                   | `aͣ`                  | Lettre + U+0363 |
| Lettre avec e dessus                   | `aͤ`                  | Lettre + U+0364 |
| Lettre avec i dessus                   | `aͥ`                  | Lettre + U+0365 |
| Lettre avec o dessus                   | `aͦ`                  | Lettre + U+0366 |
| Lettre avec u dessus                   | `aͧ`                  | Lettre + U+0367 |
| Lettre avec v dessus                   | `aͮ`                  | Lettre + U+036E |
| Lettre avec w dessus                   | `a`                  | Lettre + U+F03C |
| **Autres lettres modifiées**           |                       |                 |
| i avec ligne (= un et demi)            | `ɨ`                   | U+0268          |
| i avec deux lignes                     | ``                   | U+E8A1          |
| j avec ligne                           | `ɉ`                   | U+0249          |
| j avec deux lignes                     | ``                   | U+E8A2          |
| q avec ligne                           | `ꝗ`                   | U+A757          |
| t avec ligne                           | `ŧ`                   | U+0167          |
| v avec ligne (= quatre et demi)        | ``                   | U+E8BB          |
| v avec ligne diagonale                 | `ꝟ`                   | U+A75F          |
| v avec deux ligne                      | ``                   | U+E8BC          |
| x avec ligne dessus                    | ``                   | U+E8BD          |
| x avec ligne dessous  (= neuf et demi) | ``                   | U+E8BE          |
| x avec deux lignes dessous             | ``                   | U+E8CE          |
| **Devises et unités**                  |                       |                 |
| Florin                                 | ``                   | U+F2E8          |
| Gulden                                 | ``                   | U+F2E9          |
| h mit Strich (= Haller)                | `ħ`                   | U+0127          |
| Helbling                               | ``                   | U+F2FB          |
| Krone                                  | ``                   | U+F2FA          |
| Krone (alternativ)                     | ``                   | U+F2FC          |
| Pfennig/Denar                          | `₰`                   | U+20B0          |
| Pfund (Währung)                        | ``                   | U+F2EA          |
| Pfund (Gewicht)                        | `℔`                   | U+2114          |
| Schilling                              | ``                   | U+F2F7          |
| Scudo                                  | ``                   | U+F2F9          |
| **Autres symboles**                    |                       |                 |
| Symbole de main pointée                | `☞`                   | U+261E          |
| Symbole de paragraphe                  | `§`                   | U+00A7          |
| Symbole de paragraphe                  | `¶`                   | U+00B6          |
| Croix                                  | `†`                   | U+2020          |
| Double croix                           | `‡`                   | U+2021          |
| Triple croix                           | ``                   | U+F1D2          |
| Symbole de mariage                     | `⚭`                   | U+26AD          |
| Symbole circulaire                     | `○`                   | U+25CB          |
| Symbole pour Mars (Abbr. pour Mardi)   | `♂`                   | U+2642          |
| Symbole de droit d’auteur              | `©`                   | U+00a9          |
| **Signes de ponctuation etc.**         |                       |                 |
| Point                                  | `.`                   | U+002E          |
| Virgule                                | `,`                   | U+002C          |
| Point-virgule                          | `;`                   | U+003B          |
| Côlon                                  | `:`                   | U+003A          |
| Point culminant                        | `·`                   | U+00B7          |
| Apostrophe                             | `’`                   | U+2019          |
| Point d’exclamation                    | `!`                   | U+0021          |
| Point d’interrogation                  | `?`                   | U+003F          |
| Ellipse                                | `…`                   | U+2026          |
| Un point avant deux                    | `⁖`                   | U+2056          |
| Un point sur deux                      | `∵`                   | U+2235          |
| Quatre points                          | `⁘`                   | U+2058          |
| Ligne en demi-tiret                    | `–`                   | U+2013          |
| Ligne verticale simple                 | <code>&#x007c;</code> | U+007C          |
| Double ligne verticale                 | `‖`                   | U+2016          |
| Double solidus                         | `⫽`                   | U+2AFD          |
| Guillemet à gauche                     | `‹`                   | U+2039          |
| Guillemet à droite                     | `›`                   | U+203A          |
| Guillemets à gauche                    | `«`                   | U+00AB          |
| Guillemets à droite                    | `»`                   | U+00BB          |
| Croix de multiplication                | `×`                   | U+00D7          |
| Caractère ordinal (1º, 2º, etc.)       | `º`                   | U+00BA          |

## Script grec et hébreu

Les passages dans le script grec et hébreu sont également codés directement dans Unicode.
Cela s’applique que les accents grecs, les *spiritus* ainsi que le *iota subscriptum* ou
*adscriptum* et les signes de vocalisation hébraïque avec des caractères combinés doivent
être montrés.
L’alpha grec et l’hébreu Alef en servent d’exemples.

| Description                                               | Caractère spécial | Unicode                           |
|-----------------------------------------------------------|-------------------|-----------------------------------|
| **Lettres grecques**                                      |                   |                                   |
| Alpha                                                     | `Α`, `α`          | U+0391, U+03B1                    |
| Beta                                                      | `Β`, `β`          | U+0392, U+03B2                    |
| Gamma                                                     | `Γ`, `γ`          | U+0393, U+03B3                    |
| Delta                                                     | `Δ`, `δ`          | U+0394, U+03B4                    |
| Epsilon                                                   | `Ε`, `ε`          | U+0395, U+03B5                    |
| Zeta                                                      | `Ζ`, `ζ`          | U+0396, U+03B6                    |
| Eta                                                       | `Η`, `η`          | U+0397, U+03B7                    |
| Theta                                                     | `Θ`, `θ`          | U+0398, U+03B8                    |
| Iota                                                      | `Ι`, `ι`          | U+0399, U+03B9                    |
| Kappa                                                     | `Κ`, `κ`          | U+039A, U+03BA                    |
| Lambda                                                    | `Λ`, `λ`          | U+039B, U+03BB                    |
| My                                                        | `Μ`, `μ`          | U+039C, U+03BC                    |
| Ny                                                        | `Ν`, `ν`          | U+039D, U+03BD                    |
| Xi                                                        | `Ξ`, `ξ`          | U+039E, U+03BE                    |
| Omikron                                                   | `Ο`, `ο`          | U+039F, U+03BF                    |
| Pi                                                        | `Π`, `π`          | U+03A0, U+03C0                    |
| Rho                                                       | `Ρ`, `ρ`          | U+03A1, U+03C1                    |
| Sigma                                                     | `Σ`, `ς`, `σ`     | U+03A3, U+03C2, U+03C3            |
| Tau                                                       | `Τ`, `τ`          | U+03A4, U+03C4                    |
| Ypsilon                                                   | `Υ`, `υ`          | U+03A5, U+03C5                    |
| Phi                                                       | `Φ`, `φ`          | U+03A6, U+03C6                    |
| Chi                                                       | `Χ`, `χ`          | U+03A7, U+03C7                    |
| Psi                                                       | `Ψ`, `ψ`          | U+03A8, U+03C8                    |
| Omega                                                     | `Ω`, `ω`          | U+03A9, U+03C9                    |
| **Diacritica grecques**                                   |                   |                                   |
| Lettre avec accent grave                                  | `ὰ`              | Lettre + U+0300                   |
| Lettre avec accent aigu                                   | `ά`              | Lettre + U+0301                   |
| Lettre avec circonflexe                                   | `ᾶ`              | Lettre + U+0342                   |
| Lettre avec *spiritus lenis*                              | `ἀ`              | Lettre + U+0313                   |
| Lettre avec *spiritus asper*                              | `ἁ`              | Lettre + U+0314                   |
| Lettre avec *iota sub- bzw. adscriptum*                   | `ᾳ`              | Lettre + U+0345                   |
| Lettre avec *spiritus* et accent aigu                     | `ἅ`             | Lettre + U+0314 + U+0301          |
| Lettre avec *spiritus*, accent aigu et *iota subscriptum* | `ᾅ`            | Lettre + U+0314 + U+0301 + U+0345 |
| **Lettres hébraïques**                                    |                   |                                   |
| Alef                                                      | `א`               | U+05D0                            |
| Bet                                                       | `ב`               | U+05D1                            |
| Gimel                                                     | `ג`               | U+05D2                            |
| Dalet                                                     | `ד`               | U+05D3                            |
| He                                                        | `ה`               | U+05D4                            |
| Waw                                                       | `ו`               | U+05D5                            |
| Sajin                                                     | `ז`               | U+05D6                            |
| Chet                                                      | `ח`               | U+05D7                            |
| Tet                                                       | `ט`               | U+05D8                            |
| Jud                                                       | `י`               | U+05D9                            |
| Kaf                                                       | `כ`, `ך`          | U+05DA, U+05DB                    |
| Lamed                                                     | `ל`               | U+05DC                            |
| Mem                                                       | `מ`, `ם`          | U+05DD, U+05DE                    |
| Nun                                                       | `נ`, `ן`          | U+05DF, U+05E0                    |
| Samech                                                    | `ס`               | U+05E1                            |
| Ajin                                                      | `ע`               | U+05E2                            |
| Pe                                                        | `פ`, `ף`          | U+05E3, U+05E4                    |
| Zade                                                      | `צ`, `ץ`          | U+05E5, U+05E6                    |
| Kuf                                                       | `ק`               | U+05E7                            |
| Resch                                                     | `ר`               | U+05E8                            |
| Sin, Schin                                                | `ש`               | U+05E9                            |
| Taw                                                       | `ת`               | U+05EA                            |
| **Diacritica hébraïques**                                 |                   |                                   |
| Lettre avec Schwa                                         | `אְ`              | Lettre + U+05B0                   |
| Lettre avec Schwa et Seggol                               | `אֱ`              | Lettre + U+05B1                   |
| Lettre avec Schwa et Patach                               | `אֲ`              | Lettre + U+05B2                   |
| Lettre avec Schwa et Qamäz                                | `אֳ`              | Lettre + U+05B3                   |
| Lettre avec Chiriq                                        | `אִ`              | Lettre + U+05B4                   |
| Lettre avec Sere                                          | `אֵ`              | Lettre + U+05B5                   |
| Lettre avec Seggol                                        | `אֶ`              | Lettre + U+05B6                   |
| Lettre avec Patach                                        | `אַ`              | Lettre + U+05B7                   |
| Lettre avec Qamäz                                         | `אַָ`             | Lettre + U+05B8                   |
| Lettre avec Choläm                                        | `אֹ`              | Lettre + U+05B9                   |
| Lettre avec Qubbuz                                        | `אֻ`              | Lettre + U+05BB                   |