
# GitHub Anleitung: Öffentliches Repository erstellen und Dokumentation

## Schritt 1: GitHub-Account erstellen und einloggen
- Gehe auf [github.com](https://github.com)
- Erstelle einen Account oder melde dich an

## Schritt 2: Neues Repository erstellen
- Klicke auf das `+`-Symbol oben rechts
- Wähle `New repository`
- Vergib einen Namen, setze es auf `Public`
- Optional: README und .gitignore hinzufügen
- Erstelle das Repository

## Schritt 3: Token generieren
- Gehe zu `Settings` > `Developer settings`
- Wähle `Personal Access Tokens` > `Generate new token`
- Notiere dir den Token sicher

## Schritt 4: Git lokal installieren
### Option 1: Mit Winget (Windows)
```bash
winget install --id Git.Git -e --source winget
```

### Option 2: Manuell herunterladen
- Besuche [https://git-scm.com/](https://git-scm.com/)
- Lade die passende Version herunter und installiere Git mit den Standardoptionen

## Schritt 5: Lokales Repository einrichten (Konsole)
```bash
# Repository klonen
git clone <repo-url>

# Token bei Aufforderung eingeben

# In den Ordner wechseln
cd <repo-name>

# Datei anlegen (README.md)
echo "# Mein Projekt" > README.md

# Änderungen speichern
git add .
git commit -m "Initial commit"

# Änderungen hochladen
git push
```

## Schritt 6: Datei bearbeiten (VS Code oder Dateimanager)
- Öffne den Ordner mit Visual Studio Code oder dem Dateimanager
- Bearbeite die `README.md` Datei
- Speichere und pushe die Änderungen

## Schritt 7: Link an Lehrer senden
- Kopiere den Link zu deinem Repository
- Sende ihn per Mail an den Lehrer
