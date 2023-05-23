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


while nodes:
    graph = defaultdict(list)
    color = [0] * (nodes+1)
    color[1] = 1
    e = integer()
    for i in range(e):
        x,y = num_lst()
        graph[x].append(y)
        graph[y].append(x)

    stk = [1]
    test = 1
    while stk and test:
        # print(color)

        curr = stk.pop()

        for child in graph[curr]:
            if color[child] == 0:
                color[child] = color[curr] * -1
                stk.append(child)
            else:
                if color[child] == color[curr]:
                    print("NOT BICOLOURABLE.")
                    test = 0
                    break
    
    
    if test:
        print("BICOLOURABLE.")
    nodes = integer()