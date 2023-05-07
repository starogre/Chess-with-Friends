from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.has_moved = False

    def move_piece(self, new_position):
        self.position = new_position
        self.has_moved = True

    @abstractmethod
    def find_moves(self):
        # should this do anything in base class?
        pass


class Pawn(ChessPiece):
    def find_moves(self):
        # return result of algo to pass to state handler to check valid moves for Pawn
        pass


class Bishop(ChessPiece):
    def find_moves(self):
        # return result of algo to pass to state handler to check valid moves for Bishop
        pass


class Knight(ChessPiece):
    def find_moves(self):
        # return result of algo to pass to state handler to check valid moves for Knight
        pass


class Rook(ChessPiece):
    def find_moves(self):
        # return result of algo to pass to state handler to check valid moves for Rook

        # returns moves NOT accounting for other pieces on board. just the "shape" of movement of the piece.
        # not sure if we should check that here or elsewhere, since some movement is more complex than just a shape
        # for example, pawns, castling, etc.

        # assuming self.position is [x,y] coord:
        moves = []
        board_size = 8
        x = self.position[0]
        y = self.position[1]
        up = y
        down = y
        left = x
        right = x
        while up < board_size - 1:
            up += 1
            moves.append([x, up])
        while down > 0:
            down -= 1
            moves.append([x, down])
        while right < board_size - 1:
            right += 1
            moves.append([right, y])
        while left > 0:
            left -= 1
            moves.append([left, down])

        return moves


class Queen(ChessPiece):
    def find_moves(self):
        # return result of algo to pass to state handler to check valid moves for Queen
        pass


class King(ChessPiece):
    def find_moves(self):
        # return result of algo to pass to state handler to check valid moves for King
        pass
