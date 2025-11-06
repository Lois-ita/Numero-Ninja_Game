import tkinter as tk
from tkinter import messagebox
import random

class NumberNinjaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🥷 Number Ninja")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.level = None
        self.secret_number = None
        self.attempts = 0
        self.max_number = 0

        self.create_welcome_screen()

    # --- Screen 1: Choose difficulty ---
    def create_welcome_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(
            self.root, text="🥷 Welcome to Number Ninja! 🥷",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        tk.Label(
            self.root, text="Choose your difficulty level:",
            font=("Arial", 12)
        ).pack(pady=10)

        tk.Button(self.root, text="Simple (1–20, 6 attempts)",
                  command=lambda: self.start_game("Simple")).pack(pady=5)
        tk.Button(self.root, text="Medium (1–50, 5 attempts)",
                  command=lambda: self.start_game("Medium")).pack(pady=5)
        tk.Button(self.root, text="Hard (1–100, 4 attempts)",
                  command=lambda: self.start_game("Hard")).pack(pady=5)

    # --- Start Game based on difficulty ---
    def start_game(self, level):
        self.level = level
        if level == "Simple":
            self.max_number = 20
            self.attempts = 6
        elif level == "Medium":
            self.max_number = 50
            self.attempts = 5
        elif level == "Hard":
            self.max_number = 100
            self.attempts = 4

        self.secret_number = random.randint(1, self.max_number)
        self.create_game_screen()

    # --- Screen 2: Game Interface ---
    def create_game_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Level: {self.level}", font=("Arial", 12)).pack(pady=10)
        tk.Label(self.root, text=f"Guess a number between 1 and {self.max_number}").pack(pady=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 11))
        self.result_label.pack(pady=10)

        self.guess_entry = tk.Entry(self.root, font=("Arial", 12))
        self.guess_entry.pack(pady=5)

        tk.Button(self.root, text="Submit Guess", command=self.check_guess).pack(pady=10)

        self.attempts_label = tk.Label(self.root, text=f"Attempts left: {self.attempts}", font=("Arial", 11))
        self.attempts_label.pack(pady=5)

        tk.Button(self.root, text="🏠 Back to Menu", command=self.create_welcome_screen).pack(side="bottom", pady=10)

    # --- Check Guess ---
    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number!")
            return

        if guess < 1 or guess > self.max_number:
            messagebox.showinfo("Out of Range", f"Enter a number between 1 and {self.max_number}.")
            return

        if guess == self.secret_number:
            messagebox.showinfo("🎯 Victory!", f"You did it, Ninja! The secret number was {self.secret_number}!")
            self.create_welcome_screen()
            return
        elif guess < self.secret_number:
            self.result_label.config(text="⬆️ Too low! Aim higher!", fg="blue")
        else:
            self.result_label.config(text="⬇️ Too high! Aim lower!", fg="red")

        self.attempts -= 1
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")

        if self.attempts == 0:
            messagebox.showerror("💀 Game Over!", f"You ran out of attempts!\nThe number was {self.secret_number}.")
            self.create_welcome_screen()

        self.guess_entry.delete(0, tk.END)

# --- Run the Game ---
if __name__ == "__main__":
    root = tk.Tk()
    app = NumberNinjaGUI(root)
    root.mainloop()
