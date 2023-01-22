rng = int(input())


def x_sum(row, col, matrix):
    to_right = {}
    to_left = {}
    for i in range(row):
        for j in range(col):
            s = i + j
            d = i - j
            if s not in to_left:
                to_left[s] = matrix[i][j]
            else:
                to_left[s] = to_left[s] + matrix[i][j]
                
            if d not in to_right:
                to_right[d] = matrix[i][j]
            else:
                to_right[d] = to_right[d] + matrix[i][j]
                
    ans = 0
    for i in range(row):
        for j in range(col):
            ans = max(ans,(to_left[i+j] + to_right[i-j] - matrix[i][j]))
    print(ans)
    

for i in range(rng):
    lst = list(map(int, input().split()))
    row = lst[0]
    col = lst[1]
    matrix = []
    
    for i in range(row):
        temp = list(map(int, input().split()))
        matrix.append(temp)
    
    x_sum(row, col, matrix)
