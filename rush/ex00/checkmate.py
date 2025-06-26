#!/usr/bin/env python3
def checkmate(board_str):
    # Convert the board string into a grid (2D list)
    board = [list(row) for row in board_str.strip().split('\n')]
    size = len(board)  # Size of the board (assuming it's square)

    # Step 1: Find the King's position
    king_x, king_y = -1, -1
    for y in range(size):
        for x in range(size):
            if board[y][x] == 'K':
                king_x, king_y = x, y
                break
        if king_x != -1:
            break

    # Step 2: Check for threats from Rooks or Queens (straight lines)
    # Directions: up, down, left, right
    straight_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in straight_directions:
        x, y = king_x + dx, king_y + dy
        while 0 <= x < size and 0 <= y < size:
            piece = board[y][x]
            if piece == 'R' or piece == 'Q':
                print("Success")  # King is in check
                return
            if piece != '.':  # Blocked by another piece
                break
            x += dx
            y += dy

    # Step 3: Check for threats from Bishops or Queens (diagonal lines)
    # Directions: top-right, top-left, bottom-right, bottom-left
    diagonal_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in diagonal_directions:
        x, y = king_x + dx, king_y + dy
        while 0 <= x < size and 0 <= y < size:
            piece = board[y][x]
            if piece == 'B' or piece == 'Q':
                print("Success")  # King is in check
                return
            if piece != '.':  # Blocked by another piece
                break
            x += dx
            y += dy

    # Step 4: Check for threats from Pawns (they attack diagonally from below)
    # Pawns are only a threat if they are one row below the king
    for dx in [-1, 1]:  # Check left and right diagonals
        x, y = king_x + dx, king_y + 1
        if 0 <= x < size and 0 <= y < size:
            if board[y][x] == 'P':
                print("Success")  # King is in check
                return

    # If no threats found, the king is safe
    print("Fail")