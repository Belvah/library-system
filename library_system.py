class Book:
    def __init__(self, title, author, book_no):
        self.title = title
        self.author = author
        self.book_no = book_no
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed.")
            return False
        self.is_borrowed = True
        return True

    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}' is not currently borrowed.")
            return False
        self.is_borrowed = False
        return True

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book({self.book_no}): '{self.title}' by {self.author} [{status}]"


class Member:
    def __init__(self, name, member_id, borrowed_books):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
                print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}'.")

    def __str__(self):
        book_titles = ", ".join(b.title for b in self.borrowed_books) or "None"
        return f"Member({self.member_id}): {self.name} | Borrowed: [{book_titles}]"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: '{book.title}'")

    def register_member(self, member):
        self.members.append(member)
        print(f"Registered member: {member.name}")

    def find_book(self, book_no):
        for book in self.books:
            if book.book_no == book_no:
                return book
        print(f"Book with number '{book_no}' not found.")
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        print(f"Member with ID '{member_id}' not found.")
        return None

    def borrow_book(self, member_id, book_no):
        member = self.find_member(member_id)
        book = self.find_book(book_no)
        if member and book:
            member.borrow_book(book)

    def return_book(self, member_id, book_no):
        member = self.find_member(member_id)
        book = self.find_book(book_no)
        if member and book:
            member.return_book(book)

    def __str__(self):
        lines = ["=== Library State ==="]
        lines.append(f"Books ({len(self.books)}):")
        for book in self.books:
            lines.append(f"  {book}")
        lines.append(f"Members ({len(self.members)}):")
        for member in self.members:
            lines.append(f"  {member}")
        return "\n".join(lines)


# --- Main Program ---
if __name__ == "__main__":
    library = Library()

    # Add books
    b1 = Book("Things Fall Apart", "Chinua Achebe", "B001")
    b2 = Book("You Said I Was Your Favourite", "Monica Murphy", "B002")
    b3 = Book("Predator", "Tom Cain", "B003")
    b4 = Book("Sophie's World", "Jostein Gaarder", "B004")
    b5 = Book("The Stranger", "Albert Camus", "B005")
    b6 = Book("Soumission", "Michel Houellebecq", "B006")
    b7 = Book("The Murder That Never Was", "Julie McElwain", "B007")

    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)
    library.add_book(b4)
    library.add_book(b5)
    library.add_book(b6)
    library.add_book(b7)

    print()

    # Register members
    m1 = Member("Nilla", "M001", [])
    m2 = Member("Nalla", "M002", [])
    m3 = Member("Jacky", "M003", [])
    m4 = Member("James", "M004", [])

    library.register_member(m1)
    library.register_member(m2)
    library.register_member(m3)
    library.register_member(m4)

    print("\n" + str(library))

    # Borrow books
    print("\n--- Borrowing ---")
    library.borrow_book("M001", "B001")
    library.borrow_book("M001", "B004")
    library.borrow_book("M002", "B003")
    library.borrow_book("M003", "B005")
    library.borrow_book("M004", "B007")

    print("\n" + str(library))

    # Try to borrow an already-borrowed book
    print("\n--- Attempting duplicate borrow ---")
    library.borrow_book("M002", "B001")

    # Return a book
    print("\n--- Returning ---")
    library.return_book("M001", "B001")

    print("\n" + str(library))

    # Borrow the now-returned book
    print("\n--- Nalla borrows the returned book ---")
    library.borrow_book("M002", "B001")

    # James returns his book
    print("\n--- James returns his book ---")
    library.return_book("M004", "B007")

    print("\n" + str(library))