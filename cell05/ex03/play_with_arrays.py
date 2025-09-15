#!/usr/bin/env -S python3

array = [10, 5, 7, -2, 3, 8, 8]
new_array = []

print(array)

for i in array:
    if array.count(i) > 1:
        continue

    if i > 5:
        i = i + 2
        new_array.append(i)

print(new_array)
