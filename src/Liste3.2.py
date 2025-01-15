# Warteschlange erzeugen (mit 5 Elementen)
queue = []
# 5 Elemente zur Warteschlange hinzufügen
queue.append(10)  # Hinzufügen von 10
queue.append(20)  # Hinzufügen von 20
queue.append(30)  # Hinzufügen von 30
queue.append(40)  # Hinzufügen von 40
queue.append(50)  # Hinzufügen von 50
# Warteschlange von vorne nach hinten abbauen
while len(queue) > 0:  # Solange die Warteschlange nicht leer ist
    print("Poppe:", queue.pop(0))  # Entfernt das erste Element (Index 0) und gibt es aus
