class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zer = 0
        one = 0
        two = 0
        
        for num in nums:
            if num == 0:
                zer += 1
            elif num == 1:
                one += 1
            else:
                two += 1
        
        for i in range(len(nums)):
            if zer > 0:
                nums[i] = 0
                zer -= 1
                continue
            if one > 0:
                nums[i] = 1
                one -= 1
                continue
            if two > 0:
                nums[i] = 2
                two -= 1
                continue
            