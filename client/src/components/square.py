class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        self.selected = False

    def get_selected(self):
        return self.selected

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def set_piece(self, piece):
        self.piece = piece

    def get_piece(self):
        return self.piece

    def is_empty(self):
        return self.piece is None
