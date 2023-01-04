if __name__ == '__main__':
    N = int(input())
    final_lst = []
    
    def switch(inp, final_lst):
        
        if inp[0] == "insert":
            final_lst.insert(int(inp[1]), int(inp[2]))
        elif inp[0] == "print":
            print(final_lst)
        elif inp[0] == "remove":
            final_lst.remove(int(inp[1]))
        elif inp[0] == "append":
            final_lst.append(int(inp[1]))            
        elif inp[0] == "sort":
            final_lst.sort()
        elif inp[0] == "pop":
            final_lst.pop()
        elif inp[0] == "reverse":
            final_lst.reverse()
    for i in range(N):
        temp = list(map(str, input().split()))
        switch(temp, final_lst)
        
