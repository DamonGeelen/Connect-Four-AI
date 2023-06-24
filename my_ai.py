from connect_four import *


def right_streak_check(board, symbol):
    # Keep track of streak
    right_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks moving to the right
    for col in range(len(board) - 3):
        for row in range(len(board[0])):

            # Skip checked spaces
            if [col, row] in checked:
                continue

            else:
                if board[col][row] == symbol:
                    i = 1
                    while col + i < 7 and board[col + i][row] == symbol:
                        checked.append([col + i, row])
                        i += 1

                    # Only count streak if it is not blocked
                    if col + i < 7 and board[col + i][row] == ' ':
                        right_streak += i - 1

    return right_streak


def left_streak_check(board, symbol):
    # Keep track of streak
    left_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks moving to the right
    for col in range(len(board) - 1, 3, -1):
        for row in range(len(board[0])):

            # Skip checked spaces
            if [col, row] in checked:
                continue

            else:
                if board[col][row] == symbol:
                    i = 1
                    while col - i >= 0 and board[col - i][row] == symbol:
                        checked.append([col - i, row])
                        i += 1

                    # Only count streak if it is not blocked
                    if col + i >= 0 and board[col - i][row] == ' ':
                        left_streak += i - 1

    return left_streak


def up_streak_check(board, symbol):
    # Keep track of streak
    up_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks moving downward
    for col in range(len(board)):
        for row in range(len(board[0]) - 3, 1, -1):

            # Skip checked spaces
            if [col, row] in checked:
                continue

            else:
                if board[col][row] == symbol:
                    i = 1
                    while row - i >= 0 and board[col][row - i] == symbol:
                        checked.append([col, row - i])
                        i += 1

                    # Only count streak if it is not blocked
                    if row + i >= 0 and board[col][row - i] == ' ':
                        up_streak += i - 1

    return up_streak


def total_streak_check(board, symbol):

    # Keep track of streak
    total_streak = sum([
        right_streak_check(board, symbol),
        left_streak_check(board, symbol),
        up_streak_check(board, symbol)
    ])

    return total_streak


def my_evaluate_board(board):
    # X wins
    if has_won(board, "X"):
        return float("Inf")

    # O wins
    if has_won(board, "O"):
        return -float("Inf")

    # No win yet
    # Keep track of streaks for both players
    x_streak = total_streak_check(board, "X")
    o_streak = total_streak_check(board, "O")

    return x_streak - o_streak
