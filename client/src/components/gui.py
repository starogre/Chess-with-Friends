from components.constants import BLACK, ROW_COUNT, DARKGRAY, LIGHTGRAY, SQUARE_SIZE, WIDTH, HEIGHT, TITLE, PAWN_BLACK
import pygame

class GUI:
    # draw things to the window
    # pass in information from board, square, piece, player, state handler, and game controller
    # use that to render graphics

    def __init__(self, fps, win, title):
        self.fps = fps
        self.win = win
        self.title = title

    def draw_board_squares(self, win):
        win.fill(DARKGRAY)
        for row in range(ROW_COUNT):
            for col in range(row % 2, ROW_COUNT, 2):
                pygame.draw.rect(win, LIGHTGRAY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def calc_piece_pos(self, pieces):
        # calculate pieces positions and return x y of where each piece image should render
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw_piece(self, win):
        # loop through board / pieces and draw a given piece on screen at the calculated positions
        win.blit(PAWN_BLACK, (self.x - PAWN_BLACK.get_width() // 2, self.y - PAWN_BLACK.get_height() // 2))

    def draw_game(self, win):
        self.draw_board_squares(win)


    def draw_valid_moves(self, moves):
        # draw dots to hint where you can move a piece after selected
        pass

    def update_gui(self):
        self.draw_game(self.win)
        pygame.display.update()


