from unittest.mock import Mock, MagicMock

from client.src.components.state_handler import *
from client.src.components.board import *


def test_pawn_init():
    piece = Pawn("White", (1, 1))
    assert piece.color == "White"
    assert piece.position == (1, 1)
    assert piece.has_moved == False
    assert piece.moved_two_spaces == False

    piece.move_piece((2, 2))
    assert piece.position == (2, 2)
    assert piece.has_moved == True


def test_pawn_find_moves_empty_board():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    # pawn first move 1 or 2
    pawn = Pawn("WHITE", (6, 1))
    expected_moves = [[5, 1], [4, 1]]
    assert pawn.find_moves(board) == expected_moves

    # pawn has moved already
    pawn.has_moved = True
    pawn.move_piece((4, 1))
    expected_moves = [[3, 1]]
    assert pawn.find_moves(board) == expected_moves


def test_pawn_find_moves_full_board_allied_pieces():
    board = Board()

    for row in board.squares:
        for square in row:
            # all squares occupied by allied pawns
            square.set_piece(Pawn("WHITE", (square.row, square.col)))

    expected_moves = []
    pawn = Pawn("WHITE", (4, 4))
    assert pawn.find_moves(board) == expected_moves
    pawn = Pawn("WHITE", (0, 0))
    assert pawn.find_moves(board) == expected_moves
    pawn = Pawn("WHITE", (8, 8))
    assert pawn.find_moves(board) == expected_moves


def test_pawn_find_moves_enemy_pieces_white():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    # setup enemy pieces on the pawns landing squares
    board.squares[4][0].set_piece(Pawn("BLACK", (4, 0)))
    board.squares[5][1].set_piece(Pawn("BLACK", (5, 1)))
    board.squares[3][4].set_piece(Pawn("BLACK", (3, 4)))
    board.squares[3][3].set_piece(Pawn("BLACK", (3, 3)))
    board.squares[3][5].set_piece(Pawn("BLACK", (3, 5)))

    # pawn hasn't moved yet
    pawn = Pawn("WHITE", (6, 0))
    expected_moves = [[5, 1], [5, 0]]
    assert pawn.find_moves(board) == expected_moves

    # pawn moved already, can't move up but can attack diagonally
    pawn = Pawn("WHITE", (4, 4))
    pawn.has_moved = True
    expected_moves = [[3, 3], [3, 5]]
    assert pawn.find_moves(board) == expected_moves


def test_pawn_find_moves_enemy_pieces_black():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    # setup enemy pieces on the pawns landing squares
    board.squares[3][0].set_piece(Pawn("WHITE", (3, 0)))
    board.squares[2][1].set_piece(Pawn("WHITE", (2, 1)))
    board.squares[4][3].set_piece(Pawn("WHITE", (4, 3)))
    board.squares[4][4].set_piece(Pawn("WHITE", (4, 4)))
    board.squares[4][5].set_piece(Pawn("WHITE", (4, 5)))

    # pawn hasn't moved yet
    pawn = Pawn("BLACK", (1, 0))
    expected_moves = [[2, 1], [2, 0]]
    assert pawn.find_moves(board) == expected_moves

    # pawn moved already, can't move up but can attack diagonally
    pawn = Pawn("BLACK", (3, 4))
    pawn.has_moved = True
    expected_moves = [[4, 3], [4, 5]]
    assert pawn.find_moves(board) == expected_moves


def test_pawn_corners_and_edges():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    # assume pawn has moved already
    pawn = Pawn("WHITE", (0, 0))
    pawn.has_moved = True
    expected_moves = []
    assert pawn.find_moves(board) == expected_moves

    pawn = Pawn("WHITE", [0, 7])
    pawn.has_moved = True
    expected_moves = []
    assert pawn.find_moves(board) == expected_moves

    pawn = Pawn("WHITE", [7, 0])
    pawn.has_moved = True
    expected_moves = [[6, 0]]
    assert pawn.find_moves(board) == expected_moves

    pawn = Pawn("WHITE", [7, 7])
    pawn.has_moved = True
    expected_moves = [[6, 7]]
    assert pawn.find_moves(board) == expected_moves

    pawn = Pawn("WHITE", (4, 0))
    pawn.has_moved = True
    expected_moves = [[3, 0]]
    assert pawn.find_moves(board) == expected_moves


