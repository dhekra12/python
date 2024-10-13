import random
# correct_password = "a1b2c3"
# enterd_password= input("Enter password: ")
# while enterd_password !=  correct_password:
#     print("Incorrect passwoed. Try again:")
#     enterd_password= input("Enter password again: ")
# print("Access Granted!")

# correct_number= 8
print("")
secret_number= random.randint(0, 10)
guess_number= int(input("Guess the number between 1 to 10: "))
while guess_number != secret_number:
    if guess_number > secret_number:
     guess_number =int(input("Too high! Guess again: "))
    elif guess_number < secret_number:
     guess_number = int(input("Too low! Guess again: "))
print("Congratulations! You guess the number!")

        


