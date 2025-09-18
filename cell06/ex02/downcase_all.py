#!/usr/bin/env -S python3

from sys import argv


def downcase_it(text: str):
    return text.lower()


if len(argv) < 2:
    print("none")
    exit(0)

for arg in argv[1:]:
    print(downcase_it(arg))
