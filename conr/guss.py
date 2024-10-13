import os
import random

def clear_screan():
    # Cross-platform way to clear the console
    # the bracket for os.system
    os.system('cls' if os.name == 'nt' else 'clear')

# Generate a random number between 0 and 10
# target_number = str(random.randint(1, 10))
target_number = random.randint(1, 10)

while True:
    clear_screan()
    Guess = int(input("Guess the number between 0 and 10: "))
    if Guess == target_number:
        print("Congratulations! You guessed the correct number.")
        
        break
    else:
        clear_screan()
        print("Wrong guess. Try again")
        # input("press any key to continue...")
# choice =input("would you like to eat? (y/n): ")
# print("Hungry") if choice == "y" else print("not hungry")
        
