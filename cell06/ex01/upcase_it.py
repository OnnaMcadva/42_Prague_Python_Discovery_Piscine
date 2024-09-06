#!/usr/bin/env python3

def upcase_it(s):
    return s.upper()

print("\033[38;5;118m" + upcase_it("hello"))



# • The upcase_it method takes a string as an argument. It should return the string
# in uppercase.
# • Test the method by calling it in your program. In the example below, we test it
# with "hello":
# ?> cat upcase_it.py
# # Your method definition
# print(upcase_it("hello"))
# ?> ./upcase_it.py
# HELLO
# ?>