#!/usr/bin/env -S python3

from sys import argv


def shrink(text: str):
    """Shrink the text to 8 characters"""

    return text[:8]


def enlarge(text: str):
    """Enlarge the text to 20 characters"""

    return text + "Z" * (8 - len(text))


if len(argv) < 2:
    print("none")
else:
    for arg in argv[1:]:
        if len(arg) == 8:
            print(arg)
        elif len(arg) > 8:
            print(shrink(arg))
        else:
            print(enlarge(arg))
