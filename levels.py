import random

def number_ninja():
    print("🥷 Welcome to Number Ninja! 🥷")
    print("Your mission: Guess the secret number before your chances run out!")
    print("\nChoose your difficulty:")
    print("1. Simple (1–20, 6 attempts)")
    print("2. Medium (1–50, 5 attempts)")
    print("3. Hard (1–100, 4 attempts)")

    # Choose difficulty
    while True:
        try:
            choice = input("\nEnter 1, 2, or 3: ").strip()
            if choice == '1':
                max_number = 20
                attempts = 6
                level = "Simple"
                break
            elif choice == '2':
                max_number = 50
                attempts = 5
                level = "Medium"
                break
            elif choice == '3':
                max_number = 100
                attempts = 4
                level = "Hard"
                break
            else:
                print("⚠️ Invalid choice! Please choose 1, 2, or 3.")
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")

    print(f"\nYou chose {level} mode! Guess a number between 1 and {max_number}.")

    # Generate secret number
    secret_number = random.randint(1, max_number)

    # Game loop
    while attempts > 0:
        try:
            guess_input = input("\nEnter your guess: ").strip()
            if not guess_input.isdigit():
                print("⚠️ Please enter a valid number (no letters or symbols)!")
                continue

            guess = int(guess_input)

            # Ensure guess is within range
            if guess < 1 or guess > max_number:
                print(f"⚠️ The number must be between 1 and {max_number}! Try again.")
                continue

            # Check guess
            if guess == secret_number:
                print(f"🎯 You did it, Ninja! The secret number was {secret_number}!")
                break
            elif guess < secret_number:
                print("⬆️ Too low! Aim higher!")
            else:
                print("⬇️ Too high! Aim lower!")

            attempts -= 1
            print(f"🕐 Attempts left: {attempts}")

        except ValueError:
            print("⚠️ Invalid input! Please enter an integer.")
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")

    else:
        print(f"\n💀 Game Over! The secret number was {secret_number}. Better luck next time, Ninja!")

# Run the game
if __name__ == "__main__":
    number_ninja()
