# Funktion zur Ausgabe der BMI-Kategorisierung
def bmi_ausgabe(bmi):
    if bmi < 18.5:
        print("Untergewicht")
    elif 18.5 <= bmi < 25:
        print("Normalgewicht")
    else:
        print("Übergewicht")

# Funktion zum Einfügen von Personendaten in den Datenspeicher
def person_daten_hinzufuegen(name, groesse, gewicht, datenbank):
    bmi = berechne_bmi(gewicht, groesse)                                            # Berechne den BMI
    person = {"Name": name, "Größe": groesse, "Gewicht": gewicht, "BMI": bmi}
    datenbank.append(person)                                                        # Füge die Person zur Datenbank hinzu
    print(f"{name} wurde hinzugefügt. BMI: {bmi:.2f}")
    bmi_ausgabe(bmi)                                                                # Zeige die BMI-Kategorisierung

# Funktion zur Berechnung des BMI
def berechne_bmi(gewicht, groesse):
    return gewicht / (groesse ** 2)  # BMI = Gewicht / (Größe^2)

# Hauptfunktion, die den gesamten Ablauf steuert
def main():
    datenbank = []                                                                  # Liste, um alle Personen zu speichern
    while True:
        # Benutzereingaben
        name = input("Name der Person: ")
        groesse = float(input("Größe in Metern (z.B. 1.75): "))
        gewicht = float(input("Gewicht in Kilogramm: "))
        
        # Personendaten hinzufügen
        person_daten_hinzufuegen(name, groesse, gewicht, datenbank)
        
        # Frage, ob eine weitere Person erfasst werden soll
        weitermachen = input("Weitere Person hinzufügen? (j/n): ")
        if weitermachen.lower() == 'n':
            break
    
    # Ausgabe aller gespeicherten Personen
    print("\nGespeicherte Personen und deren BMI:")
    for person in datenbank:
        print(f"Name: {person['Name']}, Größe: {person['Größe']} m, Gewicht: {person['Gewicht']} kg, BMI: {person['BMI']:.2f}")

# Das Programm startet hier
if __name__ == "__main__":
    main()