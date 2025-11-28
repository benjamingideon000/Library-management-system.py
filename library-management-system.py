class Book:
    def __init__(self, id, title, author, year, status="Available", borrower=""):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.borrower = borrower

    def __str__(self):
        return f"{self.id:<5} | {self.title:<20} | {self.author:<15} | {self.year:<5} | {self.status:<10} | {self.borrower}"

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    id, title, author, year, status, borrower = line.strip().split(",")
                    self.books.append(Book(id, title, author, year, status, borrower))
        except FileNotFoundError:
            print("No existing books file. Starting fresh.")

    def save_books(self):
        with open("books.txt", "w") as file:
            for book in self.books:
                file.write(f"{book.id},{book.title},{book.author},{book.year},{book.status},{book.borrower}\n")

    def add_book(self):
        print("\nAdd Book:")
        id = input("Enter Book ID: ")
        if any(book.id == id for book in self.books):
            print("Book ID already exists. Try again.")
            return
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        year = input("Enter Year: ")
        self.books.append(Book(id, title, author, year))
        self.save_books()
        print("Book added successfully.")

    def view_books(self):
        if not self.books:
            print("\nNo books available.")
            return
        print("\nAll Books:")
        print("ID    | Title                | Author          | Year  | Status     | Borrower")
        print("-" * 80)
        for book in self.books:
            print(book)

    def search_book(self):
        print("\nSearch Book:")
        query = input("Enter Book ID or Title: ").lower()
        found = False
        print("ID    | Title                | Author          | Year  | Status     | Borrower")
        print("-" * 80)
        for book in self.books:
            if query in book.id.lower() or query in book.title.lower():
                print(book)
                found = True
        if not found:
            print("Book not found.")

    def borrow_book(self):
        print("\nBorrow Book:")
        id = input("Enter Book ID: ")
        for book in self.books:
            if book.id == id and book.status == "Available":
                book.status = "Borrowed"
                book.borrower = input("Enter your name: ")
                self.save_books()
                print(f"Book '{book.title}' borrowed successfully.")
                return
            elif book.id == id and book.status == "Borrowed":
                print(f"Book '{book.title}' is already borrowed by {book.borrower}.")
                return
        print("Book not found.")

    def return_book(self):
        print("\nReturn Book:")
        id = input("Enter Book ID: ")
        for book in self.books:
            if book.id == id and book.status == "Borrowed":
                book.status = "Available"
                book.borrower = ""
                self.save_books()
                print(f"Book '{book.title}' returned successfully.")
                return
            elif book.id == id and book.status == "Available":
                print(f"Book '{book.title}' is already available.")
                return
        print("Book not found.")

    def delete_book(self):
        print("\nDelete Book:")
        id = input("Enter Book ID: ")
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                self.save_books()
                print(f"Book '{book.title}' deleted successfully.")
                return
        print("Book not found.")

def main():
    library = Library()
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")
        try:
            choice = input("Choose an option: ")
            if choice == "1":
                library.add_book()
            elif choice == "2":
                library.view_books()
            elif choice == "3":
                library.search_book()
            elif choice == "4":
                library.borrow_book()
            elif choice == "5":
                library.return_book()
            elif choice == "6":
                library.delete_book()
            elif choice == "7":
                break
            else:
                print("Invalid option.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()