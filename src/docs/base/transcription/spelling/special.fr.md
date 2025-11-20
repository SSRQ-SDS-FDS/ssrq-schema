# Caractères spéciaux

Tous les caractères spéciaux sont codés en Unicode et sont écrits avec les polices des SDS : 
Lexia Fontes pour l’écriture latine et Libertinus Serif pour les écritures grecque et hébraïque.

## Accents et signes diacritiques

### Règles générales

=== "Textes allemands"

    Les signes diacritiques et les lettres suscrites des textes allemands
    sont reproduits à l’identique.

    Les signes de distinction au-dessus des `u`, qui empêchent la confusion
    avec les `n`, ne sont pas reproduits.

=== "Textes latins"

    Une distinction est faite entre le e caudata (`ę`) et le `e` ordinaire.

    Aux XVII<sup>e</sup> et XVIII<sup>e</sup> siècles, les érudits avaient tendance,
    par hypercorrection, à préférer la diphtongaison.

    Si un original médiéval est préservé, l’orthographe du texte source doit être respectée,
    p. ex. le `ę`, qui apparait probablement comme `æ` dans les copies ultérieures,
    doit être transcrit par `ę`.

    S’il ne subsiste qu’une copie ultérieure, il convient de reproduire l’orthographe
    de cette copie et de restituer fidèlement la diphtongue.

=== "Textes français et italiens"

    Les signes diacritiques du français et de l’italien sont utilisés selon
    l’usage moderne, sauf exceptions.

    Pour les accents, un système cohérent doit être utilisé dans tout le corpus,
    fidèle aux usages graphiques et typographiques de l’époque considérée.

### Règles spéciales pour les textes français

=== "Manuscrits médiévaux"

    Dans le cas des manuscrits français médiévaux, les accents ne doivent pas être ajoutés, 
    sauf s’ils permettent d’éviter une confusion entre des homophones en raison de la 
    distinction entre le `e` atone et tonique. De cette façon, les finales en `-e` ou `-es`
    reçoivent un accent.

    Exemples :  
    afr. `aprés` signifie fr. `après`  
    afr. `apres` signifie fr. `âpres`  
    afr. `leve` signifie fr. `lève`,  
    alors que afr. `levé` est le participe du verbe afr. `lever`
    
    L’article afr. `des` est toujours transcrit inchangé, donc `des` et pas `dés`.

=== "Mss. XVI<sup>e</sup> siècle"

    Pour les textes français du XVI<sup>e</sup> siècle (jusqu’à environ 1580),
    les normes d’édition des textes français médiévaux s’appliquent.
    L’accent sur la lettre `e` est utilisé uniquement pour faire la distinction
    entre `e` tonique et atone.
    
    Exemples :  
    mfr. `né`, `tombé`, `vous avés`, `aprés`, `procés`
    
    Les terminaisons en `-ee` ne sont pas accentuées.
    
    Exemples :  
    mfr. `nee`, `armee`

=== "Mss. XVII<sup>e</sup> siècle"

    Lors du traitement des manuscrits français du XVII<sup>e</sup> siècle
    (jusqu’à environ 1715), les accents peuvent être plus largement utilisés,
    en particulier, les fins en `-ée`.

    Exemples :  
    fr. `née`, `armée`
    
    Les lettres `a`, `e` et `u` dans les prépositions et les adverbes monosyllabiques
    sont accentuées pour les distinguer des mots homographes.
    
    Exemples :  
    fr. `à`, `là`, `dès`, `lès`, `où`
    
    En revanche, la lettre `e` à l’intérieur d’un mot n’est pas accentuée.
    
    Exemples :  
    fr. `maniere`, `pere`, `present`

=== "Mss. XVIII<sup>e</sup> siècle"
    
    Pour les manuscrits français du XVIII<sup>e</sup> siècle, les règles de français
    actuelles sont utilisées.

### Signes diacritiques spécifiques dans les textes français

=== "Tréma"

    En règle générale, un tréma doit être supprimé dans des mots qui sont écrits
    aujourd’hui sans tréma. Il en va de même pour `ÿ` (voir [normalisation](normalization.fr.md)).

    Exemples :  
    fr. `queüe`, `veü`

    Dans les textes littéraires médiévaux, le tréma peut avoir une fonction phonétique,
    dans ce cas, il est conservé.

=== "Cédille (`ç`)"

    Le `c`, qui a une valeur phonétique comme /s/, doit être complété par une cédille.
    
    Exemples :  
    `François` et pas `Francois`  
    `il sçait` et pas `il scait`

