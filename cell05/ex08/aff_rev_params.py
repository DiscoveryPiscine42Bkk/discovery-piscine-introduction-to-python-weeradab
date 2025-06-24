#!/usr/bin/env python3
import sys

args = sys.argv[1:]  # Get all arguments except script name
if not args:
    print("none")
elif len(args) < 2:
    print("none")
else:
    for arg in reversed(args):
        print(arg)