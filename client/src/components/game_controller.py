from state_handler import StateHandler
from board import Board


class GameController:
    def __init__(self):
        self.board = None

    def start_game(self):
        self.board = Board()

        StateHandler.setup_chess_pieces(self.board)


