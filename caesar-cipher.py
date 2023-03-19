#!/bin/python3
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
def get_alphabet():
    _from = 97 # a in ansii
    to = 122 # z in anssi
    
    return [chr(i) for i in range(_from, to + 1)]

def caesarCipher(s, k):
    alphabet = get_alphabet()
    rotated_alphabet = [ None ] * len(alphabet)
    
    for i in range(len(alphabet)):
        k = k % len(alphabet)
        new_index = i - k
        
        if new_index < 0:
            new_index += len(alphabet)
            
        rotated_alphabet[new_index] = alphabet[i]
    
    res = ''
    
    for c in s:
        
        try:
            
            index = alphabet.index(c.lower())
            is_uppercase = c == c.upper()
            to_add = rotated_alphabet[index]
            
            if is_uppercase:
                to_add = to_add.upper()
                
            res += to_add
        except:
            res += c
    
    return res
            
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
