from random import randint  # randint - Used to generate a random number for the player to guess
from IPython.display import clear_output  # clear_out -  Used to clear the output in the console


def play_game():
    while True:  # Loop to play multiple games
        number = randint(0, 100)
        guess_limit = 10  # Setting a limit of 10 guesses
        guesses = 0
        previous_guesses = []
        guessed = False

        while not guessed and guesses < guess_limit:  # Added condition to limit guesses
            remaining_guesses = guess_limit - guesses
            ans = input(
                f"Try to guess the number I am thinking of, you have {remaining_guesses} guesses remaining! ")
            guesses += 1
            clear_output()

            try:
                guess = int(ans)
                if guess < 0 or guess > 100:
                    print("Please input a number between 0 and 100.")
                    guesses -= 1  # Decrement guesses count to compensate for invalid guess
                    continue  # Prompt for guess again without advancing to next step

                if int(ans) in previous_guesses:
                    print("You have already guessed that number.")
                    guesses -= 1  # Decrement guesses count to compensate for repeated guess
                    continue  # Prompt for guess again without advancing to next step

                previous_guesses.append(int(ans))  # Adding the guess to previous guesses

                if int(ans) == number:
                    print(f"Congrats! You guessed it correctly, It took you {guesses} guesses!")
                    guessed = True  # Set the flag to end the game
                elif int(ans) > number:
                    print("The number is lower than what you guessed.")
                elif int(ans) < number:
                    print("The number is greater than what you guessed.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if not guessed:
            print("Sorry, you ran out of guesses. The number was:", number)

        while True:
            play_again = input("Would you like to play again? (yes/no): ").lower()
            if play_again == "no":
                print("Goodbye, Thanks for playing!")
                return
            elif play_again == "yes":
                print("Great! lets play again!")
                break  # Exit the loop if the player chooses not to play again
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


# Start the game
play_game()
