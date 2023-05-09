from state_handler import *
from board import Board

class GameController:

    def start_game(self):
        board = Board()
        StateHandler.setup_chess_pieces(board)

