#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("\033[38;5;227mnone")
else:
    for param in sys.argv[1:]:
        if not param.endswith("ism"):
            print("\033[38;5;051m" + param + "\033[38;5;118mism")


# • The program will display each parameter passed as an argument, one by one, by
# appending it with "ism".
# • If the parameter already ends with "ism", it will be skipped and not displayed. If
# there are no parameters, it should display "none" followed by a newline.
# ?> ./append_it.py | cat -e
# none$
# ?> ./append_it.py "parallel" "egoism" "human" | cat -e
# parallelism$
# humanism$
# ?>
# Use matching.

# ORANGE      = \033[38;5;222m
# GREEN_BR    = \033[38;5;118m
# YELLOW_BR   = \033[38;5;227m
# PINK_BR     = \033[38;5;206m
# BLUE_BR     = \033[38;5;051m
# PINK_BRR    = \033[38;5;219m