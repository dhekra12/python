import random
stages = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
words= [' office', 'books', 'library', 'university']
random_words = random.choice(words)

# for letter in random_words:
#     display.append("_")
# print(display)

def play_hangman():
 print("Let's play Hangman!")
 display =['_'] * len(random_words)
 print(" ".join(display))
 lives = 6 
 guessed_letters = []
 print(stages[0]) 
 while "_" in display and lives > 0:
    guessed= input("please guess the letter: ").lower()
    if guessed in guessed_letters:
        print("You already guessed the letter", guessed)
        continue
    guessed_letters.append(guessed)
    if guessed not in random_words :
        lives-=1
        print(stages[6-lives])
    else:
        for position in range(len (random_words)):
         if random_words[position] == guessed:
          display[position]= guessed
    print(' '.join(display))
    print(f"You have {lives} more trips")
# print(random_words)


 if lives == 0:
    print("""
      ********
      YOU LOSE!
      ********
      """)
    print(stages[-1])
 else:
  print("""
      ********
      YOU WINE!
      ********
      """)
 play_again = input("Do you want to play again? (yes/no): ").lower()
 if play_again == 'yes':
        play_hangman()
if __name__ == "__main__":
    play_hangman()
        

# for letter in random_words:
#     if letter == guessed:
#         print("Right")
#     else:
#         print("Wrong")