from connect_four import *


def my_evaluate_board(board):
    # X wins
    if has_won(board, "X"):
        return float("Inf")

    # O wins
    if has_won(board, "O"):
        return -float("Inf")

    # No win yet
    # Keep track of streaks for both players
    x_streak = 0
    o_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks horizontally
    for col in range(len(board) - 1):
        for row in range(len(board[0])):

            # Skip checked spaces
            if [col, row] in checked:
                continue

            else:
                # X streaks
                if board[col][row] == "X":
                    i = 1
                    while col + i < 7 and board[col + i][row] == "X":
                        x_streak += 1
                        checked.append([col + i, row])
                        i += 1

                # O streaks
                if board[col][row] == "O":
                    i = 1
                    while col + i < 7 and board[col + i][row] == "O":
                        o_streak += 1
                        checked.append([col + i, row])
                        i += 1

    # Reset checked spaces
    checked = []

    # Check for streaks vertically
    for col in range(len(board)):
        for row in range(len(board[0]) - 1):

            # Skip checked spaces
            if [col, row] in checked:
                continue

            else:
                # X streaks
                if board[col][row] == "X":
                    i = 1
                    while row + i < 6 and board[col][row + i] == "X":
                        x_streak += 1
                        checked.append([col, row + i])
                        i += 1

                # O streaks
                if board[col][row] == "O":
                    i = 1
                    while row + i < 6 and board[col][row + i] == "O":
                        o_streak += 1
                        checked.append([col, row + i])
                        i += 1

    return x_streak - o_streak


def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
        # The "X" player finds their best move.
        result = minimax(my_board, True, 6, -float("Inf"), float("Inf"), my_evaluate_board)
        print("X Turn\nX selected ", result[1])
        print(result[1])
        select_space(my_board, result[1], "X")
        print_board(my_board)

        if not game_is_over(my_board):
            # The "O" player finds their best move
            result = minimax(my_board, False, 6, -float("Inf"), float("Inf"), codecademy_evaluate_board)
            print("O Turn\nO selected ", result[1])
            print(result[1])
            select_space(my_board, result[1], "O")
            print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")


two_ai_game()
