from chess_piece import *


class StateHandler:

    last_move = None

    @staticmethod
    def setup_chess_pieces(board):
        start_white_pieces = [[0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1],
                              [4, 3, 2, 5, 6, 2, 3, 4]]
        start_black_pieces = [[4, 3, 2, 5, 6, 2, 3, 4],
                              [1, 1, 1, 1, 1, 1, 1, 1],
                              [0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0]]
        for i in range(len(board.squares)):
            for j in range(len(board.squares)):
                if start_white_pieces[i][j] == 1:
                    board.squares[i][j].set_piece(Pawn("WHITE", [i, j]))
                if start_black_pieces[i][j] == 1:
                    board.squares[i][j].set_piece(Pawn("BLACK", [i, j]))
                if start_white_pieces[i][j] == 2:
                    board.squares[i][j].set_piece(Bishop("WHITE", [i, j]))
                if start_black_pieces[i][j] == 2:
                    board.squares[i][j].set_piece(Bishop("BLACK", [i, j]))
                if start_white_pieces[i][j] == 3:
                    board.squares[i][j].set_piece(Knight("WHITE", [i, j]))
                if start_black_pieces[i][j] == 3:
                    board.squares[i][j].set_piece(Knight("BLACK", [i, j]))
                if start_white_pieces[i][j] == 4:
                    board.squares[i][j].set_piece(Rook("WHITE", [i, j]))
                if start_black_pieces[i][j] == 4:
                    board.squares[i][j].set_piece(Rook("BLACK", [i, j]))
                if start_white_pieces[i][j] == 5:
                    board.squares[i][j].set_piece(Queen("WHITE", [i, j]))
                if start_black_pieces[i][j] == 5:
                    board.squares[i][j].set_piece(Queen("BLACK", [i, j]))
                if start_white_pieces[i][j] == 6:
                    board.squares[i][j].set_piece(King("WHITE", [i, j]))
                if start_black_pieces[i][j] == 6:
                    board.squares[i][j].set_piece(King("BLACK", [i, j]))

    @staticmethod
    def execute_move(board, piece, target_row, target_col):
        # move_is_valid()
        # is_capture, is_stalemate, is_check, is_checkmate

        # check what last move was
        last_move = (piece, target_row, target_col)

        # change state of Pawn if it moved 2 spaces for first move
        if isinstance(piece, Pawn):
            cur_pos = piece.get_position()
            if cur_pos[0] > target_row - 2 and piece.color == "WHITE":
                piece.moved_two_spaces = True
            elif cur_pos[0] < target_row + 2 and piece.color == "BLACK":
                piece.moved_two_spaces = True

