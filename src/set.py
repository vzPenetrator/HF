zahlen1 = set()                 # Erstellt ein leeres Set `zahlen1`. Ein Set ist eine ungeordnete Sammlung von einzigartigen Werten.
zahlen2 = {"a", "b"}            # Erstellt ein Set `zahlen2` mit den Elementen "a" und "b".
print(zahlen2)                  # Gibt das Set `zahlen2` aus. In diesem Fall: {'a', 'b'}.
i = 1                           # Initialisiert die Variable `i` mit dem Wert 1.
while (i < 50):                 # Schleife, die so lange läuft, wie `i` kleiner als 50 ist.
    zahlen1.add(i)              # Fügt `i` zum Set `zahlen1` hinzu.
    i += 1                      # Erhöht `i` um 1.
print(zahlen1)                  # Gibt das Set `zahlen1` aus. Es enthält die Zahlen von 1 bis 49.
i = 0                           # Setzt die Variable `i` auf 0 zurück.
while (i < 6):                  # Schleife, die 6 mal durchläuft.
    zahlen2.add(zahlen1.pop())  # Entfernt und gibt ein beliebiges Element aus `zahlen1` zurück und fügt es zu `zahlen2` hinzu.
    i += 1                      # Erhöht `i` um 1.
print(zahlen2)                  # Gibt das Set `zahlen2` aus. Es enthält die ursprünglichen Elemente plus 6 zufällige Zahlen aus `zahlen1`.
print(zahlen1)                  # Gibt das Set `zahlen1` aus. Es enthält die verbleibenden Zahlen, nachdem 6 Elemente entfernt wurden.
