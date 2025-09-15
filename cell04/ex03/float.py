#!/usr/bin/env -S python3

number = float(input("Give me a number: "))

if number - int(number) == 0:
    print(f"This number is an integer.")
else:
    print(f"This number is a decimal.")