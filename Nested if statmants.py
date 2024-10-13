is_yemeni = input("Are you Yemeni? Type 'yes' or 'no' ").lower()
if is_yemeni == 'yes' :
 print("Good, that the first step ")
 is_18=input("Are you above 18? Type 'yes' or 'no' ").lower()
 if is_18 == 'yes':
     print("You can have ID")
 else:
     print("Sorry, you have to be 18 or older")
else:
    print("sorry, an yemeni ID is given only to yemeni ")