#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    def addDig(num):
        ans = 0
        while num:
            ans += num % 10
            num = num // 10
        
        return ans
    n = int(n)
    num = addDig(n)* k
    
    def rec(num):  
        print(num)     
        if addDig(num) == num:
            return num
        
        ans = addDig(num)
        
        return rec(ans)
    
    return rec(num)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
