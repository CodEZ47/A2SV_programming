arr1_len = input()
arr1 = set(map(int, input().split()))
arr2_len = input()
arr2 = set(map(int, input().split()))

diff_set = arr1.union(arr2)

print(len(diff_set))
