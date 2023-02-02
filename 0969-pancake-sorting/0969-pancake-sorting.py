class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(arr, e):
            s = 0
            while s < e:
                arr[s], arr[e] = arr[e], arr[s]
                s += 1
                e -= 1
        
        n = len(arr)
        ans = []
        for i in range(n-1, -1, -1):
            max_num = i
            for j in range(i, -1, -1):
                if arr[max_num] <  arr[j]:
                    max_num = j
            if max_num != i:
                flip(arr,max_num)
                flip(arr, i)
                ans.append(max_num + 1)
                ans.append(i + 1)
        
        return ans