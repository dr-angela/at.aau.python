import os
import re

# Pfad zum Verzeichnis
script_dir = os.path.dirname(os.path.abspath(__file__))

# Absoluter Pfad zu den Dateien
lakes1_path = os.path.join(script_dir, 'files_ub10', 'lakes1')
lakes2_path = os.path.join(script_dir, 'files_ub10', 'lakes2')

# Dateien einlesen
with open(lakes1_path, 'r', encoding='utf-8') as f:
    lakes1_data = f.readlines()

with open(lakes2_path, 'r', encoding='utf-8') as f:
    lakes2_data = f.readlines()

# Aufgabe 1

# Seen aus lakes1 extrahieren
lakes1 = []     # leere Liste, später Tupel: (rank, lake_name)
for line in lakes1_data:
    parts = re.split(r',', line.strip())  # Zeile an Hand von Komma trennen
    rank = int(parts[0].strip('.'))  # Rang extrahieren und in eine Zahl umwandeln
    lake_name = str(parts[1].strip())  # Seename extrahieren
    lakes1.append((rank, lake_name))

# Seen und Flächen aus lakes2 extrahieren
lakes2 = {}     # leeres Dictionary
for line in lakes2_data:
    parts = re.split(r',', line.strip())  # Zeile nach Komma trennen
    lake_name = str(parts[0].strip('"'))  # Seename extrahieren
    area = float(parts[2].strip())  # Fläche extrahieren und in float umwandeln
    lakes2[lake_name] = area

# Kombiniere Seen aus lakes1 mit den Flächen aus lakes2
combined_lakes = []
for rank, lake_name in lakes1:
    if lake_name in lakes2:
        area = lakes2[lake_name]
        combined_lakes.append((rank, lake_name, area))

# Sortiere die Seen nach Rang und gib die 10 beliebtesten mit ihrer Fläche aus
combined_lakes.sort(key=lambda x: x[0])
for rank, lake_name, area in combined_lakes[:10]:
    print(f"{lake_name},{area}")
