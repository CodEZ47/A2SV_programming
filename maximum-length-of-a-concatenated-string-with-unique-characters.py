class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = []
        subset = []
        maxi = 0
        def dfs(i):
            nonlocal maxi
            if i >= len(arr):
                temp = "".join(subset.copy())
                if len(temp) == len(set(temp)):
                    maxi = max(maxi,len(temp))
                return
            
            subset.append(arr[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        
        dfs(0)

        return maxi