from abc import ABC, abstractmethod


def is_in_bounds(board_size, x, y):
    return 0 <= x < board_size and 0 <= y < board_size


def is_enemy_piece(selected_piece, target_piece):
    if target_piece is not None and selected_piece.color != target_piece.color:
        return True
    else:
        return False


def is_ally_piece(selected_piece, target_piece):
    if target_piece is not None and selected_piece.color == target_piece.color:
        return True
    else:
        return False


def can_en_passant(board, selected_row, selected_col, last_move):
    if last_move is not None:
        last_piece, last_target_row, last_target_col = last_move

        board_size = len(board.squares)
        if is_in_bounds(board_size, selected_row, selected_col - 1):
            left_piece = board.squares[selected_row][selected_col - 1].get_piece()
            if isinstance(left_piece, Pawn) and left_piece.moved_two_spaces and last_piece == left_piece:
                return True, "left"
        if is_in_bounds(board_size, selected_row, selected_col + 1):
            right_piece = board.squares[selected_row][selected_col + 1].get_piece()
            if isinstance(right_piece, Pawn) and right_piece.moved_two_spaces and last_piece == right_piece:
                return True, "right"

    return False, ""


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
        self.moved_two_spaces = False

    def find_moves(self, board, last_move=None):
        moves = []
        board_size = len(board.squares)
        y = self.position[0]
        x = self.position[1]
        up = y
        down = y
        en_passant_move = can_en_passant(board, y, x, last_move)
        direction = None

        # add more directions if we add more players, etc
        if self.color == "WHITE":
            direction = "up"
        elif self.color == "BLACK":
            direction = "down"

        # diagonal attacks
        if direction == "up":
            move_y, move_x = y - 1, x - 1
            if is_in_bounds(board_size, move_y, move_x):
                if is_enemy_piece(self, board.squares[move_y][move_x].get_piece()):
                    moves.append([move_y, move_x])
            move_y, move_x = y - 1, x + 1
            if is_in_bounds(board_size, move_y, move_x):
                if is_enemy_piece(self, board.squares[move_y][move_x].get_piece()):
                    moves.append([move_y, move_x])
        elif direction == "down":
            move_y, move_x = y + 1, x - 1
            if is_in_bounds(board_size, move_y, move_x):
                if is_enemy_piece(self, board.squares[move_y][move_x].get_piece()):
                    moves.append([move_y, move_x])
            move_y, move_x = y + 1, x + 1
            if is_in_bounds(board_size, move_y, move_x):
                if is_enemy_piece(self, board.squares[move_y][move_x].get_piece()):
                    moves.append([move_y, move_x])

        # moves based on if selected pawn has moved or not already
        if not self.has_moved:
            if direction == "up":
                for i in range(2):  # white piece moving up 1 and 2
                    up -= 1
                    if is_in_bounds(board_size, up, x):
                        if board.squares[up][x].is_empty():
                            moves.append([up, x])
            elif direction == "down":
                for i in range(2):  # black piece moving down 1 and 2
                    down += 1
                    if is_in_bounds(board_size, down, x):
                        if board.squares[down][x].is_empty():
                            moves.append([down, x])
        else:
            if direction == "up":  # white piece moving up 1
                up -= 1
                if is_in_bounds(board_size, up, x):
                    if board.squares[up][x].is_empty():
                        moves.append([up, x])
                # en passant
                if en_passant_move == (True, "left"):
                    moves.append([y - 1, x - 1])
                elif en_passant_move == (True, "right"):
                    moves.append([y - 1, x + 1])

            elif direction == "down":  # black piece moving down 1
                down += 1
                if is_in_bounds(board_size, down, x):
                    if is_in_bounds(board_size, down, x):
                        if board.squares[down][x].is_empty():
                            moves.append([down, x])
                # en passant
                if en_passant_move == (True, "left"):
                    moves.append([y + 1, x - 1])
                elif en_passant_move == (True, "right"):
                    moves.append([y + 1, x + 1])

        return moves


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
    def find_moves(self, board, last_move=None):
        moves = []
        board_size = len(board.squares)
        y, x = self.position

        landing_squares = [[y - 1, x - 1], [y - 1, x + 1], [y + 1, x - 1], [y + 1, x + 1],
                           [y + 1, x], [y - 1, x], [y, x + 1], [y, x - 1]]
        for move in landing_squares:
            new_y, new_x = move
            if is_in_bounds(board_size, new_y, new_x):
                target_piece = board.squares[new_y][new_x].get_piece()
                if target_piece and is_ally_piece(self, board.squares[new_y][new_x].get_piece()):
                    continue
                moves.append([new_y, new_x])

        return moves

