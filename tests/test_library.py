import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from library import Book, PrintedBook, EBook, User, Librarian, Library

def test_book_creation():
    book = Book("Test Book", "Test Author", 2023)
    assert book.get_title() == "Test Book"
    assert book.get_author() == "Test Author"
    assert book.get_year() == 2023
    assert book.is_available() == True

def test_book_borrow_return():
    book = Book("Test Book", "Test Author", 2023)
    book.mark_as_taken()
    assert book.is_available() == False
    book.mark_as_returned()
    assert book.is_available() == True

def test_printed_book():
    pbook = PrintedBook("Printed Book", "Author", 2023, 300, "хорошая")
    assert pbook.pages == 300
    assert pbook.condition == "хорошая"
    assert pbook.get_title() == "Printed Book"

def test_ebook():
    ebook = EBook("E Book", "Author", 2023, 2, "pdf")
    assert ebook.file_size == 2
    assert ebook.format == "pdf"

def test_user_borrow():
    user = User("Test User")
    book = Book("Test Book", "Author", 2023)
    user.borrow(book)
    assert len(user.get_borrowed_books()) == 1
    user.return_book(book)
    assert len(user.get_borrowed_books()) == 0

def test_library():
    library = Library()
    book = Book("Test Book", "Author", 2023)
    user = User("Test User")
    
    library.add_book(book)
    library.add_user(user)
    
    found_book = library.find_book("Test Book")
    assert found_book is not None
    assert found_book.get_title() == "Test Book"

def test_librarian():
    library = Library()
    librarian = Librarian("Test Librarian")
    book = Book("Test Book", "Author", 2023)
    user = User("Test User")
    
    librarian.add_book(library, book)
    librarian.register_user(library, user)
    
    assert library.find_book("Test Book") is not None

if __name__ == "__main__":
    test_book_creation()
    test_book_borrow_return()
    test_printed_book()
    test_ebook()
    test_user_borrow()
    test_library()
    test_librarian()
    print("All tests passed!")