def test_pawn_en_passant_white():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    pawn = Pawn("WHITE", (3, 2))
    pawn.has_moved = True

    # create an enemy pawn that has moved 2 spaces next to our pawn on left
    pawn_enemy = Pawn("BLACK", (3, 1))
    board.squares[3][1].set_piece(pawn_enemy)
    pawn_enemy.has_moved = True
    pawn_enemy.moved_two_spaces = True

    # our pawn can en passant to left diagonal or move up 1
    game_last_move = (pawn_enemy, 3, 1)
    expected_moves = [[2, 2], [2, 1]]
    assert pawn.find_moves(board, game_last_move) == expected_moves

    # create an enemy pawn that has moved 2 spaces next to our pawn on right
    pawn_enemy = Pawn("BLACK", (3, 3))
    board.squares[3][3].set_piece(pawn_enemy)
    pawn_enemy.has_moved = True
    pawn_enemy.moved_two_spaces = True

    # our pawn can en passant to right diagonal or move up 1
    game_last_move = (pawn_enemy, 3, 3)
    expected_moves = [[2, 2], [2, 3]]
    assert pawn.find_moves(board, game_last_move) == expected_moves


def test_pawn_en_passant_black():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    pawn = Pawn("BLACK", (4, 5))
    pawn.has_moved = True

    # create an enemy pawn that has moved 2 spaces next to our pawn on left
    pawn_enemy = Pawn("WHITE", (4, 4))
    board.squares[4][4].set_piece(pawn_enemy)
    pawn_enemy.has_moved = True
    pawn_enemy.moved_two_spaces = True

    # our pawn can en passant to left diagonal or move up 1
    game_last_move = (pawn_enemy, 4, 4)
    expected_moves = [[5, 5], [5, 4]]
    assert pawn.find_moves(board, game_last_move) == expected_moves

    # create an enemy pawn that has moved 2 spaces next to our pawn on right
    pawn_enemy = Pawn("WHITE", (4, 6))
    board.squares[4][6].set_piece(pawn_enemy)
    pawn_enemy.has_moved = True
    pawn_enemy.moved_two_spaces = True

    # our pawn can en passant to right diagonal or move up 1
    game_last_move = (pawn_enemy, 4, 6)
    expected_moves = [[5, 5], [5, 6]]
    assert pawn.find_moves(board, game_last_move) == expected_moves


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
    board.squares[2][5].set_piece(Knight("Black", (2, 5)))
    board.squares[3][2].set_piece(Knight("Black", (3, 2)))
    board.squares[3][6].set_piece(Knight("Black", (3, 6)))
    board.squares[5][2].set_piece(Knight("Black", (5, 2)))
    board.squares[5][6].set_piece(Knight("Black", (5, 6)))
    board.squares[6][3].set_piece(Knight("Black", (6, 3)))
    board.squares[6][5].set_piece(Knight("Black", (6, 5)))

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


def test_rook_init():
    piece = Rook("White", (1, 1))
    assert piece.color == "White"
    assert piece.position == (1, 1)
    assert piece.has_moved == False

    piece.move_piece((2, 2))
    assert piece.position == (2, 2)
    assert piece.has_moved == True


def test_rook_find_moves_empty_board():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    rook = Rook("White", (4, 4))
    expected_moves = [[2, 3], [2, 5], [3, 2], [3, 6], [5, 2], [5, 6], [6, 3], [6, 5]]
    assert rook.find_moves(board) == expected_moves


def test_rook_find_moves_full_board_allied_pieces():
    board = Board()

    for row in board.squares:
        for square in row:
            # all squares occupied by an allied rook
            square.set_piece(Rook("White", (square.row, square.col)))

    expected_moves = []
    rook = Rook("White", (4, 4))
    assert rook.find_moves(board) == expected_moves
    rook = Rook("White", (0, 0))
    assert rook.find_moves(board) == expected_moves
    rook = Rook("White", (8, 8))
    assert rook.find_moves(board) == expected_moves


