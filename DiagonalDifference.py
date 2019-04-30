#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    l_sum = 0
    r_sum = 0
    n = len(arr) - 1
    for i in arr:
        m = arr.index(i)
        l_sum += arr[m][m]
        r_sum += arr[m][n]
        n -= 1
    print(l_sum, r_sum)
    return abs(l_sum - r_sum)

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(arr)
    result = diagonalDifference(arr)

    print(result)
