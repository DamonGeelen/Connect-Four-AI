from my_ai import *


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
            result = minimax(my_board, False, 3, -float("Inf"), float("Inf"), codecademy_evaluate_board)
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
    pass


# ai_test()
two_ai_game()
