#!/bin/usr/python3
def square_digits(num):
    number = str(num)
    result = []
    for digit in number:
        square_digits = int(digit) ** 2
        result.append(str(square_digits))
    return int("".join(result))
