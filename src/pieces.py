######################################################################
#
#   Purpose:    This program serves as the rule library for the game
#
#   Author:     William Hall
#
#   Date:       July 5, 2026
#
#   Version:    0.0.0
#
######################################################################


#   PAWN

#   This function defines pawn move validation
def is_valid_pawn_move(board, start_row, start_col, end_row, end_col):
    piece = board.grid[start_row][start_col]
    target = board.grid[end_row][end_col]

    row_change = end_row - start_row
    col_change = end_col - start_col

    if piece =='P':
        direction = -1
    else:
        direction = 1

#   one-square forward rule
    if col_change == 0 and row_change == direction and target == '.':
        return True
    
#   initialize variables for two-square forward rule 
    middle_row = start_row + direction
    middle_square = board.grid[middle_row][start_col]

    if piece == 'P':
      starting_row = 6 
    else: 
        starting_row = 1

#   two-square forward rule
    if (
        col_change == 0
    and start_row == starting_row
    and row_change == 2 * direction
    and target == '.'
    and middle_square == '.'
    ):
        return True

#   pawn capture rule
    if piece.isupper():
        enemy = target.islower()
    else:
        enemy = target.isupper()

    if (
        abs(col_change) == 1 
        and row_change == direction
        and target != '.'
        and enemy
    ):
         return True
    
    return False