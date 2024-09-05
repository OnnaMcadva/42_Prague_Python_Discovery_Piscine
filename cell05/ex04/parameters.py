#!/usr/bin/env python3

import sys

param = len(sys.argv) - 1

print(f"\033[38;5;219mNumber of parameters: \033[38;5;118m{param}\033[38;5;219m.")


# ?> ./parameters.py
# Number of parameters: 0.
# ?> ./parameters.py "initiation"
# Number of parameters: 1.
# ?> ./parameters.py "this" "is" "crazy" "there's" "everywhere!"
# Number of parameters: 5.
# ?>