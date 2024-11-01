# Exercise 5: ebook.py
from book import Book

class EBook(Book):  # class SubClass(ParentClass)
    # Initializing ebook with given instances
    def __init__(self, author: str, title: str):
        super().__init__(author, title)
        self.borrowed_users = set()

    # User borrows ebook, if limit of 3 is not reached yet
    def add_user(self, user):
        if len(self.borrowed_users) < 3:
            self.borrowed_users.add(user)
            print(f"Das E-Book '{self.title}' wurde erfolgreich von {user.name} ausgeliehen.")
            return True
        else:
            print(f"Das E-Book '{self.title}' kann nicht mehr ausgeliehen werden, da die maximale Ausleihgrenze erreicht ist.")
            return False

    # User returns ebook
    def remove_user(self):
        if self.borrowed_users:
            user = self.borrowed_users.pop()    # pop() is built-in method for removing elements from a set
            print(f"Das E-Book '{self.title}' wurde von {user.name} zurückgegeben.")
            return True
        else:
            print(f"Das E-Book '{self.title}' wurde nicht ausgeliehen.")
            return False
