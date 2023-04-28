import Square

class Board:
    def __init__(self):
        self.squares = self.initialize_squares()

    def initialize_squares(self):
        # Initialize the board with empty Square objects
        square = [[Square(row, col) for col in range(8)] for row in range(8)]
        return square

    def get_piece_at(self, row, col):
        return self.square[row][col].get_piece()

    def set_piece_at(self, row, col, piece):
        self.square[row][col].set_piece(piece)

    def execute_move(self, start_row, start_col, end_row, end_col):
        piece = self.get_piece_at(start_row, start_col)
        if piece is None:
            raise ValueError("No piece found at the given start position.")

        # If the move is valid, update the board and set the start position to None.
        self.set_piece_at(end_row, end_col, piece)
        self.set_piece_at(start_row, start_col, None)

    def is_empty(self, row, col):
        return self.square[row][col].is_empty()