=== "Apostrophe"

    Afin de clarifier le sens d’un texte et d’en améliorer la lisibilité,
    l’ajout d’apostrophes est indispensable.
    P. ex., la forme `se` pour `c’est` doit être retranscrite `s’e`.
    Puisque le pronom à la troisième personne du singulier ou du pluriel est souvent réduit à `i`, 
    une apostrophe doit le précéder lorsqu’il est combiné avec un pronom relatif ou une
    conjonction, afin d’éviter toute confusion entre `qui` et `qu’il`.

    Exemple :  
    ```Item ledit detenu a dit et confesé que illiaz quattre ans qu’i 
    deroba une boiste avec l’estuy.```

    L’exemple mentionné ci-dessus montre également qu’une apostrophe doit être ajoutée pour
    séparer l’article défini du substantif auquel il est lié.

    Exemple :  
    `l’estuy` et pas `lestuy`

    Si la combinaison `Quil` est employée comme pronom relatif, elle doit être transcrite
    telle quelle, c’est-à-dire sans apostrophe.

    Exemple :  
    ```Item for celuy quil allat querir le maistre d’ovre```

## Ligatures

Dans les imprimés, les ligatures sont décomposées en lettres simples.
Il en va de même dans les textes manuscrits, où leur utilisation est évitée.

Exceptions : les signes existants peuvent être utilisés pour les ligatures `Æ, æ, Œ, œ` et `ß`.

Par exemple, au lieu du e caudata (`ę`), une copie tardive peut utiliser `æ` par hypercorrection.

L’éditeur doit être conscient que les `æ` et `ae` ne sont pas équivalents
en traitement de texte numérique : ils ne sont pas reconnus comme un graphème identique.

D’autres ligatures à caractère principalement typographique ne sont pas codées
avec des caractères Unicode spécifiques, mais simplement par leurs lettres de base, 
c’est-à-dire : `ff, fi, fl, ffi, ffl` et pas `ﬀ, ﬁ, ﬂ, ﬃ, ﬄ`.

## Fractions

Bien qu’Unicode comporte un certain nombre de signes spécifiques destinés aux fractions les
plus courantes, ceux-ci ne doivent pas être utilisés car ils ne couvrent pas tous les cas
qui apparaissent dans les textes. Les fractions doivent plutôt être codées avec 
[`<num>`](num.fr.md).

Exemples :  
`<num value="0.5">1/2</num>` et pas `½`  
`<num value="0.75">3/4</num>` et pas `¾`

## Tableau de code des caractères spéciaux

Le tableau ci-dessous montre comment les caractères individuels doivent être codés.

Pour certains des caractères spécifiques, il a plusieurs options de codage : p. ex., 
le e caudata peut être codé comme un caractère unique `ę` (U+0119) ou comme une lettre
de base `e` (U+0065) avec un Ogonek combiné `ę` (U+0328).
Ainsi, on peut produire `Ą ą Ę ę Į į Ǫ ǫ Ų ų` en entrant d’abord la lettre de base puis 
l’Ogonek combiné, comme avec le e caudata.

Si nécessaire, plusieurs signes combinés peuvent être appliqués à une même lettre de base, 
p. ex. : ā̧ (= a + Macron combiné + Cédille combinée) ou `uͦ̈` (= o + o suscrit + tréma combiné).

En règle générale, la variante de combinaison est à privilégier, car les caractères
de combinaison peuvent être ajoutés à toutes les lettres de base.

Exception : Par souci de simplicité, les umlauts allemands `Ä ä Ö ö Ü ü` et les lettres
françaises `À à Â â Æ æ Ç ç È è É é Ê ê Ë ë Î î Ï ï Ô ô Œ œ Ù ù Û û Ü ü Ÿ ÿ`
peuvent être entrés directement comme caractères uniques.

Dans le tableau, les combinaisons de caractères sont illustrées avec la lettre a ;
l’application aux autres lettres suit la même logique.

