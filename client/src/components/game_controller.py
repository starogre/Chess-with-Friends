from client.src.components.state_handler import StateHandler
from client.src.components.board import Board
from client.src.components.player import Player


class GameController:
    def __init__(self):
        self.board = None
        self.players = [Player("WHITE"), Player("BLACK")]
        self.current_player = self.players[0] # set start player

    def start_game(self):
        self.board = Board()
        StateHandler.setup_chess_pieces(self.board)
        self.game_loop()

    def game_loop(self):
        while not self.is_game_over():
            self.display_board()
            self.take_turn()

    def take_turn(self):
        player = self.current_player
        selected_piece = None
        target_square = None

        # player selects a piece and target square
        # interact with UI or CLI
        selected_piece = player.select_piece()
        target_square = player.select_target_square()
            
        pass

    def switch_players(self):
        # switch to next player for next turn
        self.current_player = self.players[(self.players.index(self.current_player) + 1) % len(self.players)]
        pass

    def is_game_over(self):
        # check if stalemate or checkmate or game is quit
        pass

    def display_board(self):
        # logic to display current state of board
        # UI or printed output
        pass
