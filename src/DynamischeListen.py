zahlen = [2, 3, 5, 7, 11]                   # Erstellt eine Liste namens `zahlen` mit den Werten: 2, 3, 5, 7 und 11.
print(zahlen[0])                            # Gibt das erste Element der Liste `zahlen` aus, welches 2 ist.
person = ["Hans", "Dampf", 45, True, None]  # Erstellt eine Liste namens `person` mit den Werten: Vorname, Nachname, Alter, Wahrheitswert und `None`.
print(person[1])                            # Gibt das zweite Element der Liste `person` aus, welches "Dampf" ist.
liste1 = (zahlen, person)                   # Erstellt ein Tupel namens `liste1`, das die beiden Listen `zahlen` und `person` enthält.
print(liste1[0])                            # Gibt das erste Element von `liste1` aus, welches die Liste `zahlen` ist: [2, 3, 5, 7, 11].
print(liste1[1][0])                         # Gibt das erste Element der Liste `person` aus (das zweite Element von `liste1`): "Hans".
liste2 = [[1, 2], [3, 4]]                   # Erstellt eine Liste namens `liste2`, die zwei weitere Listen ([1, 2] und [3, 4]) enthält.
print(liste2[1][1])                         # Gibt das zweite Element der zweiten Liste in `liste2` aus, welches 4 ist.