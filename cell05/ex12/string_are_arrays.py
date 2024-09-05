#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("\033[38;5;222mnone")
else:
    input_string = sys.argv[1]
    
    z_count = input_string.count('z')
    
    if z_count == 0:
        print("\033[38;5;222mnone")
    else:
        print('\033[38;5;051mz' * z_count)


# ?> ./string_are_arrays.py | cat -e
# none$
# ?> ./string_are_arrays.py "The character Z is not found in this string" | cat -e
# none$
# ?> ./string_are_arrays.py "The character z is found in this string" | cat -e
# z$
# ?> ./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat -e
# zzz$
# ?>

# ORANGE      = \033[38;5;222m
# GREEN_BR    = \033[38;5;118m
# YELLOW_BR   = \033[38;5;227m
# PINK_BR     = \033[38;5;206m
# BLUE_BR     = \033[38;5;051m
# PINK_BRR    = \033[38;5;219m