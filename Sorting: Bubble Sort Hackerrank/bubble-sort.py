#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    sorted = False
    ctr = 0
    n = len(a)
    while not sorted:
        sorted = True;
        for i in range(n-1):
            
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                ctr += 1
                sorted = False
    print("Array is sorted in", ctr, "swaps." )
    print("First Element:", a[0] )
    print("Last Element:", a[-1] )
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
