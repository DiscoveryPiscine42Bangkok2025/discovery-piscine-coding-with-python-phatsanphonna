#!/usr/bin/env -S python3


def array_of_names(persons: dict):
    names = []
    for firstname, lastname in persons.items():
        names.append(f"{firstname.capitalize()} {lastname.capitalize()}")
    return names


persons = {"jean": "valjean", "grace": "hopper", "xavier": "niel", "fifi": "brindacier"}

print(array_of_names(persons))
