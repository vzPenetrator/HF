# Benutzer gibt den Start- und Endwert des Wertebereichs ein.
start = int(input("Geben Sie den Startwert des Wertebereichs ein: "))   # Startwert des Bereichs.
end = int(input("Geben Sie den Endwert des Wertebereichs ein: "))       # Endwert des Bereichs.

# Überprüft, ob der Startwert kleiner oder gleich dem Endwert ist.
if start > end:
    print("Ungültiger Bereich: Der Startwert muss kleiner oder gleich dem Endwert sein.")
else:
    print(f"Gerade Zahlen zwischen {start} und {end}:")
    while start <= end:                                                 # Schleife läuft, solange der Startwert kleiner oder gleich dem Endwert ist.
        if (start % 2) == 0:                                            # Überprüft, ob die Zahl gerade ist.
            print(start)                                                # Gibt die gerade Zahl aus.
        start += 1                                                      # Erhöht den Startwert um 1.
    print("Ausgabe beendet.")