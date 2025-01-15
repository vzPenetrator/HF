a = [66.25, 333, 333, 1, 1234.5]  # Erstellt eine Liste `a` mit den Werten: 66.25, 333, 333, 1 und 1234.5.
print(a.count(333), a.count(66.25), a.count('x'))  
# Gibt die Häufigkeit der Elemente 333, 66.25 und 'x' in der Liste `a` aus.
# `a.count(333)` gibt 2 zurück, da 333 zweimal in der Liste vorkommt.
# `a.count(66.25)` gibt 1 zurück, da 66.25 einmal in der Liste vorkommt.
# `a.count('x')` gibt 0 zurück, da 'x' nicht in der Liste ist.
a.insert(2, -1)         # Fügt das Element -1 an der Stelle mit dem Index 2 in die Liste `a` ein.
a.append(333)           # Fügt das Element 333 ans Ende der Liste `a` an.
print(a)                # Gibt die modifizierte Liste `a` aus: [66.25, 333, -1, 333, 1, 1234.5, 333]
print(a.index(333))     # Gibt den Index des ersten Auftretens von 333 in der Liste `a` aus. (In diesem Fall wird Index 1 zurückgegeben).
print(a.remove(333))    # Entfernt das erste Vorkommen von 333 aus der Liste `a`.
# Es wird keine Ausgabe zurückgegeben, da `remove()` die entfernte Zahl nicht zurückgibt.
print(a)                # Gibt die Liste `a` nach der Entfernung des ersten 333 aus: [66.25, -1, 333, 1, 1234.5, 333]
a.reverse()             # Kehrt die Reihenfolge der Elemente in der Liste `a` um.
print(a)                # Gibt die umgekehrte Liste `a` aus: [333, 1234.5, 1, 333, -1, 66.25]
a.sort()                # Sortiert die Liste `a` in aufsteigender Reihenfolge.
print(a)                # Gibt die sortierte Liste `a` aus: [-1, 1, 66.25, 333, 333, 1234.5]
print(a.pop)