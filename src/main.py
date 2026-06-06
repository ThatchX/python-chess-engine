from board import Board

def main():
    board = Board()
    board.setup_pieces()
    
    print("Initial Position:")
    board.display()

    board.move_piece(6, 4, 5, 4)

    print()
    print("After Move:")
    board.display()

if __name__ == "__main__":
    main()

