from board import Board

def test_starting_position_check():
    board = Board()
    board.setup_pieces()

    print('Starting position')
    board.display()

    print()
    print('White in check:',  board.is_in_check('white'))
    print('Black in check:',  board.is_in_check('black'))

def main():
    test_starting_position_check()

if __name__ == '__main__':
    main()
