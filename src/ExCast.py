var_1 = 4                        # Variablen var_1 wird der Wert 4 (eine Ganzzahl) zugewiesen.
var_2 = 3.14                     # Variablen var_2 wird der Wert 3.14 (eine Fließkommazahl) zugewiesen.
var_3 = "123"                    # Variablen var_3 wird der String "123" zugewiesen.
print(type(var_1))               # Gibt den Datentyp von var_1 aus (hier: int).
print(type(var_2))               # Gibt den Datentyp von var_2 aus (hier: float).
print(type(var_3))               # Gibt den Datentyp von var_3 aus (hier: str).
print(type(float(var_1)))        # Wandelt var_1 zu einem Float um und gibt den Datentyp aus (hier: float).
print(type(float(var_3)))        # Wandelt var_3 zu einem Float um (wobei der Inhalt als Zahl interpretiert wird) und gibt den Datentyp aus (hier: float).
print(type(int(var_2)))          # Wandelt var_2 zu einer Ganzzahl um und gibt den Datentyp aus (hier: int).
print(type(int(var_3)))          # Wandelt var_3 zu einer Ganzzahl um (wobei der Inhalt als Zahl interpretiert wird) und gibt den Datentyp aus (hier: int).
print(type(str(var_1)))          # Wandelt var_1 zu einem String um und gibt den Datentyp aus (hier: str).
print(type(str(var_2)))          # Wandelt var_2 zu einem String um und gibt den Datentyp aus (hier: str).