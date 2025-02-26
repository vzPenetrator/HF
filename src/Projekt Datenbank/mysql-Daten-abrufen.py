# Read (Daten abrufen)
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Alle Datensätze:")
for row in rows:
    print(row)