import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n, -1, n):
        print('*')


if __name__ == '__main__':
    n = int(input())

    staircase(n)