class Player:
    def __init__(self, color, active, captured_pieces=None):
        self.color = color
        self.active = active
        self.captured_pieces = captured_pieces

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_active(self, active):
        self.active = active

    def get_active(self):
        return self.active

    def get_pieces(self):
        return self.captured_pieces

