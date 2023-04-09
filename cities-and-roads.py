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


nodes = integer()
ctr = 0
for i in range(nodes):
    ctr += sum(num_lst())

print(ctr//2)
