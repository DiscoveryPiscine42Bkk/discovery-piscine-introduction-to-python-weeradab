#!/usr/bin/env python3
from checkmate import checkmate

def main():
    # Test case 1: King in check by rook
    board1 = """\
R...
.K..
....
...."""
    checkmate(board1)  # Prints: Success
    
    # Test case 2: Safe king
    board2 = """\
....
.K..
....
...."""
    checkmate(board2)  # Prints: Fail
    
    # Test case 3: Invalid board (multiple kings)
    board3 = """\
K...
.K..
....
...."""
    checkmate(board3)  # Prints: Fail

if __name__ == "__main__":
    main()
