i = 0                       # Initialisiert die Variable `i` mit dem Wert 0.
while True:                 # Startet eine Endlosschleife, die nur durch `break` beendet wird.
    i += 1                  # Erhöht den Wert von `i` um 1 in jedem Schleifendurchlauf.
    print(i, ":", i * i)    # Gibt den aktuellen Wert von `i` und dessen Quadrat aus.
    if i > 9:               # Überprüft, ob `i` größer als 9 ist.
        break               # Beendet die Schleife, wenn die Bedingung erfüllt ist.
print("Schleife beendet")   # Gibt aus, dass die Schleife beendet wurde.