class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        ans = []
        while i < len(nums):
            temp = nums[i] - 1

            if nums[temp] != nums[i]:
                nums[temp], nums[i] = nums[i], nums[temp]
            else:
                i += 1
        
        
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                ans.append(i+1)
        
        return ans
        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i
        
        # return len(nums)