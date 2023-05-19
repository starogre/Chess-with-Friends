from client.src.components.square import Square


class Board:
    def __init__(self):
        self.squares = [[Square(row, col) for col in range(8)] for row in range(8)]