#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("\033[38;5;219m" + "none")
else:
    for param in reversed(sys.argv[1:]):
        print("\033[38;5;219m" + param)
