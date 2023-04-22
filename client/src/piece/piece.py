class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def generate_possible_moves(self):
        raise NotImplementedError("This method should be implemented in derived classes.")
