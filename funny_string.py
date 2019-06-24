#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the funnyString function below.
def funnyString(s):
    s = [ord(x) for x in s]
    r = s[::-1]
    for i in range(1, len(s)):
        if abs(s[i] - s[i-1]) == abs(r[i] - r[i-1]):
            continue
        else:
            return "Not Funny"
    return "Funny"


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        print(result)
