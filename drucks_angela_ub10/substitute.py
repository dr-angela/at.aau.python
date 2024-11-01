import os
import re

# Pfad zum Verzeichnis des Skripts ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))

# Absoluten Pfad zur Datei 'mail_addresses' im Verzeichnis 'files_ub10' erstellen
filename = os.path.join(script_dir, 'files_ub10', 'mail_addresses')


def clean_text(text):
    # Regulärer Ausdruck für E-Mail-Adressen
    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'

    # Funktion zum Bereinigen eines Wortes
    def clean_word(word):
        if re.match(email_pattern, word):
            return word  # E-Mail-Adresse bleibt unverändert
        return re.sub(r'^[^\w\s]+|[^\w\s]+$', '', word)  # Entfernen von Interpunktion

    # Text in Wörter aufteilen, jedes Wort bereinigen und wieder zusammenfügen
    cleaned_text = ' '.join(clean_word(word) for word in text.split())

    # Ersetzen mehrfacher Whitespaces durch ein einzelnes Leerzeichen
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

    return cleaned_text


# Datei einlesen
with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()

# Text bereinigen
cleaned_text = clean_text(text)

# Resultierenden String auf die Konsole ausgeben
print(cleaned_text)
