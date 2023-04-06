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
    return list(input().split(" "))


lst = str_lst()

if lst[0] == lst[1]:
    print(lst[0])
else:
    print(1)
