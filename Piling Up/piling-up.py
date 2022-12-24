# Enter your code here. Read input from STDIN. Print output to STDOUT
T = input()
T = int(T)
lst = []

for l in range(T):
    n = input()
    lst.append(input().split(" "))


def block_sorter(blocks):
    p_start = 0
    p_end = len(blocks)-1
    curr = 0
    fin_lst = False

    while p_start <= p_end:
        if fin_lst:
            if blocks[p_end] >= blocks[p_start] and blocks[p_end] <= curr:
                curr = blocks[p_end]
                p_end -= 1
            elif blocks[p_start] > blocks[p_end] and blocks[p_start] <= curr:
                curr = blocks[p_start]
                p_start += 1
            else:
                print("No")
                return
        else:
            if (blocks[p_end] >= blocks[p_start]):
                curr = blocks[p_end]
                p_end -= 1
                fin_lst = True
            else:
                curr = blocks[p_start]
                p_start += 1
                fin_lst = True

    print("Yes")

for x in range(T):
    temp = [int(num) for num in lst[x]]
    block_sorter(temp)
