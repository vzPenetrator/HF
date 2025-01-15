# Stapel erzeugen (mit 5 Elementen)
stack = []
# 5 Elemente zum Stapel hinzufügen
stack.append(10)  # Hinzufügen von 10
stack.append(20)  # Hinzufügen von 20
stack.append(30)  # Hinzufügen von 30
stack.append(40)  # Hinzufügen von 40
stack.append(50)  # Hinzufügen von 50
# Stapel von oben nach unten abbauen
while stack:  # Solange der Stapel nicht leer ist
    print("Poppe:", stack.pop())  # Entfernt das oberste Element und gibt es aus