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


r = integer()
lst = num_lst()

temp = lst[0]
isOdd = lst[0]%2

def calc(r):
    for i in range(1,r):
        if isOdd and lst[i] % 2 == 0 or not isOdd and lst[i] % 2 != 0 :
            lst.sort()
            print(lst)
            return
    print(lst)

calc(r)
    