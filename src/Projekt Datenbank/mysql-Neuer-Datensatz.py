# Create (Datensatz einfügen)
sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
values = ("Andrey", 28)
cursor.execute(sql, values)
conn.commit()
print(f"Datensatz eingefügt, ID: {cursor.lastrowid}")