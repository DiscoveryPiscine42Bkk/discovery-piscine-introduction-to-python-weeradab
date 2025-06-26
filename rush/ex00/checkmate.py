#!/usr/bin/env python3

def checkmate(board_str):
    """
    Check if the king is in check on a chess board.
    Prints "Success" if in check, "Fail" if safe or invalid board.
    """
    # 1. Prepare and validate the board
    if not board_str or not isinstance(board_str, str):
        print("Fail")
        return
    
    rows = [row.strip() for row in board_str.strip().split('\n') if row.strip()]
    if not rows:
        print("Fail")
        return
        
    board_size = len(rows)
    
    # 2. Check if board is square
    for row in rows:
        if len(row) != board_size:
            print("Fail")
            return
    
    # 3. Find the king
    king_pos = None
    board = []
    valid_pieces = {'K', 'Q', 'R', 'B', 'P', '.'}
    
    for y in range(board_size):
        row = list(rows[y])
        board.append(row)
        for x in range(board_size):
            piece = row[x]
            if piece not in valid_pieces:
                print("Fail")
                return
            if piece == 'K':
                if king_pos is not None:
                    print("Fail")  # Multiple kings
                    return
                king_pos = (x, y)
    
    if not king_pos:
        print("Fail")  # No king found
        return
    
    # 4. Check for threats
    king_x, king_y = king_pos
    
    # Check straight lines (Rooks/Queens)
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        x, y = king_x + dx, king_y + dy
        while 0 <= x < board_size and 0 <= y < board_size:
            piece = board[y][x]
            if piece in {'R', 'Q'}:
                print("Success")
                return
            if piece != '.':
                break
            x += dx
            y += dy
    
    # Check diagonals (Bishops/Queens)
    for dx, dy in [(1,1), (1,-1), (-1,1), (-1,-1)]:
        x, y = king_x + dx, king_y + dy
        while 0 <= x < board_size and 0 <= y < board_size:
            piece = board[y][x]
            if piece in {'B', 'Q'}:
                print("Success")
                return
            if piece != '.':
                break
            x += dx
            y += dy
    
    # Check pawn attacks (from below)
    for dx in (-1, 1):
        x, y = king_x + dx, king_y + 1
        if 0 <= x < board_size and 0 <= y < board_size:
            if board[y][x] == 'P':
                print("Success")
                return
    
    # 5. If no threats found
    print("Fail")

