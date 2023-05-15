from abc import ABC, abstractmethod


def is_in_bounds(board_size, x, y):
    return 0 <= x < board_size and 0 <= y < board_size


def is_enemy_piece(color, target_piece):
    return color != target_piece.color


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
    def find_moves(self, board):
        pass


class Pawn(ChessPiece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.moved_once = False
        self.moved_two_spaces = False

    def can_en_passant(self, board, target_row, target_col):
        pass

    def find_moves(self, board):
        # return result of algo to pass to state handler to check valid moves for Pawn
        moves = []
        board_size = len(board.squares)
        x = self.position[0]
        y = self.position[1]
        up = y
        down = y
        left = x
        right = x
        en_passant = [0, 0]  # [left flag, right flag]

        # add more directions if we add more players, etc
        if self.color == "white":
            direction = "up"
        elif self.color == "black":
            direction = "down"

        if not self.has_moved:
            if direction == "up":  # white piece
                for i in range(2):
                    up += 1
                    if is_in_bounds(board_size, up, x):
                        next_piece = board.squares[up][x].get_piece()
                        if next_piece:
                            if next_piece.color != self.color:
                                moves.append([up, x])
                                break
                            elif next_piece.color == self.color:
                                break
                        moves.append([up, x])
            elif direction == "down":  # black piece
                for i in range(2):
                    down -= 1
                    if is_in_bounds(board_size, down, x):
                        next_piece = board.squares[down][x].get_piece()
                        if next_piece:
                            if next_piece.color != self.color:
                                moves.append([down, x])
                                break
                            elif next_piece.color == self.color:
                                break
                        moves.append([down, x])
        else:
            if direction == "up":  # white piece
                up += 1
                if is_in_bounds(board_size, up, x):
                    next_piece = board.squares[up][x].get_piece()
                    if next_piece and next_piece.color != self.color:
                        moves.append([up, x])

                if en_passant[0] == 1:  # ep left
                    if is_in_bounds(board_size, y, left):
                        next_piece = board.squares[y][left].get_piece()
                        if next_piece and next_piece.color != self.color:
                            moves.append([y, left])
                if en_passant[1] == 1:  # ep right
                    if is_in_bounds(board_size, y, right):
                        next_piece = board.squares[y][right].get_piece()
                        if next_piece and next_piece.color != self.color:
                            moves.append([y, right])
            elif direction == "down":  # black piece
                down -= 1
                if is_in_bounds(board_size, down, x):
                    next_piece = board.squares[down][x].get_piece()
                    if next_piece and next_piece.color != self.color:
                        moves.append([down, x])

                if en_passant[0] == 1:  # ep left
                    if is_in_bounds(board_size, y, left):
                        next_piece = board.squares[y][left].get_piece()
                        if next_piece and next_piece.color != self.color:
                            moves.append([y, left])
                if en_passant[1] == 1:  # ep right
                    if is_in_bounds(board_size, y, right):
                        next_piece = board.squares[y][right].get_piece()
                        if next_piece and next_piece.color != self.color:
                            moves.append([y, right])


class Bishop(ChessPiece):
    def find_moves(self, board):
        # return result of algo to pass to state handler to check valid moves for Bishop
        pass


class Knight(ChessPiece):
    def find_moves(self, board):
        moves = []
        board_size = len(board.squares)
        x, y = self.position

        landing_squares = [[x - 2, y - 1], [x - 2, y + 1], [x - 1, y - 2], [x - 1, y + 2],
                           [x + 1, y - 2], [x + 1, y + 2], [x + 2, y - 1], [x + 2, y + 1]]

        for move in landing_squares:
            new_y, new_x = move

            if is_in_bounds(board_size, new_y, new_x):
                square = board.squares[new_y][new_x]
                target_piece = square.get_piece()

                if target_piece and target_piece.color == self.color:
                    continue

                moves.append([new_y, new_x])

        return moves


class Rook(ChessPiece):
    def find_moves(self, board):
        moves = []
        board_size = len(board.squares)
        x = self.position[0]
        y = self.position[1]
        up = y
        down = y
        left = x
        right = x
        while up < board_size - 1:
            up += 1
            next_piece = board.squares[up][x].get_piece()
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
    def find_moves(self, board):
        # return result of algo to pass to state handler to check valid moves for Queen
        pass


class King(ChessPiece):
    def find_moves(self, board):
        # return result of algo to pass to state handler to check valid moves for King
        pass
