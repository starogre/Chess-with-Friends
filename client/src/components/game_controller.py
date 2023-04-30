# init a statehandler object
# init board (using the state handler)
# init players (also can be a state handler function)


from state_handler import StateHandler
from constants import *
from board import Board

class GameController:
    def __init__(self, win, p1, p2):
        self.player1 = p1
        self.player2 = p2
        self.win = win

    def start_game(self):
        game_state = StateHandler()

    def on_piece_select(self, row, col):
        # logic for selecting a piece
        pass

    def on_destination_select(self, row, col):
        # logic for selecting a valid destination for your piece
        self.change_turn()
        # logic for selecting invalid location

    def change_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    def game_over(self):
        # player wins or loses
        pass


