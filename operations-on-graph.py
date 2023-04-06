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


nodes_no = integer()
rng = integer()

node_dict = defaultdict(list)

for i in range(rng):
    lst = num_lst()

    if lst[0] == 1:
        node_dict[lst[1]].append(lst[2])
        node_dict[lst[2]].append(lst[1])
    else:
        print(*node_dict[lst[1]])