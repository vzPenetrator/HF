# Delete (Datensatz löschen)
sql = "DELETE FROM users WHERE name = %s"
values = ("Andrey",)
cursor.execute(sql, values)
conn.commit()
print("Datensatz gelöscht.")