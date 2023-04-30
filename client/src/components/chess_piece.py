from abc import ABC, abstractmethod

class ChessPiece(ABC):
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.has_moved = False
    

    @abstractmethod
    def move_piece(self, new_position):
        self.position = new_position
        self.has_moved = True

class Rook(ChessPiece):
    def __init__(self):
        ChessPiece.__init__(self)

    def find_moves(self):
        # return result of algo to pass to state handler to check valid moves for Rook
        pass

class Pawn(ChessPiece):
    def __init__(self):
        ChessPiece.__init__(self)

class Bishop(ChessPiece):
    def __init__(self):
        ChessPiece.__init__(self)

class Knight(ChessPiece):
    def __init__(self):
        ChessPiece.__init__(self)

class Queen(ChessPiece):
    def __init__(self):
        ChessPiece.__init__(self)

class King(ChessPiece):
    def __init__(self):
        ChessPiece.__init__(self)

