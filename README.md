# Library Management System

A simple library management system built with Python's object-oriented programming principles. It manages books and members, tracks borrowed books, and provides basic functionalities such as adding books, registering members, and borrowing/returning books.

## Classes

### Book
Represents a book in the library.

- **Attributes:** `title`, `author`, `book_no`, `is_borrowed`
- **Methods:**
  - `borrow()` — Marks the book as borrowed
  - `return_book()` — Marks the book as returned
  - `__str__()` — Returns a string representation of the book

### Member
Represents a library member.

- **Attributes:** `name`, `member_id`, `borrowed_books`
- **Methods:**
  - `borrow_book(book)` — Adds a book to the member's borrowed list and marks it as borrowed
  - `return_book(book)` — Removes a book from the member's borrowed list and marks it as returned
  - `__str__()` — Returns a string representation of the member

### Library
Manages the collection of books and members.

- **Attributes:** `books`, `members`
- **Methods:**
  - `add_book(book)` — Adds a new book to the library
  - `register_member(member)` — Registers a new member
  - `find_book(book_no)` — Finds a book by its book number
  - `find_member(member_id)` — Finds a member by their ID
  - `borrow_book(member_id, book_no)` — Allows a member to borrow a book
  - `return_book(member_id, book_no)` — Allows a member to return a book
  - `__str__()` — Returns the library's current state

## Usage

```python
# Create a library
library = Library()

# Add books
library.add_book(Book("Things Fall Apart", "Chinua Achebe", "B001"))
library.add_book(Book("You Said I Was Your Favourite", "Monica Murphy", "B002"))
library.add_book(Book("Predator", "Tom Cain", "B003"))
library.add_book(Book("Sophie's World", "Jostein Gaarder", "B004"))
library.add_book(Book("The Stranger", "Albert Camus", "B005"))
library.add_book(Book("Soumission", "Michel Houellebecq", "B006"))
library.add_book(Book("The Murder That Never Was", "Julie McElwain", "B007"))

# Register members
library.register_member(Member("Nilla", "M001", []))
library.register_member(Member("Nalla", "M002", []))
library.register_member(Member("Jacky", "M003", []))
library.register_member(Member("James", "M004", []))

# Borrow and return books
library.borrow_book("M001", "B001")
library.borrow_book("M001", "B004")
library.borrow_book("M002", "B003")
library.return_book("M001", "B001")

# Print library state
print(library)
```

## Contact

- **Name:** Belvah Shanyisa
- **Email:** misshuey3@gmail.com
- **GitHub:** [Belvah](https://github.com/Belvah)
