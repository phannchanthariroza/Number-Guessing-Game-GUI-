import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.difficulty = tk.StringVar(value="Easy")
        self.target_number = 0
        self.guess_count = 0
        self.max_range = 50

        self.create_widgets()
    
    def create_widgets(self):
        # Difficulty selection
        tk.Label(self.root, text="Please Select level of Difficulty:").pack()
        tk.Radiobutton(self.root, text="Easy (1-50)", variable=self.difficulty, value="Easy", command=self.set_difficulty).pack()
        tk.Radiobutton(self.root, text="Medium (1-100)", variable=self.difficulty, value="Medium", command=self.set_difficulty).pack()
        tk.Radiobutton(self.root, text="Hard (1-500)", variable=self.difficulty, value="Hard", command=self.set_difficulty).pack()
        
        # Guess input
        self.entry_guess = tk.Entry(self.root)
        self.entry_guess.pack()
        tk.Button(self.root, text="Submit Guess", command=self.check_guess).pack()
        
        # Output label
        self.label_output = tk.Label(self.root, text="")
        self.label_output.pack()

        # Restart Button
        tk.Button(self.root, text="Restart Game", command=self.restart_game).pack()

        self.start_new_game()

    def set_difficulty(self):
        difficulty = self.difficulty.get()
        if difficulty == "Easy":
            self.max_range = 50
        elif difficulty == "Medium":
            self.max_range = 100
        elif difficulty == "Hard":
            self.max_range = 500
        self.start_new_game()

    def start_new_game(self):
        self.target_number = random.randint(1, self.max_range)
        self.guess_count = 0
        self.label_output.config(text=f"Guess a number between 1 and {self.max_range}!")

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.guess_count += 1
            if guess < 1 or guess > self.max_range:
                raise ValueError(f"Number must be between 1 and {self.max_range}.")

            if guess == self.target_number:
                self.show_result_popup(f"Yahoo!Congratulations! You guessed the correct number {self.target_number} in {self.guess_count} attempts!")
                self.start_new_game()
            elif guess < self.target_number:
                self.label_output.config(text="Higher! Try again.")
            else:
                self.label_output.config(text="Lower! Try again.")
        
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
        finally:
            self.entry_guess.delete(0, tk.END)

    def show_result_popup(self, message):
        popup = tk.Toplevel(self.root)
        popup.title("Game Result")
        tk.Label(popup, text=message, padx=20, pady=10).pack()
        tk.Button(popup, text="Close", command=popup.destroy).pack(pady=5)

    def restart_game(self):
        self.start_new_game()

# Create the main window and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGameApp(root)
    root.mainloop()
