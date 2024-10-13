# for i in range(0, 20, 2):
#     print(i)
# print("*** Welcome to the multiplication table")
# number = int(input("Enter a number: "))
# print(f"\nMultiplication table for {number}: \n")
# for i in range(1,11):
#     result = number * i
#     print(f"{number} X {i} = {result}")
    
items= []
prices= []
print("*** Welcome to ishop calculator ")
number_of_items = int(input("how many items are there in your basket today?: "))
if number_of_items > 0 :
 print ( "Let's get counting them ...")

 # item= range(1, len(basket))
 for i in range(1, number_of_items +1): # (0 , number_of_items)
  names=input(f"please tell me the name of the item number {i} ")# {i+1}
  items.append(names)
  
  price= float(input(f"what is the price of {names} \n$"))
  prices.append(price)

 choice = input("would you like to see entire basket items? ").lower()
 if choice == "yes":
    print(items)
    see_price = input("would you like to see how much it'll cost? ")
    if see_price == "yes":
     print(f"Buying these items will cost: ")
     print(sum(prices)) 
    else:
     print("press enter to exit")
 else:
    
  print("press enter to exite")
else:
    print("seems like you're not un mood for shopping today")
    