# Exercise 2: book.py
from book import Book


class User:
    def __init__(self, name: str, email: str):  # constructor
        self.name = name    # refers to the name attribute of the object that self points to
        self.email = email
        self.borrowed_books = set()  # set with immutable elements for all borrowed books

    def __str__(self):
        return f"Name: {self.name}\nAusgeliehene Bücher: {len(self.borrowed_books)}"

    # Exercise 4: Adding def borrow_book and def return_book
    def borrow_book(self, book: 'Book'):    # book  is an object of type Book
        if book in self.borrowed_books:
            print(f"{self.name} hat das Buch '{book.title}' bereits ausgeliehen.")
            return False
        if book.add_user(self):
            print(f"{self.name} hat das Buch '{book.title}' erfolgreich ausgeliehen.")
            return True
        return False

    def return_book(self, book: 'Book'):
        if book not in self.borrowed_books:
            print(f"{self.name} hat das Buch '{book.title}' nicht ausgeliehen.")
            return False
        if book.remove_user():
            print(f"{self.name} hat das Buch '{book.title}' erfolgreich zurückgegeben.")
            return True
        return False
