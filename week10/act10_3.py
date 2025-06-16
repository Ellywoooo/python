"""Play a game of noughts and crosses"""

def main():
    board = new_board()
    display_board(board)
    human_player = get_O_or_X()
    outcome = play_game(board, human_player)
    print_result(outcome)

def new_board():
    return [" "]*9

def display_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")

def get_O_or_X():
    while True:
        choice = input("Enter O or X: ").upper()
        if choice in ["O", "X"]:
            return choice
        print("Please select O or X.")

# Play until a win or a draw
def play_game(board, human_player):
    computer = "X" if human_player == "O" else "O"
    current_player = human_player
    
    while True:
        display_board(board)
        play_one_turn(board, current_player)
        # Check if the game is over after the current player's turn
        if game_over(board, current_player) is not None:
            display_board(board)
            return game_over(board, current_player)
        else:    
            # Once the human player has played, the computer takes its turn
            current_player = computer if current_player == human_player else human_player

# Takes the position and updates the board
def play_one_turn(board, current_player):
    while True:
        position = int(input(f"{current_player}'s turn. Please Enter the position (0-8): "))
        if (position < 0 or position > 8):
            print("Please enter a number 0-8.")
            continue
        if board[position] != " ":
            print("That position is already taken.")
            continue
        board[position] = current_player
        break

# Saves all the possible ways to win and compares the board to see if there is a winner
def game_over(board, current_player):
    # Tuples representing winning combinations
    winning_options = [
        (0,1,2), (3,4,5), (6,7,8), # Rows
        (0,3,6), (1,4,7), (2,5,8), # Columns
        (0,4,8), (2,4,6)          # Diagonals
    ]
    
    # Tuple unpacking to check for a winner
    for a, b, c in winning_options:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return current_player
    # Check for a draw
    if " " not in board:
        return "draw"

def print_result(outcome):
    if outcome == "draw":
        print("It's a draw!")
    else:
        print(f"The winner is {outcome}!")

if __name__ == "__main__":
    main()