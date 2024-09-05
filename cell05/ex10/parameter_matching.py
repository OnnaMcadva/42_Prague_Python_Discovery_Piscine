#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("\033[38;5;227mnone")
else:
    parameter = sys.argv[1]
    
    user_input = input("\033[38;5;051mWhat was the parameter? " + "\033[38;5;206m")
    
    if user_input == parameter:
        print("\033[38;5;222mGood job!")
    else:
        print("\033[38;5;118mNope, sorry...")

# ?> ./parameter_matching.py
# none
# ?> ./parameter_matching.py "Hello"
# What was the parameter? Bonjour
# Nope, sorry...
# ?> ./parameter_matching.py "Hello"
# What was the parameter? Hello
# Good job!
# ?>

# ORANGE      = \033[38;5;222m
# GREEN_BR    = \033[38;5;118m
# YELLOW_BR   = \033[38;5;227m
# PINK_BR     = \033[38;5;206m
# BLUE_BR     = \033[38;5;051m
# PINK_BRR     = \033[38;5;219m
