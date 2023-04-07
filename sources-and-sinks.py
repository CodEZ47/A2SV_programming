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
sources = []
sinks = []
matrix = []

for i in range(nodes):
    row = num_lst()
    s = sum(row)
    if not s:
        sinks.append(i+1)
    matrix.append(row)

for col in range(nodes):
    sum = 0
    for row in range(nodes):
        if matrix[row][col]:
            sum += 1
            break
    if not sum:
        sources.append(col+1)


print(len(sources), *sources)
print(len(sinks), *sinks)
