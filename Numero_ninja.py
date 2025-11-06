import random

def number_ninja():
    print("🥷 Welcome to Number Ninja! 🥷")
    print("Your goal: Guess the secret number between 1 and 100!")
    print("You have 7 attempts. Can you slice the right number?")

    secret_number = random.randint(1, 100)
    attempts = 7

    while attempts > 0:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        if guess < 1 or guess > 100:
            print("⚠️ The number must be between 1 and 100!")
            continue

        if guess == secret_number:
            print(f"🎯 You did it, Ninja! The secret number was {secret_number}!")
            break
        elif guess < secret_number:
            print("⬆️ Too low! Try a higher number.")
        else:
            print("⬇️ Too high! Try a lower number.")

        attempts -= 1
        print(f"🕐 Attempts left: {attempts}")

    else:
        print(f"\n💀 Game Over! The secret number was {secret_number}. Better luck next time, Ninja!")

# Run the game
if __name__ == "__main__":
    number_ninja()
