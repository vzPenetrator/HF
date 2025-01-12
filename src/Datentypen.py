a = "text"                  # a ist ein String (Text).
print(type(a))              # Ausgabe: <class 'str'>, da "a" ein String ist.
b = 1                       # b ist eine Ganzzahl (Integer).
print(type(b))              # Ausgabe: <class 'int'>, da "b" ein Integer ist.
c = 1.0                     # c ist eine Fließkommazahl (Float).
print(type(c))              # Ausgabe: <class 'float'>, da "c" ein Float ist.
d = True                    # d ist ein boolescher Wert (Boolean).
print(type(d))              # Ausgabe: <class 'bool'>, da "d" ein Boolean ist.
print(1 == True)            # Ausgabe: True, da 1 und True im Vergleich gleich sind (True entspricht numerisch 1).
e = 1 + 3j                  # e ist eine komplexe Zahl (mit Real- und Imaginärteil).
print(type(e))              # Ausgabe: <class 'complex'>, da "e" eine komplexe Zahl ist.
f = 4e2                     # f ist eine Zahl in wissenschaftlicher Schreibweise (4 × 10² = 400.0).
print(type(f))              # Ausgabe: <class 'float'>, da "f" als Fließkommazahl interpretiert wird.
'''g = 1L                   
print(type(g))'''
print("abc\adef")           #Ausgabe "abcdef"