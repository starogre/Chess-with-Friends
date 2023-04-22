1) Board
This class can represent the chessboard and handle move execution.
Methods:
init: Initialize the board with the initial positions of pieces.
get_piece: Get the piece at a specific square.
set_piece: Set a piece on a specific square.
execute_move: Handle move execution, updating piece positions on the board.

2) Piece
Base class for all chess pieces, with common attributes and methods.
Attributes:
color: The color of the piece (white or black).
position: The current position of the piece on the board.
Methods:
generate_possible_moves: Generate all possible moves for the piece.

3) Derived classes for each piece type
Create a class for each chess piece type (e.g., Rook, Knight, Bishop, Queen, King, Pawn) that inherits from the base Piece class.
Methods (for each derived class):
validate_move: Validate if a move is legal for that specific piece type.

4) Player
This class can represent a player in the game.
Attributes:
color: The color of the player (white or black).
pieces: A list of the player's remaining pieces on the board.

5) State Management
This class manages the game state and checks for check and checkmate situations.
Methods:
update_state: Update the game state after each move.
get_active_player: Get the player whose turn it is.
is_in_check: Check if a player is in check.
is_checkmate: Check if a player is in checkmate.

6) UI and Game Flow
GUI library like tkinter for creating the user interface. Potential classes and methods for the UI:

a. MainWindow PyQt

This class represents the main window of the chess app.
Methods:
init_new_game: Initialize a new game.
draw_board: Draw the chessboard.
draw_pieces: Draw the pieces on the board.
select_piece: Allow the user to select a piece.
select_dest: Allow the user to select a destination square for the selected piece.
update_curr_player: Update the display to show the current player.
update_game_status: Update the game status display (e.g., check, checkmate, stalemate).

b. GameController

This class can handle the user's interactions with the game.
Methods:
on_piece_select: Handle the event when a user selects a piece.
on_dest_select: Handle the event when a user selects a destination square for a piece.
