# Enter your code here. Read input from STDIN. Print output to STDOUT
grp_size = input()
room_lst = list(map(int, input().split()))

def cap_finder(size, lst):
    room_lst_len = len(lst)-1
    size = int(size)
    
    lst.sort()
    
    for ind in range(0,room_lst_len, size):
        # print(lst[ind], lst[ind+1])
        if lst[ind] == lst[ind+1]:
            continue
        elif lst[ind] != lst[ind+1]:
            print(lst[ind])
            return
        
    print(lst[-1])
    
cap_finder(grp_size, room_lst)
