#!/usr/bin/env python3
num = int(input("Enter a number\n"))
# Loop from 0 to 9 to display the multiplication table
i = 0
while i < 10:
    print(f"{i} x {num} = {i * num}")    #This prints the multiplication result using an f-string:4
    i += 1 
