#!/bin/python3
#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    b_days = 0
    for d in range(i, j+1):
        rev_day = str(d)[::-1]
        
        if abs(d - int(rev_day)) % k == 0:
            b_days += 1
            
    return b_days
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
