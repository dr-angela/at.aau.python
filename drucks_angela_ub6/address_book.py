# 2.1. Kontakt hinzufügen / updaten
def add_info(book, alias, key, value):
    """Aktualisiert einen Kontakt bzw. legt diesen an, sollte er nicht vorhanden sein.
    Dabei wird ein Kontaktfeld (key) mit dem gewünschten Wert(value) aktualisiert oder hinzufügt.

    'book' ist eine Variable, die auf das Adressbuch-Dictionary zeigt:
    Erinnere dich: Dictionaries sind veränderlich!
    """
    if alias in book:  # alias is primary key
        book[alias][key] = value  # 'key' is for specific field in book (name, mail, phone..)
    else:
        book[alias] = {key: value}


# 2.3. Kontaktfeld anzeigen
def show_info(book, alias, key):
    """Gibt die Angabe in einem Kontaktfeld (key) für einen Kontakt (alias) aus (Format: key -> value)
    Sollte der Kontakt (alias) oder das Kontaktfeld (key) nicht vorhanden sein,
    wird eine kurze Meldung (Kein Eintrag für / Keine Information zu) ausgegeben
    """
    if alias in book:  # check if alias exists
        if key in book[alias]:  # check if special key exists
            print(f"{key} -> {book[alias][key]}")  # print if key exists
        else:  # if key not exists
            print(f"Keine Informationen zu {key} für den Eintrag {alias} vorhanden.")
    else:  # if alias does not exist
        print(f"Keine Informationen zu {alias} vorhanden.")


# 2.2. Kontakt anzeigen
def show_entry(book, alias):
    """Gibt den kompletten Eintrag zu einem Kontakt (alias) aus,
    das heißt alle Kontaktfelder und die zugehörigen Werte
    Ist der Kontakt nicht vorhanden, wird eine dementsprechende Meldung ausgegeben.
    """
    if alias in book:
        print(f"Eintrag für '{alias}': ")
        for key, value in book[alias].items():  # Iterate over all contact fields and values for the alias
            print(f"{key} -> {value}")
    else:
        print(f"Keine Informationen zu {alias} vorhanden.")


# 2.4. Kontakt löschen
def del_entry(book, alias):
    """Löscht den gesamten Eintrag für einen Alias vom Adressbuch (sofern vorhanden)
    """
    if alias in book:
        del book[alias]  # 'del' is a python keyword for deleting objects in containers..
        print(f"Eintrag für '{alias}' wurde gelöscht.")
    else:
        print(f"Kein Eintrag für '{alias} gefunden, es konnte nichts gelöscht werden.'")


# 2.5. Kontaktfeld löschen
def del_info(book, alias, key):
    """Löscht ein bestimmtes Kontaktfeld (key) aus dem Kontakteintrag für alias
    Die restlichen Kontaktfelder des Kontaktes sollen nicht gelöscht werden.
    Stelle sicher, dass es zu keinem Fehler kommt, wenn Kontakt (alias) oder Kontaktfeld (key) nicht vorhanden sind.
    """
    if alias in book:  # check if alias exists
        if key in book[alias]:  # check if key exists
            del book[alias][key]
        else:
            print(f"Kein Eintrag zu {key} für '{alias}' gefunden.")
    else:
        print(f"Kein Eintrag für {alias} gefunden. Es konnte nichts gelöscht werden.")


# 2.6. Adressbuch anzeigen (alle Einträge)
def show_book(book):
    """Gibt das komplette Adressbuch aus, das heißt, alle Kontakte zusammen mit deren Kontaktfeldern
    Tipp: Vielleicht kannst du eine der Funktionen oben wiederverwenden.
    """
    if book:  # check if book exists
        print("Adressbuch:")
        for alias in book:  # Iterating over all entries
            show_entry(book, alias)  # Using function from 2.2.
            print()  # Leerzeile
    else:
        print("Das Adressbuch ist leer, keine Einträge vorhanden.")


if __name__ == '__main__':

    # Ein leeres Telefonbuch (Dictionary) erstellen
    book = {}

    # Menü
    menu = """1 - Kontakt hinzufügen / updaten
2 - Kontakt anzeigen
3 - Kontaktfeld anzeigen
4 - Kontakt löschen
5 - Kontaktfeld löschen
6 - Adressbuch anzeigen
Zum Beenden ENTER dücken
>> """

    # Schleife für User-Input
    while True:
        choice = input(menu)

        if choice == "":
            break
        try:
            choice = int(choice)
        except:
            print("Sorry, deine Wahl wurde nicht erkannt.\n")
            continue

        if choice == 1:
            alias = input("Alias: ")
            key = input("Kontaktfeld: ")
            value = input("Wert: ")
            add_info(book, alias, key, value)

        elif choice == 2:
            alias = input("Alias: ")
            show_entry(book, alias)

        elif choice == 3:
            alias = input("Alias: ")
            key = input("Kontaktfeld: ")
            show_info(book, alias, key)

        elif choice == 4:
            alias = input("Alias: ")
            del_entry(book, alias)

        elif choice == 5:
            alias = input("Alias: ")
            key = input("Kontaktfeld: ")
            del_info(book, alias, key)

        elif choice == 6:
            show_book(book)

        else:
            print("Sorry, deine Wahl wurde nicht erkannt.\n")
