class Square:
    def __init__(self, piece=None):
        self.piece = piece

    def set_piece(self, piece):
        self.piece = piece

    def get_piece(self):
        return self.piece

    def is_empty(self):
        return self.piece is None
