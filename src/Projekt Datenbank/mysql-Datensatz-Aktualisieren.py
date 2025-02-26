# Update (Datensatz aktualisieren)
sql = "UPDATE users SET age = %s WHERE name = %s"
values = (30, "Andrey")
cursor.execute(sql, values)
conn.commit()
print("Datensatz aktualisiert.")