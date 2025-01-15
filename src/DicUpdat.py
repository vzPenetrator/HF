teilnehmer = {}                   # Erstellt ein leeres Dictionary `teilnehmer`, das später die Namen und Firmen speichern wird.
name = input("Name")              # Fordert den Benutzer auf, seinen Namen einzugeben und speichert ihn in der Variablen `name`.
firma = input("Firma")            # Fordert den Benutzer auf, den Firmennamen einzugeben und speichert ihn in der Variablen `firma`.
teilnehmer.update({name: firma})  # Fügt dem Dictionary `teilnehmer` ein neues Schlüssel-Wert-Paar hinzu.
# Der Schlüssel ist der eingegebene Name, der Wert ist die eingegebene Firma.
print(teilnehmer)                 # Gibt das `teilnehmer` Dictionary aus, das nun den Namen und die Firma des Teilnehmers enthält.