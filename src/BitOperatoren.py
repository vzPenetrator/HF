zahl = 42                            # Variable `zahl` wird mit dem Wert 42 initialisiert.
a = zahl << 1                        # Bitweise Verschiebung von `zahl` um 1 Bit nach links (entspricht Multiplikation mit 2).
b = zahl >> 1                        # Bitweise Verschiebung von `zahl` um 1 Bit nach rechts (entspricht ganzzahliger Division durch 2).
c = zahl << 2                        # Bitweise Verschiebung von `zahl` um 2 Bits nach links (entspricht Multiplikation mit 4).
d = zahl << 3                        # Bitweise Verschiebung von `zahl` um 3 Bits nach links (entspricht Multiplikation mit 8).
print("Der Wert von 42 << 1: " , a)  # Gibt den Wert von 42 nach 1 Bit Linksverschiebung aus.
print("Der Wert von 42 >> 1: " , b)  # Gibt den Wert von 42 nach 1 Bit Rechtsverschiebung aus.
print("Der Wert von 42 << 2: " , c)  # Gibt den Wert von 42 nach 2 Bits Linksverschiebung aus.
print("Der Wert von 42 << 3: " , d)  # Gibt den Wert von 42 nach 3 Bits Linksverschiebung aus.
zahl1 = 10                           # Variable `zahl1` wird mit dem Wert 10 initialisiert.
zahl2 = 12                           # Variable `zahl2` wird mit dem Wert 12 initialisiert.
a = zahl1 & zahl2                    # Bitweises UND zwischen `zahl1` und `zahl2`.
b = zahl1 | zahl2                    # Bitweises ODER zwischen `zahl1` und `zahl2`.
c = zahl1 ^ zahl2                    # Bitweises XOR zwischen `zahl1` und `zahl2`.
d = ~zahl1                           # Bitweise Negation von `zahl1`.
print("Der Wert von 10 & 12: " , a)  # Gibt das Ergebnis des bitweisen UND zwischen 10 und 12 aus.
print("Der Wert von 10 | 12: " , b)  # Gibt das Ergebnis des bitweisen ODER zwischen 10 und 12 aus.
print("Der Wert von 10 ^ 12: " , c)  # Gibt das Ergebnis des bitweisen XOR zwischen 10 und 12 aus.
print("Der Wert von ~ 10: " , d)     # Gibt das Ergebnis der bitweisen Negation von 10 aus.
