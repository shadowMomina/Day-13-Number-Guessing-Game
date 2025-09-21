"""
Day 13 of 90-Day Coding Series
Number Guessing Game (Beginner-Friendly)

How it works:
- The computer picks a random secret number.
- You try to guess it. After each guess the program tells you
  whether the secret number is higher or lower.
- You can choose a difficulty (controls number of allowed attempts and range).
- After the round finishes you can choose to play again or quit.

Save this file as: number_guessing_game_day13.py
Run: python number_guessing_game_day13.py
"""

import random

def get_int(prompt, min_value=None, max_value=None):
    """
    Ask the user for an integer until they give a valid one.
    Optionally enforce a minimum and/or maximum value.
    Returns the integer.
    """
    while True:
        s = input(prompt).strip()
        if s.lstrip('-').isdigit():  # allow negative if needed (not used here)
            n = int(s)
            if min_value is not None and n < min_value:
                print(f"Please enter a number >= {min_value}.")
            elif max_value is not None and n > max_value:
                print(f"Please enter a number <= {max_value}.")
            else:
                return n
        else:
            print("That's not a valid number. Try again.")

def choose_difficulty():
    """
    Let the player choose difficulty.
    Returns a tuple (min_value, max_value, max_attempts).
    """
    print("\nChoose difficulty:")
    print("1) Easy   - Range 1 to 20, 7 attempts")
    print("2) Medium - Range 1 to 50, 6 attempts")
    print("3) Hard   - Range 1 to 100, 5 attempts")
    choice = get_int("Enter 1, 2 or 3: ", 1, 3)

    if choice == 1:
        return (1, 20, 7)
    elif choice == 2:
        return (1, 50, 6)
    else:
        return (1, 100, 5)

def play_round():
    """
    Play one round of the number guessing game.
    Returns True if the player found the number, False otherwise.
    """
    low, high, max_attempts = choose_difficulty()
    secret = random.randint(low, high)
    attempts = 0

    print(f"\nI have chosen a number between {low} and {high}.")
    print(f"You have {max_attempts} attempts to guess it. Good luck!")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        guess = get_int(f"\nAttempt {attempts+1} - Enter your guess ({low}-{high}): ", low, high)
        attempts += 1

        if guess == secret:
            print(f"🎉 Correct! You found the number {secret} in {attempts} attempt(s).")
            return True
        elif guess < secret:
            print("Too low ⬇️")
        else:
            print("Too high ⬆️")

        # Helpful hint: show how many attempts remain
        if attempts < max_attempts:
            print(f"You have {max_attempts - attempts} attempt(s) left.")
        else:
            print("No attempts left.")

    # If loop ends without return, player failed to guess
    print(f"\n😞 You've used all attempts. The secret number was {secret}.")
    return False

def main():
    print("=== Day 13: Number Guessing Game ===")
    print("Welcome! Try to guess the secret number chosen by the computer.")

    while True:
        play_round()

        # Ask player if they want to play again
        print("\nWhat would you like to do next?")
        print("1. Quit")
        print("2. Play again")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            print("Thanks for playing! See you next time.")
            break
        elif choice == "2":
            continue
        else:
            print("Invalid choice. Exiting the game. Goodbye!")
            break

if __name__ == "__main__":
    main()
