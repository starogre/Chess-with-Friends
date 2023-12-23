from client.src.components.square import Square


class Board:
    def __init__(self):
        self.squares = [[Square(row, col) for col in range(8)] for row in range(8)]
    
    def copy(self):
        # create new instance of Board class
        new_board = Board()

        # copy state of each square to new board
        for row in range(8):
            for col in range(8):
                new_board.squares[row][col].set_piece(self.squares[row][col].get_piece())
            
        return new_board