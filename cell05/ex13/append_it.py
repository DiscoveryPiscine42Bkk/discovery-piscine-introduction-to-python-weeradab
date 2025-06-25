#!/usr/bin/env python3

import sys

def add_ism(word):
    """Add 'ism' suffix to a word if it doesn't already end with it."""
    if not word.endswith("ism"):
        return word + "ism"
    return word

def main():
    
    arguments = sys.argv[1:]
    
    # Handle case with no arguments
    if not arguments:
        print("none")
        return
    
    # Process each word
    for word in arguments:
        modiword = add_ism(word)
        print(modiword)

if __name__ == "__main__":
    main()