
# LIBRARAY SYSTEM

#Create a class Book that represents a book in a library.

class Book:
#The Book class containing attributes such as title, author, and ISBN.
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

#Implementing a method to display book information.
    def display_format(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN:{self.isbn}"


#Create a subclass EBook that inherits from the Book
class Ebook(Book):

#The EBook Class containing an additional attribute for the file format (e.g., PDF, EPUB).
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

#Overriding the display method to include the file format.
    def display_format(self):
        return f"{super().display_format()}, File Format: {self.file_format}"


#Create a class Library that represents a library.
class Library:

#The Library class should have a list to store books.
    def __init__(self):
        self.books = []

#Implementing a method to add a book to the library
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print("Book added to the library.")
        else:
            print("Invalid book object")


#Implementing a method to display all books in the library
    def display_books(self):
        if self.books:
            for book in self.books:
                print(book.display_format())
        else:
            print("Library is Empty")


#Implementing a method to search for a book by title
    def search_by_title(self, title):
        found_books = [book for book in self.books if book.title == title]
        if found_books:
            for book in found_books:
                print(book.display_format())
        else:
            print("No books are found with the given title")

#Creating instances of the Book, Library, and EBook classes and test their functionality.
library = Library()

book1 = Book("Wings of fire", "Abdul kalam", 457285348)
ebook1 = Ebook("sruihg", "shakespeare", 736567890, "PDF")

library.add_book(book1)
library.add_book(ebook1)

# Display all books in the library
all_books = library.display_books()

# Search for a book by title
search_result = library.search_by_title("Wings of fire")

all_books, search_result




