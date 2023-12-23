import client.src.components.board as Board

class CommandLineInteraface:
    def __init__(self):
        pass
    
    def display_board(self, board):
        # display current state of board
        pass

    def select_piece(self):
        # logic to prompt user to select piece
        piece_selected = input("Select a piece (e.g. 'A2'): ")
        # convert input into coordinates or piece representation
        return piece_selected
    
    def select_target_square(self):
        # logic to prompt user to select a target square
        target_selected = input("Select a target square (e.g. 'A2'): ")
        # convert input into coordinates or piece representation
        return target_selected