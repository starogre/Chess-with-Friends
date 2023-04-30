from board import Board
# from square import Square
# from chess_piece import ChessPiece


class StateHandler:
    # validate and execute moves
    # alter board state
    # fill up squares with pieces
    # used by game controller to manage Game flow, player turn, extend to gui??

    def __init__(self):
        self.selected_piece = None
        self.board = Board()

    def start_pieces(self):
        # fill pieces on chess board at start of game
        pass

    def get_active_player(self):
        # return which players turn it is
        pass

    def select_piece(self):
        # check type of piece and get its board square
        pass

    def move_is_valid(self):
        # check that move is possible
        pass

    def execute_move(self):
        #
        pass

    def update_state(self):
        # update game state after each move
        pass

    def is_in_check(self):
        # check if player is in check
        pass

    def is_checkmate(self):
        # check if a player is in checkmate
        pass

    def print_gui(self):
        # draw ascii board in console
        # request player input and show messages
        # later to become real gui
        # later we can also record moves on the side like chess.com so you can see the different board states?
        pass