| Description                            | Caractère spécial     | Unicode         |
|----------------------------------------|-----------------------|-----------------|
| **Ligatures**                          |                       |                 |
| A+E-ligature                           | `Æ`                   | U+00C6          |
| a+e-ligature                           | `æ`                   | U+00E6          |
| O+E-ligature                           | `Œ`                   | U+0152          |
| o+e-ligature                           | `œ`                   | U+0153          |
| s+z-ligature                           | `ß`                   | U+00DF          |
| **Signes diacritiques de combinaison** |                       |                 |
| Lettre avec accent grave               | `à`                  | Lettre + U+0300 |
| Lettre avec accent aigu                | `á`                  | Lettre + U+0301 |
| Lettre avec circonflexe                | `â`                  | Lettre + U+0302 |
| Lettre avec tilde                      | `ã`                  | Lettre + U+0303 |
| Lettre avec macron                     | `ā`                  | Lettre + U+0304 |
| Lettre avec point                      | `ȧ`                  | Lettre + U+0307 |
| Lettre avec tréma                      | `ä`                  | Lettre + U+0308 |
| Lettre avec caron                      | `ǎ`                  | Lettre + U+030C |
| Lettre avec ligne verticale            | `a̍`                  | Lettre + U+030D |
| Lettre avec cédille                    | `a̧`                  | Lettre + U+0327 |
| Lettre avec ogonek                     | `ą`                  | Lettre + U+0328 |
| **Lettres suscrites**                  |                       |                 |
| Lettre avec a suscrit                  | `aͣ`                  | Lettre + U+0363 |
| Lettre avec e suscrit                  | `aͤ`                  | Lettre + U+0364 |
| Lettre avec i suscrit                  | `aͥ`                  | Lettre + U+0365 |
| Lettre avec o suscrit                  | `aͦ`                  | Lettre + U+0366 |
| Lettre avec u suscrit                  | `aͧ`                  | Lettre + U+0367 |
| Lettre avec v suscrit                  | `aͮ`                  | Lettre + U+036E |
| Lettre avec w suscrit                  | `a`                  | Lettre + U+F03C |
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
| Gulden (Florin)                        | ``                   | U+F2E9          |
| h avec trait (= maille/obole)          | `ħ`                   | U+0127          |
| Demi-denier                            | ``                   | U+F2FB          |
| Écu                                    | ``                   | U+F2FA          |
| Écu (alternative)                      | ``                   | U+F2FC          |
| Denier                                 | `₰`                   | U+20B0          |
| Livre (monnaie)                        | ``                   | U+F2EA          |
| Livre (poids)                          | `℔`                   | U+2114          |
| Sou                                    | ``                   | U+F2F7          |
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
| Symbole de Mars (abr. pour mardi)      | `♂`                   | U+2642          |
| Symbole de droit d’auteur              | `©`                   | U+00a9          |
| **Signes de ponctuation, etc.**        |                       |                 |
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
| Croix de multiplication                | `×`                   | U+00D7          |
| Caractère ordinal (1º, 2º, etc.)       | `º`                   | U+00BA          |

## Écriture grecque et hébraïque

Les passages en caractères grecs et hébreux sont également codés directement dans Unicode. 
Il est demandé que les accents grecs, les *esprits* ainsi que *l’iota souscrit* ou *adscrit* 
et les signes de vocalisation hébraïque soient représentés à l’aide de signes de combinaison. 
Les exemples sont donnés à partir de l’alpha grec et l’alef hébreux.

