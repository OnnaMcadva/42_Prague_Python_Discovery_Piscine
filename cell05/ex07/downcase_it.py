#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("\033[38;5;219mnone")
else:
    print("\033[38;5;219m" + sys.argv[1].lower())


# ?> ./downcase_it.py | cat -e
# none$
# ?> ./downcase_it.py "LUCIOLE" | cat -e
# luciole$
# ?> ./downcase_it.py 'This exercise is quite easy!' | cat -e
# this exercise is quite easy!$
# ?>