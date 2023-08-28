Drucke:
Die Handhabung entspricht derjenigen der [handschriftlichen Quellen](#b-handschriftliche-texte).

Hss:
## 6 Abkürzungen

### 6.1 Häufige Abkürzungen

Typische, im selben Schriftstück oder in mehreren Schriftstücken wiederkehrende Abkürzungen werden stehen
  gelassen. Abkürzungen werden mit [`<abbr/>`](../../elements/abbr.de.md) getaggt, mit dem Abkürzungsverzeichnis verlinkt oder, wenn fehlend, ins
  Abkürzungsverzeichnis aufgenommen. Es werden keine Kürzungspunkte verwendet, da die Abkürzungen durch die Auszeichnung
  bereits als solche gekennzeichnet sind.

`to do: Beispiel in abbr  hinzufügen, dann kann dieses Beispiel hier gelöscht werden<abbr>etc</abbr>`

Kürzel  werden konsequent als Kürzel belassen und mit [`<abbr/>`](../../elements/abbr.de.md) ausgezeichnet. Die Auflösung erfolgt im Abkürzungsverzeichns.

Beispiele:  `lobl., m. g. h., tit.,  s. v., LL.EE., MM., no, art., etc.  `

### 6.2 Abbkürzungen auflösen

Auflösungen wurden früher in Zweifelsfällen in [   ] gesetzt, in der digitalen Edition werden sie
mit [`<choice/>`](../../elements/choice.de.md), [`<abbr/>`](../../elements/abbr.de.md) und [`<expan/>`](../../elements/expan.de.md)
getaggt.

Abkürzungen in der Textvorlage werden aufgelöst, wenn es möglich und sinnvoll ist. Orthographische Gepflogenheiten des
Schreibers werden ohne besondere Kennzeichnung berücksichtigt. Einige Abkürzungen (wie z. B. Ao = anno, dz= das) sowie
Endungen werden stillschweigend aufgelöst.

In einigen mehrdeutigen Fällen ist es besser, ein abgekürztes Wort unverändert wiederzugeben.

Beispiele:  `sr (sieur oder seigneur?), monsr (monsieur oder monseigneur?), me (maître oder messire?) `

Bei der Auflösung von Abkürzungen sollte so weit wie möglich auf Schreibweisen zurückgegriffen werden, die in anderen Teilen des bearbeiteten Textes eindeutig belegt sind, ansonsten ist die klassische Form zu bevorzugen (insbesondere für Latein).  In jedem Fall sollte man konsequent bleiben.

Die gebräuchlichen lateinischen Abkürzungen werden stillschweigend aufgelöst, sofern nicht Zweifel an der korrekten Auflösung bestehen. Die Auflösung erfolgt gemäss (mittellateinischem) Wörterbuch, ausser bei abweichender Praxis des Schreibers.

### 6.3 Abkürzungen von Mass- und Münzbezeichnungen

Abkürzungen von Mass- und Münzbezeichnungen werden ausser in Fliesstexten (Kommentaren, Bemerkungen) nicht aufgelöst und erscheinen im Abkürzungsverzeichnis. Es werden die entsprechenden Sonderzeichen verwendet.

Zur Liste der Mass- und Münzbezeichnungen vgl. (to do: Verlinkung mit Liste im Portal bzw. Wiki Tastaturbelegung -> CURRENCY SYMBOLS).

Zur Auszeichnung der Währungen, Masse und Gewichte
vgl. [`<measure/>`](../../elements/measure.de.md).
