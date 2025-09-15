#!/usr/bin/env -S python3


def average(class_list: dict):
    scores = 0
    students = 0

    for _, score in class_list.items():
        scores += score
        students += 1

    return scores / students


class_3B = {"marine": 18, "jean": 15, "coline": 8, "luc": 9}
class_3C = {"quentin": 17, "julie": 15, "marc": 8, "stephanie": 13}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
