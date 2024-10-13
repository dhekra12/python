import random

pin_code= random.randint(1000,9999)
user_input= int(input('Enter a 4-digit PIN code: '))
if len(str( user_input)) != 4:
    print('please enter 4 digit ')
elif user_input == pin_code:
    print("Success")
else:
    print("Failure! PIN code did not match")
    print(f"The computer generated this PIN: {pin_code}")
    




# # my_random_number = random.randint(-5 , +5)
# # print(my_random_number)
# import octocode
# print(octocode.teacher)