from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.has_moved = False

    def get_position(self):
        return self.position

    def move_piece(self, new_position):
        self.position = new_position
        self.has_moved = True

    @abstractmethod
    def find_moves(self):
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
        moves = []
        board_size = 8  # use some passed in param for this later
        x = self.position[0]
        y = self.position[1]
        up = y
        down = y
        left = x
        right = x
        while up < board_size - 1:
            up += 1
            next_piece = board.squares[x][up].get_piece()  # create a global board variable to use here
            if next_piece:
                if next_piece.color != self.color:
                    moves.append([x, up])
                    break
                elif next_piece.color == self.color:
                    break
            moves.append([x, up])
        while down > 0:
            down -= 1
            next_piece = board.squares[x][down].get_piece()
            if next_piece:
                if next_piece.color != self.color:
                    moves.append([x, down])
                    break
                elif next_piece.color == self.color:
                    break
            moves.append([x, down])
        while right < board_size - 1:
            right += 1
            next_piece = board.squares[right][y].get_piece()
            if next_piece:
                if next_piece.color != self.color:
                    moves.append([right, y])
                    break
                elif next_piece.color == self.color:
                    break
            moves.append([right, y])
        while left > 0:
            left -= 1
            next_piece = board.squares[left][y].get_piece()
            if next_piece:
                if next_piece.color != self.color:
                    moves.append([left, y])
                    break
                elif next_piece.color == self.color:
                    break
            moves.append([left, y])

        return moves


class Queen(ChessPiece):
    def find_moves(self):
        # return result of algo to pass to state handler to check valid moves for Queen
        pass


class King(ChessPiece):
    def find_moves(self):
        # return result of algo to pass to state handler to check valid moves for King
        pass
