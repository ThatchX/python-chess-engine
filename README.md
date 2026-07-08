##Python Chess Engine ♟️

A chess engine written entirely in Python as a personal learning project for Programming I.

The objective of this project is to build a complete chess engine from scratch while learning the fundamentals of software engineering, object-oriented programming, algorithms, debugging, testing, and version control.

⸻

##Features

Board

* 8×8 board representation
* Standard chess starting position
* Terminal board display
* Piece movement

##Piece Movement

* ✅ Pawn
* ✅ Rook
* ✅ Knight
* ✅ Bishop
* ✅ Queen
* ✅ King

Each piece has its own movement validation function contained within pieces.py.

##Game Logic

* Move validation
* Check detection
* Board rule enforcement

##Testing

* Dedicated board testing file
* Easily expandable test suite for future development

⸻

##Project Structure

src/
│
├── main.py          # Starts the program
├── game.py          # Future game loop and turn management
├── board.py         # Board state and game rules
├── pieces.py        # Individual piece movement rules
└── test_board.py    # Board testing

⸻

##Current Progress

Completed

* Board implementation
* Initial piece setup
* Piece movement validation
* Move dispatcher
* Check detection
* GitHub version control
* Basic testing framework

##In Progress

* Prevent illegal moves that leave the king in check

##Planned Features

* Checkmate detection
* Stalemate detection
* Castling
* En passant
* Pawn promotion
* Turn management
* Complete game loop
* Move history
* Game saving/loading
* Simple AI opponent

⸻

##Technologies

* Python
* Git
* GitHub
* Visual Studio Code

⸻

##Purpose

This project is intended as an educational exercise to strengthen understanding of:

* Python programming
* Object-oriented programming
* Algorithms
* Modular software design
* Chess engine architecture
* Testing and debugging
* Git workflow

Rather than relying on external chess libraries, every rule is implemented from scratch to better understand both the game of chess and software development.

⸻

Author

William Hall
