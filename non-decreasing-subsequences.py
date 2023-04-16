class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        subset = []
        def dfs(i):
            if i >= len(nums) and len(subset) >= 2:
                res.add(tuple(subset.copy()))
                return
            if i >= len(nums):
                return
            
            if not subset or subset[-1] <= nums[i]:
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()
            dfs(i + 1)
        dfs(0)

        # print(res)
        return list(res)
