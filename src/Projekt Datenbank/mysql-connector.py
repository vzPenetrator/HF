import mysql.connector

# Verbindung zur MySQL-Datenbank herstellen
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Dein MySQL-Benutzername
    password="Is365Td$",  # Dein MySQL-Passwort
    database="LogbuchDB"  # Name deiner Datenbank
)
cursor = conn.cursor()
print("Verbindung erfolgreich!")

# Tabelle erstellen (falls nicht vorhanden)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT
    )
""")
conn.commit()
print("Tabelle erstellt oder bereits vorhanden.")

# Create (Datensatz einfügen)
sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
values = ("Andrey", 28)
cursor.execute(sql, values)
conn.commit()
print(f"Datensatz eingefügt, ID: {cursor.lastrowid}")

# Read (Daten abrufen)
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Alle Datensätze:")
for row in rows:
    print(row)

# Update (Datensatz aktualisieren)
sql = "UPDATE users SET age = %s WHERE name = %s"
values = (30, "Andrey")
cursor.execute(sql, values)
conn.commit()
print("Datensatz aktualisiert.")

# Delete (Datensatz löschen)
sql = "DELETE FROM users WHERE name = %s"
values = ("Andrey",)
cursor.execute(sql, values)
conn.commit()
print("Datensatz gelöscht.")

# Verbindung schließen
cursor.close()
conn.close()
print("Verbindung geschlossen.")