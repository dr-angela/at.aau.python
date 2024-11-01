def word_count(input_file, output_file, search_word):
    word_freq = {}
    with open(input_file, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                # Entfernen von Interpunktionszeichen
                word = word.strip(",.?!;:")
                # Groß-/Kleinschreibung ignorieren
                word = word.lower()
                # Wenn das Wort dem gesuchten Wort entspricht, erhöhe die Häufigkeit um 1
                if word == search_word.lower():
                    word_freq[word] = word_freq.get(word, 0) + 1

    # Ergebnisse in die Ausgabedatei schreiben
    with open(output_file, 'w') as output:  # w is for write
        for word, freq in word_freq.items():
            output.write(f"{word}\t{freq}\n")


if __name__ == "__main__":
    input_file = input("Bitte geben Sie den Dateipfad der Eingabedatei ein: ")
    output_file = input("Bitte geben Sie den Dateipfad der Ausgabedatei ein: ")
    search_word = input("Bitte geben Sie das gesuchte Wort ein: ")

    word_count(input_file, output_file, search_word)
