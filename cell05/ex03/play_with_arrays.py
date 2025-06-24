#!/usr/bin/env python3
original_array = [2, 8, 9, 48, 8, 22, -12, 2]
# Only values greater than 5, add 2 
new_array = [x + 2 for x in original_array if x > 5]
# Remove duplicates by converting to set
rd_array = set(new_array)
print(original_array)
print(rd_array)
