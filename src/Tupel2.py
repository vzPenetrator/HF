zahlen = (2, 3, 5, 7, 11)                   # Erstellt ein Tupel namens `zahlen` mit den Werten: 2, 3, 5, 7 und 11.
print(zahlen[0])                            # Gibt das erste Element des Tupels `zahlen` aus, welches 2 ist.
person = ("Hans", "Dampf", 45, True, None)  # Erstellt ein Tupel namens `person` mit den Werten: Vorname, Nachname, Alter, Wahrheitswert und `None`.
print(person[1])                            # Gibt das zweite Element des Tupels `person` aus, welches "Dampf" ist.
tupel1 = (zahlen, person)                   # Erstellt ein Tupel namens `tupel1`, das die beiden Tupel `zahlen` und `person` enthält.
print(tupel1[0])                            # Gibt das erste Element von `tupel1` aus, welches das Tupel `zahlen` ist: (2, 3, 5, 7, 11).
print(tupel1[1][0])                         # Gibt das erste Element des Tupels `person` aus (das zweite Element von `tupel1`): "Hans".
tupel2 = ((1, 2), (3, 4))                   # Erstellt ein Tupel namens `tupel2`, das zwei weitere Tupel (1, 2) und (3, 4) enthält.
print(tupel2[1][1])                         # Gibt das zweite Element des zweiten Tupels in `tupel2` aus, welches 4 ist.