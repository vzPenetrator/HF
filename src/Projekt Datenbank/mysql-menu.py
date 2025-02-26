import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",  # Ändere dies, falls deine DB woanders läuft
        user="root",  # Dein MySQL-Benutzername
        password="password",  # Dein MySQL-Passwort
        database="testdb"  # Dein Datenbankname
    )

def insert_entry():
    conn = connect_db()
    cursor = conn.cursor()
    name = input("Gib den Namen ein: ")
    age = input("Gib das Alter ein: ")
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    print("Eintrag erfolgreich hinzugefügt!")
    conn.close()

def update_entry():
    conn = connect_db()
    cursor = conn.cursor()
    id = input("Gib die ID des zu aktualisierenden Eintrags ein: ")
    name = input("Gib den neuen Namen ein: ")
    age = input("Gib das neue Alter ein: ")
    cursor.execute("UPDATE users SET name = %s, age = %s WHERE id = %s", (name, age, id))
    conn.commit()
    print("Eintrag erfolgreich aktualisiert!")
    conn.close()

def retrieve_entries():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def delete_entry():
    conn = connect_db()
    cursor = conn.cursor()
    id = input("Gib die ID des zu löschenden Eintrags ein: ")
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    conn.commit()
    print("Eintrag erfolgreich gelöscht!")
    conn.close()

def main():
    while True:
        print("\nMenü:")
        print("1 - Neuen Eintrag hinzufügen")
        print("2 - Eintrag aktualisieren")
        print("3 - Daten abrufen")
        print("4 - Eintrag löschen")
        print("5 - Beenden")
        
        choice = input("Wähle eine Option: ")
        
        if choice == "1":
            insert_entry()
        elif choice == "2":
            update_entry()
        elif choice == "3":
            retrieve_entries()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe, bitte erneut versuchen.")

if __name__ == "__main__":
    main()