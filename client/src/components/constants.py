import pygame

# Chess settings
ROW_COUNT = 8
COL_COUNT = 8
CHESS_PIECES = {"pawn": 1, "bishop": 2, "knight": 3, "rook": 4, "queen": 5, "king": 6, None: 0}
START_PIECES = [[4, 3, 2, 5, 6, 2, 3, 4],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [4, 3, 2, 5, 6, 2, 3, 4]]

PAWN_BLACK = pygame.image.load('assets/pawn_black.png')

# Knight, Pawn, King, MOVE1 = 1, MOVE2 = 2
UP1 = 1
DOWN1 = 1
LEFT1 = 1
RIGHT1 = 1
UP2 = 2
DOWN2 = 2
LEFT2 = 2
RIGHT2 = 2

# Graphics / GUI values?
SQUARE_SIZE = 80
CHESSFPS = 60

# Sound FX frequencies
BEEP1 = 880
BEEP2 = 659
BEEP3 = 554
BEEP4 = 440


# COLORS (r, g, b)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGRAY = (40, 40, 40)
LIGHTGRAY = (100, 100, 100)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
BLUE = (0, 0, 255)
DARKBLUE = (0, 0, 155)
RED = (255, 0, 0)
DARKRED = (155, 0, 0)
YELLOW = (255, 255, 0)
DARKYELLOW = (155, 155, 0)
BGCOLOR = DARKGRAY




# Program settings
FPS = 60
WIDTH = 640
HEIGHT = 640
TITLE = "Chess Game"
# Game size
# Animation speed