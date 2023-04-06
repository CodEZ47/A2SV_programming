from collections import defaultdict
from collections import Counter
import math


def integer():
    return int(input())


def num_lst():
    return list(map(int, input().split()))


def string():
    return input()


def str_lst():
    return list(input())


rng = integer()

for i in range(rng):
    num = integer()
    if num < 3:
        print(3)
    elif num & 1:
        print(1)
    else:
        j = 0
        while num and not num & 1:
            num = num >> 1
            j += 1
        num = num >> 1
        if not num:
            print((2**j)+1)
        else:
            print(2**j)
