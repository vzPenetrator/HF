s = (2, 3, 5, 7)    # Erstellt ein Tupel `s` mit den Werten: 2, 3, 5, 7.
t = (11, 13)        # Erstellt ein Tupel `t` mit den Werten: 11, 13.
u = s + t           # Verbindet die Tupel `s` und `t` miteinander und erstellt ein neues Tupel `u`. 
# Das Ergebnis ist das Tupel: (2, 3, 5, 7, 11, 13).
print(u)            # Gibt das Tupel `u` aus, welches die kombinierten Werte von `s` und `t` enthält: (2, 3, 5, 7, 11, 13).
v = (s * 3, t * 2)  # Multipliziert das Tupel `s` 3-mal und das Tupel `t` 2-mal.
# Das Tupel `s * 3` ergibt (2, 3, 5, 7, 2, 3, 5, 7, 2, 3, 5, 7).
# Das Tupel `t * 2` ergibt (11, 13, 11, 13).
print(v)            # Gibt das Tupel `v` aus, welches die wiederholten Tupel von `s` und `t` enthält: ((2, 3, 5, 7, 2, 3, 5, 7, 2, 3, 5, 7), (11, 13, 11, 13)).