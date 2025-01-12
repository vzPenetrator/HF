var_1 = True                    # var_1 ist ein boolescher Wert mit dem Wahrheitswert "True".
var_2 = True                    # var_2 ist ebenfalls "True".
print(var_1 + var_2)            # Ausgabe: 2, da True numerisch als 1 interpretiert wird (1 + 1 = 2).
print(bool(var_1))              # Prüft den Wahrheitswert von var_1. Ausgabe: True, da var_1 bereits True ist.
print(bool(5))                  # Prüft den Wahrheitswert der Zahl 5. Ausgabe: True, da jede Zahl ≠ 0 True ergibt.
print(bool(-42))                # Prüft den Wahrheitswert der Zahl -42. Ausgabe: True, da jede Zahl ≠ 0 True ergibt.
print(bool(0))                  # Prüft den Wahrheitswert von 0. Ausgabe: False, da 0 der einzige Zahlenwert ist, der False ergibt.