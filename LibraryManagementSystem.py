class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.year)
        if self.available:
            print("Status: Available")
        else:
            print("Status: Borrowed")

    def is_available(self):
        return self.available
    
    def borrow_book(self):
        if self.available:
            self.available = False
            print("You have borrowed the book.")
        else:
            print("The book is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print('You have returned the book.')
        else:
            print("The book was already borrowed.")

title = input("Enter book title: ")
author = input("Enter author name: ")
year_input = input("Enter publication year: ")

year = int(year_input)

book = Book(title, author, year)

while True:
    print("\nLibrary Management System")
    print("[1] Borrow Book")
    print("[2] Return Book")
    print("[3] Display Book")
    print("[4] Exit Program")

    choice = input("Enter your choice: ")

    if choice == "1":
        book.borrow_book()
    elif choice == "2":
        book.return_book()
    elif choice == "3":
        book.display_info()
    elif choice == "4":
        print("Exiting Program...")
        break
    else:
        print("Invalid Command.")


