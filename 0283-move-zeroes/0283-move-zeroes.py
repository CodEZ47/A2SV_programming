class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr_fir = 0
        ptr_sec = 1
        nums_len = len(nums)
        
        while ptr_sec < nums_len:
            if nums[ptr_fir] == 0:
                if nums[ptr_sec] != 0:
                    nums[ptr_fir], nums[ptr_sec] = nums[ptr_sec], nums[ptr_fir]
                else:
                    ptr_sec += 1
                    continue
            else:
                ptr_fir += 1
                ptr_sec += 1
                
        return nums