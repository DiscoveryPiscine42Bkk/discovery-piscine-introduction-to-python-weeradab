#!/usr/bin/env python3

import sys
def print_number_range(start_param, end_param):
    """
    Prints a list of numbers from start to end (inclusive).
    Returns None and prints "none" if parameters are invalid.
    """
    try:
        start = int(start_param)
        end = int(end_param)
        return list(range(start, end + 1))
    except ValueError:
        return None

def main():
    # Check for exactly 2 command-line arguments 
    if len(sys.argv) != 3:
        print("none")
        return
    
    result = print_number_range(sys.argv[1], sys.argv[2])
    
    if result is None:
        print("none")
    else:
        print(result)

if __name__ == "__main__":
    main()