#!/usr/bin/env -S python3

text = input()

output = ""

for char in text:
    if char.islower():
        output += char.upper()
    else:
        output += char.lower()

print(output)
