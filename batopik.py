import random

def main():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    print("Let's play Rock, Paper, Scissors!")
    player_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
    
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {player_choice}")

    if player_choice not in choices:
        print("Invalid choice. Please select rock, paper, or scissors.")
        return

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "scissors" and computer_choice == "paper") or
        (player_choice == "paper" and computer_choice == "rock")
    ):
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == "__main__":
    main()
