#!/usr/bin/env python3
num = int(input("Enter a number: "))
# check if the number is negative, positive, or zero
if num < 0:
    print("This number is negative.")
elif num > 0:                              #elif = else if 
    print("This number is positive.")
else:
    print("This number is both positive and negative.")
