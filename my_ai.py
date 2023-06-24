from connect_four import *

# The following are a list of functions to count the streaks a given player has in any one direction.

# Note that there is no function to count the streak downwards since a piece cannot be placed
# directly below another piece.

# ---------------------------------------------------------------------------------------------------
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

    # Check for streaks moving to the left
    for col in range(len(board) - 1, 2, -1):
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
                    if col - i >= 0 and board[col - i][row] == ' ':
                        left_streak += i - 1

    return left_streak


def up_streak_check(board, symbol):
    # Keep track of streak
    up_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks moving upward
    for col in range(len(board)):
        for row in range(len(board[0]) - 1, 2, -1):

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
                    if row - i >= 0 and board[col][row - i] == ' ':
                        up_streak += i - 1

    return up_streak


def up_right_streak_check(board, symbol):
    # Keep track of streak
    up_right_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks moving upward and to the right
    for col in range(len(board) - 3):
        for row in range(len(board[0]) - 1, 2, -1):

            # Skip checked spaces
            if [col, row] in checked:
                continue

            else:
                if board[col][row] == symbol:
                    i = 1
                    while col + i < 7 and row - i >= 0 and board[col + i][row - i] == symbol:
                        checked.append([col + i, row - i])
                        i += 1

                    # Only count streak if it is not blocked
                    if col + i < 7 and row - i >= 0 and board[col + i][row - i] == ' ':
                        up_right_streak += i - 1

    return up_right_streak


def down_right_streak_check(board, symbol):
    # Keep track of streak
    down_right_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks moving downward and to the right
    for col in range(len(board) - 3):
        for row in range(len(board[0]) - 3):

            # Skip checked spaces
            if [col, row] in checked:
                continue

            else:
                if board[col][row] == symbol:
                    i = 1
                    while col + i < 7 and row + i < 7 and board[col + i][row + i] == symbol:
                        checked.append([col + i, row + i])
                        i += 1

                    # Only count streak if it is not blocked
                    if col + i < 7 and row + i < 7 and board[col + i][row + i] == ' ':
                        down_right_streak += i - 1

    return down_right_streak


def up_left_streak_check(board, symbol):
    # Keep track of streak
    up_left_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks moving upward and to the left
    for col in range(len(board) - 1, 2, -1):
        for row in range(len(board[0]) - 1, 2, -1):

            # Skip checked spaces
            if [col, row] in checked:
                continue

            else:
                if board[col][row] == symbol:
                    i = 1
                    while col - i >= 0 and row - i >= 0 and board[col - i][row - i] == symbol:
                        checked.append([col + i, row - i])
                        i += 1

                    # Only count streak if it is not blocked
                    if col - i >= 0 and row - i >= 0 and board[col - i][row - i] == ' ':
                        up_left_streak += i - 1

    return up_left_streak


def down_left_streak_check(board, symbol):
    # Keep track of streak
    down_left_streak = 0

    # Keep track of checked spaces
    checked = []

    # Check for streaks moving downward and to the left
    for col in range(len(board) - 1, 2, -1):
        for row in range(len(board[0]) - 3):

            # Skip checked spaces
            if [col, row] in checked:
                continue

            else:
                if board[col][row] == symbol:
                    i = 1
                    while col - i >= 0 and row + i < 7 and board[col - i][row + i] == symbol:
                        checked.append([col + i, row + i])
                        i += 1

                    # Only count streak if it is not blocked
                    if col - i >= 0 and row + i < 7 and board[col - i][row + i] == ' ':
                        down_left_streak += i - 1

    return down_left_streak
# ---------------------------------------------------------------------------------------------------

# Sum all the streaks for a given player
def total_streak_check(board, symbol):

    # Keep track of streak
    total_streak = sum([
        right_streak_check(board, symbol),
        left_streak_check(board, symbol),
        up_streak_check(board, symbol),
        up_right_streak_check(board, symbol),
        down_right_streak_check(board, symbol),
        up_left_streak_check(board, symbol),
        down_right_streak_check(board, symbol)
    ])

    return total_streak


# Find the current advantage for each player based on their total streaks,
# then return the difference so the AI can evaluate any given board scenario
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
