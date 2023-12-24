from client.src.components.state_handler import StateHandler
from client.src.components.board import Board
from client.src.components.player import Player
from client.src.components.user_interface import UserInterface as ui


class GameController:
    def __init__(self):
        self.ui = ui()
        self.active_player, self.inactive_player = StateHandler.setup_players()
        self.start_game()
        

    def start_game(self):
        self.board = Board()

        StateHandler.setup_chess_board(self.board)
        self.game_loop()

    def game_loop(self):
        
        while not self.is_game_over():
            # display game board
            self.ui.display_board(self.board, self.active_player)
            # Show current player's turn
            print(f"{self.active_player.color}'s turn.")
            # logic to prompt user to select piece
            piece_select = ui.get_user_input(self, "Select a piece (e.g. 'A2'): ")
            # convert input into coordinates or piece representation
            position = StateHandler.convert_to_coordinates(piece_select, self.active_player)
            print(f"Selected piece coordinates: {position}")
            
            self.take_turn(position)

    def take_turn(self, position):

        selected_position = position
        target_square = None


        # player selects a piece and target square
        # interact with UI or CLI
        
        StateHandler.select_square(self.board, selected_position)
        selected_piece = StateHandler.get_selected_piece_on_square(self.board)
        
        if selected_piece is not None:
            print(f"Selected piece: {selected_piece}")
        else:
            print("No piece found at the selected coordinates.")    

        target_square = self.ui.select_target_square()
        
        self.active_player, self.inactive_player = self.inactive_player, self.active_player


    def is_game_over(self):
        # check if stalemate or checkmate or game is quit
        pass

    