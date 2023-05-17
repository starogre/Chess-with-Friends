from abc import ABC, abstractmethod

from client.src.components.state_handler import StateHandler


def is_in_bounds(board_size, x, y):
    return 0 <= x < board_size and 0 <= y < board_size


def is_enemy_piece(target_piece, adjacent_piece):
    if target_piece is not None and target_piece.color != adjacent_piece.color:
        return True
    else:
        return False


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
        board_size = len(board.squares)
        if not is_in_bounds(board_size, target_row, target_col):
            return False

        target_piece = board.squares[target_row][target_col].get_piece()

        adjacent_pawn_row = target_row
        left_adjacent_pawn_col = target_col - 1
        right_adjacent_pawn_col = target_col + 1

        left_adjacent_pawn = board.squares[adjacent_pawn_row][left_adjacent_pawn_col].get_piece()
        right_adjacent_pawn = board.squares[adjacent_pawn_row][right_adjacent_pawn_col].get_piece()

        en_passant_directions = []

        if is_enemy_piece(target_piece, left_adjacent_pawn) and isinstance(left_adjacent_pawn, Pawn) \
                and left_adjacent_pawn.moved_once \
                and left_adjacent_pawn.moved_two_spaces:

            last_move = StateHandler.last_move

            # this successfully adds en passant left move without last_move considered --> en_passant_directions.append("left")

            if last_move is not None:
                last_piece, last_target_row, last_target_col = last_move
                if last_piece == left_adjacent_pawn and last_target_row == adjacent_pawn_row \
                        and last_target_col == left_adjacent_pawn_col:
                    en_passant_directions.append("left")

        # temp disabled en passant to right----
        # if isinstance(right_adjacent_pawn, Pawn) and right_adjacent_pawn.moved_once and \
        #         right_adjacent_pawn.moved_two_spaces:
        #     last_move = StateHandler.last_move
        #     if last_move is not None:
        #         last_piece, last_target_row, last_target_col = last_move
        #         if last_piece == right_adjacent_pawn and last_target_row == adjacent_pawn_row \
        #                 and last_target_col == right_adjacent_pawn_col:
        #             en_passant_directions.append("right")

        return tuple(en_passant_directions)

    def find_moves(self, board):
        # return result of algo to pass to state handler to check valid moves for Pawn
        moves = []
        board_size = len(board.squares)
        y = self.position[0]
        x = self.position[1]
        up = y
        down = y
        left = x
        right = x
        en_passant_moves = self.can_en_passant(board, y, x)

        # add more directions if we add more players, etc
        if self.color == "WHITE":
            direction = "up"
        elif self.color == "BLACK":
            direction = "down"

        if not self.has_moved:
            if direction == "up":  # white piece
                for i in range(2):
                    up -= 1
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
                    down += 1
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
                up -= 1
                if is_in_bounds(board_size, up, x):
                    if board.squares[up][x].is_empty():
                        moves.append([up, x])
                    # next_piece = board.squares[up][x].get_piece()
                    # if next_piece and next_piece.color != self.color:
                    #     moves.append([up, x])
                if en_passant_moves:
                    if "left" in en_passant_moves:
                        moves.append([y-1, x-1])
                        print(moves)
                    if "right" in en_passant_moves:
                        moves.append([y+1, x+1])

            elif direction == "down":  # black piece
                down += 1
                if is_in_bounds(board_size, down, x):
                    next_piece = board.squares[down][x].get_piece()
                    if next_piece and next_piece.color != self.color:
                        moves.append([down, x])

                if "left" in en_passant_moves:
                    moves.append([y, x-1])
                if "right" in en_passant_moves:
                    moves.append([y, x+1])

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
