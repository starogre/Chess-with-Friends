class Board:
    def __init__(self):
        self.board = self.initialize_board()

    def initialize_board(self):
        # Initialize the board with empty Square objects
        board = [[Square() for _ in range(8)] for _ in range(8)]
        return board

    def get_piece(self, row, col):
        return self.board[row][col].get_piece()

    def set_piece(self, row, col, piece):
        self.board[row][col].set_piece(piece)

    def execute_move(self, start_row, start_col, end_row, end_col):
        piece = self.get_piece(start_row, start_col)
        if piece is None:
            raise ValueError("No piece found at the given start position.")

        # If the move is valid, update the board and set the start position to None.
        self.set_piece(end_row, end_col, piece)
        self.set_piece(start_row, start_col, None)

    def is_empty(self, row, col):
        return self.board[row][col].is_empty()