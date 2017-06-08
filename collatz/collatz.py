#!/usr/bin/python3


def collatz(number):
    steps = 0
    while number != 1:
        if (number % 2 == 0):
            steps += 1
            number = number / 2
        elif (number % 2 == 1):
            steps += 1
            number = number * 3 + 1
    return (steps)

print(collatz(12))
print(collatz(3))
print(collatz(27))
