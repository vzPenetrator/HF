start = int(input("Geben Sie den Startwert des Wertebereichs ein: "))
end = int(input("Geben Sie den Endwert des Wertebereichs ein: "))
if start > end:
    print("Ungültiger Bereich: Der Startwert muss kleiner oder gleich dem Endwert sein.")
else:
    print(f"Gerade Zahlen zwischen {start} und {end}:")
    for number in range(start, end + 1):                            # Iteriert über den Wertebereich
        if number % 2 == 0:                                         # Überprüft, ob die Zahl gerade ist
            print(number)                                           # Gibt die gerade Zahl aus
    print("Ausgabe beendet.")