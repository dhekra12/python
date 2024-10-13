# my_books={
#     "English":['The givery', 'Inferno','Fucus'],
#     "Arabic":{
#         "History":['Tabari', 'kathir', 'Gabarti'],
#         "Novel":{
#             'Hanan Lashin': ['Ekadoly', 'Amanos'],
#             'Amr A.Hamid': ['zeekola', 'Jartin'],
#             'Hassan Gindy':['Ebtasim', 'Mamsoos'],
#             'Ahmed Morad':['Ard', 'Azkar'],
#         },
#         "philosophy": "Tahafot",
#     }
# }
# print(my_books)

books={}
book_coount=0
while book_coount < 3:
    book_id =input("Enter a book ID: ")
    new_book  = input("Enter a book name: ")
    books[book_id]={'Title':new_book}
    book_coount+=1
print(books)