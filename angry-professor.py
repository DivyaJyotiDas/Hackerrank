#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the angryProfessor function below.
def angryProfessor(k, a):
    print("k",k)
    print('a',a)
    late_count = 0
    for i in a:
        if i <= 0:
            late_count += 1
    if k > late_count:
        print("YES")
    if k <= late_count:
        print("NO")

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        a = list(map(int, input().rstrip().split()))
        result = angryProfessor(k, a)
        #print(result)
