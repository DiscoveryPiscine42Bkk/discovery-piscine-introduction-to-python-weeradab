#!/usr/bin/env python3
while True:
    text = input("Enter text (or 'q' to quit): ")
    if text.lower() == 'q':
        break
    print(text.swapcase())