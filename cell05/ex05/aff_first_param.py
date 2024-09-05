#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print("\033[38;5;118m" + sys.argv[1])
else:
    print("\033[38;5;222mnone")


# ?> ./aff_first_param.py | cat -e
# none$
# ?> ./aff_first_param.py "Code Ninja" "Numerique" "42" | cat -e
# Code Ninja$
# ?>