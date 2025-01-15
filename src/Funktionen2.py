def rechnen(a, b = 8):      # Definiert eine Funktion 'rechnen', bei der 'b' einen Standardwert von 8 hat
    print(a * b)            # Multipliziert 'a' mit 'b' und gibt das Ergebnis aus
def addieren(a, *b):        # Definiert eine Funktion 'addieren', bei der 'b' eine variable Anzahl von Argumenten ist
    erg = a                 # Setzt 'erg' gleich dem Wert von 'a'
    for i in b:             # Iteriert über jedes Element in der Liste 'b'
        erg += i            # Addiert jedes Element aus 'b' zu 'erg'
    print(erg)              # Gibt das Ergebnis der Addition aus
rechnen(6)                  # Ruft die Funktion 'rechnen' mit 'a=6' und dem Standardwert für 'b=8' auf
rechnen(6, 7)               # Ruft die Funktion 'rechnen' mit 'a=6' und 'b=7' auf (überschreibt den Standardwert von 'b')
addieren(6)                 # Ruft die Funktion 'addieren' mit 'a=6' und keinem weiteren Argument auf
addieren(6, 1)              # Ruft die Funktion 'addieren' mit 'a=6' und einem zusätzlichen Argument '1' auf
addieren(6, 1, 1)           # Ruft die Funktion 'addieren' mit 'a=6' und zwei zusätzlichen Argumenten '1' und '1' auf