class Person:
    def display_info(self):
        raise NotImplementedError("Subclasses must implement display_info")


class Member(Person):
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book_id):
        self.borrowed_books.append(book_id)

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
        else:
            raise ValueError("This member did not borrow that book.")

    def display_info(self):
        return f"ID: {self.member_id} | Name: {self.name} | Borrowed books: {self.borrowed_books}"