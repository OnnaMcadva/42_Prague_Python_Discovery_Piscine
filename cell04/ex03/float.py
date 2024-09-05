#!/usr/bin/env python3

user_input = input("Give me a number: ")

number = float(user_input)

#print(f"Your number is {number}")

if number == int(number):
    print("This number is an integer.")
else:
    print("This number is a decimal.")
