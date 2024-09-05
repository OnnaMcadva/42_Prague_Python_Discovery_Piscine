#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("\033[38;5;219mnone")
else:
    for param in reversed(sys.argv[1:]):
        print("\033[38;5;219m" + param)


# ?> ./aff_rev_params.py | cat -e
# none$
# ?> ./aff_rev_params.py "coucou" | cat -e
# none$
# ?> ./aff_rev_params.py "Python" "piscine" "hello" | cat -e
# hello$
# piscine$
# Python$
# ?>