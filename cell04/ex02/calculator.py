#!/usr/bin/env python3

fi_num = int(input("Give me the first number: "))
se_num = int(input("Give me the second number: "))

print("Thank you!")

print(f"{fi_num} + {se_num} = {fi_num + se_num}")
print(f"{fi_num} - {se_num} = {fi_num - se_num}")

if se_num != 0:
    print(f"{fi_num} / {se_num} = {fi_num / se_num}")
else:
    print(f"Division by zero is not allowed!")

print(f"{fi_num} * {se_num} = {fi_num * se_num}")
