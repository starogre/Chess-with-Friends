from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.has_moved = False
    

    @abstractmethod
    def move_piece(self, new_position):
        self.position = new_position
        self.has_moved = True
