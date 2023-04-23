from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self.color = color
        self.position = position

    @abstractmethod
    def generate_possible_moves(self):
        pass
