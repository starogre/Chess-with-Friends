from board import Board
from square import Square
from chess_piece import *
from state_handler import StateHandler
from game_controller import GameController

gc = GameController()
gc.start_game()

pawn_white = gc.board.squares[6][2].get_piece()
gc.board.squares[3][2].set_piece(pawn_white)
pawn_white.position[0] = 3
pawn_white.position[1] = 2
pawn_white.has_moved = True

pawn_black_left = gc.board.squares[1][1].get_piece()
pawn_black_right = gc.board.squares[1][3].get_piece()

gc.board.squares[3][1].set_piece(pawn_black_left)
pawn_black_left.position[0] = 3
pawn_black_left.position[1] = 1
cur_pos = pawn_black_left.get_position()
StateHandler.last_move = (pawn_black_left, cur_pos[0], cur_pos[1])
print(StateHandler.last_move)
pawn_black_left.moved_two_spaces = True
pawn_black_left.moved_once = True

print("moved left black pawn and find spaces for white pawn")
print(pawn_white.find_moves(gc.board))



