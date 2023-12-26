from client.src.components.board import Board
from client.src.components.state_handler import StateHandler

class UserInterface:
    def __init__(self):
        pass
    
    # def display_board(self, board):
    #     # display current state of board
    #     pass

    def get_user_input(self, prompt):
        try:
            return input(prompt)
        except KeyboardInterrupt:
            print("\nUser interrupted input.")
        except EOFError:
            print("\nUser pressed Ctrl + D (EOF) or provided empty input.")
            
    

    def select_target_square(self):
        # logic to prompt user to select a target square
        target_selected = input("Select a target square (e.g. 'A2'): ")
        # convert input into coordinates or piece representation
        return target_selected
    
    def display_board(self, board, active_player):
        piece_symbols = {
            "King": "K",
            "Queen": "Q",
            "Rook": "R",
            "Bishop": "B",
            "Knight": "N",
            "Pawn": "P"
        }

        # Define color codes
        white_piece_color = '\033[92m'  # White pieces color (white text)
        black_piece_color = '\033[91m'  # Black pieces color (black text)
        reset_color = '\033[0m'  # Reset to default color

        row_labels_black = ['1', '2', '3', '4', '5', '6', '7', '8']
        row_labels_white = ['8', '7', '6', '5', '4', '3', '2', '1']
        col_labels = ['H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
      
        print("* P L A Y - C H E S S *")

        is_white_turn = active_player.color == "WHITE"
        row_labels = row_labels_white if is_white_turn else row_labels_black

        for row_num, row in enumerate(board.squares[::-1] if is_white_turn else board.squares): # make ::1 if want to reverse order of all rows
            row_display = []
            for col_num, square in enumerate(row[::1] if is_white_turn else row[::-1]): # make ::-1 if want to reverse individual row (for instance, for black's turn)
                piece = square.get_piece()

                # alternating checkerboard pattern
                if (row_num + col_num) % 2 == 0:
                    highlight_color = '\033[47m' # light gray bg
                else:
                    highlight_color = '\033[0m'  # no bg

                exit_color = '\033[0m'
                bold = '\033[1m'

                if piece is None:
                    row_display.append(f'{highlight_color}   {exit_color}')  # empty spaces with alternating background
                else:
                    piece_type = type(piece).__name__  # get name of piece class
                    symbol = piece_symbols[piece_type]
                    if piece.color == "BLACK":
                        symbol = symbol.lower()
                    piece_color = white_piece_color if piece.color == 'WHITE' else black_piece_color
                    row_display.append(f"{bold}{highlight_color} {piece_color}{symbol} {reset_color}")
            print(f'{row_labels[row_num]} ' + ''.join(row_display))

        print('   ' + '  '.join(col_labels[::-1] if is_white_turn else col_labels))