# Commandlines für MySQL

Create database name;          # Generiert eine Datenbank (bei name wird die Benennung der DB eingegeben)
USE mydatabase;                # Benutzt die gewünschte Datenbank
cd mydatabase;                 # Geht in die Datenbank rein


/# Dies generiert eine Tabelle mit Benutzer, einer ID, Namen und E-Mail register.
CREATE TABLE Benutzer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);



/# Diese Zeilen fügen die Informationen für die jeweiligen Felder hinzu.
INSERT INTO Benutzer (name, email) VALUES
('Max Mustermann', 'max.mustermann@example.com');


SELECT * FROM Benutzer;                  # Gibt nun die hinterlegte Tabelle mit informationen in der Shell aus.

SHOW DATABASES;                          # Alle Datenbanken auflisten: Zeige eine Übersicht aller vorhandenen Datenbanken.

SELECT DATABASE();                       # Wählt die ()-Datenbank aus.Zwischen Datenbanken wechseln: Wechsle zu einer anderen Datenbank und überprüfe, welche Tabellen darin existieren.

SHOW TABLES                              # Alle Tabellen einer Datenbank anzeigen: Liste alle Tabellen in der aktiven Datenbank auf.

SHOW COLUMNS FROM Bentuzer;              # Tabellenstruktur anzeigen: Zeige die Struktur einer bestehenden Tabelle (z. B. Spaltennamen, Datentypen).

SELECT * FROM benutzer                   # Daten nach bestimmten Kriterien abrufen: 
WHERE email LIKE '%@example.com';        # Schreibe eine Abfrage, um z. B. alle Benutzer mit einer bestimmten E-Mail-Domain (@example.com) auszugeben.

ORDER BY name ASC;                                  # Daten sortieren: ASC = A-Z / DESC = Z-A
ORDER BY name DESC;                                 # Sortiere die Daten in einer Tabelle nach einem bestimmten Feld, z. B. alphabetisch nach dem Namen.

LIMIT 5;                                            # Daten begrenzen: Gib nur eine begrenzte Anzahl von Datensätzen aus, z. B. die ersten 5 Einträge

ALTER TABLE Benutzer;                               # Neue Spalte hinzufügen:
ADD COLUMN geburtsdatum DATE;                       # Füge einer bestehenden Tabelle eine neue Spalte hinzu, z. B. für das Geburtsdatum.
ADD COLUMN gbeurtsdatum DATE AFTER name;            # Fügt die Spalte Geburtsdatum direkt nach der Spalte Name ein.

ALTER TABLE Benutzer                                # Spalte umbenennen:
CHANGE COLUMN email contact_email VARCHAR(255);     # Benenne eine bestehende Spalte um, z. B. von email zu contact_email.

ALTER TABLE Benutzer                                # Spalte löschen:
DROP COLUMN geburtsdatum;                           # Entferne eine Spalte aus der Tabelle, z. B. die zuvor hinzugefügte Spalte.

DELETE FROM Benutzer                                #Einzelne Datensätze löschen:
Where name = 'Test';                                # Lösche bestimmte Einträge basierend auf einem Kriterium, z. B. alle Benutzer mit dem Namen "Test".

RENAME TABLE benutzer TO kunden;                    # Tabelle umbenennen: Ändere den Namen einer bestehenden Tabelle.

DROP TABLE Benutzer;                                # Tabelle löschen: Entferne eine Tabelle aus der Datenbank.
DROP TABLE IF EXISTS benutzer;                      # Tabelle löschen, falls Tabelle vorhanden.