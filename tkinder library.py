import mysql.connector
import tkinter as tk
from tkinter import messagebox

# MySQL connection
class Library:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='nantha'
        )
        self.cursor = self.conn.cursor()

    def add_user(self, name):
        query = "INSERT INTO users (name) VALUES (%s)"
        self.cursor.execute(query, (name,))
        self.conn.commit()
        messagebox.showinfo("Success", f"User '{name}' added successfully!")

    def add_book(self, title):
        query = "INSERT INTO books (title, is_lent) VALUES (%s, 0)"
        self.cursor.execute(query, (title,))
        self.conn.commit()
        messagebox.showinfo("Success", f"Book '{title}' added successfully!")

    def display_available_books(self):
        query = "SELECT * FROM books WHERE is_lent = 0"
        self.cursor.execute(query)
        books = self.cursor.fetchall()
        if books:
            return books
        else:
            messagebox.showinfo("Info", "No books are currently available.")

    def display_all_books(self):
        query = "SELECT * FROM books"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def lend_book(self, book_id, user_id):
        query = "SELECT * FROM books WHERE book_id = %s AND is_lent = 0"
        self.cursor.execute(query, (book_id,))
        book = self.cursor.fetchone()

        if book:
            update_query = "UPDATE books SET is_lent = 1, lent_to = %s WHERE book_id = %s"
            self.cursor.execute(update_query, (user_id, book_id))
            self.conn.commit()
            messagebox.showinfo("Success", f"Book ID: {book_id} lent to User ID: {user_id}")
        else:
            messagebox.showwarning("Warning", "Book is either already lent or does not exist.")

    def return_book(self, book_id):
        query = "SELECT * FROM books WHERE book_id = %s AND is_lent = 1"
        self.cursor.execute(query, (book_id,))
        book = self.cursor.fetchone()

        if book:
            update_query = "UPDATE books SET is_lent = 0, lent_to = NULL WHERE book_id = %s"
            self.cursor.execute(update_query, (book_id,))
            self.conn.commit()
            messagebox.showinfo("Success", f"Book ID: {book_id} has been returned.")
        else:
            messagebox.showwarning("Warning", "Book is either already available or does not exist.")

    def close_connection(self):
        self.conn.close()


class LibraryApp:
    def __init__(self, master):
        self.library = Library()
        self.master = master
        master.title("Library Management System")

        # Add User
        self.add_user_frame = tk.Frame(master)
        self.add_user_frame.pack(pady=10)
        tk.Label(self.add_user_frame, text="Add User:").pack(side=tk.LEFT)
        self.add_user_entry = tk.Entry(self.add_user_frame)
        self.add_user_entry.pack(side=tk.LEFT)
        self.add_user_button = tk.Button(self.add_user_frame, text="Add", command=self.add_user)
        self.add_user_button.pack(side=tk.LEFT, padx=5)

        # Add Book
        self.add_book_frame = tk.Frame(master)
        self.add_book_frame.pack(pady=10)
        tk.Label(self.add_book_frame, text="Add Book:").pack(side=tk.LEFT)
        self.add_book_entry = tk.Entry(self.add_book_frame)
        self.add_book_entry.pack(side=tk.LEFT)
        self.add_book_button = tk.Button(self.add_book_frame, text="Add", command=self.add_book)
        self.add_book_button.pack(side=tk.LEFT, padx=5)

        # Display Available Books
        self.display_available_button = tk.Button(master, text="Display Available Books", command=self.display_available_books)
        self.display_available_button.pack(pady=5)

        # Display All Books
        self.display_all_button = tk.Button(master, text="Display All Books", command=self.display_all_books)
        self.display_all_button.pack(pady=5)

        # Lend Book
        self.lend_book_frame = tk.Frame(master)
        self.lend_book_frame.pack(pady=10)
        tk.Label(self.lend_book_frame, text="Lend Book ID:").pack(side=tk.LEFT)
        self.lend_book_entry = tk.Entry(self.lend_book_frame)
        self.lend_book_entry.pack(side=tk.LEFT)
        tk.Label(self.lend_book_frame, text="User ID:").pack(side=tk.LEFT)
        self.lend_user_entry = tk.Entry(self.lend_book_frame)
        self.lend_user_entry.pack(side=tk.LEFT)
        self.lend_book_button = tk.Button(self.lend_book_frame, text="Lend", command=self.lend_book)
        self.lend_book_button.pack(side=tk.LEFT, padx=5)

        # Return Book
        self.return_book_frame = tk.Frame(master)
        self.return_book_frame.pack(pady=10)
        tk.Label(self.return_book_frame, text="Return Book ID:").pack(side=tk.LEFT)
        self.return_book_entry = tk.Entry(self.return_book_frame)
        self.return_book_entry.pack(side=tk.LEFT)
        self.return_book_button = tk.Button(self.return_book_frame, text="Return", command=self.return_book)
        self.return_book_button.pack(side=tk.LEFT, padx=5)

    def add_user(self):
        name = self.add_user_entry.get()
        self.library.add_user(name)

    def add_book(self):
        title = self.add_book_entry.get()
        self.library.add_book(title)

    def display_available_books(self):
        books = self.library.display_available_books()
        if books:
            result = "\n".join([f"Book ID: {book[0]}, Title: {book[1]}" for book in books])
            messagebox.showinfo("Available Books", result)

    def display_all_books(self):
        books = self.library.display_all_books()
        result = "\n".join([f"Book ID: {book[0]}, Title: {book[1]}, Status: {'Available' if book[2] == 0 else f'Lent to User ID: {book[3]}'}" for book in books])
        messagebox.showinfo("All Books", result)

    def lend_book(self):
        book_id = self.lend_book_entry.get()
        user_id = self.lend_user_entry.get()
        self.library.lend_book(book_id, user_id)

    def return_book(self):
        book_id = self.return_book_entry.get()
        self.library.return_book(book_id)


# Run the Tkinter app
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
    app.library.close_connection()
