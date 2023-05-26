
from client.src.components.state_handler import StateHandler

from game_controller import GameController


gc = GameController()
gc.start_game()

# test no last move
# grab a white pawn on right edge of board
pawn_white_z = gc.board.squares[6][1].get_piece()
pawn_white_x = gc.board.squares[4][4].get_piece()
print(pawn_white_x)
# print all moves white pawn can make
print("white pawn #1 can attack a pawn diagonal left, move up one space, or en passant to right:")
print(pawn_white_z.find_moves(gc.board))

# grab a white pawn and move it up 3 spaces
pawn_white = gc.board.squares[6][2].get_piece()
gc.board.squares[3][2].set_piece(pawn_white)
pawn_white.position[0] = 3
pawn_white.position[1] = 2
pawn_white.has_moved = True

# grab a second white pawn
pawn_white2 = gc.board.squares[6][6].get_piece()

# grab a couple black pawns to sides of white pawn
pawn_black_left = gc.board.squares[1][1].get_piece()
pawn_black_right = gc.board.squares[1][3].get_piece()

# grab a third black pawn
pawn_black3 = gc.board.squares[1][5].get_piece()
# grab a black bishop and move it to block 3rd black pawn
bishop_black = gc.board.squares[0][6].get_piece()
gc.board.squares[3][5].set_piece(bishop_black)
bishop_black.position[0] = 3
bishop_black.position[1] = 5

# test left pawn en passant
# gc.board.squares[3][1].set_piece(pawn_black_left)
# pawn_black_left.position[0] = 3
# pawn_black_left.position[1] = 1
# cur_pos_left = pawn_black_left.get_position()
# StateHandler.last_move = (pawn_black_left, cur_pos_left[0], cur_pos_left[1])
# last_move = StateHandler.last_move
# pawn_black_left.moved_two_spaces = True

# test right pawn en passant
gc.board.squares[3][3].set_piece(pawn_black_right)
pawn_black_right.position[0] = 3
pawn_black_right.position[1] = 3
cur_pos_right = pawn_black_right.get_position()
StateHandler.last_move = (pawn_black_right, cur_pos_right[0], cur_pos_right[1])
last_move = StateHandler.last_move
pawn_black_right.moved_two_spaces = True

# diagonal left attack test white pawn attack left black pawn (don't use at same time as left en passant test)
gc.board.squares[2][1].set_piece(pawn_black_right)
pawn_black_left.position[0] = 2
pawn_black_left.position[1] = 1

# print all moves white pawn 1 can make
print("white pawn #1 can attack a pawn diagonal left, move up one space, or en passant to right:")
print(pawn_white.find_moves(gc.board, last_move))

# print all moves white pawn 2 can make
print("white pawn #2 can move up 1 or 2 spaces because it hasn't moved yet:")
print(pawn_white2.find_moves(gc.board, last_move))

# print all moves black pawn 3 can make
print("black pawn #3 can move down 1 space because there is a bishop blocking its second space move:")
print(pawn_black3.find_moves(gc.board, last_move))

