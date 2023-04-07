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
adj_dict = defaultdict(list)
matrix = []

for i in range(nodes):
    matrix.append(num_lst())

for row in range(nodes):
    for col in range(nodes):
        if matrix[row][col]:
            adj_dict[row + 1].append(col+1)


for val in adj_dict.values():
    print(len(val), *val)
