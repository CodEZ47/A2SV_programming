rng = int(input())
 
 
def finder(arr):
    lst = [arr[0]]
 
    for i in range(1, len(arr)):
        if lst[-1] < 0 and arr[i] < 0:
            if arr[i] > lst[-1]:
                lst.pop()
                lst.append(arr[i])
        elif lst[-1] > 0 and arr[i] > 0:
            if arr[i] > lst[-1]:
                lst.pop()
                lst.append(arr[i])
        else:
            lst.append(arr[i])
 
    add = sum(lst)
    print(add)
 
 
for i in range(rng):
    length = int(input())
    arr = list(map(int, input().split()))
 
    finder(arr)
