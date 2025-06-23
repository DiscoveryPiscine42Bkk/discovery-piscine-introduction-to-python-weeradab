#!/usr/bin/env python3
print("Enter the first number:")
num1 = int(input())
print("Enter the second number:")
num2 = int(input())

# Multiply and show result
result = num1 * num2
print(f"{num1} x {num2} = {result}")
if result < 0:
    print("The result is negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")
