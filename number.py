import random

def number_game():
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)

    number_of_tries = 0
    has_guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print(f"I've selected a random number between {lower_bound} and {upper_bound}. Can you guess it?")

    while not has_guessed_correctly:
        user_guess = int(input("Enter your guess: "))
        number_of_tries += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            has_guessed_correctly = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {number_of_tries} tries.")

if __name__ == "__main__":
    number_game()
