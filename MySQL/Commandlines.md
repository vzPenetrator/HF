# Commandlines für MySQL

Create database name;          Generiert eine Datenbank
USE mydatabase;                Benutzt die gewünschte Datenbank
cd mydatabase;                 Geht in die Datenbank rein


Dies generiert eine Tabelle mit Benutzer, einer ID, Namen und E-Mail register.
CREATE TABLE Benutzer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);



Diese Zeilen fügen die Informationen für die jeweiligen Felder hinzu.
INSERT INTO Benutzer (name, email) VALUES
('Max Mustermann', 'max.mustermann@example.com');


SELECT * FROM Benutzer;             Gibt nun die hinterlegte Tabelle mit informationen in der Shell aus.

