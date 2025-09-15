#!/usr/bin/env -S python3


def greetings(name=None):
    if not name:
        print("Hello, Noble stranger!")
    elif isinstance(name, str):
        print(f"Hello, {name}!")
    else:
        print("Error, It was not a name.")


greetings("Alexandra")
greetings("Wil")
greetings()
greetings(42)
