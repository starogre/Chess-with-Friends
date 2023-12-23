from client.src.components.board import Board
from client.src.components.chess_piece import King, Queen, Rook, Bishop
from client.src.components.player import Player
from client.src.components.state_handler import StateHandler
from client.src.components.game_controller import GameController


gc = GameController()
gc.start_game()

print("hi")

def main():
    board = Board()
    state_handler = StateHandler()

    # set up board and pieces
    for row in board.squares:
        for square in row:
            square.set_piece(None)

    king = King("WHITE", [0, 0])
    queen = Queen("BLACK", [1, 1])
    king2 = King("BLACK", [7, 7])
    rook = Rook("BLACK", [2, 1])
    board.squares[0][0].set_piece(king)
    board.squares[1][1].set_piece(queen)
    board.squares[7][7].set_piece(king2)
    board.squares[2][1].set_piece(rook)
    player = Player("WHITE")
    player2 = Player("BLACK")
    print(state_handler.find_all_enemy_moves(board, player))
    is_valid = state_handler.move_is_valid(board, queen, 1, 5, player2, king2)
    print(f"Is the move valid? {is_valid}")



if __name__ == "__main__":
    main()