# Exercise 1: book.py

class Book:
    def __init__(self, author, title):    # constructor with two attributes
        self.author = author  # refers to the author attribute of the object that self points to
        self.title = title
        self.available = True
        self.user = None

    def __str__(self):  # "magic method" for converting object into string
        return f"Autor: {self.author}\nTitel: {self.title}\nVerfügbarkeit: {self.available}"

    # Exercise 3: Adding def add_user and def remove_user

    def add_user(self, user):
        if self.available:
            self.user = user
            self.available = False
            print(f"Das Buch '{self.title}' wurde erfolgreich von {user.name} ausgeliehen.")
            return True
        else:
            print(f"Das Buch '{self.title}' ist nicht mehr verfügbar.")
            return False

    def remove_user(self):
        if self.user is not None:
            user_name = self.user.name
            self.user.borrowed_books.remove(self)
            self.user = None
            self.available = True
            print(f"Das Buch '{self.title}' wurde von {user_name} zurückgegeben und ist jetzt wieder verfügbar.")
            return True
        else:
            print(f"Das Buch '{self.title}' wurde nicht ausgeliehen.")
            return False
