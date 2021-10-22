#!/bin/python3

import math
import os
import random
import re
import sys

def check_digits():
    position = 0
    counter = 0
    binary_counter = 0

    for position in range(len(binary)-1):
        if binary[position] == 1 and binary[position] == binary[position + 1]:
            counter += 1
        else:
            if counter >= binary_counter:
                binary_counter = counter
            counter = 0

    if binary[len(binary)-1] == 1:
        counter += 1
        binary_counter += 1

    if binary_counter >= counter:
        result = binary_counter
    else:
        result = counter

    print(result)

if __name__ == '__main__':
    n = int(input().strip())
    binary = list()

    while True:
        if n >= 1:
            module = n % 2
            division = n/2
            n = math.floor(division)
            binary.append(module)
        else:
            break

    check_digits()