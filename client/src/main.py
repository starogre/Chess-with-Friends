import state_handler
import game_controller

# game loop
game_over = False

# constants
ROW_COUNT = 8  # use to initialize chess board
COL_COUNT = 8

while not game_over:
    pass
    # event handlers for GUI
    # game loop
    # start game, create chess board, fill pieces

gc = GameController(board, player1, player2)
gc.start_game()