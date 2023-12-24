from client.src.components.board import Board

class UserInterface:
    def __init__(self):
        pass
    
    # def display_board(self, board):
    #     # display current state of board
    #     pass

    def select_piece(self):
        # logic to prompt user to select piece
        piece_selected = input("Select a piece (e.g. 'A2'): ")
        # convert input into coordinates or piece representation
        return piece_selected
    
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

        # Determine orientation
        is_white_turn = active_player.color == "WHITE"

        print('   ' + ' '.join(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']))

        rows_to_print = range(8)
        if not is_white_turn:
            rows_to_print = reversed(rows_to_print)

        for row_num in rows_to_print:
            row = board.squares[row_num]
            row_display = []
            pieces_in_row = [square.get_piece() for square in row]

            if is_white_turn:
                pieces_in_row = reversed(pieces_in_row)

            for piece in pieces_in_row:
                if piece is None:
                    row_display.append('-')  # empty spaces
                else:
                    piece_type = type(piece).__name__  # get name of piece class
                    symbol = piece_symbols[piece_type]
                    if piece.color == "BLACK":
                        symbol = symbol.lower()
                    row_display.append(symbol)

            print(f'{8 - row_num}  ' + ' '.join(reversed(row_display)) if is_white_turn else ' '.join(row_display))

        print('   ' + ' '.join(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']))

        # row_labels_black = ['8', '7', '6', '5', '4', '3', '2', '1']
        # col_labels_black = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        # row_labels_white = row_labels_black[::-1]
        # col_labels_white = col_labels_black[::-1]

        # if active_player.color == "BLACK":
        #     row_labels = row_labels_black
        #     col_labels = col_labels_black
        # else:
        #     row_labels = row_labels_white
        #     col_labels = col_labels_white
        
        # # create board display array
        # board_display = [['-' for _ in range(8)] for _ in range(8)]
        # for i, row in enumerate(board.squares):
        #     for j, square in enumerate(row):
        #         piece = square.get_piece()
        #         if piece is not None:
        #             piece_type = type(piece).__name__
        #             symbol = piece_symbols[piece_type]
        #             if piece.color == "BLACK":
        #                 symbol = symbol.lower()
        #             board_display[i][j] = symbol

        # # display board with selected labels
        # for i, row in enumerate(board_display):
        #     print(row_labels[i] + '  ' + ' '.join(row))
        # print('   ' + ' '.join(col_labels))
######################
        # for row_idx, row_label in enumerate(reversed(row_labels)):
        #     row = board.squares[row_idx]
        #     row_display = []
        #     for square in row:
        #         piece = square.get_piece()
        #         if piece is None:
        #             row_display.append('-') # empty spaces
        #         else:
        #             piece_type = type(piece).__name__ # get name of piece class
        #             symbol = piece_symbols[piece_type]
        #             if piece.color == "BLACK":
        #                 symbol = symbol.lower()
        #             row_display.append(symbol)
        #     print(row_label + '  ' + ' '.join(row_display))
        
        # print(' ' + ' '.join(col_labels))