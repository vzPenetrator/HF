Zähler = 1
eingabe = ''
while (Zähler <= 3 and eingabe !='AB123456'):
    print("Passwortabfrage")
    eingabe = input("Eingabe")
    if eingabe == 'AB123456':
        print("Es war was war und es kommt was kommt")
    else:
        print("Hallo gehts!")
    Zähler = Zähler + 1