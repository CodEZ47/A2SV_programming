class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        p_str = 0
        p_end = len(nums)-1
        nums_len = len(nums)
        temp = 0
        
        if nums_len == 1:
            return nums
        
        
        while p_str < p_end:
            num1 = nums[p_str] % 2
            num2 = nums[p_end] % 2
            
            if(num1 != 0 and num2 == 0):
                temp = nums[p_str]
                nums[p_str] = nums[p_end]
                nums[p_end] = temp
                p_str += 1
                p_end -= 1
            elif(num1 != 0 and num2 != 0):
                p_end -= 1
            elif(num1 == 0 and num2 != 0 ):
                p_str += 1
            elif(num1 == 0 and num2 == 0):
                p_str += 1
        
        return nums