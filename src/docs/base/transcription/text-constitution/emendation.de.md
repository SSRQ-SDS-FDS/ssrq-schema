# Eingriffe in den Text

## Drucktexte

Eindeutige Druckfehler werden mit [`<choice>`](choice.de.md), 
[`<sic>`](sic.de.md) und [`<corr>`](corr.de.md) korrigiert.

## Handschriftliche Texte

### Klammern

Vom Schreiber in runde Klammern gesetzte Textteile werden ohne Eingriff
identisch wiedergegeben.

### Lücken

Vom Schreiber zwecks späterer Ergänzung bewusst gelassene Lücken 
(Freiräume) wurden in analogen Bänden durch drei Auslassungspunkte
ohne Klammer gekennzeichnet und in einer textkritischen Anmerkung unter
Angabe der Grösse der Textlücke erläutert. 
In der digitalen Edition werden sie mit [`<space/>`](space.de.md) getaggt.

Referenzpunkte bzw. Reverenzpunkte vor Namen oder Amtsbezeichnungen 
wurden in der analogen Edition durch 2 Punkte ohne Klammer wiedergegeben. 
In der digitalen Edition werden sie ebenfalls mit 2 Punkten ohne Klammer 
wiedergegeben.

### Weggelassene Textteile

Vom Schreiber irrtümlich weggelassene Textteile,
z. B. beim Abschreiben durch Augensprung übersehene Zeilen,
wurden in der analogen Edition durch einen Ersatztext aus
einer anderen originalen oder kopialen Quelle oder durch
den Bearbeitenden selbst im Sinne einer sinngemässen
Textwiedergabe in eckigen Klammern ergänzt.
Eine Anmerkung war notwendig.

In der digitalen Edition wird der ergänzte Text mit
[`<supplied>`](supplied.de.md) getaggt.
Falls notwendig, kann eine Anmerkung mit [`<note>`](note.de.md) 
hinzugesetzt werden. 
Bei Ergänzungen anhand einer anderen Vorlage (2. Original, Kopie etc.)
wird auf diesen Textzeugen referenziert. 
Vgl. dazu auch [`<app>`](app.de.md).

Ein Textverlust infolge von Beschädigungen wie etwa Mäusefrass, 
verblasster Tinte, Brand, Pilzbefall, Rissen, Löchern, Kassation usw. 
wird mit [`<damage>`](damage.de.md) in Kombination mit [`<gap/>`](gap.de.md),
[`<supplied>`](supplied.de.md) oder [`<unclear>`](unclear.de.md) erfasst.

### Wiederholungen

Irrtümliche Wiederholungen von Silben, Wörtern und Satzteilen (Dittographien) 
sollen mit [`<choice>`](choice.de.md) in Kombination mit [`<sic>`](sic.de.md) 
und [`<corr>`](corr.de.md) normalisiert werden.

### Unsichere Lesung

Bei Wörtern mit unsicherer Lesung wurden bei der analogen Edition in einer
textkritischen Anmerkung denkbare Lesevarianten angeführt.
Sie konnten zusätzlich mit `[?]` gekennzeichnet werden.

In der digitalen Edition werden unsichere Lesungen mit
[`<unclear>`](unclear.de.md) getaggt.
Falls dies nicht genügt, kann auch eine Anmerkung mit
[`<note>`](note.de.md) gemacht werden.

### Schreib-, Sprach- und Stilfehler

Schreib-, Sprach- und Stilfehler werden im Text nicht korrigiert.
In der analogen Edition wurden sie in einer textkritischen Anmerkung 
erläutert oder mit einem `[!]` gekennzeichnet.

In der digitalen Edition werden solche Fehler mit [`<sic>`](sic.de.md)
gekennzeichnet und allenfalls mit [`<choice>`](choice.de.md) zusammen
mit [`<sic>`](sic.de.md) und [`<corr>`](corr.de.md) korrigiert.

### Bewusste Auslassungen von Text durch den Bearbeitenden

Bewusste Auslassungen von Text durch den Bearbeitenden (Teilabdruck) werden
in der analogen Edition mit `[...]` und in der digitalen mit 
[`<gap reason="irrelevant"/>`](gap.de.md) wiedergegeben.
Dies sollte, wenn möglich, vermieden werden.

Werden spätere Nachträge nicht beim Original, sondern als eigenständiges
Stück ediert, können die Teile, die bereits in einem früheren Original
ediert wurden, mit [`<gap/>`](gap.de.md) weggelassen werden.
Auf das bereits edierte Stück wird verwiesen.
Eine Anmerkung in [`<note>`](note.md) oder eine Bemerkung
in [`<back>`](back.de.md) ist nötig.

### Behandlung redaktioneller Eingriffe des Schreibers

=== "Allgemeine Regeln"

    Grundsätzlich hat ein transkribierter Text, auch wenn er auf einer von
    verschiedenen Händen mehrfach überarbeiteten Vorlage basiert,
    gut lesbar und verständlich zu sein. 
    Der Bearbeitende muss sich für eine Textvariante entscheiden und
    die übrigen Varianten mit Tags auszeichnen.
    Zu beachten sind besonders Streichungen 
    bzw. Rasuren und Zusätze bzw. Nachträge.

=== "Streichungen"

    Auf einfache Korrekturen, die beim Schreibvorgang entstanden sind, 
    wird nur in Ausnahmefällen hingewiesen.
    
    Streichungen wurden in der analogen Transkription mit `a–...–a` 
    gekennzeichnet und in einer textkritischen Anmerkung aufgeführt.
    
    In der digitalen Edition werden Streichungen mit [`<del>`](del.de.md)
    getaggt.
    
    Bei komplexen, hierarchieübergreifenden Streichungen müssen 
    [`<delSpan/>`](delSpan.de.md) und [`<anchor/>`](anchor.de.md)
    eingesetzt werden.
    
    Durch Streichungen unlesbar gewordene Textstellen wurden in der analogen 
    Edition mit `[...]a` gekennzeichnet und mit einer Anmerkung versehen.
    
    In der digitalen Edition werden sie mit [`<del>`](del.de.md) und
    [`<gap/>`](gap.de.md) ausgezeichnet.
    
    Bei Textstellen, die Streichungen und Hinzufügungen in Kombination 
    aufweisen, muss [`<subst>`](subst.de.md) verwendet werden.

=== "Rasuren"

    Mit Rasuren wurde in der analogen Edition gleich verfahren wie mit
    Streichungen und eine textkritische Anmerkung war erforderlich.
    
    In der digitalen Edition wird eine Rasur mit 
    [`<del rend="rubbing">`](del.de.md) ausgezeichnet.
    Wenn bei Rasuren oder auch bei heftigen Streichungen gar nichts
    mehr lesbar ist, wird [`<gap/>`](gap.de.md) innerhalb von 
    [`<del>`](del.de.md) verwendet.

=== "Zusätze oder Nachträge"

    Zusätze oder Nachträge von erster oder späterer Hand müssen
    in den Text aufgenommen werden und wurden in der analogen
    Edition in einer textkritischen Anmerkung erklärt.
    
    In der digitalen Edition wird der Tag [`<add>`](add.de.md) verwendet.
    Der Ort der Ergänzung muss und die Hand der ergänzten Stelle kann
    festgehalten werden.

    Bei komplexen, hierarchieübergreifenden Zusätzen müssen 
    [`<addSpan/>`](addSpan.de.md) und [`<anchor/>`](anchor.de.md)
    eingesetzt werden.