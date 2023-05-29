from client.src.components.state_handler import *
from client.src.components.board import *
from client.src.components.player import *


def test_select_piece():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    piece = King("WHITE", (0, 0))
    square = board.squares[0][0]
    square.select()
    square.set_piece(piece)

    assert StateHandler.select_piece(board, square) == True

    new_square = board.squares[4][4]

    assert StateHandler.select_piece(board, new_square) == False

    new_square.select()

    assert StateHandler.select_piece(board, new_square) == True
    assert StateHandler.select_piece(board, square) == False


def test_select_destination():
    pass


def test_find_all_player_moves():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    piece1 = Rook("WHITE", (0, 0))
    piece2 = Rook("WHITE", (7, 7))
    board.squares[0][0].set_piece(piece1)
    board.squares[7][7].set_piece(piece2)

    player = Player("WHITE")

    expected_all_moves = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],
                          [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],
                          [6, 7], [5, 7], [4, 7], [3, 7], [2, 7], [1, 7], [0, 7],
                          [7, 6], [7, 5], [7, 4], [7, 3], [7, 2], [7, 1], [7, 0]]

    assert StateHandler.find_all_player_moves(board, player) == expected_all_moves


def test_find_all_enemy_moves():
    pass


def test_move_is_valid():
    pass


def test_is_capture():
    pass


def test_pawn_moved_two():
    pass


def test_set_last_move():
    pass


def test_check():
    board = Board()
    king = King("WHITE", (0, 0))


def test_checkmate():
    pass


def test_stalemate():
    pass


def test_execute_move():
    pass


def test_update_state():
    pass
