class Library:

    def __init__(self, book_list):
        # Initialize with the list of all books and available books
        self.booklist = book_list
        self.available_books = book_list.copy()
        self.lent_books = {}

    def display_all_books(self):
        # Display all books in the library
        print("Books in the library:")
        for book in self.booklist:
            print(book)

    def display_available_books(self):
        # Display the available books for borrowing
        print("Available books for borrowing:")
        for book in self.available_books:
            print(book)

    def lend_book(self, book, borrower_name):
        # Lend a book to a user
        if book not in self.booklist:
            print("Incorrect book name. Please check the book list.")
        elif book not in self.available_books:
            print(f"The book is already lent to {self.lent_books[book]}.")
        else:
            # Lend the book and update the available and lent books
            self.lent_books[book] = borrower_name
            self.available_books.remove(book)
            print(f"{borrower_name}, you can take the book '{book}'.")

    def return_book(self, book):
        # Return a book to the library
        if book in self.lent_books:
            # Remove from lent books and add back to available books
            del self.lent_books[book]
            self.available_books.append(book)
            print(f"The book '{book}' has been returned.")
        else:
            print("The book wasn't borrowed or incorrect book name.")


if __name__ == '__main__':
    # Initialize the library with some books
    lib = Library(['The Life Divine', 'Da Vinci Code', 'The Alchemist', 'Mahabharath', 'Ramayanam'])

    print("************* Welcome to the Library **************")

    while True:
        # Display the menu options
        print('1. Display available books\n2. Display all books\n3. Borrow a book\n4. Return a book\n5. Quit')
        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            lib.display_available_books()
        elif user_choice == 2:
            lib.display_all_books()
        elif user_choice == 3:
            borrower_name = input("Enter your name: ")
            book_name = input("Enter the book name you want to borrow: ")
            lib.lend_book(book_name, borrower_name)
        elif user_choice == 4:
            book_name = input("Enter the name of the book you want to return: ")
            lib.return_book(book_name)
        elif user_choice == 5:
            print("Thank you for visiting the library!")
            break
        else:
            print("Please enter a valid option.")
