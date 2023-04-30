# init a statehandler object
# init board (using the state handler)
# init players (also can be a state handler function)

# fire a start_game function

class GameController:
    def __init__(self, b, p1, p2):
        self.board = b
        self.player1 = p1
        self.player2 = p2

    def start_game(self):
        # initialize board with pieces on it
        pass

    def on_piece_select(self):
        # event handler when user selects piece
        pass

    def on_destination_select(self):
        # event handler when a user selects destination square for a piece
        pass

    def game_over(self):
        # player wins or loses
        pass


