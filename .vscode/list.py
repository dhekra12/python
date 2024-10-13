# favorites_frindes = ['nada' , 'afaf', 'waleh' , 'entithar' , 'zenab']
# favorites_frindes [-2] = 'entidhar'
# #print(f'the first friends in our list is ', favorites_frindes [0]  , ' and the last is ' , favorites_frindes[-1])
# print (favorites_frindes)
# colors = []
# fav_color = input("Add the color you like: ")
# colors.append(fav_color)
# choice = input("Do you want to add another color? (y/n) ").lower()
# if choice == "y":
#     fav_color = input("Add another color to the list: ")
#     colors.append(fav_color)
#     print(f"the colors you like are:")
#     print(colors)
# else:
#     print("the colors you like is:")
#     print(colors)
    
# class_a = ['dhekra' , 'mohammed' , 'yusra']
# class_b = ['taha' , 'ali' , 'ahmed']
# class_b.remove('ali')
# students= class_a + class_b
# print(students)
# print(type(students))

# class_a.extend(class_b)
# all_student = []
# all_student.extend(class_a)
# all_student.extend(class_b)
# print(all_student)

fruit_basket = ['apple' , 'orange' , 'limon' , 'bananas' , 'dates' ]
Guess= input("Guess the name of the fruits in the basket: ")
if Guess in fruit_basket:
    print("good guess")
else:
    print("sorry, better luck next time")