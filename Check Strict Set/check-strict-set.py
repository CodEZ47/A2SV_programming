# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(map(int, input().split()))
setA_len = len(setA)
sets_num = int(input())


def supr_set_chkr(setA, setA_len, sets_num):
    sets_lst = []
    for i in range(sets_num):
        set_temp = (set(map(int, input().split())))
        set_len = len(set_temp)
        bool = setA.issuperset(set_temp)
        if set_len == setA_len or not bool:
            return False
    return True


print(supr_set_chkr(setA, setA_len, sets_num))        


