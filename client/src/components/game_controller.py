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
        print(self.board.squares[7][0].get_piece().color)
        print(self.board.squares[0][1].get_piece().color)
        self.game_loop()

    def game_loop(self):
        
        while not self.is_game_over():
            # # testing stuff
            # print(StateHandler.convert_to_coordinates("A1", self.active_player))
            # print(StateHandler.convert_to_coordinates("A2", self.active_player))
            # print(StateHandler.convert_to_coordinates("B1", self.active_player))
            # print(StateHandler.convert_to_coordinates("B2", self.active_player))
            # print(StateHandler.convert_to_coordinates("C1", self.active_player))
            # print(StateHandler.convert_to_coordinates("C2", self.active_player))
            
            # display game board
            self.ui.display_board(self.board, self.active_player)
            # Show current player's turn
            print(f"{self.active_player.color}'s turn.")
            # print(self.board.squares[0][0].get_piece())

            while True:
                # logic to prompt user to select piece
                piece_select = ui.get_user_input(self, "Select a piece (e.g. 'A2'): ")
                # convert input into coordinates or piece representation
                position = StateHandler.convert_to_coordinates(piece_select, self.active_player)
                print(f"Selected piece coordinates: {position}")
                

                StateHandler.select_square(self.board, position)
                selected_piece = StateHandler.get_selected_piece_on_square(self.board)
                print(f"Selected piece: {selected_piece}")
                print(f"Possible moves: {selected_piece.find_moves(self.board)}")

                target_select = ui.get_user_input(self, "Select a space to move to (e.g. 'A2'): ")
                target_position = StateHandler.convert_to_coordinates(target_select, self.active_player)
                print(f"Target position coordinates: {target_position}")

                

                
                if selected_piece is not None:
                    print(f"Selected piece: {selected_piece}")
                    print("Target selected: ", target_select)
                    print("Target position: ", target_position)
                    print("Active player color turn: ", self.active_player.color)
                    # attempt to execute move
                    move_successful = StateHandler.execute_move(self.board, selected_piece, target_position[0], target_position[1], self.active_player)
                
                    if move_successful:
                        # move successful switch players
                        self.active_player, self.inactive_player = self.inactive_player, self.active_player
                        break
                    else:
                        # invalid move, please choose again
                        print("Invalid move. Please choose a valid move.")
                else:
                    # no piece found at selected coords, prompt new input
                    print("No piece found there, choose a different square.")
                
                

    def take_turn(self, position, target):

        selected_position = position
        selected_target = target


        # player selects a piece and target square
        # interact with UI or CLI
        
        StateHandler.select_square(self.board, selected_position)
        selected_piece = StateHandler.get_selected_piece_on_square(self.board)
        

        if selected_piece is not None:
            print(f"Selected piece: {selected_piece}")
        else:
            print("No piece found at the selected coordinates.")    

        # Attempt to execute the move
        move_successful = StateHandler.execute_move(self.board, selected_piece, selected_target[0], selected_target[1], self.active_player, self.active_player.king)

        if move_successful:
            self.active_player, self.inactive_player = self.inactive_player, self.active_player
        else:
            # Invalid move, display a message and allow the player to choose again
            print("Invalid move. Please choose a valid move.")

        


    def is_game_over(self):
        # check if stalemate or checkmate or game is quit
        pass

    