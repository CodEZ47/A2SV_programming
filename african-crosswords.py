from collections import defaultdict
from collections import Counter
import math
def intger():
    return int(input())
def num_lst():
    return list(map(int, input().split()))
def string():
    return input()
def str_lst():
    return list(input())


r = num_lst()
row_dict = defaultdict(set)
col_dict = defaultdict(set)

mat = []
for i in range(r[0]):
    temp = str_lst()
    mat.append(temp)


for i in range(r[0]):
    temp = set()
    for j in range(r[1]):
        if mat[i][j] in temp:
            row_dict[i].add(mat[i][j])
        temp.add(mat[i][j])

for i in range(r[1]):
    temp = set()
    for j in range(r[0]):
        if mat[j][i] in temp:
            col_dict[i].add(mat[j][i])
        temp.add(mat[j][i])

for i in range(r[0]):
    for j in range(r[1]):
        if mat[i][j] in row_dict[i] or mat[i][j] in col_dict[j]:
            mat[i][j] = 0

ans = ""
for i in range(r[0]):
    for j in range(r[1]):
        if mat[i][j] != 0:
            ans += mat[i][j]
            

print(ans)
    
