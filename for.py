# name = 'dhekra'
# for i in name:
#     print(f"the letter is {i.upper()}")

# colors = ['red', 'green', 'pink','blue','yellow']
# for  y in colors:
#     if y == 'pink':
#         print(f'my favorite colors is {y}')
#     else:
#         print(y)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]

# for a in numbers:
#     if a % 2==0:
#         print(f"\n {a}")
# print("finished the loop successfully")
# attendees =['dhekra' , 'taha', 'mohammed']
attendees_input = input("Enter the names of attendees separated by commas: ").split(", ")
# attendees =attendees_input.split(', ')
for person in attendees_input:
 print("\n" + person + "\n")
 response= input("Is this {person} attending? (yes? no): ").lower()
 if response == 'no':
        print("attendance not confirmed!\n")
 elif response == 'yes':
        print("attendees confirmed!\n")
 print("------------")
print("press enrer to exit....")
        
   
    

