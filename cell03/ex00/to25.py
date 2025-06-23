#!/usr/bin/env python3
num = int(input("Enter a number less than 25\n"))

# Check if input is valid
if num > 25:
    print("Error")  #If true, it prints "Error" and skips the loop below
else:
    while num <= 25:    #It uses a while loop that keeps running as long as num is less than or equal to 25
        print(f"Inside the loop, my variable is {num}")
        num += 1   #It adds 1 to num with num += 1 (to eventually stop the loop)21
