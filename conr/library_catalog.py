import os

# Dictionary to store books with ISBN as the key
library_catalog = {}
library_catalog = []

def clear_terminal():

    os.system('cls' if os.name == 'nt' else 'clear')

def add_book():
    while True:
        clear_terminal()
        ISBN = input("Enter ISBN: ")
        title = input("Enter book title: ")
        author = input("Enter author: ")
        # Add book details to the dictionary
        library_catalog[ISBN] = {"Title": title, "Author": author, "available": True}
        print(f"Book {title} by {author} added to the catalog with the ISBN {ISBN}.")
        
        choice = input('Do you want to add another book? (y/n) ')
        if choice.lower() != 'y':
            break

def check_out_book():
    while True:
        clear_terminal()
        ISBN = input("Enter ISBN of the book to check out: ")
        if ISBN in library_catalog:
            if library_catalog[ISBN]['available']:
                library_catalog[ISBN]["available"] = False
                print(f'Book "{library_catalog[ISBN]["Title"]}" checked out successfully!')
            else:
                print("Book is already checked out.")
        else:
            print("Book not found in the catalog.")
        
        choice = input('Do you want to check out another book? (y/n) ')
        if choice.lower() != 'y':
            break

def check_in_book():
    while True:
        clear_terminal()
        ISBN = input("Enter ISBN of the book to check in: ")
        if ISBN in library_catalog and not library_catalog[ISBN]["available"]:
            library_catalog[ISBN]["available"] = True
            print(f'Book "{library_catalog[ISBN]["Title"]}" checked in successfully!')
        else:
            print("Book not found or already available in the library.")
        
        choice = input('Do you want to check in another book? (y/n) ')
        if choice.lower() != 'y':
            break

def list_books():
    while True:
        clear_terminal()
        print("\nLibrary Catalog")
        if library_catalog:
            for ISBN, details in library_catalog.items():
                status = "Available" if details["available"] else "Checked out"
                print(f'ISBN: {ISBN}, Title: {details["Title"]}, Author: {details["Author"]}, Status: {status}')
        else:
            print("No books in the catalog.")
        
        choice = input('Do you want to go back to the main menu? (y/n) ')
        if choice.lower() == 'y':
            break

while True:
    print("""
          Menu:
          1- Add book
          2- Check out book
          3- Check in book
          4- List Books
          5- Exit""")
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        add_book()
    elif choice == '2':
        check_out_book()
    elif choice == '3':
        check_in_book()
    elif choice == '4':
        list_books()
    elif choice == '5':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

    input("Press Enter to continue...")
