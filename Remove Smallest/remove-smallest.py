rng = int(input())

def rem(lst, n):
    lst.sort()
    lst.reverse()
    i = n-1
    
    while i > 0:
        num = abs(lst[i] - lst[i-1])
        if num <= 1:
            lst.pop()
            i -= 1
            continue
        print("NO")
        return
    
    print("YES")
            
        
    
    
for i in range(rng):
    n = int(input())
    lst = list(map(int, input().split()))
    rem(lst, n)