def test_rook_find_moves_with_enemy_pieces():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    # setup enemy pieces on the knights landing squares
    board.squares[2][3].set_piece(Rook("Black", (2, 3)))
    board.squares[2][5].set_piece(Rook("Black", (2, 5)))
    board.squares[3][2].set_piece(Rook("Black", (3, 2)))
    board.squares[3][6].set_piece(Rook("Black", (3, 6)))
    board.squares[5][2].set_piece(Rook("Black", (5, 2)))
    board.squares[5][6].set_piece(Rook("Black", (5, 6)))
    board.squares[6][3].set_piece(Rook("Black", (6, 3)))
    board.squares[6][5].set_piece(Rook("Black", (6, 5)))

    rook = Rook("White", (4, 4))
    expected_moves = [[2, 3], [2, 5], [3, 2], [3, 6], [5, 2], [5, 6], [6, 3], [6, 5]]
    assert rook.find_moves(board) == expected_moves


def test_rook_find_moves_from_corners_and_edges():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    rook = Rook("White", (0, 0))
    expected_moves = [[1, 2], [2, 1]]
    assert rook.find_moves(board) == expected_moves

    rook = Rook("White", [0, 7])
    expected_moves = [[1, 5], [2, 6]]
    assert rook.find_moves(board) == expected_moves

    rook = Rook("White", [7, 0])
    expected_moves = [[5, 1], [6, 2]]
    assert rook.find_moves(board) == expected_moves

    rook = Rook("White", [7, 7])
    expected_moves = [[5, 6], [6, 5]]
    assert rook.find_moves(board) == expected_moves

    rook = Rook("White", (4, 0))
    expected_moves = [[2, 1], [3, 2], [5, 2], [6, 1]]
    assert rook.find_moves(board) == expected_moves


def test_king_init():
    piece = King("White", (1, 1))
    assert piece.color == "White"
    assert piece.position == (1, 1)
    assert piece.has_moved == False

    piece.move_piece((2, 2))
    assert piece.position == (2, 2)
    assert piece.has_moved == True


def test_king_find_moves_empty_board():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    king = King("White", (4, 4))
    expected_moves = [[3, 3], [3, 5], [5, 3], [5, 5], [5, 4], [3, 4], [4, 5], [4, 3]]
    assert king.find_moves(board) == expected_moves


def test_king_find_moves_full_board_allied_pieces():
    board = Board()

    for row in board.squares:
        for square in row:
            # all squares occupied by an allied king
            square.set_piece(King("White", (square.row, square.col)))

    expected_moves = []
    king = King("White", (4, 4))
    assert king.find_moves(board) == expected_moves
    king = King("White", (0, 0))
    assert king.find_moves(board) == expected_moves
    king = King("White", (8, 8))
    assert king.find_moves(board) == expected_moves


def test_king_find_moves_with_enemy_pieces():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    # setup enemy pieces on the knights landing squares
    board.squares[3][3].set_piece(King("Black", (3, 3)))
    board.squares[3][5].set_piece(King("Black", (3, 5)))
    board.squares[5][3].set_piece(King("Black", (5, 3)))
    board.squares[5][5].set_piece(King("Black", (5, 5)))
    board.squares[5][4].set_piece(King("Black", (5, 4)))
    board.squares[3][4].set_piece(King("Black", (3, 4)))
    board.squares[4][5].set_piece(King("Black", (4, 5)))
    board.squares[4][3].set_piece(King("Black", (4, 3)))

    king = King("White", (4, 4))
    expected_moves = [[3, 3], [3, 5], [5, 3], [5, 5], [5, 4], [3, 4], [4, 5], [4, 3]]
    assert king.find_moves(board) == expected_moves


def test_king_find_moves_with_corners_and_edges():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    king = King("White", (0, 0))
    expected_moves = [[1, 1], [1, 0], [0, 1]]
    assert king.find_moves(board) == expected_moves

    king = King("White", [0, 7])
    expected_moves = [[1, 6], [1, 7], [0, 6]]
    assert king.find_moves(board) == expected_moves

    king = King("White", [7, 0])
    expected_moves = [[6, 1], [6, 0], [7, 1]]
    assert king.find_moves(board) == expected_moves

    king = King("White", [7, 7])
    expected_moves = [[6, 6], [6, 7], [7, 6]]
    assert king.find_moves(board) == expected_moves

    king = King("White", (4, 0))
    expected_moves = [[3, 1], [5, 1], [5, 0], [3, 0], [4, 1]]
    assert king.find_moves(board) == expected_moves
