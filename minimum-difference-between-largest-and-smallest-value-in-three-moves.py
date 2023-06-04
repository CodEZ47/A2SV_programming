class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        

        nums.sort()
        n = len(nums)
        mini = sys.maxsize
        for i in range(4):
            print(n-1-3+i, i)
            mini = min(mini, nums[n - 1 - 3 + i] - nums[i])

        return mini