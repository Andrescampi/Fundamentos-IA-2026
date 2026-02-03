# Abstract
from environment_state import EnvironmentState

# Types
from typing import Optional, List, Any

# Libraries
import numpy as np
import matplotlib.pyplot as plt


class ConnectState(EnvironmentState):
    """
    Environment state representation for the Connect Four game.
    """

    def __init__(self, board: Optional[np.ndarray] = None, current_player: int = -1):
        """
        Initializes the Connect Four game state.

        Parameters
        ----------
        board : Optional[np.ndarray]
            A NumPy array representing the board state. If None, an empty board is created.
        current_player : int
            The current player (-1 for red, 1 for yellow). Defaults to -1.
        """
        if board is not None:
            self.board = board.copy()
        else:
            self.board = np.zeros((6, 7), dtype=int)
        self.current_player = current_player

    def is_final(self) -> bool:
        """See base class."""
        return self.get_winner() != 0 or np.all(self.board != 0)

    def is_applicable(self, event: Any) -> bool:
        if self.is_final():
            return False
        if isinstance(event, int) and 0 <= event < self.board.shape[1]:
            return self.is_col_free(event)
        return False

    def transition(self, event: Any) -> "EnvironmentState":
        """See base class."""
        if not self.is_applicable(event):
            raise ValueError("Invalid move: column is full, out of range, or game is over.")
        col = int(event)
        heights = self.get_heights()
        row = heights[col]
        new_board = self.board.copy()
        new_board[row, col] = self.current_player
        new_current_player = -self.current_player
        return ConnectState(new_board, new_current_player)

    def get_winner(self) -> int:
        """
        Determines the winner in the current state.

        Returns
        -------
        int
            -1 if red has won, 1 if yellow has won, 0 if no winner.
        """
        # Check rows
        for row in range(self.board.shape[0]):
            for col in range(self.board.shape[1] - 3):
                if self.board[row, col] == self.board[row, col+1] == self.board[row, col+2] == self.board[row, col+3] != 0:
                    return self.board[row, col]

        # Check columns
        for col in range(self.board.shape[1]):
            for row in range(self.board.shape[0] - 3):
                if self.board[row, col] == self.board[row+1, col] == self.board[row+2, col] == self.board[row+3, col] != 0:
                    return self.board[row, col]

        # Check diagonals (top-left to bottom-right)
        for row in range(self.board.shape[0] - 3):
            for col in range(self.board.shape[1] - 3):
                if self.board[row, col] == self.board[row+1, col+1] == self.board[row+2, col+2] == self.board[row+3, col+3] != 0:
                    return self.board[row, col]

        # Check diagonals (top-right to bottom-left)
        for row in range(self.board.shape[0] - 3):
            for col in range(3, self.board.shape[1]):
                if self.board[row, col] == self.board[row+1, col-1] == self.board[row+2, col-2] == self.board[row+3, col-3] != 0:
                    return self.board[row, col]

        return 0

    def is_col_free(self, col: int) -> bool:
        """
        Checks if a column has at least one free cell.

        Parameters
        ----------
        col : int
            The column index to check.

        Returns
        -------
        bool
            True if the column has at least one free cell; False otherwise.
        """
        return self.board[0, col] == 0

    def get_heights(self) -> List[int]:
        """
        Gets the heights of each column in the board.

        Returns
        -------
        List[int]
            A list containing the height of each column.
        """
        return [int(np.count_nonzero(self.board[:, col])) for col in range(self.board.shape[1])]      
        

    def get_free_cols(self) -> List[int]:
        """
        Gets the list of columns where a tile can still be placed.

        Returns
        -------
        List[int]
            Indices of columns with at least one free cell.
        """
        return [col for col in range(self.board.shape[1]) if self.is_col_free(col)]

    def show(self, size: int = 1500, ax: Optional[plt.Axes] = None) -> None:
        """
        Visualizes the current board state using matplotlib.

        Parameters
        ----------
        size : int, optional
            Size of the stones, by default 1500.
        ax : Optional[matplotlib.axes._axes.Axes], optional
            Axes to plot on. If None, a new figure is created.
        """
        if ax is None:
            fig, ax = plt.subplots()
        else:
            fig = None

        pos_red = np.where(self.board == -1)
        pos_yellow = np.where(self.board == 1)

        ax.scatter(pos_yellow[1] + 0.5, 5.5 - pos_yellow[0], color="yellow", s=size)
        ax.scatter(pos_red[1] + 0.5, 5.5 - pos_red[0], color="red", s=size)

        ax.set_ylim([0, self.board.shape[0]])
        ax.set_xlim([0, self.board.shape[1]])
        ax.grid()

        if fig is not None:
            plt.show()
