#!/usr/bin/env python3

#number = float(input("Please enter a number: ").strip())

try :

    #number = float(input().strip())
    number = float(input())

    if number < 0:
        print("This number is negative.")
    elif number > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")

except :

    print("This is not a number.")