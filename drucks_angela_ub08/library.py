from EBook import EBook
from book import Book
from user import User

# Assignment 8: Rental system for bookstore
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: 'Book'):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)
            print()

    def find_book_by_title(self, title: str):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_available_books(self):
        # creates a list 'available_books' containing all the books that are marked available
        available_books = [book for book in self.books if book.available]
        return available_books


# Testing implementation
if __name__ == "__main__":
    # Creating books and e-books
    book1 = Book("J. R. R. Tolkien", "Der Hobbit")
    book2 = Book("J. K. Rowling", "Harry Potter und der Stein der Weisen")
    book3 = Book("George Orwell", "1984")
    ebook1 = EBook("Stephen King", "The Shining")
    ebook2 = EBook("Agatha Christie", "Murder on the Orient Express")
    ebook3 = EBook("J. D. Salinger", "The Catcher in the Rye")

    # Creating two test users
    user1 = User("Bibi Blocksberg", "b.blocksberg@aau.at")
    user2 = User("User Two", "user2@example.com")

    # Creating a library object
    library = Library()

    # Adding books and e-books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(ebook1)
    library.add_book(ebook2)
    library.add_book(ebook3)

    # Displaying all books and e-books
    print("Alle Bücher in der Bibliothek:")
    library.display_books()

    # Renting and returning books and e-books by users
    print("\nAusleihe und Rückgabe von Büchern und E-Books:")
    user1.borrow_book(book1)
    user1.borrow_book(ebook1)
    user1.return_book(book1)
    user2.borrow_book(ebook2)
    user2.borrow_book(book3)

    # Displaying available books and e-books again
    print("\nVerfügbare Bücher und E-Books in der Bibliothek:")
    available_items = library.find_available_books()
    for item in available_items:
        print(item)