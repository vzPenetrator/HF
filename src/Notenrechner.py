def berechne_note(punkte):
    return round(1 + 5 * (punkte + 5) / 45, 2)
def main():
    while True:
        try:
            punkte = int(input("Gib die erreichte Punktzahl (0-45) ein: "))
            if 0 <= punkte <= 45:
                note = berechne_note(punkte)
                print(f"Deine Note: {note:.2f}")
                break
            else:
                print("Ungültige Eingabe! Bitte eine Zahl zwischen 0 und 45 eingeben.")
        except ValueError:
            print("Ungültige Eingabe! Bitte eine ganze Zahl eingeben.")
if __name__ == "__main__":
    main()