#!/usr/bin/env python3

def find_the_redheads(family_dict):
    redheads = list(filter(lambda name: family_dict[name] == 'red', family_dict.keys()))
    return redheads

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))


# • Create a script called family_affairs.py.
# • It will contain a method called find_the_redheads.
# • This method will take a dictionary as a parameter, representing family members
# with their first name as the key and their hair color as the value.
# • This method will use the filter function to gather the first names of the red-haired
# individuals into a new list, which it will return.
# • For example, the following script:

# # your method definition here
# dupont_family = {
# "florian": "red",
# "marie": "blond",
# "virginie": "brunette",
# "david": "red",
# "franck": "red"
# }
# print(find_the_redheads(dupont_family))

# Will have the following output:
# ?> ./family_affairs.py
# ['florian', 'david', 'franck']
# ?>

# Google Python dictionary filter, keys(), tolist()