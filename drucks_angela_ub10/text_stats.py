import os
import spacy

# Spacy-Modell laden
nlp = spacy.load("de_core_news_sm")

# Pfad zum Verzeichnis des Skripts ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))

# Absoluten Pfad zur Datei 'zelda' im Verzeichnis 'files_ub10' erstellen
filename = os.path.join(script_dir, 'files_ub10', 'zelda')


def calculate_stats(text):
    # Text mit Spacy verarbeiten
    doc = nlp(text)

    # Anzahl der Zeichen
    num_chars = len(text)

    # Anzahl der Token
    num_tokens = len(doc)

    # Anzahl der Types
    num_types = len(set(token.text for token in doc))

    # Anzahl der Sätze
    num_sents = len(list(doc.sents))

    # Durchschnittliche Satzlänge in Token
    avg_sent_length = num_tokens / num_sents if num_sents > 0 else 0

    # Durchschnittliche Tokenlänge in Zeichen
    avg_token_length = sum(len(token.text) for token in doc) / num_tokens if num_tokens > 0 else 0

    return num_chars, num_tokens, num_types, num_sents, avg_sent_length, avg_token_length


# Datei einlesen
with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()

# Statistiken berechnen
num_chars, num_tokens, num_types, num_sents, avg_sent_length, avg_token_length = calculate_stats(text)

# Resultierende Statistiken auf die Konsole ausgeben
print(f"Anzahl der Zeichen: {num_chars}")
print(f"Anzahl der Token: {num_tokens}")
print(f"Anzahl der Types: {num_types}")
print(f"Anzahl der Sätze: {num_sents}")
print(f"Durchschnittliche Satzlänge in Token: {avg_sent_length:.2f}")
print(f"Durchschnittliche Tokenlänge in Zeichen: {avg_token_length:.2f}")
