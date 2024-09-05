#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = [x + 2 for x in original_array if x > 5]

print("\033[38;5;051mOriginal array:", original_array)
print("\033[38;5;118mNew array:", new_array)


# • Take the previous program and modify it to only process values greater than 5 from
# the original array.
# • For example, if your original array is [2, 8, 9, 48, 8, 22, -12, 2], you should have the
# following output:
# ?> ./play_with_arrays.py | cat -e
# [2, 8, 9, 48, 8, 22, -12, 2]$
# [10, 11, 50, 10, 24]$
# ?>