person = ("Hans", "Otto")                       # Erstellt ein Tupel `person` mit den Werten "Hans" und "Otto".
print(person[0])                                # Gibt das erste Element des Tupels `person` aus, also "Hans".
person2 = {"vname": "Hans", "nname": "Otto"}    # Erstellt ein Dictionary `person2` mit den Schlüsseln "vname" und "nname", deren Werte "Hans" und "Otto" sind.
print(type(person2))                            # Gibt den Datentyp von `person2` aus. Da es sich um ein Dictionary handelt, wird <class 'dict'> angezeigt.
print(person2)                                  # Gibt das Dictionary `person2` aus: {'vname': 'Hans', 'nname': 'Otto'}.
print(person2["vname"])                         # Gibt den Wert des Schlüssels "vname" im Dictionary `person2` aus, also "Hans".
for v in person2.values():                      # Iteriert über die Werte im Dictionary `person2`.
    print(v)                                    # Gibt jeden Wert im Dictionary `person2` aus. In diesem Fall "Hans" und "Otto".
daten = {1: 0, 2: True}                         # Erstellt ein Dictionary `daten` mit den Schlüsseln 1 und 2, deren Werte 0 und True sind.
logisch = {True: False, False: True}            # Erstellt ein Dictionary `logisch` mit den Schlüsseln True und False, deren Werte False und True sind.
print(logisch[True])                            # Gibt den Wert des Schlüssels True im Dictionary `logisch` aus, also False.
auchnochlogisch = {(1, 2): True, (1, 2, 3): False}  # Erstellt ein Dictionary `auchnochlogisch` mit Tupeln als Schlüsseln.
# Die Schlüssel sind die Tupel (1, 2) und (1, 2, 3), deren Werte True und False sind.
print(auchnochlogisch[(1, 2, 3)])                   # Gibt den Wert des Schlüssels (1, 2, 3) im Dictionary `auchnochlogisch` aus, also False.
# warumgehtdasnicht = {[1, 2]: True, [1, 2, 3]: False}  
# Dieser Code führt zu einem Fehler, weil Listen unveränderlich sind und nicht als Schlüssel in einem Dictionary verwendet werden können.
# Listen sind veränderlich (mutable), daher können sie nicht als Schlüssel für ein Dictionary verwendet werden.
