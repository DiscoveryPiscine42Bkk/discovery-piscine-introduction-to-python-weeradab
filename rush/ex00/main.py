#!/usr/bin/env python3
from checkmate import checkmate
def main():
    # Example chessboards (K = King, Q = Queen, R = Rook, B = Bishop, P = Pawn)
    board1 = """
....
.K..
.P..
....
"""
    board2 = """
...Q
.K..
....
....
"""
    board3 = """
....
.K..
..B.
....
"""
    board4 = """
....
.K..
....
....
"""

    # Test the checkmate function
    print("Board 1 (King threatened by pawn):", checkmate(board1))
    print("Board 2 (King threatened by queen):", checkmate(board2))
    print("Board 3 (King threatened by bishop):", checkmate(board3))
    print("Board 4 (King safe):", checkmate(board4))

if __name__ == "__main__":
    main()