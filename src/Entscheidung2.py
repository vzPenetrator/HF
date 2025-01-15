erg = int(input("Geben Sie eine Zahl zwischen 0 und 10 ein: "))  # Fragt den Benutzer nach einer Zahl zwischen 0 und 10 und konvertiert die Eingabe in eine Ganzzahl.
print("Sie haben ", erg, " eingegeben!")                         # Gibt die eingegebene Zahl aus.
if erg > 10:                                                     # Überprüft, ob die Zahl größer als 10 ist.
    print("Der Wert ist zu groß")                                # Gibt eine Fehlermeldung aus, wenn der Wert zu groß ist.
    print("Starten Sie das Programm noch einmal")                # Fordert den Benutzer auf, das Programm erneut zu starten.
elif erg < 0:                                                    # Überprüft, ob die Zahl kleiner als 0 ist.
    print("Der Wert ist zu klein")                               # Gibt eine Fehlermeldung aus, wenn der Wert zu klein ist.
    print("Starten Sie das Programm noch einmal")                # Fordert den Benutzer auf, das Programm erneut zu starten.
elif erg == 5:                                                   # Überprüft, ob die Zahl gleich 5 ist.
    print("Treffer")                                             # Gibt "Treffer" aus, wenn der Wert 5 ist.
else:                                                            # Alle anderen Fälle.
    print("Daneben")                                             # Gibt "Daneben" aus, wenn der Wert weder zu groß, zu klein noch gleich 5 ist.
