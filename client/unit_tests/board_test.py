from client.src.components.board import Board
from client.src.components.chess_piece import King
import sys
print(sys.path)

def test_board_copy():
    board = Board()
    copied_board = board.copy()

    # ensure they are different instances
    assert board is not copied_board

    # make changes to original board
    board.squares[0][0].set_piece(King("WHITE", (0, 0)))

    # ensure changes are not reflected in copied board
    assert copied_board.squares[0][0].get_piece() is None

    # make changes to copied board
    copied_board.squares[0][0].set_piece(King("BLACK", (0, 0)))
    board.squares[0][0].set_piece(None)
    assert board.squares[0][0].get_piece() is None