from abc import ABC, abstractmethod

def is_in_bounds(board_size, x, y):
        return 0 <= x < board_size and 0 <= y < board_size

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
    def find_moves(self, board):
        moves = []
        board_size = len(board.squares)
        x = self.position[0]
        y = self.position[1]

        landingSquares = [[x - 2, y - 1], [x - 2, y + 1], [x - 1, y -2], [x - 1, y + 2],
                          [x + 1, y - 2], [x + 1, y + 2], [x + 2, y - 1], [x + 2, y + 1]]

        for move in landingSquares:
            new_x, new_y = move

            if is_in_bounds(board_size, new_x, new_y):
                square = board.squares[new_x][new_y]
                target_piece = square.get_piece()

                if target_piece and target_piece.color == self.color:
                    continue

                moves.append([new_x, new_y])

        return moves


class Rook(ChessPiece):
    def find_moves(self, board):
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
            next_piece = board.squares[up][x].get_piece()  # create a global board variable to use here
            if next_piece:
                if next_piece.color != self.color:
                    moves.append([up, x])
                    break
                elif next_piece.color == self.color:
                    break
            moves.append([up, x])
        while down > 0:
            down -= 1
            next_piece = board.squares[down][x].get_piece()
            if next_piece:
                if next_piece.color != self.color:
                    moves.append([down, x])
                    break
                elif next_piece.color == self.color:
                    break
            moves.append([down, x])
        while right < board_size - 1:
            right += 1
            next_piece = board.squares[y][right].get_piece()
            if next_piece:
                if next_piece.color != self.color:
                    moves.append([y, right])
                    break
                elif next_piece.color == self.color:
                    break
            moves.append([y, right])
        while left > 0:
            left -= 1
            next_piece = board.squares[y][left].get_piece()
            if next_piece:
                if next_piece.color != self.color:
                    moves.append([y, left])
                    break
                elif next_piece.color == self.color:
                    break
            moves.append([y, left])

        return moves


class Queen(ChessPiece):
    def find_moves(self):
        # return result of algo to pass to state handler to check valid moves for Queen
        pass


class King(ChessPiece):
    def find_moves(self):
        # return result of algo to pass to state handler to check valid moves for King
        pass
