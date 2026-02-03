from connect_state import ConnectState

import numpy as np
import matplotlib.pyplot as plt


board = np.zeros((6, 7), dtype=int)
board[5,3] = -1
board[0,3] = 1
board[1,3] = -1
board[2,3] = -1
board[3,3] = -1
board[4,3] = -1
s = ConnectState(board)
print(s.board)
print(s.get_heights())
print(s.is_col_free(2))
print(s.get_free_cols())
print(s.is_applicable(3))  # Should be False, column 3 is full
print(s.is_applicable(2))  # Should be True, column 2 is free
print(s.is_applicable(7))  # Should be False, invalid column
print(s.is_applicable("invalid"))  # Should be False, not an int
