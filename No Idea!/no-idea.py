# Enter your code here. Read input from STDIN. Print output to STDOUT
arr_size = map(int,input().split())
arr_size = list(arr_size)
arr = map(int,input().split())
arr = list(arr)
setA = map(int,input().split())
setA = list(setA)
setB = map(int,input().split())
setB = list(setB)


def happy_calc(arr, set1, set2, arr_size):
    set_dict = {}
    set_len = arr_size[1]
    arr_len = arr_size[0]
    happiness = 0
    
    for num in range(set_len):
        if setA[num] not in set_dict:
            set_dict[setA[num]] = "setA"
        if setB[num] not in set_dict:
            set_dict[setB[num]] = "setB"
    
    for num in range(arr_len):
        # print(arr[num])   
        if set_dict.get(arr[num]) == "setA":
            happiness += 1
        if set_dict.get(arr[num]) == "setB":
            happiness -= 1
            
    print(happiness)
    
happy_calc(arr, setA, setB, arr_size)
