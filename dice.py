import random

def roll_dice():
    return random.randint(1, 6)

def display_welcome_message():
    print("Welcome to the Dice Rolling Game!")
    print("Each player will roll a dice. The first to win 2 rounds wins the game.\n")

def get_player_choice(player_num):
    input(f"Player {player_num}, press Enter to roll the dice...")

def display_round_result(player_num, roll_result):
    print(f"Player {player_num} rolls: {roll_result}")

def display_round_winner(winner):
    print(f"{winner} wins this round!\n")

def display_game_winner(winner):
    print(f"Congratulations, {winner} wins the game!")

def main():
    display_welcome_message()

    player1_wins = 0
    player2_wins = 0
    rounds_to_win = 2
    round_num = 1

    while player1_wins < rounds_to_win and player2_wins < rounds_to_win:
        print(f"Round {round_num}:")
        
        get_player_choice(1)
        player1_roll = roll_dice()
        display_round_result(1, player1_roll)

        get_player_choice(2)
        player2_roll = roll_dice()
        display_round_result(2, player2_roll)

        if player1_roll > player2_roll:
            player1_wins += 1
            display_round_winner("Player 1")
        elif player2_roll > player1_roll:
            player2_wins += 1
            display_round_winner("Player 2")
        else:
            print("It's a tie for this round!\n")

        round_num += 1

    if player1_wins > player2_wins:
        display_game_winner("Player 1")
    else:
        display_game_winner("Player 2")

if __name__ == "__main__":
    main()

