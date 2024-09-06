#!/usr/bin/env python3

def add_one():
    global var
    try:
        var += 1
    except:
        quit("\033[38;5;206mError! It is not a integer 🐙")

print("🦎 🦎 🦎")

var = -5
print(f"\033[38;5;118mBefore: \033[38;5;227m{var}")
add_one()
print(f"\033[38;5;051mAfter1: \033[38;5;227m{var}")
add_one()
print(f"\033[38;5;051mAfter2: \033[38;5;227m{var}")
add_one()
print(f"\033[38;5;051mAfter3: \033[38;5;227m{var}")

print("🦎 🦎 🦎")

var = 5.05
print(f"\033[38;5;118mBefore: \033[38;5;227m{var}")
add_one()
print(f"\033[38;5;051mAfter1: \033[38;5;227m{var}")
add_one()
print(f"\033[38;5;051mAfter2: \033[38;5;227m{var}")
add_one()
print(f"\033[38;5;051mAfter3: \033[38;5;227m{var}")

print("🦎 🦎 🦎")

var = "A"
print(f"\033[38;5;118mBefore: \033[38;5;227m{var}")
add_one()
print(f"\033[38;5;051mAfter1: \033[38;5;227m{var}")

print("🦎 🦎 🦎")

# • Inside the program, create a method called add_one that takes a parameter and
# adds 1 to the parameter passed to the method.
# • Initialize a variable in the body of the program, display it, and then call the method
# that adds 1.
# • Display your variable again in the body of the program.
# • What do you observe?