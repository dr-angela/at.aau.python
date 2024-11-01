# made with gpt help

# Aufgabe 1
def grep():
    file_path = input("Bitte geben Sie den Dateipfad ein: ")
    keyword = input("Bitte geben Sie das zu suchende Wort ein: ")

    try:
        count = 0
        with open(file_path, 'r') as file:  # r ist reading
            for line in file:
                if keyword.lower() in line.lower(): # change into lower letters
                    count += 1
                    print(line.strip())  # for printing those lines
        print("Anzahl der gefundenen Zeilen:", count)
    except FileNotFoundError:
        print("Die angegebene Datei wurde nicht gefunden.")


if __name__ == "__main__":
    grep()
