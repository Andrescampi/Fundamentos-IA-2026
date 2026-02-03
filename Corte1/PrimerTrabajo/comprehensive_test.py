from connect_state import ConnectState
import numpy as np

def test_basic_functionality():
    print("=== Testing Basic Functionality ===")
    # Create an empty board
    s = ConnectState()
    print("Empty board:")
    print(s.board)
    print("Heights:", s.get_heights())
    print("Free columns:", s.get_free_cols())
    print("Is final:", s.is_final())
    print("Winner:", s.get_winner())
    print("Current player:", s.current_player)
    print()

def test_with_existing_board():
    print("=== Testing with Existing Board ===")
    board = np.zeros((6, 7), dtype=int)
    board[5,3] = -1
    board[0,3] = 1
    board[1,3] = -1
    board[2,3] = -1
    board[3,3] = -1
    board[4,3] = -1
    s = ConnectState(board)
    print("Board:")
    print(s.board)
    print("Heights:", s.get_heights())
    print("Is col 2 free:", s.is_col_free(2))
    print("Free columns:", s.get_free_cols())
    print("Is applicable (3):", s.is_applicable(3))  # False, column full
    print("Is applicable (2):", s.is_applicable(2))  # True
    print("Is applicable (7):", s.is_applicable(7))  # False, invalid column
    print("Is applicable ('invalid'):", s.is_applicable("invalid"))  # False, not int
    print("Is final:", s.is_final())
    print("Winner:", s.get_winner())
    print()

def test_transition():
    print("=== Testing Transition ===")
    s = ConnectState()
    print("Initial board:")
    print(s.board)
    print("Current player:", s.current_player)

    # Make a move
    try:
        new_state = s.transition(3)
        print("After placing in column 3:")
        print(new_state.board)
        print("New current player:", new_state.current_player)
    except ValueError as e:
        print("Error:", e)

    # Try invalid move
    try:
        invalid_state = s.transition(10)
        print("This shouldn't print")
    except ValueError as e:
        print("Expected error for invalid column:", e)

    print()

def test_win_conditions():
    print("=== Testing Win Conditions ===")
    # Horizontal win for red (-1)
    board = np.zeros((6, 7), dtype=int)
    board[5, 0:4] = -1
    s = ConnectState(board)
    print("Horizontal win board:")
    print(s.board)
    print("Winner:", s.get_winner())
    print("Is final:", s.is_final())
    print()

    # Vertical win for yellow (1)
    board = np.zeros((6, 7), dtype=int)
    board[5:2, 3] = 1
    s = ConnectState(board)
    print("Vertical win board:")
    print(s.board)
    print("Winner:", s.get_winner())
    print("Is final:", s.is_final())
    print()

    # Diagonal win
    board = np.zeros((6, 7), dtype=int)
    for i in range(4):
        board[5-i, i] = -1
    s = ConnectState(board)
    print("Diagonal win board:")
    print(s.board)
    print("Winner:", s.get_winner())
    print("Is final:", s.is_final())
    print()

def test_draw():
    print("=== Testing Draw ===")
    # Create a full board with no winner (no four in a row)
    board = np.array([
        [1, -1, 1, 1, -1, 1, -1],
        [-1, 1, -1, -1, 1, -1, 1],
        [1, -1, 1, 1, -1, 1, -1],
        [-1, 1, -1, -1, 1, -1, 1],
        [1, -1, 1, 1, -1, 1, -1],
        [-1, 1, -1, -1, 1, -1, 1]
    ])
    s = ConnectState(board)
    print("Draw board:")
    print(s.board)
    print("Winner:", s.get_winner())
    print("Is final:", s.is_final())
    print()

if __name__ == "__main__":
    test_basic_functionality()
    test_with_existing_board()
    test_transition()
    test_win_conditions()
    test_draw()
    print("All tests completed!")
