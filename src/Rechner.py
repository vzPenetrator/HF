# Aufgabe:
# Erstellen Sie eine neue Datei mit dem Namen Rechner.py. Der Anwender soll zur Eingabe von zwei
# Zahlen aufgefordert werden. Dazu verwenden Sie die Funktion input(). Diese liefert aber einen
# String und für die folgenden Berechnungen benötigen Sie Zahlen. Sie müssen also eine Typ konvertierung vornehmen (siehe Abschnitt 5.4.5).
# Diese beiden so ermittelten Zahlen sollen
# 1. addiert,
# 2. subtrahiert,
# 3. dividiert,
# 4. multipliziert und
# 5. potenziert werden.
# Die Ergebnisse sollen in einer Ergebnisvariablen gespeichert und mit den eingegebenen Werten
# sowie einer Beschreibung der Operation ausgegeben werden. Die Ergebnisvariable kann immer
# wieder für die Speicherung der einzelnen Berechnungen verwendet werden. 
# Eine mögliche Lösung finden Sie im Anhang ab Seite 83.
# Beachten Sie, dass das Beispiel nicht gegen Fehleingaben abgesichert wird. Wenn der Anwender also keine Zahlen eingibt,
# wird ein Fehler auftreten. Das ist einkalkuliert, da derzeit noch nicht das Wissen um eine Fehlerbehandlung vorhanden ist.

# Code:
a = int(input("Gib die erste Zahl ein"))
b = int(input("Gib die zweite Zahl ein"))
print(type(a))
print(a + b)                                    # Gibt die Rechnung "a + b" aus.
print(a - b)                                    # Gibt die Rechnung "a - b" aus.
print(a / b)                                    # Gibt die Rechnung "a / b" aus.
print(a * b)                                    # Gibt die Rechnung "a * b" aus.
print(a ** b)                                   # Gibt die Rechnung "a * b (hoch2)" aus.