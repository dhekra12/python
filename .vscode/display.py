import random

def get_random_word():
    words = ['office', 'books', 'library', 'university', 'python', 'hangman', 'computer', 'programming', 'algorithm']
    return random.choice(words)

def display_hangman(tries):
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
    return stages[tries]

def play_hangman():
    word = get_random_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()
        
        # التحقق من صحة المدخلات
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        
        # عرض رسمة الشنق بناءً على عدد المحاولات
        print(display_hangman(tries))
        print(word_completion)
        print("Guessed letters:", guessed_letters)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

    # خيار اللعب مرة أخرى
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_hangman()

if __name__ == "__main__":
    play_hangman()
