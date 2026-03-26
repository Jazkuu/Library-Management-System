from book import Book
from member import Member


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # ---------- BOOK MANAGEMENT ----------
    def add_book(self, book):
        if book.book_id in self.books:
            raise ValueError("Book ID already exists.")
        self.books[book.book_id] = book

    def remove_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found.")
        del self.books[book_id]

    def update_book(self, book_id, title=None, author=None, copies=None):
        if book_id not in self.books:
            raise ValueError("Book not found.")

        book = self.books[book_id]

        if title:
            book.title = title
        if author:
            book.author = author
        if copies is not None:
            book.copies = copies

    def display_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books.values():
            print(book.display_info())

    # ---------- MEMBER MANAGEMENT ----------
    def add_member(self, member):
        if member.member_id in self.members:
            raise ValueError("Member ID already exists.")
        self.members[member.member_id] = member

    def remove_member(self, member_id):
        if member_id not in self.members:
            raise ValueError("Member not found.")
        del self.members[member_id]

    def update_member(self, member_id, name=None):
        if member_id not in self.members:
            raise ValueError("Member not found.")
        if name:
            self.members[member_id].name = name

    def display_members(self):
        if not self.members:
            print("No members available.")
        for member in self.members.values():
            print(member.display_info())

    # ---------- ISSUE / RETURN ----------
    def issue_book(self, book_id, member_id):
        if book_id not in self.books:
            raise ValueError("Book not found.")
        if member_id not in self.members:
            raise ValueError("Member not found.")

        book = self.books[book_id]
        member = self.members[member_id]

        if book.copies <= 0:
            raise ValueError("No copies available.")

        book.copies -= 1
        member.borrow_book(book_id)

    def return_book(self, book_id, member_id):
        if book_id not in self.books:
            raise ValueError("Book not found.")
        if member_id not in self.members:
            raise ValueError("Member not found.")

        member = self.members[member_id]
        book = self.books[book_id]

        if book_id not in member.borrowed_books:
            raise ValueError("This member did not borrow that book.")

        member.return_book(book_id)
        book.copies += 1