from client.src.components.board import Board
from client.src.components.chess_piece import King, Queen, Rook
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

    king = King("WHITE", (0, 0))
    queen = Queen("BLACK", (1, 1))
    rook = Rook("BLACK", (2, 1))
    board.squares[0][0].set_piece(king)
    board.squares[1][1].set_piece(queen)
    board.squares[2][1].set_piece(rook)
    player = Player("WHITE")
    print(state_handler.find_all_enemy_moves(board, player))
    is_valid = state_handler.move_is_valid(board, king, 1, 1, player, king)
    print(f"Is the move valid? {is_valid}")



if __name__ == "__main__":
    main()