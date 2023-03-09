class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        p1 = 0
        p2 = len(nums) - 1
        
        if nums[0] > target:
            return 0
        
        while p1 < p2:
            if nums[p1] == target:
                return p1
            if nums[p2] == target:
                return p2
            if nums[p1] < target:
                p1 += 1
            if nums[p1] > target:
                return p1
            
            if nums[p2] > target:
                p2 -= 1
            
            if nums[p2] < target:
                return p2 + 1