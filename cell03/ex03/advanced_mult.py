#!/usr/bin/env -S python3

for i in range(11):
    result = ""
    for j in range(11):
        result += f"{i * j} "
    print(f"Table {i}: {result}")
