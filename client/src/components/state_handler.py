from client.src.components.chess_piece import Pawn, Knight, Bishop, Rook, Queen, King
from client.src.components.player import Player

last_move = None


class StateHandler:
    @staticmethod
    def setup_players():
        player1 = Player("WHITE")
        player2 = Player("BLACK")
        player1.active = True # set white player active first
        return player1, player2
    
    @staticmethod
    def setup_chess_board(board):
        pieces = [
            ['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'k', 'q', 'b', 'n', 'r']
        ]
        # pieces = [
        #     ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        #     ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        #     ['-', '-', '-', '-', '-', '-', '-', '-'],
        #     ['-', '-', '-', '-', '-', '-', '-', '-'],
        #     ['-', '-', '-', '-', '-', '-', '-', '-'],
        #     ['-', '-', '-', '-', '-', '-', '-', '-'],
        #     ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        #     ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        # ]
        StateHandler.setup_board(board, pieces)
    
    @staticmethod
    def setup_board(board, pieces):
        piece_mapping = {
            'P': Pawn,
            'N': Knight,
            'B': Bishop,
            'R': Rook,
            'Q': Queen,
            'K': King
        }
        for row_idx, row in enumerate(reversed(pieces)):
            for col_idx, piece in enumerate(row):
                if piece != '-':
                    piece_color = "WHITE" if piece.isupper() else "BLACK"
                    piece_type = piece.upper()
                    piece_class = piece_mapping[piece_type]
                    adjusted_row = 7 - row_idx
                    adjusted_col = 7 - col_idx
                    board.squares[adjusted_row][adjusted_col].set_piece(piece_class(piece_color, (adjusted_row, adjusted_col)))
                                                                  
    @staticmethod
    def select_square(board, position):
        x, y = position
        square = board.squares[y][x]
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
    def convert_to_coordinates(input_str, active_player):
        # print(f"Input string: {input_str}")

        file_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        file_letter = input_str[0].upper()
        rank_number = int(input_str[1]) - 1  # subtract 1 if needed to Adjust for zero indexing

        # print("File letter:", file_letter)
        # print("Rank number:", rank_number)

        if file_letter in file_mapping and 0 <= rank_number <= 7:
            # print("Inside condition block")
            # print("File index:", file_mapping[file_letter])

            file_index = file_mapping[file_letter]

            # Adjust coordinates based on player's turn
            if active_player.color == 'Black':
                file_index = 7 - file_index
                rank_number = 7 - rank_number

            return file_index, rank_number
        else:
            # Handle invalid input, maybe raise an exception or return None
            return None



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
        reversed_possible_moves = piece.find_moves(board)
        # reverse the moves back to fit with piece algorithms
        possible_moves = [[move[1], move[0]] for move in reversed_possible_moves]
        print("Possible Moves: ", possible_moves)

        if player.color == piece.color:
            for move in possible_moves:
                print("Checking Move:", move)
                if move == [target_row, target_col]:
                    if not isinstance(piece, King):
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
                    else:
                        print("King Move Matches Target Row and Column")
                        # check if it's a valid move for capturing or a regular move
                        target_piece = board.squares[target_row][target_col].get_piece()
                        print("King Target Piece: ", target_piece)
                        if StateHandler.is_capture(piece, target_piece):
                            print("King Move is a capture")
                            # temporarily remove the target piece to check for check condition
                            saved_target_row = target_piece.position[0]
                            saved_target_col = target_piece.position[1]
                            board.squares[target_row][target_col].set_piece(None)

                            # move piece temporarily
                            saved_row = piece.position[0]
                            saved_col = piece.position[1]
                            board.squares[piece.position[0]][piece.position[1]].set_piece(None)
                            board.squares[target_row][target_col].set_piece(piece)
                            temp_king = King(player.color, [target_row, target_col])
                            

                            enemy_moves = StateHandler.find_all_enemy_moves(board, player)
                            print("King's Enemy Moves:", enemy_moves)
                            if not StateHandler.is_check(temp_king, enemy_moves):
                                # print(StateHandler.is_check(temp_king, enemy_moves))
                                print("King Move is valid")
                                print("King Current position", target_row, target_col)
                                return True
                            else:
                                print("King Move puts king in check")
                                # reset board
                                board.squares[saved_row][saved_col].set_piece(piece)
                                board.squares[target_row][target_col].set_piece(None)
                                board.squares[saved_target_row][saved_target_col].set_piece(target_piece)
                                return False
                        else:
                            print("King Move is not a capture")
                            # regular move without capturing
                            # move piece temporarily
                            saved_row = piece.position[0]
                            saved_col = piece.position[1]
                            board.squares[piece.position[0]][piece.position[1]].set_piece(None)
                            board.squares[target_row][target_col].set_piece(piece)
                            temp_king = King(player.color, [target_row, target_col])

                            enemy_moves = StateHandler.find_all_enemy_moves(board, player)
                            print("King Enemy Moves:", enemy_moves)
                            if not StateHandler.is_check(temp_king, enemy_moves):
                                print("King Move is valid")
                                return True
                            else:
                                print("King Move puts king in check")
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
                if king.get_position() == move:
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
    def move_piece(board, piece, row, col, target_row, target_col):
        board.squares[target_col][target_row].set_piece(piece)
        board.squares[row][col].set_piece(None)
        piece.move_piece([target_col, target_row])

    @staticmethod
    def update_state(cls, board, piece, target_row, target_col):
        cls.set_last_move(piece, target_row, target_col)
        cls.pawn_moved_two(piece, target_row)
        # print("piece prev pos: ", piece.position)
        cls.move_piece(board, piece, piece.position[0], piece.position[1], target_row, target_col)
        # board.squares[target_row][target_col].set_piece(piece)
        # print("piece next pos: ", piece.position)

    @staticmethod
    def remove_piece(board, row, col):
        board.squares[row][col].set_piece(None)

    @staticmethod
    def find_king(board, color):
        for row in board.squares:
            for square in row:
                piece = square.get_piece()
                if isinstance(piece, King) and piece.color == color:
                    return piece  # Return the king piece for the given color
        return None  # Return None if the king piece is not found

    @staticmethod
    def execute_move(board, piece, target_row, target_col, player):
        
        player_king = StateHandler.find_king(board, player.color)
        print("EXECUTING...")
        print("Player King: ", player_king, "King Position: ", player_king.get_position())
        print("Moving piece", piece, "Color", piece.color)
        print("Target Row coord", target_row)
        print("Target Col coord", target_col)
        print("Player: ", player.color)

        # find target piece
        if board.squares[target_row][target_col].is_empty():
            print("square empty", target_row, target_col)
            target_piece = None
            # let game logic know player should keep attemping to choose space to move to
        else:
            print("get piece from square")
            target_piece = board.squares[target_row][target_col].get_piece()

        if StateHandler.move_is_valid(board, piece, target_row, target_col, player, player_king):
            print("Move is valid")
            # checks for is_check are in move_is valid (so player can't put themselves in check), add is_stalemate, is_checkmate later
            if StateHandler.is_capture(piece, target_piece):
                # remove target piece, remove target piece from players pieces, etc (need to also add player pieces inventory for UI)
                StateHandler.remove_piece(board, target_row, target_col)
            print("Updating board state...")
            StateHandler.update_state(StateHandler, board, piece, target_row, target_col)
            # move succeeded so game logic should carry out next steps
            return True
        else:
            # move isn't valid, player should try again
            print("Execute failed, move not valid")
            return False
