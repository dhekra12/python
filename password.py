import random
import string

print("welcome to the password Generator!")
length_passawords= int(input("Enter the total number of character in the password: ")) 
num_letter= int(input("Enter the  letters of character in the password: "))
num_number= int(input("Enter the numbers number of character in the password: "))
num_symbol= int(input("Enter the total symbols of character in the password: "))

if length_passawords != (num_letter + num_number +num_symbol):
    print("Invalid input. the sum of letters, numbers, and symbols doesn't match the password length. ")
else:
    letter= string.ascii_letters
    number = string.digits
    symbol= string.punctuation
    password_char = ( 
        random.choices(letter, k = num_letter)+
        random.choices(number, k = num_number)+
        random.choices(symbol, k = num_symbol)   
    )
    random.shuffle(password_char)
    password= "".join(password_char)
    print("Generated password: " , password)