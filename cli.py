# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import logging
from logic import make_empty_board, get_winner, other_player

logging.basicConfig(
    filename='logs/happyjoel_game_log.log',
    level=logging.INFO
)

def print_board(board):
    for i in range(3):
        for j in range(3):
            print(" " if board[i][j] is None else board[i][j], end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("-" * 9)

def main():
    board = make_empty_board()
    player = 'X'
    winner = None

    while winner is None:
        print_board(board)
        print(f"Player {player}'s turn:")
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))

        if board[row][col] is None:
            board[row][col] = player
            winner = get_winner(board)
            player = other_player(player)
        else:
            print("Invalid move. That position is already occupied. Try again.")

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
        logging.info('You win!')
    else:
        print("It's a draw!")
        logging.info("It's a draw!")

if __name__ == '__main__':
    main()