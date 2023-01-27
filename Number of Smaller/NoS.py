rng = list(map(int, input().split()))
lst_1 = list(map(int, input().split()))
lst_2 = list(map(int, input().split()))
j = 0
ans = []
 
for i in range(rng[1]):
    while j < rng[0] and lst_1[j] < lst_2[i]:
        j += 1
    ans.append(j)
print(*ans)