| Description                                            | Caractère spécial | Unicode                           |
|--------------------------------------------------------|-------------------|-----------------------------------|
| **Lettres grecques**                                   |                   |                                   |
| Alpha                                                  | `Α`, `α`          | U+0391, U+03B1                    |
| Beta                                                   | `Β`, `β`          | U+0392, U+03B2                    |
| Gamma                                                  | `Γ`, `γ`          | U+0393, U+03B3                    |
| Delta                                                  | `Δ`, `δ`          | U+0394, U+03B4                    |
| Epsilon                                                | `Ε`, `ε`          | U+0395, U+03B5                    |
| Zeta                                                   | `Ζ`, `ζ`          | U+0396, U+03B6                    |
| Eta                                                    | `Η`, `η`          | U+0397, U+03B7                    |
| Theta                                                  | `Θ`, `θ`          | U+0398, U+03B8                    |
| Iota                                                   | `Ι`, `ι`          | U+0399, U+03B9                    |
| Kappa                                                  | `Κ`, `κ`          | U+039A, U+03BA                    |
| Lambda                                                 | `Λ`, `λ`          | U+039B, U+03BB                    |
| My                                                     | `Μ`, `μ`          | U+039C, U+03BC                    |
| Ny                                                     | `Ν`, `ν`          | U+039D, U+03BD                    |
| Xi                                                     | `Ξ`, `ξ`          | U+039E, U+03BE                    |
| Omikron                                                | `Ο`, `ο`          | U+039F, U+03BF                    |
| Pi                                                     | `Π`, `π`          | U+03A0, U+03C0                    |
| Rho                                                    | `Ρ`, `ρ`          | U+03A1, U+03C1                    |
| Sigma                                                  | `Σ`, `ς`, `σ`     | U+03A3, U+03C2, U+03C3            |
| Tau                                                    | `Τ`, `τ`          | U+03A4, U+03C4                    |
| Ypsilon                                                | `Υ`, `υ`          | U+03A5, U+03C5                    |
| Phi                                                    | `Φ`, `φ`          | U+03A6, U+03C6                    |
| Chi                                                    | `Χ`, `χ`          | U+03A7, U+03C7                    |
| Psi                                                    | `Ψ`, `ψ`          | U+03A8, U+03C8                    |
| Omega                                                  | `Ω`, `ω`          | U+03A9, U+03C9                    |
| **Signes diacritiques grecs**                          |                   |                                   |
| Lettre avec accent grave                               | `ὰ`              | Lettre + U+0300                   |
| Lettre avec accent aigu                                | `ά`              | Lettre + U+0301                   |
| Lettre avec circonflexe                                | `ᾶ`              | Lettre + U+0342                   |
| Lettre avec *spiritus lenis*                           | `ἀ`              | Lettre + U+0313                   |
| Lettre avec *spiritus asper*                           | `ἁ`              | Lettre + U+0314                   |
| Lettre avec *iota souscrit ou adscrit*                 | `ᾳ`              | Lettre + U+0345                   |
| Lettre avec *spiritus* et accent aigu                  | `ἅ`             | Lettre + U+0314 + U+0301          |
| Lettre avec *spiritus*, accent aigu et *iota souscrit* | `ᾅ`            | Lettre + U+0314 + U+0301 + U+0345 |
| **Lettres hébraïques**                                 |                   |                                   |
| Alef                                                   | `א`               | U+05D0                            |
| Bet                                                    | `ב`               | U+05D1                            |
| Gimel                                                  | `ג`               | U+05D2                            |
| Dalet                                                  | `ד`               | U+05D3                            |
| He                                                     | `ה`               | U+05D4                            |
| Waw                                                    | `ו`               | U+05D5                            |
| Sajin                                                  | `ז`               | U+05D6                            |
| Chet                                                   | `ח`               | U+05D7                            |
| Tet                                                    | `ט`               | U+05D8                            |
| Jud                                                    | `י`               | U+05D9                            |
| Kaf                                                    | `כ`, `ך`          | U+05DA, U+05DB                    |
| Lamed                                                  | `ל`               | U+05DC                            |
| Mem                                                    | `מ`, `ם`          | U+05DD, U+05DE                    |
| Nun                                                    | `נ`, `ן`          | U+05DF, U+05E0                    |
| Samech                                                 | `ס`               | U+05E1                            |
| Ajin                                                   | `ע`               | U+05E2                            |
| Pe                                                     | `פ`, `ף`          | U+05E3, U+05E4                    |
| Zade                                                   | `צ`, `ץ`          | U+05E5, U+05E6                    |
| Kuf                                                    | `ק`               | U+05E7                            |
| Resch                                                  | `ר`               | U+05E8                            |
| Sin, Schin                                             | `ש`               | U+05E9                            |
| Taw                                                    | `ת`               | U+05EA                            |
| **Signes diacritiques hébraïques**                     |                   |                                   |
| Lettre avec Schwa                                      | `אְ`              | Lettre + U+05B0                   |
| Lettre avec Schwa et Seggol                            | `אֱ`              | Lettre + U+05B1                   |
| Lettre avec Schwa et Patach                            | `אֲ`              | Lettre + U+05B2                   |
| Lettre avec Schwa et Qamäz                             | `אֳ`              | Lettre + U+05B3                   |
| Lettre avec Chiriq                                     | `אִ`              | Lettre + U+05B4                   |
| Lettre avec Sere                                       | `אֵ`              | Lettre + U+05B5                   |
| Lettre avec Seggol                                     | `אֶ`              | Lettre + U+05B6                   |
| Lettre avec Patach                                     | `אַ`              | Lettre + U+05B7                   |
| Lettre avec Qamäz                                      | `אַָ`             | Lettre + U+05B8                   |
| Lettre avec Choläm                                     | `אֹ`              | Lettre + U+05B9                   |
| Lettre avec Qubbuz                                     | `אֻ`              | Lettre + U+05BB                   |