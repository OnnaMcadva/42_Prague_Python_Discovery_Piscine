#!/usr/bin/env python3

def array_of_names(persons):
    full_names = []
    for first_name, last_name in persons.items():
        full_name = f"\033[38;5;051m{first_name.capitalize()} {last_name.capitalize()}\033[0m"
        full_names.append(full_name)
    return full_names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

for name in array_of_names(persons):
    print(name)


# def array_of_names(persons):

#     full_names = []
#     for first_name, last_name in persons.items():
#         full_name = f"\033[38;5;051m{first_name.capitalize()} {last_name.capitalize()}\033[0m"
#         full_names.append(full_name)
#     return full_names

# persons = {
#     "jean": "valjean",
#     "grace": "hopper",
#     "xavier": "niel",
#     "fifi": "brindacier"
# }

# print(array_of_names(persons))


# • Create a script called your_namebook.py.
# • It should contain a method called array_of_names.
# • This method takes a dictionary associating first names with last names as a parameter.
# • It will build an array with the full names of the people, with the first letter capitalized. It returns this array. Refer to the example.
# • For example, the following script:

# # your method definition here
# persons = {
# "jean": "valjean",
# "grace": "hopper",
# "xavier": "niel",
# "fifi": "brindacier"
# }
# print(array_of_names(persons))
# Will produce the following output:

# ?> ./your_namebook.py
# ['Jean Valjean', 'Grace Hopper', 'Xavier Niel', 'Fifi Brindacier']
# ?>

# You can use the capitalize method in Python.