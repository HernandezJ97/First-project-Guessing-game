from random import randint  # randint - Used to generate a random number for the player to guess
import tkinter as tk
from tkinter import messagebox

# create GUI window
window = tk.Tk()
window.geometry('700x600')  # width and height
window.title('Guess The Number!')  # The title of the window
window.config(padx=10, pady=10, bg='purple')  # Change the background color

# The label of the window
guess_label = tk.Label(window, text='Try to guess the number I am thinking of!', font=("TimesNewRoman", 20),
                       bg='purple', fg='white')
guess_label.pack(padx=10, pady=10)

# Create an entry box for the user to enter their guess
guess_entry = tk.Entry(window, font=('TimesNewRoman', 20))
guess_entry.pack(padx=10, pady=10)

# Create a text box to show the user the number of guesses they have taken.
guess_text = tk.Text(window, font=("TimesNewRoman", 10, "bold"), bg='purple', fg='black')
guess_text.pack(padx=10, pady=10)

#  Global variables to keep track of the game state
number = randint(0, 100)
guess_limit = int(10)  # Setting a limit of 10 guesses
guesses = int(0)
previous_guesses = []


def reset_game():
    global number, guess_limit, guesses, previous_guesses
    number = randint(0, 100)
    guess_limit = 10
    guesses = 0
    previous_guesses = []
    guess_text.delete("1.0", tk.END)
    guess_entry.delete(0, tk.END)


def play_game():
    global guesses
    try:
        guess = int(guess_entry.get())
        if guess < int(0) or guess > int(100):
            messagebox.showinfo("Invalid input", "Please enter a number between 0 and 100.")
            return
        if guess in previous_guesses:
            messagebox.showinfo("Invalid input", "You have already guessed that number.")
            return

        previous_guesses.append(guess)  # Adding the guess to previous guesses
        guesses += int(1)
        remaining_guesses = guess_limit - guesses

        if guess == number:
            messagebox.showinfo("Congratulations!",
                                f"You guessed the number correctly it took you {guesses} guesses.")
            if messagebox.askyesno("Play again?", "Would you like to play again?"):
                reset_game()
            else:
                window.quit()
        elif guess < number:
            guess_text.insert(tk.END, f"{guess} The number is greater than what you guessed. {remaining_guesses} "
                                      f"guesses remaining.\n")
        else:
            guess_text.insert(tk.END, f"{guess} The number is less than what you guessed. {remaining_guesses} "
                                      f"guesses remaining.\n")
        if guesses >= guess_limit:
            messagebox.showinfo("Game Over", f"Sorry, you ran out of guesses. The number was {number}.")
            if messagebox.askyesno("Play again?", "Would you like to play again?"):
                reset_game()
            else:
                window.quit()

        guess_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showinfo("Invalid input", "Please enter a valid number.")


#  Create a button
submit_button = tk.Button(window, text='Submit Guess', bg='black', fg='white', command=play_game)

# The button that will start the game
submit_button.config(font=("TimesNewRoman", 12, "bold"))  # change the font
submit_button.pack(padx=10, pady=10)

window.mainloop()
