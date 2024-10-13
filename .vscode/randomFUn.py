import random
print("welcome to the coin coin Gussing game\n ")
print("Choose a method o toss the coin...\n 1. Useing random.random() \n 2. Useing random.randint() ")
choices =input("Enter your choice ( 1 or 2 ) ")
if choices == '1':
    random_number = random.random()
    if random_number >= 0.5:
     compute_result= "Heads"
    else:
        compute_result='tails'
elif choices == '2':
    if random.randint(0, 1)==0:
     compute_result= "Heads"
    else:
        compute_result='tails'
else:
    print('Invalid choice. please select either 1 or 2')
    
user_choice = input('enter your guess (Heads or tails): ')
if user_choice.lower() == compute_result.lower():
        print('congratulation ! you won')
else:
    print('sorry, you lost')
        
print(f'the computer coin toss result was: {compute_result}')
       

    
        
 
 
# rand2 =input(" ")
# random_number = random.randint(0, 5)
# if random_number >= 0:
#     print("heads")
# else:
#     print("tails")
    
    
    
    
    
# print("welcome to the virsual coin toss game")
# input("please press enter... ")
# random_number = random.randint(0, 5)
# if random_number >= 0:
#     print("heads")
# else:
#     print("tails")






# random_mumber = random.random() * 5
# print(random_mumber)