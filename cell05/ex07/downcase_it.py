#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("\033[38;5;219m" + "none")
else:
    print("\033[38;5;219m" + sys.argv[1].lower())