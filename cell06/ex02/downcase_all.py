#!/usr/bin/env -S python3

from sys import argv


def downcase_it(text: str):
    return text.lower()


for arg in argv:
    print(downcase_it(arg))
