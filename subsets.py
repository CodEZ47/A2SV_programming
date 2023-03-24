class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, res, temp, nums):
            res.append(list(temp))
            for i in range(idx, len(nums)):
                temp.append(nums[i])
                backtrack(i+1, res, temp, nums)
                temp.pop()
        
        res = []
        temp = []

        backtrack(0,res,temp,nums)

        return res