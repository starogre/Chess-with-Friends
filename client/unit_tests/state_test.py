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
    square.set_piece(piece)
    square.select()

    StateHandler.select_square(board, square)
    assert square.selected == True

    new_piece = Queen("WHITE", (4, 4))
    new_square = board.squares[4][4]
    new_square.set_piece(new_piece)

    StateHandler.select_square(board, new_square)
    assert square.selected == False
    assert new_square.selected == True

    StateHandler.select_square(board, square)
    assert square.selected == True
    assert new_square.selected == False


def test_get_piece_on_selected_square():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    piece = King("WHITE", (4, 4))
    square = board.squares[4][4]
    square.set_piece(piece)

    assert StateHandler.get_selected_piece_on_square(board) is None

    StateHandler.select_square(board, square)

    assert StateHandler.get_selected_piece_on_square(board) == piece


def test_select_destination():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    row = 3
    col = 4

    assert StateHandler.select_destination(board, 3, 4) == board.squares[3][4]


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
