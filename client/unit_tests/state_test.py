from client.src.components.state_handler import *
from client.src.components.board import *
from client.src.components.player import *

# SELECT SQUARE USES BOARD, POSITION NOW, NOT BOARD, SQUARE
# def test_select_piece():
#     board = Board()

#     for row in board.squares:
#         for square in row:
#             square.set_piece(None)

#     piece = King("WHITE", [0, 0])
#     square = board.squares[0][0]
#     square.set_piece(piece)
#     square.select()

#     StateHandler.select_square(board, square)
#     assert square.selected == True

#     new_piece = Queen("WHITE", [4, 4])
#     new_square = board.squares[4][4]
#     new_square.set_piece(new_piece)

#     StateHandler.select_square(board, new_square)
#     assert square.selected == False
#     assert new_square.selected == True

#     StateHandler.select_square(board, square)
#     assert square.selected == True
#     assert new_square.selected == False


# def test_get_piece_on_selected_square():
#     board = Board()

#     for row in board.squares:
#         for square in row:
#             square.set_piece(None)

#     piece = King("WHITE", (4, 4))
#     square = board.squares[4][4]
#     square.set_piece(piece)

#     assert StateHandler.get_selected_piece_on_square(board) is None

#     StateHandler.select_square(board, square)

#     assert StateHandler.get_selected_piece_on_square(board) == piece


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
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)
    
    piece1 = Rook("BLACK", (0, 0))
    piece2 = Rook("BLACK", (7, 7))
    piece3 = Rook("WHITE", (4, 4))
    board.squares[0][0].set_piece(piece1)
    board.squares[7][7].set_piece(piece2)
    board.squares[4][4].set_piece(piece3)

    player = Player("WHITE")
    
    expected_all_moves = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],
                          [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],
                          [6, 7], [5, 7], [4, 7], [3, 7], [2, 7], [1, 7], [0, 7],
                          [7, 6], [7, 5], [7, 4], [7, 3], [7, 2], [7, 1], [7, 0]]
    
    assert StateHandler.find_all_enemy_moves(board, player) == expected_all_moves


def test_move_is_valid():
    # Set up board
    board = Board()
    state_handler = StateHandler()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    king = King("WHITE", [0, 0])
    queen = Queen("BLACK", [1, 1]) # place queen in position
    king2 = King("BLACK", [7, 7])  
    board.squares[0][0].set_piece(king)
    board.squares[1][1].set_piece(queen)
    board.squares[7][7].set_piece(king2)
    
    player = Player("WHITE")
    player2 = Player("BLACK")

    # Valid move for the king to capture the queen
    is_valid_capture = state_handler.move_is_valid(board, king, 1, 1, player, king)
    assert is_valid_capture is True


    # reset board
    board = Board()
    state_handler = StateHandler()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    king = King("WHITE", [0, 0])
    queen = Queen("BLACK", [1, 1]) # place queen in position
    king2 = King("BLACK", [7, 7])  
    board.squares[0][0].set_piece(king)
    board.squares[1][1].set_piece(queen)
    board.squares[7][7].set_piece(king2)
    
    player = Player("WHITE")
    player2 = Player("BLACK")

    # Valid move for the black queen to move across the board somewhere
    is_regular_move = state_handler.move_is_valid(board, queen, 1, 5, player2, king2)
    assert is_regular_move is True


    # reset board
    board = Board()
    state_handler = StateHandler()

    for row in board.squares:
        for square in row:
            square.set_piece(None)

    king = King("WHITE", [0, 0])
    queen = Queen("BLACK", [1, 1]) # place queen in position
    king2 = King("BLACK", [7, 7])  
    board.squares[0][0].set_piece(king)
    board.squares[1][1].set_piece(queen)
    board.squares[7][7].set_piece(king2)
    
    player = Player("WHITE")
    player2 = Player("BLACK")
    # Invalid move for the king to move to a move in check
    is_valid_regular_move = state_handler.move_is_valid(board, king, 0, 1, player, king)
    assert is_valid_regular_move is False

    # # add more pieces
    # rook = Rook("BLACK", [2, 1]) # place rook in position"
    # board.squares[2][1].set_piece(rook)

    # # Invalid move for the king to move to a position that puts it in check while capturing a piece
    # is_valid_capture_into_check = state_handler.move_is_valid(board, king, 1, 1, player, king)
    # assert is_valid_capture_into_check is False

def test_is_capture():
    state_handler = StateHandler()

    # capture pieces for testing
    white_piece = Pawn("WHITE", (0, 0))
    black_piece = Pawn("BLACK", (1, 1))
    empty_square = None

    # testing when no piece is present in the target square
    is_valid_capture_empty_square = state_handler.is_capture(white_piece, empty_square)
    assert is_valid_capture_empty_square is False

    # testing when the pieces are of different colors (valid capture)
    is_valid_capture = state_handler.is_capture(white_piece, black_piece)
    assert is_valid_capture is True

    # testing when the pieces are of the same color (not a valid capture)
    is_invalid_capture = state_handler.is_capture(white_piece, Pawn("WHITE", (2, 2)))
    assert is_invalid_capture is False



