# This is the main code for the game rules of sudoku.

import random
import numpy as np

class Sudoku:
    # Sudoku class

    def __init__(self, seed=None):
        # Constructor
        self.seed = seed
        self.board = np.zeros((9, 9), dtype=int)
        self.solution = np.zeros((9, 9), dtype=int)
        self.generate_board()

    def generate_board(self):
        # Generate a new board
        if self.seed is not None:
            random.seed(self.seed)
        self.board = np.zeros((9, 9), dtype=int)
        self.solution = np.zeros((9, 9), dtype=int)
        self.generate_solution()


    def generate_solution(self):
        # Generate a new solution
        return None
