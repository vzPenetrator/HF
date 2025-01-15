# Eine Liste, die alle erfassten Daten der Personen speichert
personen_daten = []

# Start einer Schleife zur Eingabe von mehreren Personen
while True:
    # Eine Liste, die die Daten einer einzelnen Person speichert
    person_daten = []
    
    # Abfrage des Namens der Person
    name = input("Bitte geben Sie den Namen der Person ein: ")
    
    # Abfrage der Größe der Person in Metern
    groesse = float(input(f"Bitte geben Sie die Größe von {name} in Metern ein: "))
    
    # Abfrage des Gewichts der Person in Kilogramm
    gewicht = float(input(f"Bitte geben Sie das Gewicht von {name} in Kilogramm ein: "))
    
    # Berechnung des BMI
    bmi = gewicht / (groesse ** 2)
    
    # Ausgabe des BMI und der Bewertung
    print(f"Der BMI von {name} ist {bmi:.2f}.")
    
    if bmi < 18.5:
        print(f"{name} hat Untergewicht.")
    elif bmi >= 25:
        print(f"{name} hat Übergewicht.")
    else:
        print(f"{name} hat Normalgewicht.")
    
    # Speichern der Personendaten in der Personendatenliste
    person_daten.append(name)
    person_daten.append(groesse)
    person_daten.append(gewicht)
    person_daten.append(bmi)
    
    # Hinzufügen der Daten der Person zur Gesamtliste
    personen_daten.append(person_daten)
    
    # Abfrage, ob eine weitere Person erfasst werden soll
    weitere_person = input("Möchten Sie eine weitere Person erfassen? (Drücken Sie 'q' zum Beenden, Enter zum Fortfahren): ")
    
    if weitere_person.lower() == "q":
        break

# Ausgabe der gesamten Liste mit den Daten aller Personen
print("\nAlle erfassten Daten:")
for person in personen_daten:
    print(f"Name: {person[0]}, Größe: {person[1]} m, Gewicht: {person[2]} kg, BMI: {person[3]:.2f}")