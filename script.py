from my_ai import *
import os

def ai_test():
    my_board = make_board()
    while not game_is_over(my_board):
        # The "X" player moves
        result = random.randint(1, 7)
        print("X Turn\nX selected ", result)
        select_space(my_board, result, "X")
        print_board(my_board)
        print(my_evaluate_board(my_board), "\n")

        if not game_is_over(my_board):
            # The "O" player moves
            result = random.randint(1, 7)
            print("O Turn\nO selected ", result)
            select_space(my_board, result, "O")
            print_board(my_board)
            print(my_evaluate_board(my_board), "\n")

    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")


def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
        # The "X" player finds their best move.
        result = minimax(my_board, True, 6, -float("Inf"), float("Inf"), my_evaluate_board)
        print("X Turn\nX selected ", result[1])
        select_space(my_board, result[1], "X")
        print_board(my_board)

        if not game_is_over(my_board):
            # The "O" player finds their best move
            result = minimax(my_board, False, 6, -float("Inf"), float("Inf"), codecademy_evaluate_board)
            print("O Turn\nO selected ", result[1])
            select_space(my_board, result[1], "O")
            print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")


def user_vs_ai_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Connect Four!")
    print("You will be playing with the 'O' pieces")
    print("while the computer plays with the 'X' pieces.\n")
    difficulty = int(input("Please select the difficulty by entering a number between 1 and 7: "))
    while 1 > difficulty or difficulty > 7:
        print("Error: Invalid Input")
        difficulty = int(input("Please select the difficulty by entering a number between 1 and 7: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    my_board = make_board()
    print_board(my_board)
    while not game_is_over(my_board):
        # User's turn to play
        print("\nYour Turn")
        user_move = int(input("Please type a number between 1 and 7 and press 'Enter': "))
        while 1 > user_move > 7:
            print("Error: Invalid Input")
            user_move = int(input("Please type a number between 1 and 7 and press 'Enter': "))
        select_space(my_board, user_move, "O")
        print_board(my_board)

        if not game_is_over(my_board):
            # The "X" player finds their best move.
            result = minimax(my_board, True, difficulty, -float("Inf"), float("Inf"), my_evaluate_board)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("X selected column ", result[1])
            select_space(my_board, result[1], "X")
            print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")


# ai_test()
# two_ai_game()
user_vs_ai_game()
