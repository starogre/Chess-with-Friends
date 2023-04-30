import square

class Board:
    def __init__(self, c, r):
        self.board = self.initialize_board()
        self.__col = c
        self.__row = r

    def get_col(self):
        return self.__col

    def get_row(self):
        return self.__row

    def initialize_board(self):
        # Initialize the board with empty Square objects
        board = [[Square(row, col) for col in range(self.__col)] for row in range(self.__row)]
        return board

    def get_piece_at(self, row, col):
        return self.board[row][col].get_piece()

    def set_piece_at(self, row, col, piece):
        self.board[row][col].set_piece(piece)

    def execute_move(self, start_row, start_col, end_row, end_col):
        piece = self.get_piece_at(start_row, start_col)
        if piece is None:
            raise ValueError("No piece found at the given start position.")

        # If the move is valid, update the board and set the start position to None.
        self.set_piece_at(end_row, end_col, piece)
        self.set_piece_at(start_row, start_col, None)

    def is_empty(self, row, col):
        return self.board[row][col].is_empty()
