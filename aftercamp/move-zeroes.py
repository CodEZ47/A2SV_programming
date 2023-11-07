class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 1
        n = len(nums)

        while p2 < n:
            if nums[p1] == 0:
                if nums[p2] != 0:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                else:
                    p2 += 1
                    continue
            
            else:
                p1 += 1
                p2 += 1
        

        