from unittest.mock import Mock, MagicMock

from client.src.components.state_handler import *
from client.src.components.board import *


def test_knight_init():
    piece = Knight("White", (1, 1))
    assert piece.color == "White"
    assert piece.position == (1, 1)
    assert piece.has_moved == False

    piece.move_piece((2, 2))
    assert piece.position == (2, 2)
    assert piece.has_moved == True


def test_knight_find_moves_empty_board():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    knight = Knight("White", (4, 4))
    expected_moves = [[2, 3], [2, 5], [3, 2], [3, 6], [5, 2], [5, 6], [6, 3], [6, 5]]
    assert knight.find_moves(board) == expected_moves


def test_knight_find_moves_full_board_allied_pieces():
    board = Board()

    for row in board.squares:
        for square in row:
            # all squares occupied by an allied knight
            square.set_piece(Knight("White", (square.row, square.col)))

    expected_moves = []
    knight = Knight("White", (4, 4))
    assert knight.find_moves(board) == expected_moves
    knight = Knight("White", (0, 0))
    assert knight.find_moves(board) == expected_moves
    knight = Knight("White", (8, 8))
    assert knight.find_moves(board) == expected_moves


def test_knight_find_moves_with_enemy_pieces():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    # setup enemy pieces on the knights landing squares
    board.squares[2][3].set_piece(Knight("Black", (2, 3)))
    board.squares[6][5].set_piece(Knight("Black", (2, 5)))
    board.squares[6][5].set_piece(Knight("Black", (3, 2)))
    board.squares[6][5].set_piece(Knight("Black", (3, 6)))
    board.squares[6][5].set_piece(Knight("Black", (5, 2)))

    knight = Knight("White", (4, 4))
    expected_moves = [[2, 3], [2, 5], [3, 2], [3, 6], [5, 2], [5, 6], [6, 3], [6, 5]]
    assert knight.find_moves(board) == expected_moves


def test_knight_find_moves_from_corners_and_edges():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    knight = Knight("White", (0, 0))
    expected_moves = [[1, 2], [2, 1]]
    assert knight.find_moves(board) == expected_moves

    knight = Knight("White", [0, 7])
    expected_moves = [[1, 5], [2, 6]]
    assert knight.find_moves(board) == expected_moves

    knight = Knight("White", [7, 0])
    expected_moves = [[5, 1], [6, 2]]
    assert knight.find_moves(board) == expected_moves

    knight = Knight("White", [7, 7])
    expected_moves = [[5, 6], [6, 5]]
    assert knight.find_moves(board) == expected_moves

    knight = Knight("White", (4, 0))
    expected_moves = [[2, 1], [3, 2], [5, 2], [6, 1]]
    assert knight.find_moves(board) == expected_moves
