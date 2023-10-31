class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        pre = []
        temp = nums[0]
        for n in nums:
            pre.append(temp)
            temp = min(temp, n)
        
        
        for i in range(len(nums)):
            while stk and nums[stk[-1]] <= nums[i]:
                stk.pop()
            if stk and nums[stk[-1]] > nums[i]:
                if pre[stk[-1]] < nums[i]:
                    return True
            stk.append(i)
        return False