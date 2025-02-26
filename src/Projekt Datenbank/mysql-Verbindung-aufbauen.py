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