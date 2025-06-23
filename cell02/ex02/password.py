#!/usr/bin/env python3  

# Set the correct password
password = "Python is awesome"

entered = input("Enter password: ")

# Check if password matches
if entered == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
