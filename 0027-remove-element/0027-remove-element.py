class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p_str = 0
        p_end = len(nums)-1
            
        while p_str <= p_end:
            
            if nums[p_end] == val:
                nums.pop()
                p_end -= 1
                continue
            if nums[p_str] == val:
                nums[p_str] = nums[p_end]
                nums.pop()
                p_end -= 1
                p_str += 1
                continue
                
            p_str += 1
        
        print(nums)