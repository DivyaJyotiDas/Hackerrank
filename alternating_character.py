#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count = count + 1
    return count


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(result)
