from client.src.components.chess_piece import Pawn, Knight, Bishop, Rook, Queen, King
from client.src.components.player import Player

last_move = None


class StateHandler:

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
    def select_square(board, square):
        if not square.is_empty():
            if not square.selected:
                for row in board.squares:
                    for squares in row:
                        squares.deselect()
                square.select()

    @staticmethod
    def get_selected_piece_on_square(board):
        for row in board.squares:
            for squares in row:
                if squares.selected:
                    return squares.get_piece()

    @staticmethod
    def select_destination(board, target_row, target_col):
        return board.squares[target_row][target_col]

    @staticmethod
    def find_all_player_moves(board, player):
        all_moves = []
        flattened_list = []
        for row in board.squares:
            for squares in row:
                piece = squares.get_piece()
                if piece is not None and piece.color == player.color:
                    all_moves.append(piece.find_moves(board))
                    flattened_list = [inner for outer in all_moves for inner in outer]
        return flattened_list

    @staticmethod
    def find_all_enemy_moves(board, player):
        all_moves = []
        for row in board.squares:
            for squares in row:
                piece = squares.get_piece()
                if piece is not None and piece.color != player.color:
                    moves = piece.find_moves(board)
                    all_moves.extend(moves)
        return all_moves

    @staticmethod
    def move_is_valid(board, piece, target_row, target_col, player, player_king):
        possible_moves = piece.find_moves(board)
        print("Possible Moves: ", possible_moves)

        if player.color == piece.color:
            for move in possible_moves:
                print("Checking Move:", move)
                if move == [target_row, target_col]:
                    print("Move Matches Target Row and Column")
                    # check if it's a valid move for capturing or a regular move
                    target_piece = board.squares[target_row][target_col].get_piece()
                    print("Target Piece: ", target_piece)
                    if StateHandler.is_capture(piece, target_piece):
                        print("Move is a capture")
                        # temporarily remove the target piece to check for check condition
                        saved_target_row = target_piece.position[0]
                        saved_target_col = target_piece.position[1]
                        board.squares[target_row][target_col].set_piece(None)

                        # move piece temporarily
                        saved_row = piece.position[0]
                        saved_col = piece.position[1]
                        board.squares[piece.position[0]][piece.position[1]].set_piece(None)
                        board.squares[target_row][target_col].set_piece(piece)

                        enemy_moves = StateHandler.find_all_enemy_moves(board, player)
                        print("Enemy Moves:", enemy_moves)
                        if not StateHandler.is_check(player_king, enemy_moves):
                            print("Move is valid")
                            print("Current position", target_row, target_col)
                            return True
                        else:
                            print("Move puts king in check")
                            # reset board
                            board.squares[saved_row][saved_col].set_piece(piece)
                            board.squares[target_row][target_col].set_piece(None)
                            board.squares[saved_target_row][saved_target_col].set_piece(target_piece)
                            return False
                    else:
                        print("Move is not a capture")
                        # regular move without capturing
                        # move piece temporarily
                        saved_row = piece.position[0]
                        saved_col = piece.position[1]
                        board.squares[piece.position[0]][piece.position[1]].set_piece(None)
                        board.squares[target_row][target_col].set_piece(piece)

                        enemy_moves = StateHandler.find_all_enemy_moves(board, player)
                        print("Enemy Moves:", enemy_moves)
                        if not StateHandler.is_check(player_king, enemy_moves):
                            print("Move is valid")
                            return True
                        else:
                            print("Move puts king in check")
                            # reset temp movements
                            board.squares[saved_row][saved_col].set_piece(piece)
                            board.squares[target_row][target_col].set_piece(None)
                            return False
            print("No matching move found")
        return False

    @staticmethod
    def is_check(king, enemy_moves):
        if isinstance(king, King):
            for move in enemy_moves:
                if king.get_position() == tuple(move):
                    return True
            return False

    @staticmethod
    def make_temporary_move(board, piece, target_row, target_col):
        temp_board = board.copy() # create copy of current board

        original_row, original_col = piece.get_position() # save original position of piece to be moved
        temp_board.squares[original_row][original_col].set_piece(None) # remove piece from original position
        temp_board.squares[target_row][target_col].set_piece(piece) # place piece in new position

        return temp_board


    @staticmethod
    def is_checkmate(cls, board, player, king, enemy_moves):
        if cls.is_check(king, enemy_moves):
            all_player_moves = cls.find_all_player_moves(board, player)
            for move in all_player_moves:
                # simulate move on copy of board
                piece = board.squares[move[0]][move[1]].get_piece()
                if piece and piece.color == player.color:
                    if cls.move_is_valid(board, piece, move[0], move[1], player, king):
                        return False # at least one move resolves check so no checkmate
            
            return True # if no move can resolve check, it's checkmate
        return False # if king isn't in check, no checkmate from start

    @staticmethod
    def is_stalemate(cls, board, king, enemy_moves):
        if not cls.is_check(king, enemy_moves):
            possible_moves = king.find_moves(board)
            no_moves = all(move in enemy_moves for move in possible_moves)
            if no_moves:
                return True
        return False

    @staticmethod
    def is_capture(selected_piece, target_piece):
        if selected_piece and target_piece and selected_piece.color != target_piece.color:
            return True
        return False

    @staticmethod
    def pawn_moved_two(piece, target_row):
        # change state of Pawn if it moved 2 spaces for first move
        if isinstance(piece, Pawn):
            cur_pos = piece.get_position()
            if cur_pos[0] > target_row - 2 and piece.color == "WHITE":
                piece.moved_two_spaces = True
            elif cur_pos[0] < target_row + 2 and piece.color == "BLACK":
                piece.moved_two_spaces = True

    @staticmethod
    def set_last_move(piece, target_row, target_col):
        StateHandler.last_move = (piece, target_row, target_col)

    @staticmethod
    def update_state(cls, board, piece, target_row, target_col, player):
        cls.set_last_move(piece, target_row, target_col)
        cls.pawn_moved_two(piece, target_row)
        piece.move_piece([target_row], [target_col])
        board.squares[target_row][target_col].set_piece(piece)

    @staticmethod
    def execute_move(cls, board, piece, target_row, target_col, player):
        # find target piece
        if board.squares[target_row][target_col].is_empty():
            target_piece = None
        else:
            target_piece = board.squares[target_row][target_col].get_piece()
        if cls.move_is_valid(board, piece, target_row, target_col, player):
            # add checks for is_stalemate, is_check, is_checkmate
            if cls.is_capture(piece, target_piece):
                # remove target piece, remove target piece from players pieces, etc
                pass
            cls.update_state(board, piece, target_row, target_col, player)
