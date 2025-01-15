gz = (1234, 5678, 87654, 12333, 4711)                                                   # Definiert ein Tupel `gz` mit Geheimzahlen.
i = 0                                                                                   # Initialisiert den Zähler `i` auf 0 (Versuchsanzahl).
while i < 3:                                                                            # Startet eine Schleife, die maximal 3 Versuche erlaubt.
    e = int(input("Eingabe der Geheimzahl\n"))                                          # Fordert den Benutzer auf, eine Geheimzahl einzugeben und konvertiert die Eingabe in eine Ganzzahl.
    if e in gz:                                                                         # Überprüft, ob die eingegebene Geheimzahl in der Liste `gz` enthalten ist.
        print("Auszahlen")                                                              # Gibt "Auszahlen" aus, wenn die Geheimzahl korrekt ist.
        break                                                                           # Beendet die Schleife, da die richtige Geheimzahl eingegeben wurde.
    print("Die Geheimzahl war leider nicht korrekt.")                                   # Gibt eine Fehlermeldung aus, wenn die Geheimzahl nicht korrekt ist.
    i += 1                                                                              # Erhöht den Zähler `i` um 1 für den nächsten Versuch.
    if i >= 3:                                                                          # Überprüft, ob der Benutzer bereits 3 Versuche unternommen hat.
        print("Sie haben zu viele Versuche benötigt.\nDie Karte wird eingezogen.")      # Gibt eine Nachricht aus, wenn die maximalen Versuche überschritten wurden.
