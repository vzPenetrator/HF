# 1) Benutzerführung:
# Zeige beim Start des Programms ein Menü an.
# Das Menü soll folgende Optionen enthalten:
# 1: Neue Berechnung durchführen
# 0: Programm beenden
# Das Programm soll erst enden, wenn der Benutzer 0 eingibt.
# 2) Eingaben:
# Der Benutzer soll zwei Zahlen eingeben können.
# Der Benutzer soll danach einen Operator wählen können: +, -, *, /.
# Falsche Eingaben sollen erkannt und mit einer Fehlermeldung behandelt werden.
# 3) Rechenoperationen: Implementiere folgende Rechenoperationen in separaten Funktionen:
# addiere(a, b) → Addiert zwei Zahlen.
# subtrahiere(a, b) → Subtrahiert zwei Zahlen.
# multipliziere(a, b) → Multipliziert zwei Zahlen.
# dividiere(a, b) → Teilt zwei Zahlen, aber verhindere die Division durch 0.
# 4) Fehlerbehandlung:
# Wenn der Benutzer etwas anderes als eine Zahl eingibt, soll eine Fehlermeldung erscheinen.
# Bei der Division durch 0 soll eine Fehlermeldung erscheinen, dass dies nicht erlaubt ist.
# 6) Programmlogik:
# Nutze eine Endlosschleife (while True), um sicherzustellen, dass der Taschenrechner erst endet, wenn der Benutzer 0 eingibt.
# Verwende if-elif-else, um die verschiedenen Rechenoperationen und Optionen zu steuern.


def addiere(zahl1, zahl2):
    return zahl1 + zahl2

def subtrahiere(zahl1, zahl2):
    return zahl1 - zahl2

def multipliziere(zahl1, zahl2):
    return zahl1 * zahl2

def dividiere(zahl1, zahl2):
    if zahl2 == 0:
        print("Fehler: Division durch 0 ist nicht erlaubt.")
        return None
    return zahl1 / zahl2



print("Menu:")
print("Die Eingabe von 1, starte eine neue Berechnung")
print("Die Eingabe von 0, beendet das Rechenprogramm")
menuEingabe = input("Eingabe: ")
while menuEingabe == "1":
    print("Gib 2 Zahlen ein")
    zahl1 = int(input("Bitte gib die erste Zahl ein: "))
    zahl2 = int(input("Bitte gib die zweite Zahl ein: "))
    print("Bitte wähle den gewünschten Operator")
    Operator = input("Bitte den Operator eingeben (+, -, *, /): ")
    if Operator == "+":
            print("Addition")
            result = addiere (zahl1, zahl2)
            print(result)
    elif Operator == "-":
            result = subtrahiere (zahl1, zahl2)
            print(result)
    elif Operator == "*":
            result = multipliziere (zahl1, zahl2)
            print(result)
    elif Operator == "/":
            result = dividiere (zahl1, zahl2)
            if result is not None:
                print(result)      
    else:
        print("Bitte korrekten Operator wählen")
    
    menuEingabe = input("Eingabe: 1 für neue Berechnung, 0 zum Beenden: ")
print("Programm Beendet")