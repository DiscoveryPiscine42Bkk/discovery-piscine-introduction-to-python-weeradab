#!/usr/bin/env python3
import sys
def main():
    
    arguments = sys.argv[1:]
    
    if len(arguments) != 1:
        print("none")
        return
    
    input_string = arguments[0]
    count = input_string.count('z')
    
    if count == 0:
        print("none")
    else:
        print('z' * count)

if __name__ == "__main__":
    main()