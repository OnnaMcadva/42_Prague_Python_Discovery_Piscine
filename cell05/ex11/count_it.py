#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("\033[38;5;222mnone")
else:
    num_params = len(sys.argv) - 1
    print(f"\033[38;5;118mparameters: \033[38;5;227m{num_params}")
    
    for param in sys.argv[1:]:
        print(f"\033[38;5;051m{param}: \033[38;5;219m{len(param)}")

# ?> ./count_it.py | cat -e
# none$
# ?> ./count_it.py "Game" "of" "Thrones" | cat -e
# parameters: 3$
# Game: 4$
# of: 2$
# Thrones: 7$
# ?>

# ORANGE      = \033[38;5;222m
# GREEN_BR    = \033[38;5;118m
# YELLOW_BR   = \033[38;5;227m
# PINK_BR     = \033[38;5;206m
# BLUE_BR     = \033[38;5;051m
# PINK_BRR     = \033[38;5;219m