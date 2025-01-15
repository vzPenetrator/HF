def addiere(a, b):
    return a + b

def subtrahiere(a, b):
    return a - b

def multipliziere(a, b):
    return a * b

def dividiere(a, b):
    if b == 0:
        return "Fehler: Division durch 0 ist nicht erlaubt."
    return a / b

def eingabe_zahl(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")

def eingabe_operator():
    while True:
        operator = input("Wähle einen Operator (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Ungültiger Operator. Bitte wähle +, -, * oder /.")

def berechnung_durchfuehren():
    zahl1 = eingabe_zahl("Gib die erste Zahl ein: ")
    zahl2 = eingabe_zahl("Gib die zweite Zahl ein: ")
    operator = eingabe_operator()

    if operator == '+':
        ergebnis = addiere(zahl1, zahl2)
    elif operator == '-':
        ergebnis = subtrahiere(zahl1, zahl2)
    elif operator == '*':
        ergebnis = multipliziere(zahl1, zahl2)
    elif operator == '/':
        ergebnis = dividiere(zahl1, zahl2)

    print(f"Das Ergebnis ist: {ergebnis}")

def menue_anzeigen():
    print("\nMenü:")
    print("1: Neue Berechnung durchführen")
    print("0: Programm beenden")

def main():
    while True:
        menue_anzeigen()
        auswahl = input("Wähle eine Option: ")

        if auswahl == '1':
            berechnung_durchfuehren()
        elif auswahl == '0':
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Auswahl. Bitte 1 oder 0 eingeben.")

if __name__ == "__main__":
    main()