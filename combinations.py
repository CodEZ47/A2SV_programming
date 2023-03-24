class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(idx, res, temp, nums):
            if len(list(temp)) == k:
                res.append(list(temp))

            for i in range(idx, len(nums)):
                temp.append(nums[i])
                backtrack(i+1, res, temp, nums)
                temp.pop()
        
        nums = []
        for i in range(1,n+1):
            nums.append(i)
        
        res, temp = [], []

        backtrack(0,res,temp,nums)

        return res