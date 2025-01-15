def ausgabe():                          # Definiert eine Funktion namens 'ausgabe', die keine Argumente benötigt
    print("Die Antwort ist 42")         # Gibt die Zeichenkette "Die Antwort ist 42" aus
    print("Wie war doch die Frage?")    # Gibt die Zeichenkette "Wie war doch die Frage?" aus
def rechnen(a, b):                      # Definiert eine Funktion namens 'rechnen', die zwei Argumente 'a' und 'b' erwartet
    print(a * b)                        # Gibt das Produkt der beiden Eingabewerte 'a' und 'b' aus
def addieren(a, b):                     # Definiert eine Funktion namens 'addieren', die zwei Argumente 'a' und 'b' erwartet
    return a + b                        # Gibt die Summe von 'a' und 'b' zurück
ausgabe()                               # Ruft die Funktion 'ausgabe' auf und führt ihren Code aus
rechnen(6, 8)                           # Ruft die Funktion 'rechnen' mit den Werten 6 und 8 als Argumente auf und gibt das Produkt aus
rechnen(7, 8)                           # Ruft die Funktion 'rechnen' mit den Werten 7 und 8 als Argumente auf und gibt das Produkt aus
print(addieren(30, 12))                 # Ruft die Funktion 'addieren' mit den Werten 30 und 12 als Argumente auf und gibt die Summe aus