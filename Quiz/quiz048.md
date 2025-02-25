# Quiz 048

## Paper Solution
![image](https://github.com/user-attachments/assets/fef43ddf-c807-4bb5-87b1-f320b2d25fa4)

## Flow Chart
![image](https://github.com/user-attachments/assets/362be7ab-99b2-4f36-8f06-b353d6b753aa)

## Code
```.py
class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"The book {self.title} by {self.author} has the code: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def show_book(self):
        if not self.books: return "The libary doesn't have any book"
        else:
            for book in self.books:
                print(book.display_info())

book1 = Book("To Kill a Mockingbird", "Harper Lee", "1234567890")
book2 = Book("1984", "George Orwell", "2345678901")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "3456789012")

# Create a library
my_library = Library()

# Add books to the library
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# Show all books in the library
print("Books in the library:")
my_library.show_book()
```
## Proof of work
![image](https://github.com/user-attachments/assets/d477a274-9d53-4db9-b60d-ae7255fd1c77)
