#!/usr/bin/env -S python3

from sys import argv

if len(argv) < 4:
    print("none")
    exit(0)

array = argv[1:]

for text in reversed(array):
    print(text)
