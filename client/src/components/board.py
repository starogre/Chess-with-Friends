from square import Square
from constants import *

class Board:
    def __init__(self):
        self.board = []
        self.squares = [[Square(row, col) for col in range(8)] for row in range(8)]
        self.create_board()

    def create_board(self):
        for row in range(ROW_COUNT):
            self.board.append([])
            for col in range(COL_COUNT):
                # get piece objects into a start pieces array for piece= ?
                self.board[row].append(Square(row, col, piece=START_PIECES[row][col]))
        print(self.board)