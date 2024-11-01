import os
import re

# Pfad zum Verzeichnis des Skripts ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))

# Absoluten Pfad zur Datei 'mail_addresses' im Verzeichnis 'files_ub10' erstellen
filename = os.path.join(script_dir, 'files_ub10', 'mail_addresses')


def extract_emails(filename):
    # Datei im Lesemodus mit UTF-8-Kodierung öffnen und den gesamten Text einlesen
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # Regulärer Ausdruck für E-Mail-Adressen
    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'

    # Alle E-Mail-Adressen im Text finden, die dem Muster entsprechen
    emails = re.findall(email_pattern, text)

    # Gefundene E-Mail-Adressen zurückgeben
    return emails


# E-Mail-Adressen aus der Datei extrahieren
emails = extract_emails(filename)

# Jede gefundene E-Mail-Adresse ausgeben
for email in emails:
    print(email)

# Regulärer Ausdruck für E-Mail-Adressen
# [A-Za-z0-9._%+-]+ : Ein oder mehrere Zeichen, die Buchstaben (groß oder klein), Ziffern, Punkte, Unterstriche, Prozentzeichen, Pluszeichen oder Bindestriche sein können.
# @                : Ein Literal-@-Zeichen.
# [A-Za-z0-9.-]+   : Ein oder mehrere Zeichen, die Buchstaben (groß oder klein), Ziffern, Punkte oder Bindestriche sein können.
# \.               : Ein Literal-Punkt. Der Backslash \ wird verwendet, um den Punkt zu maskieren, da der Punkt in regulären Ausdrücken ein Platzhalter für ein beliebiges Zeichen ist.
# [A-Za-z]{2,4}    : Zwei bis vier Buchstaben, die die Domain-Endung darstellen (z.B. .com, .org, .net).
