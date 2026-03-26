from library import Library
from book import Book
from member import Member


def show_menu():
    print("\n=== Library Management System ===")
    print("1. Add book")
    print("2. Remove book")
    print("3. Update book")
    print("4. Display books")
    print("5. Add member")
    print("6. Remove member")
    print("7. Update member")
    print("8. Display members")
    print("9. Issue book")
    print("10. Return book")
    print("11. Search books")
    print("0. Exit")


def main():
    library = Library()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                book_id = int(input("Enter book ID: "))
                title = input("Enter title: ")
                author = input("Enter author: ")
                copies = int(input("Enter number of copies: "))
                library.add_book(Book(book_id, title, author, copies))
                print("Book added successfully.")

            elif choice == "2":
                book_id = int(input("Enter book ID to remove: "))
                library.remove_book(book_id)
                print("Book removed successfully.")

            elif choice == "3":
                book_id = int(input("Enter book ID to update: "))
                title = input("Enter new title (leave blank to keep old): ")
                author = input("Enter new author (leave blank to keep old): ")
                copies_input = input("Enter new number of copies (leave blank to keep old): ")
                copies = int(copies_input) if copies_input else None
                library.update_book(book_id, title or None, author or None, copies)
                print("Book updated successfully.")

            elif choice == "4":
                library.display_books()

            elif choice == "5":
                member_id = int(input("Enter member ID: "))
                name = input("Enter member name: ")
                library.add_member(Member(member_id, name))
                print("Member added successfully.")

            elif choice == "6":
                member_id = int(input("Enter member ID to remove: "))
                library.remove_member(member_id)
                print("Member removed successfully.")

            elif choice == "7":
                member_id = int(input("Enter member ID to update: "))
                name = input("Enter new name: ")
                library.update_member(member_id, name)
                print("Member updated successfully.")

            elif choice == "8":
                library.display_members()

            elif choice == "9":
                book_id = int(input("Enter book ID: "))
                member_id = int(input("Enter member ID: "))
                library.issue_book(book_id, member_id)
                print("Book issued successfully.")

            elif choice == "10":
                book_id = int(input("Enter book ID: "))
                member_id = int(input("Enter member ID: "))
                library.return_book(book_id, member_id)
                print("Book returned successfully.")

            elif choice == "11":
                keyword = input("Enter title or author to search for: ")
                results = []
                for book in library.books.values():
                    if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                        results.append(book)

                if results:
                    print("\nSearch results:")
                    for book in results:
                        print(book.display_info())
                else:
                    print("No books found.")

            elif choice == "0":
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()