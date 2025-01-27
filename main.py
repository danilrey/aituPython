class Book:
    def __init__(self, title, author,price):
        self.title = title
        self.author = author
        self.price = price
    def __str__(self):
        return f"{self.title} by {self.author} - ${self.price}\n"
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_price(self):
        return self.price

class Shelf:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def get_books(self):
        return self.books
    def get_total_books(self):
        return len(self.books)

class Library:
    def __init__(self):
        self.shelves = []
    def add_shelf(self, shelf):
        self.shelves.append(shelf)
    def get_shelves(self):
        return self.shelves
    def get_total_books(self):
        total_books = 0
        for shelf in self.shelves:
            total_books += shelf.get_total_books()
        return total_books
    def get_books(self):
        books = []
        for shelf in self.shelves:
            books.extend(shelf.get_books())
        return ''.join(str(book) for book in books)

book1 = Book("Harry Potter", "J.K. Rowling", 20)
book2 = Book("The Da Vinci Code", "Dan Brown", 15)
book3 = Book("The Alchemist", "Paulo Coelho", 10)
book4 = Book("The Catcher in the Rye", "J.D. Salinger", 12)
book5 = Book("The Great Gatsby", "F. Scott Fitzgerald", 18)
book6 = Book("The Hobbit", "J.R.R. Tolkien", 25)
book7 = Book("The Outsider", "Steven King", 30)
book8 = Book("The Shining", "Steven King", 35)
book9 = Book("The Stand", "Steven King", 40)
book10 = Book("The Hunger Games", "Suzanne Collins", 22)

shelve1 = Shelf()
shelve1.add_book(book1)
shelve1.add_book(book2)
shelve1.add_book(book3)
shelve1.add_book(book4)
shelve1.add_book(book5)

shelve2 = Shelf()
shelve2.add_book(book6)
shelve2.add_book(book7)
shelve2.add_book(book8)
shelve2.add_book(book9)
shelve2.add_book(book10)

library = Library()
library.add_shelf(shelve1)
library.add_shelf(shelve2)

print("Total Books in Shelf 1: ", shelve1.get_total_books())
print("Total Books in Shelf 2: ", shelve2.get_total_books())
print("Total Books in Library: ", library.get_total_books())
print("Books in Library: ", library.get_books())
