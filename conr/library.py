import os

# Dictionary to store books with ISBN as the key
library_catalog = {}

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
        # print("Book added successfully!")
        print(
            f" Book {title} by {author} added to the catalog with the ISBN {ISBN}."
        )
        
        choice=  input('Do you want to add another book? (y/n) ')
        if choice.lower() != 'y':
            break
def check_out_book():
    while True:
        clear_terminal()
        ISBN = input("Enter ISBN of the book to check out: ")
        # if ISBN in books and not books[ISBN]["CheckedOut"]:
        if ISBN in library_catalog :
            if library_catalog[ISBN] ['available'] :
             library_catalog[ISBN]["available"] = False
             print(f'Book "{library_catalog[ISBN]["Title"]}" checked out successfully!')
            else:
                print("Book not found or already checked out.")
        else:
            print("Book not found in th catalog")
        choice=  input('Do you want to add another book? (y/n)')
        if choice.lower() != 'y':
            break
def check_in_book():
    while True:
        clear_terminal()
        ISBN = input("Enter ISBN of the book to check in: ")
        if ISBN in library_catalog and library_catalog[ISBN]["available"]:
            library_catalog[ISBN]["available"] = False
            print(f'Book "{library_catalog[ISBN]["Title"]}" checked in successfully!')
        else:
            print("Book not found or already available in the library.")
        choice=  input('Do you want to adcheck in another book? (y/n)')
        if choice.lower() != 'y':
            break
def list_books():
    while True:
        clear_terminal()
        print("\nlibrary Cataloge")
        # if library_catalog:
        #     for ISBN, details in library_catalog.items():
        #         status = "Checked out" if details["available"] else "Not Available"
        #         print(f'ISBN: {ISBN}, Title: {details["Title"]}, Author: {details["Author"]}, Status: {status}')
        # else:
        #     print("No books in the catalog.")
        for isbn in library_catalog:
         book_info= library_catalog[ isbn]
         print(
            f"ISBN: {isbn}, Title: {book_info['title']}, Author: {book_info['author']}, Available {book_info['available']}"
         )
        choice=  input('Do you want to go back to the main menu? (y/n)')
        if choice.lower() != 'y':
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

    # input("Press Enter to continue...")
    

