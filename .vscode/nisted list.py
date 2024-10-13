# basket = [['banana' , 'apple'], ['water' , 'milk']]
# # desert = [ 'cake', 'candy']
# basket.append(['Candy' , 'cake'])
# print(basket)
# books = ['book1' ,'bool3' , 'book4']
# books.insert(1, 'book2')
# books.insert(4, 'book5')
# books.append( 'book6')
# print(books)
basket = [['apple', 'banana'], ['milk', 'water']]
print(basket)
input("press enter to change the content")

basket[0].insert(0, 'orange')
basket[0].insert(3, 'kiwi')
basket[1].insert(0, 'coffee')
basket[1].remove('water')
basket[1].insert(2, 'tea')
basket.append([1 , 2, 3])
print("here is the update basket \n ", basket)




