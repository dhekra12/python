laibrary = []
own_books = input("Enter the name of a book you won: ")
laibrary.append(own_books)
choice = input("Entet the name of another book you own (or press 'Enter' to skip): ").lower()
laibrary.append(choice)
print('Your library:' , laibrary)

wishList=[]
book_for_future = input("Enter a book you wish to have in the future: \n ")
wishList.append(book_for_future)
another_book = input("Entet the name of another book you wish to have (or press 'Enter' to skip): \n ").lower()
wishList.append(another_book)
print('Your wishList:' , wishList)
add_book=input('Enter a name of a book from wishList that you have acquired (or press Enter to skip): ')
laibrary.append(add_book)
print("Upadte library" , laibrary)
wishList.remove(add_book)
print("Update your wishlist" , wishList)
donate_book=input('Enter a name of a book from your library you wish to donate (or press Enter to skip): ')
laibrary.remove(donate_book)
print("Final library after Donation: " , laibrary)



