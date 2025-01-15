start = int(input("Geben Sie den Startwert des Wertebereichs ein: "))
end = int(input("Geben Sie den Endwert des Wertebereichs ein: "))
if start > end:
    print("Ungültiger Bereich: Der Startwert muss kleiner oder gleich dem Endwert sein.")
else:
    print(f"Gerade Zahlen zwischen {start} und {end}:")
    while start <= end:
        if (start % 2) == 0:                                # Prüft, ob die Zahl gerade ist
            print(start)                                    # Gibt die gerade Zahl aus
        start += 1
    print("Ausgabe beendet.")