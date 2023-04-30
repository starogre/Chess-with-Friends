class Player:
    def __init__(self, color, turn, label):
        self.color = color
        self.turn = turn
        self.label = label

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_turn(self, turn):
        self.turn = turn

    def get_turn(self):
        return self.turn

    def set_label(self, label):
        self.label = label

    def get_label(self):
        return self.label

