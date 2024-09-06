#!/usr/bin/env python3

import sys

def downcase_it(s):
    return s.lower()

if len(sys.argv) <= 1:
    print("\033[38;5;222mnone")
else:
    for arg in sys.argv[1:]:
        print("\033[38;5;051m" + downcase_it(arg))


# • You must define a method in this program. This method is called downcase_it.
# • The downcase_it method takes a string as an argument. It should return the string
# in lowercase.
# • Apply this method, and display its return value, on the program’s parameters.
# • If there are no parameters, display "none" followed by a line break.
# ?> ./downcase_all.py
# none
# ?> ./downcase_all.py 'HELLO WORLD' 'I understood Arrays well!'
# hello world
# i understood arrays well!
# ?>

# ORANGE      = \033[38;5;222m
# GREEN_BR    = \033[38;5;118m
# YELLOW_BR   = \033[38;5;227m
# PINK_BR     = \033[38;5;206m
# BLUE_BR     = \033[38;5;051m
# PINK_BRR    = \033[38;5;219m