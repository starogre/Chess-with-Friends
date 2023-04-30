
from components.game_controller import GameController
import pygame
from components.constants import *
from components.gui import GUI
from components.player import Player


# Program data
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WINTITLE = pygame.display.set_caption(TITLE)
chessgui = GUI(CHESSFPS, WIN, WINTITLE)
player1 = Player("White", 1, "Me")
player2 = Player("Black", 2, "Enemy")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = GameController(WIN, player1, player2)


    # start game, create chess board, fill pieces

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.on_piece_select(row, col)

        chessgui.update_gui()



main()