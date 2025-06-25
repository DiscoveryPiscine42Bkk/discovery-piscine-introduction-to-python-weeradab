#!/usr/bin/env python3

import sys

comline = sys.argv[1:]
if not comline:
    print("none")
else:
    # Print the total number of parameters
    print(f"Number of parameters: {len(comline)}")
    
    # Print each parameter and its length
    for argument in comline:
        print(f"Parameter: '{argument}' | Length: {len(argument)} characters")