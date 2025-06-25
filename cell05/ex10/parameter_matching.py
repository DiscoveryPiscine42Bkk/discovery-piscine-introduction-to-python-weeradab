#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    # store the command-line argument in a descriptive variable
    parameter = sys.argv[1]
    
    # user to guess the parameter
    uinput = input("What was the parameter? ")
    
    # Compare with the actual parameter
    if uinput == parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")
