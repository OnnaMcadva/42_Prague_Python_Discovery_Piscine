#!/usr/bin/env python3
import sys

def shrink(string):
    print("\033[38;5;051m" + string[:8])

def enlarge(string):
    print("\033[38;5;118m" + string + '\033[38;5;206mZ' * (8 - len(string)))

if len(sys.argv) < 2:
    print("\033[38;5;222mnone")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)



# • You must create two different methods in this program:
# • The method shrink takes a string as a parameter and displays the first eight
# characters of that string.
# Use slices.
# • The method enlarge takes a string as a parameter and appends ’Z’ characters to
# make it a total of eight characters. Then, it displays the resulting string.
# Similar to arrays, you can add characters to a string using the
# concatenation operator.
# • For each argument of the program: if the argument has more than eight characters,
# call the shrink method on it; if the argument has less than eight characters, call
# the enlarge method on it; and if the argument has exactly eight characters, display
# it directly followed by a new line.
# • If the number of parameters is less than 1, display ’none’ followed by a new line.

# ?> ./methods_everywhere.py | cat -e
# none$
# ?> ./methods_everywhere.py 'lol' 'physically' 'backpack' | cat -e
# lolZZZZZ$
# physical$
# backpack$
# ?>
# ./methods_everywhere.py 'lol' 'physically' 'c444c' '!-!-!-' "kUkUkUkUk" "1234567"