#!/usr/bin/env -S python3

from sys import argv


if len(argv) < 2:
    print("none")
    exit(0)

for arg in argv[1:]:
    if arg.endswith("ism"):
        print(arg)
    else:
        print(f"{arg}ism")
