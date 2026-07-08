######################################################################
#
#   Purpose:    This program contains move validation functions for
#               for each piece
#
#   Author:     William Hall
#
#   Date:       July 5, 2026
#
#   Version:    0.0.4
#
######################################################################


#   PAWN

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


#   ROOK

def is_valid_rook_move(board, start_row, start_col, end_row, end_col):
    piece = board.grid[start_row][start_col]
    target = board.grid[end_row][end_col]

    row_change = end_row - start_row
    col_change = end_col - start_col

#   reject diagonal moves

    if row_change != 0 and col_change != 0:
        return False
    
#   vertical move
    
    if col_change == 0:
        if end_row > start_row:
            step = 1
        else:
            step = -1

        for row in range(start_row + step, end_row, step):
            if board.grid[row][start_col] != '.':
                return False
    
#   horizontal move
    
    if row_change == 0:
        if end_col > start_col:
            step = 1
        else:
            step = -1

        for col in range(start_col + step, end_col, step):
            if board.grid[start_row][col] != '.':
                return False
        
#   team test

    return is_valid_destination (piece, target)


#   KNIGHT
        
def is_valid_knight_move(board, start_row, start_col, end_row, end_col):
    piece = board.grid[start_row][start_col]
    target = board.grid[end_row][end_col]

    row_change = abs(end_row - start_row)
    col_change = abs(end_col - start_col)

#   define L movement

    if not(
        (row_change == 2 and col_change == 1)
        or
        (row_change == 1 and col_change == 2)
    ):
        return False

#   team test

    return is_valid_destination (piece, target)


#   BISHOP

def is_valid_bishop_move(board, start_row, start_col, end_row, end_col):
    piece = board.grid[start_row][start_col]
    target = board.grid[end_row][end_col]

    row_change = abs(end_row - start_row)
    col_change = abs(end_col - start_col)

#   diagonal test
    if row_change != col_change:
        return False

#   destination test
    if not is_valid_destination(piece, target):
        return False

#   path test
    row_step = 1 if end_row > start_row else -1
    col_step = 1 if end_col > start_col else -1

    current_row = start_row + row_step
    current_col = start_col + col_step

    while current_row != end_row and current_col != end_col:
        if board.grid[current_row][current_col] != '.':
            return False
        
        current_row += row_step
        current_col += col_step

    return True


#   QUEEN
def is_valid_queen_move(board, start_row, start_col, end_row, end_col):
    if is_valid_bishop_move(
        board,
        start_row,
        start_col,
        end_row,
        end_col,
    ):
        return True
    
    if is_valid_rook_move(
        board,
        start_row,
        start_col,
        end_row,
        end_col,
    ):
        return True
    

def is_valid_king_move(board, start_row, start_col, end_row, end_col):
    piece = board.grid[start_row][start_col]
    target = board.grid[end_row][end_col]

    row_change = abs(end_row - start_row)
    col_change = abs(end_col - start_col)

    if row_change == 0 and col_change == 0:
        return False
    
    if row_change <= 1 and col_change <= 1:
        return True
     
    return False

     
#   HELPERS

def is_enemy(piece, target):
    return (
        (piece.isupper() and target.islower())
        or
        (piece.islower() and target.isupper())
    )

def is_valid_destination (piece, target):
    return target == '.' or is_enemy(piece, target)






