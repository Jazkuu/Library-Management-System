from library import Library
from book import Book
from member import Member


def test_add_book():
    lib = Library()
    book = Book(1, "Test Book", "Author", 1)
    lib.add_book(book)
    assert 1 in lib.books


def test_add_member():
    lib = Library()
    member = Member(1, "Nicholai")
    lib.add_member(member)
    assert 1 in lib.members


def test_issue_book():
    lib = Library()
    book = Book(1, "Test", "Author", 1)
    member = Member(1, "Test User")

    lib.add_book(book)
    lib.add_member(member)

    lib.issue_book(1, 1)

    assert book.copies == 0
    assert 1 in member.borrowed_books