#######################################################################
#
#   Purpose:    This program serves as the board for the game
#
#   Author:     William Hall
#
#   Date:       Jul 5, 2026
#
#   Version:    0.0.1
#
######################################################################

import pieces

class Board:
    def __init__(self):
        self.grid = []

        for row in range(8):
            current_row = []

            for col in range(8):
                current_row.append(".")

            self.grid.append(current_row)

    def display(self):
        for row in self.grid:
            print(" ".join(row))

    def setup_pieces(self):
        self.grid[0] = ["r", "n", "b", "q", "k", "b", "n", "r"]
        self.grid[1] = ["p"] * 8

        self.grid[6] = ["P"] * 8
        self.grid[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"]

    def move_piece(self, start_row, start_col, end_row, end_col):
        if self.is_valid_move(start_row, start_col, end_row, end_col):
            piece = self.grid[start_row][start_col]

            self.grid[start_row][start_col] = "."
            self.grid[end_row][end_col] = piece

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        piece = self.grid[start_row][start_col]

        if piece == '.':
            return False

        if piece.upper() == 'P':
            return pieces.is_valid_pawn_move(
                self,
                start_row,
                start_col,
                end_row,
                end_col,
            )
        elif piece.upper() == 'R':
            return pieces.is_valid_rook_move(
                self,
                start_row,
                start_col,
                end_row,
                end_col,
            )
        elif piece.upper() == 'N':
                    return pieces.is_valid_knight_move(
                        self,
                        start_row,
                        start_col,
                        end_row,
                        end_col,
                    )
        elif piece.upper() == 'B':
                    return pieces.is_valid_bishop_move(
                        self,
                        start_row,
                        start_col,
                        end_row,
                        end_col,
                    )
        elif piece.upper() == 'Q':
                    return pieces.is_valid_queen_move(
                        self,
                        start_row,
                        start_col,
                        end_row,
                        end_col,
                    )
        elif piece.upper() == 'K':
                    return pieces.is_valid_king_move(
                        self,
                        start_row,
                        start_col,
                        end_row,
                        end_col,
                    )


#   TODO: KING
        else:
            return False