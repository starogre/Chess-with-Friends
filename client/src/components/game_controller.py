from client.src.components.state_handler import StateHandler
from client.src.components.board import Board
from client.src.components.player import Player
from client.src.components.user_interface import UserInterface as ui


class GameController:
    def __init__(self):
        self.ui = ui()
        self.start_game()

    def start_game(self):
        self.board = Board()

        self.players = [Player("WHITE"), Player("BLACK")]
        self.current_player = self.players[0] # set start player
        StateHandler.setup_chess_board(self.board)
        self.game_loop()

    def game_loop(self):
        while not self.is_game_over():
            self.ui.display_board(self.board, self.current_player)
            self.take_turn()

    def take_turn(self):
        player = self.current_player
        selected_piece = None
        target_square = None

        # Show current player's turn
        print(f"{player.color}'s turn.")
        # player selects a piece and target square
        # interact with UI or CLI
        selected_piece = self.ui.select_piece()
        target_square = self.ui.select_target_square()
        
        self.switch_players()

    def switch_players(self):
        # switch to next player for next turn
        self.current_player = self.players[(self.players.index(self.current_player) + 1) % len(self.players)]
        pass

    def is_game_over(self):
        # check if stalemate or checkmate or game is quit
        pass
