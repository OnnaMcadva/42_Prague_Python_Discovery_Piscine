#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# new_array = [x + 2 for x in original_array if x > 5]

# unique_values = set(new_array)

# print("\033[38;5;051mOriginal array:", original_array)
# print("\033[38;5;118mNew array:", unique_values)


new_array = {x + 2 for x in original_array if x > 5}

print("\033[38;5;051mOriginal array:", original_array)
print("\033[38;5;118mNew array:", new_array)


# • Take the previous program and modify it to remove duplicates from the output.
# Note that you should not explicitly remove values from your arrays.
# • For example, if your original array is [2, 8, 9, 48, 8, 22, -12, 2], the expected output
# would be:
# ?> ./play_with_arrays.py | cat -e
# [2, 8, 9, 48, 8, 22, -12, 2]$
# {24, 10, 11, 50}$
# ?>