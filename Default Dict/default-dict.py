# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

len_a, len_b = map(int, input().split())
wrd_dict = defaultdict(list)

for idx in range(len_a):
    char = input()
    wrd_dict[char].append(idx + 1)#idx + 1 cause answer is in 1-indexed
    
    
for idx in range(len_b):
    char = input()
    print(*wrd_dict.get(char, [-1]))#-1 is in a list because it is not iterable by the *
