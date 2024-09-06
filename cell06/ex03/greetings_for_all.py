#!/usr/bin/env python3

def greetings(name="\033[38;5;051mmnoble stranger"):
    if isinstance(name, str):
        print(f"\033[38;5;118mHello, \033[38;5;227m{name}\033[38;5;118m.")
    else:
        print("\033[38;5;219mError! It was not a name.")

greetings("Alexandra")
greetings('AbRaCaDaBrA')
greetings("")
greetings(42)
greetings()


# • Create a method inside called greetings that takes a name as a parameter and
# displays a welcome message with that name.
# • If the method is called without an argument, its default parameter will be "noble
# stranger".
# • If the method is called with an argument that is not a string, an error message
# should be displayed instead of the welcome message.
# • For example, the following program:

# ?> cat greetings_for_all.py | cat -e
# # your method definition here
# greetings('Alexandra')
# greetings('Wil')
# greetings()
# greetings(42)

# will produce the following output:
# ?> ./greetings_for_all.py | cat -e
# Hello, Alexandra.$
# Hello, Wil.$
# Hello, noble stranger.$
# Error! It was not a name.$
# ?>

# Google default parameter, isinstance method.