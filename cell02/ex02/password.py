#!/usr/bin/env python3

password = "Python is awesome"

#entered_password = input("Please enter the password: ")
entered_password = input()

if entered_password == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")


# Функция getpass.getpass() в Python используется для безопасного ввода пароля без отображения введенных символов в консоли.

# getpass()
# import getpass

# password = getpass.getpass("Введите пароль: ")
# print(f"Ваш пароль: {password}")  # Не делай так в реальном коде! 🤦‍♂️
