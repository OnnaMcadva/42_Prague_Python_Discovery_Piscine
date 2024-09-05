#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("\033[38;5;222mnone")
else:
    print("\033[38;5;219m" + sys.argv[1].upper())


# ?> ./upcase_it.py | cat -e
# none$
# ?> ./upcase_it.py "initiation" | cat -e
# INITIATION$
# ?> ./upcase_it.py 'This exercise is quite easy!' | cat -e
# THIS EXERCISE IS QUITE EASY!$
# ?>