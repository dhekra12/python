import random
rock_ascii = """"
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""""
paper_ascii = """"
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""""
Scissors_ascii = """"
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""""


print("\nwelcome to the Rock, Paper, Scissors game")
confirm = input("press enter to continue or type (help) for the rules help ").lower()
if confirm == "help":
    print(""""
          ********* RULES **********"
    1) you choose and the computer chooses
    2) Rock smashes scissors -> Rock win
    3) Scissors cut paper -> scissors win 
    4) paper covers Rock -> paper wins 
    """)

User_choice = input("Enter your choice (rock, paper, scissors):").lower()

if User_choice not in ['rock ', 'paper', 'scissors']:
    print("invalid choice. please run the program again and choose rock, paper, and scissors.")
else:
    if User_choice == "rock":
        print(f"\nyou chose:\n{rock_ascii}")
    elif User_choice == "paper":
        print(f"\nyou chose:\n{paper_ascii}")
    else:
        print(f"\nyou chose:\n{Scissors_ascii}")
        
        # compter choice
computer_choice = random.choice(['rock ', 'paper', 'scissors'])
if computer_choice == "rock ":
    print(f"\ncomputer chose:\n{rock_ascii}")
elif computer_choice == "paper ":
    print(f"\ncomputer chose:\n{paper_ascii}")
else:
    print(f"\ncomputer chose:\n{Scissors_ascii}")


if User_choice == computer_choice:
    print("It's a tie!")
elif (
        (User_choice == 'rock' and computer_choice == 'Scissors'  )
        or        
        (User_choice == 'paper' and computer_choice == 'rock')
        or
        (User_choice == 'scissors' and computer_choice == 'paper')
  ):
    print(f"You Win! {User_choice} beats {computer_choice}.")
else:
    print(f"You lose! {computer_choice} beats {User_choice}.")

        

   
