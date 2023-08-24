# Table of Contents
# 1. Section 1: Python Basics
#   1.1. Expressions (values + operators) and their precedence: Used to compute 'secretNumber' in a more complex way (Search: "1.1").
#   1.2. The Integer, Floating-Point, and String Data Types: Used to format 'secretNumber' and 'guess' as integers (Search: "1.2").
#   1.3. String Concatenation and Replication: Used to repeat the congratulatory message with the player's name (Search: "1.3").
#   1.4. Storing Values in Variables: Used to store secret numbers, guessed numbers, and time information (Search: "1.4").
#   1.5. Program: Refers to the overall structure of the program, particularly in the 'if __name__ == "__main__":' block (Search: "1.5").
# 2. Section 2: Flow Control
#   2.1. Boolean Values: Checking if guess is too low or high (Search: "2.1").
#   2.2. Comparison Operators: Used to compare the guessed number with the secret number (Search: "2.2").
#   2.3. Binary Boolean Operators: Used with comparison operators (Search: "2.3").
#   2.4. Elements of Flow Control: Demonstrated through the 'for' and 'while' loops (Search: "2.4").
#   2.5. Importing Modules: Importing 'random' and 'time' modules (Search: "2.5").
# 3. Section 3: Functions
#   3.1. Def, return and None: The function 'play_guess_the_number()' encapsulates the game logic (Search: "3.1").
#   3.2. Keyword Arguments and print(): Using f-string for formatted output (Search: "3.2").
#   3.3. Local and Global Scope: Demonstrated by the 'start_time' and 'end_time' variables within the function (Search: "3.3").
# 4. Section 4: Handling Errors with try/except
#   4.1. Used to catch a 'ValueError' if the user does not enter a valid integer as a guess (Search: "4.1").
# 5. Section 5: Writing a Complete Program. Guess the Number
#   5.1. Explains the complete structure of the game, referenced in the 'if __name__ == "__main__":' block (Search: "5.1").
# 6. Section 6: Lists
#   6.1. The Augmented Assignment Operators: Incrementing 'game_count' with the '+=' operator (Search: "6.1").
#   6.2. Methods: The '.append()' method adds guesses to the 'guesses' list (Search: "6.2").
#   6.3. List-like Types: Strings and Tuples: Utilizing 'guesses' as a list to store previously guessed numbers (Search: "6.3").


import random  # Section 2.5: Importing Modules
import time  # Section 2.5: Importing Modules


# Section 3: Functions
# Section 3.1: Def, return and None
def play_guess_the_number():
    # 1. Section 1: Python Basics
    # Section 1.4: Storing Values in Variables
    secretNumber = random.randint(1, 20)
    # Section 1.1: Expressions (values + operators) and their precedence
    secretNumber = (secretNumber - 1) * ((7 + 1) / (3 - 1))
    # Section 1.2: The Integer, Floating-Point, and String Data Types
    secretNumber = int((secretNumber % 20) + 1)  # Adjusting to fit into 1-20 range using modulo operator (%)

    # Section 6: Lists
    # Section 6.3: List-like Types: Strings and Tuples
    guesses = []

    # Section 1.5: Program
    print('I am thinking of a number between 1 and 20.')

    # Section 1.4: Storing Values in Variables
    start_time = time.time()  # Storing the current time in start_time

    # 2. Section 2: Flow Control ()
    # Section 2.4: Elements of Flow Control
    for guessesTaken in range(1, 7):
        while True:
        # 4. Section 4: Handling Errors with try/except
        #   4.1. Used to catch a 'ValueError' if the user does not enter a valid integer as a guess
            try:
                # Section 1.5: Program
                # Section 1.2: The Integer, Floating-Point, and String Data Types
                guess = int(input('Take a guess: '))
                if guess in guesses:
                    print("You've already guessed that number. Try again.")
                    continue
                else:
                    # Section 6.2: Methods
                    guesses.append(guess)
                    break
            except ValueError:
                # Section 4: Handling Errors with try/except
                print('Please enter a number.')

        # Section 2.2: Comparison Operators
        #   2.1. Boolean Values: Checking if guess is too low or high
        #   2.3. Binary Boolean Operators: Used with comparison operators
        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            # Section 3.2: Keyword Arguments and print()
            # Section 3.3: Local and Global Scope
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f'Good job! You guessed my number in {guessesTaken} guesses!')
            print(f'It took you {elapsed_time:.2f} seconds.')

            # Section 1.3: String Concatenation and Replication
            name = input("What's your name? ")
            print((name.upper() + " WELL DONE! ") * 5)
            return  # Exiting the function if the number is guessed correctly

    print(f'Sorry. The number I was thinking of was {secretNumber}.')
    print(f'Your guesses were: {", ".join(map(str, guesses))}')


# Section 1.5: Program
# 5. Section 5: Writing a Complete Program. Guess the Number
# 5.1. Explains the complete structure of the game, referenced in the 'if __name__ == "__main__":' block
if __name__ == "__main__":
    game_count = 0  # Initialize game_count to 0
    play_again = True

    # Section 2.4: Elements of Flow Control
    while play_again:
        play_guess_the_number()

        # Section 6.1: The Augmented Assignment Operators
        game_count += 1
        print(f'You have played {game_count} games.')

        while True:
            choice = input('Do you want to play again? (yes/no): ').lower()
            if choice not in ['yes', 'no']:
                print('Please answer with "yes" or "no".')
            else:
                # Section 6.1: The Augmented Assignment Operators
                play_again = choice == 'yes'
                break