def test_check():
    board = Board()

    for row in board.squares:
        for square in row:
            square.set_piece(None)
    
    # King in check
            
    king_piece = King("WHITE", [3, 0])
    board.squares[3][0].set_piece(king_piece)

    enemy_moves = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],
                   [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],
                   [6, 7], [5, 7], [4, 7], [3, 7], [2, 7], [1, 7], [0, 7],
                   [7, 6], [7, 5], [7, 4], [7, 3], [7, 2], [7, 1], [7, 0]]

    assert StateHandler.is_check(king_piece, enemy_moves) == True

    # King not in check
    king_piece = King("WHITE", (4, 4))
    board.squares[4][4].set_piece(king_piece)

    enemy_moves = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],
                   [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],
                   [6, 7], [5, 7], [4, 7], [3, 7], [2, 7], [1, 7], [0, 7],
                   [7, 6], [7, 5], [7, 4], [7, 3], [7, 2], [7, 1], [7, 0]]

    assert StateHandler.is_check(king_piece, enemy_moves) == False

def test_make_temporary_move():
    board = Board()
    state_handler = StateHandler()

    # create a piece and place it on the board
    piece = King("WHITE", (0, 0))
    board.squares[0][0].set_piece(piece)

    # create temp board and apply move
    temp_board = state_handler.make_temporary_move(board, piece, 1, 0)

    # ensure move was applied to temp board
    assert temp_board.squares[1][0].get_piece() is piece

    # ensure the original board was not modified
    assert board.squares[0][0].get_piece() is piece


def test_checkmate():
    board = Board()
    state_handler = StateHandler()

    king = King("WHITE", (0, 0))
    queen = Queen("BLACK", (1, 1)) # place queen in position
    # rook = Rook("BLACK", (1, 2)) # place rook in position")
    board.squares[0][0].set_piece(king)
    board.squares[1][1].set_piece(queen)
    # board.squares[1][2].set_piece(rook)

    enemy_moves = state_handler.find_all_enemy_moves(board, Player("WHITE"))

    is_checkmate = state_handler.is_checkmate(StateHandler, board, Player("WHITE"), king, enemy_moves)
    # print(state_handler.find_all_enemy_moves(board, Player("WHITE")))
    # print(king.find_moves(board))
    # assert is_checkmate is False

def test_move_piece():
    # create board and specify positions
    board = Board()
    piece = King("WHITE", [0, 0])
    board.squares[0][0].set_piece(piece)

    # define target position to move piece to
    target_row = 1
    target_col = 1

    # store initial position of piece
    initial_position = piece.get_position()

    # move piece to target position using state handler method
    StateHandler.move_piece(board, piece, initial_position[0], initial_position[1], target_row, target_col)

    # Assert piece has moved to target position
    assert piece.position == [1, 1]
    assert board.squares[target_row][target_col].get_piece() is piece
    assert board.squares[initial_position[0]][initial_position[1]].get_piece() is None


def test_update_state():
    board = Board()
    state_handler = StateHandler()

    # set up board and pieces
    for row in board.squares:
        for square in row:
            square.set_piece(None)

    king = King("WHITE", [0, 0])
    queen = Queen("BLACK", [1, 1])
    board.squares[0][0].set_piece(king)
    board.squares[1][1].set_piece(queen)
    player = Player("WHITE")

    # save initial state
    # list comprehension to slice each row into a list of rows, copies of the board.squares list of lists
    initial_state = [row[:] for row in board.squares]
    # execute update_state
    state_handler.update_state(StateHandler, board, king, 1, 1)

    # assertions
    assert board.squares[0][0].get_piece() is None # check if king was removed from old square
    assert board.squares[1][1].get_piece() == king # check if king was moved to new square
    assert initial_state[0][0].get_piece() is None # check if board state at 0, 0 was updated
    assert initial_state[1][1].get_piece() == king # check if board state at 1, 1 was updated

def test_find_king_when_exists():
    board = Board()
    state_handler = StateHandler()

    # set up board and pieces
    for row in board.squares:
        for square in row:
            square.set_piece(None)

    king = King("WHITE", [0, 0])
    board.squares[0][0].set_piece(king)

    test_king = state_handler.find_king(board, "WHITE")
    assert test_king is not None


def test_execute_move():
    board = Board()
    state_handler = StateHandler()

    # set up board and pieces
    for row in board.squares:
        for square in row:
            square.set_piece(None)
    
    king = King("WHITE", [0, 0])
    queen = Queen("BLACK", [1, 1])
    board.squares[0][0].set_piece(king)
    board.squares[1][1].set_piece(queen)
    player = Player("WHITE")

    # execute move
    state_handler.execute_move(board, king, 1, 1, player)

    # assertions
    assert king.position == [1, 1] # check if king is in new position
    assert board.squares[0][0].get_piece() is None # check if previous position is empty


def test_stalemate():
    pass

def test_castle():
    pass

def test_pawn_moved_two():
    pass

def test_set_last_move():
    pass

def test_remove_piece():
    pass