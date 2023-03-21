from collections import defaultdict
def rng():
    return int(input())
def lst():
    return list(map(int, input().split()))
def string():
    return input()
def str_lst():
    return list(input())
 
r = rng()

for i in range(r):
    nums = lst()
    l = min(nums)
    r = max(nums)
    
    print(min(l, ((l+r)//4)))
        
