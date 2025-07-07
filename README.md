# Manuelles Aktualisieren von `requirements.txt` mit **pigar**

> Dieses Dokument beschreibt in vier Schritten, wie du **pigar** manuell ausführst, um deine Abhängigkeitsliste (`requirements.txt`) aktuell zu halten.

---

## 1  Überblick

**pigar** analysiert die Import‑Anweisungen deines Projekts (einschließlich Jupyter‑Notebooks) und erstellt daraus eine `requirements.txt`, die nur die tatsächlich genutzten Pakete enthält – keine transitiven Abhängigkeiten.

---

## 2  Voraussetzungen

| Voraussetzung      | Empfehlung                                                                       |
| ------------------ | -------------------------------------------------------------------------------- |
| Python‑Version     | ≥ 3.8                                                                            |
| Virtuelle Umgebung | *dringend empfohlen* (z. B. `python -m venv .venv && source .venv/bin/activate`) |
| Internetzugang     | Für Installation von **pigar** und Paketrecherche                                |

---

## 3  Installation

```bash
pip install --upgrade pigar
```

*(Füge **pigar** in deine dev‑Abhängigkeiten ein, damit es allen Mitwirkenden zur Verfügung steht.)*

---

## 4  Schnellstart

```bash
# Im Projektstamm ausführen
pigar gen -f requirements.txt .
```

* **`gen`** – erzeugt/aktualisiert die Datei.
* **`-f`** – Ziel‑Datei (Standard: `requirements.txt`).
* `.` – Verzeichnis, das gescannt werden soll (mehrere Pfade möglich, z. B. `src tests`).

Nach dem Lauf:

1. Prüfe mit `git diff requirements.txt`, ob die Änderungen erwartbar sind.
2. Bei Bedarf `git add requirements.txt` und committen.

---
