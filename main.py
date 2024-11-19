from random import randint  # randint - Used to generate a random number for the player to guess
import tkinter as tk
from tkinter import messagebox

''' Creates GUI window '''
window = tk.Tk()
window.geometry('700x600')  # width and height of the window
window.title('Guess The Number!')  # The name or header of the window
window.config(padx=10, pady=10, bg='purple')  # Change the background color of the entire window

# The Title of the window right below the name of the window using Times New Roman font with 20 as the font size
guess_label = tk.Label(window, text='Try to guess the number I am thinking of!', font=("TimesNewRoman", 20),
                       bg='purple', fg='white')
guess_label.pack(padx=10, pady=10)

# Create an entry box for the user to enter their guess this is where they input there guesses
guess_entry = tk.Entry(window, font=('TimesNewRoman', 20))
guess_entry.pack(padx=10, pady=10)

# Create a text box to show the user the result of their, this is where it will be displayed
guess_text = tk.Text(window, font=("TimesNewRoman", 10, "bold"), fg='black')  # font size 10 and changed the font size
# to bold and changed the text color
guess_text.pack(padx=10, pady=10)
''' Where everything is displayed '''



''''
Global variables are used to keep track of the game state!
Variables defined outside a function have a global scope and they can be accessed from any part of your code.
'''
number = randint(0, 100)
guess_limit = int(10)  # Setting a limit of 10 guesses
guesses = int(0)  # A counter variable to keep track of how many guesses the player has made, starting from 0
previous_guesses = []  # Creates an empty list  to store all the guesses that the player has made so far.
'''
Variables defined inside a function are local to that function and cannot be accessed outside of it.
'''

''''
all this does is define a function called `reset_game()`
'''
def reset_game():
    global number, guess_limit, guesses, previous_guesses
    number = randint(0, 100)
    guess_limit = 10
    guesses = 0
    previous_guesses = []
    guess_text.delete("1.0", tk.END)  # Deletes any text from a GUI element called `guess_text`, which is
    # likely used to display the player's guesses.
    guess_entry.delete(0, tk.END)  # Deletes any text from another GUI element called `guess_entry`,
    # which is probably an input field where players enter their guesses.
'''
that resets the game state to its initial values.
'''



'''
This is the logic of the game itself
'''
def play_game():
    """
    this function starts the game
    It retrieves the user's guess, validates it, and checks if it has been previously entered.
    If the input is valid, it processes with the next step; otherwise, it displays an error message.
    """
    # Access the global variable "guesses"
    global guesses
    try:
        # Attempt to convert user's input into an integer
        guess = int(guess_entry.get())

        # Validate if the guess is within the allowed range(0 - 100)
        if guess < int(0) or guess > int(100):
            # If valid, display a message box and exit the function
            messagebox.showinfo("Invalid input", "Please enter a number between 0 and 100.")
            return
        # Check if the user has already guessed this number
        if guess in previous_guesses:
            # If yes, display a message box and exit the function
            messagebox.showinfo("Invalid input", "You have already guessed that number.")
            return



        # Add the current guess to the list of previous guesses
        previous_guesses.append(guess)
        # Increment the total number of guesses made by 1
        guesses += int(1)
        # Calculating the remaining number of allowed guesses (guess_limit is a global variable)
        remaining_guesses = guess_limit - guesses



        # Check if the user's guess matches the target number (stored in 'number')
        if guess == number:
            # Display a congratulatory message box with a total number of guesses taken
            messagebox.showinfo("Congratulations!",
                                f"You guessed the number correctly it took you {guesses} guesses.")

            # Ask the user if they would like to play again; if yes, reset the state of the game
            if messagebox.askyesno("Play again?", "Would you like to play again?"):
                # Call the function to reset the game state
                reset_game()
            else:
                # If not, close the application window
                window.quit()



        # Check if the user's guess is too low (less than the target number)
        elif guess < number:
            # Display a message in the history of the text box that the next guess should be higher
            guess_text.insert(tk.END, f"{guess} The number is greater than what you guessed. {remaining_guesses} "
                                      f"guesses remaining.\n")
        # Check if the user's guess is too high (greater than the target number)
        else:
            # Display a message in the history of the text box that the next guess should be lower
            guess_text.insert(tk.END, f"{guess} The number is less than what you guessed. {remaining_guesses} "
                                      f"guesses remaining.\n")
        # Check if the user's has used up all there guesses ( if guesses are greater
        # or equal to global variable 'guess_limit
        if guesses >= guess_limit:
            # Display a game over message box revealing the target number
            messagebox.showinfo("Game Over", f"Sorry, you ran out of guesses. The number was {number}.")
            # Ask the user if they would like to play again: if yes, reset the state of the game
            if messagebox.askyesno("Play again?", "Would you like to play again?"):
                # Call the function to reset the game state
                reset_game()
            else:
                # If not, close the application window
                window.quit()

        guess_entry.delete(0, tk.END)  # Clear the contents of the guess entry field for the next guess

    except ValueError:  # All this does is display a window seeing if the input is an integer
        messagebox.showinfo("Invalid input", "Please enter a valid number.")



# created a button that will start the game
submit_button = tk.Button(window,
                          # Set the button text and initial state
                          text='Submit Guess',
                          bg='black',  # Button background color (black)
                          fg='white',  # Button foreground color (white)
                          command=play_game)  # Associate the 'play_game' function with this button's click event

# This is the font style and font size of the button
submit_button.config(font=("TimesNewRoman", 12, "bold"))
#  Add some padding around the button to create space and improve readability
submit_button.pack(padx=10, pady=10)

#  starts the main application loop (runs indefinitely until the window is closed)
window.mainloop()
