def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("\n  1   2   3")
    print(" ──┼───┼───")
    for i in range(3):
        print(f"{i+1} ", end="")
        for j in range(3):
            print(f"{board[i][j]} ", end="")
            if j < 2:
                print("│ ", end="")
        print()
        if i < 2:
            print(" ──┼───┼───")

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = initialize_board()
    players = ['Player 1', 'Player 2']
    symbols = ['X', 'O']
    current_player = 0

    print("Welcome to Tic-Tac-Toe!\n")

    while True:
        print_board(board)
        player_name = players[current_player]
        player_symbol = symbols[current_player]

        print(f"\n{player_name}'s turn ({player_symbol})\n")
        while True:
            try:
                row = int(input("Enter row number (1-3): ")) - 1
                col = int(input("Enter column number (1-3): ")) - 1

                if not (0 <= row <= 2 and 0 <= col <= 2):
                    raise ValueError("Row and column must be between 1 and 3.")

                if board[row][col] != ' ':
                    raise ValueError("That position is already taken. Choose another.")

                break
            except ValueError as e:
                print(f"Error: {e}")

        board[row][col] = player_symbol

        if check_win(board, player_symbol):
            print_board(board)
            print(f"\nCongratulations! {player_name} wins!\n")
            break
        elif is_board_full(board):
            print_board(board)
            print("\nIt's a draw!\n")
            break

        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    main()
