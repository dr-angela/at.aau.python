# Task 5: pos_tagging.py

import spacy

# Lade das deutsche Modell, nlp: natural language processing
nlp = spacy.load("de_core_news_sm")

# Beispielsatz
text = "Wenn Fliegen hinter Fliegen fliegen, fliegen Fliegen Fliegen nach."

# Verarbeite den Text mit dem Modell
doc = nlp(text)

# List Comprehension, um eine Liste mit Tupeln (Wort, Wortart) zu erstellen
# Interpunktionszeichen werden nicht berücksichtigt
pos_tags = [(token.text, token.pos_) for token in doc if not token.is_punct]

# Ausgabe
print(pos_tags)
