print( (4 + 4 == 8) and (2 + 3 == 5) )  # Prüft, ob beide Bedingungen wahr sind: (4 + 4 == 8) & (2 + 3 == 5). Ergebnis: True, da beide wahr sind.
print( (4 + 4 == 8) and (2 + 3 == 7) )  # Prüft, ob beide Bedingungen wahr sind: (4 + 4 == 8) & (2 + 3 == 7). Ergebnis: False, da 2 + 3 != 7.
print( (4 + 4 == 8) or (2 + 3 == 5) )   # Prüft, ob mindestens eine der beiden Bedingungen wahr ist: (4 + 4 == 8) oder (2 + 3 == 5). Ergebnis: True, da beide wahr sind.
print( (4 + 4 == 7) or (2 + 3 != 5) )   # Prüft, ob mindestens eine der beiden Bedingungen wahr ist: (4 + 4 == 7) oder (2 + 3 != 5). Ergebnis: True, da 2 + 3 != 5.
print( not(4 + 4 == 8) )                # Prüft, ob die Bedingung (4 + 4 == 8) falsch ist, indem sie mit `not` negiert wird. Ergebnis: False, da 4 + 4 == 8 wahr ist.