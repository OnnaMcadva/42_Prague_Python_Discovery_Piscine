#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("\033[38;5;222mnone")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        
        result = list(range(start, end + 1))
        
        print(f"\033[38;5;051m{result}")
    except ValueError:
        print("\033[38;5;222mnone")


# • You must construct an array containing all the values between these two numbers
# using a range. Then, you will display the array using the print function.
# • If the number of parameters is different from 2, you should display ’none’ followed
# by a newline.
# ?> ./free_range.py | cat -e
# none$
# ?> ./free_range.py 10 14 | cat -e
# [10, 11, 12, 13, 14]$
# ?>
# Use the range function.

# ORANGE      = \033[38;5;222m
# GREEN_BR    = \033[38;5;118m
# YELLOW_BR   = \033[38;5;227m
# PINK_BR     = \033[38;5;206m
# BLUE_BR     = \033[38;5;051m
# PINK_BRR    = \033[38;5;219m