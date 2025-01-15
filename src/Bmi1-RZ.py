# Beispielcode für Abschlussaufgabe Kapitel 5:
 
def calculate_bmi(weight: float, height: float):
    bmi: float = weight / (height * height)
 
    if bmi < 18.5:
        print("Untergewicht")
    elif bmi >= 25:
        print("Übergewicht")
    else:
        print("Normalgewicht")
 
 
def main():
 
 
    weight = None
    while weight is None:
        try:
            weight = float(input("Geben Sie Ihr Gewicht an (kg): "))
        except ValueError as err:
            print("Invalid input value!")
            print(err)
 
    height = None
    while height is None:
        try:
            height = float(input("Geben Sie ihre Körpergrösse an (m): "))
        except ValueError as err:
            print("Invalid input value!")
            print(err)
 
    calculate_bmi(weight, height)
 
 
if __name__ == "__main__":
    main()