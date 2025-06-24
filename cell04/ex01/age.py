#!/usr/bin/env python3
age = int(input("please tell me your age: " ))
print(f"you are currently {age} years old . ")
for years in [10, 20, 30]:
    fage = age + years
    print(f"In {years} years, you'll be {fage} years old .")
