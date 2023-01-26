class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = set()
        for num in nums:
            temp = str(num)
            temp = temp[::-1]
            temp = int(temp)
            ans.add(temp)
        
        ans = list(ans)
        nums += ans
        
        nums = set(nums)
        
        return len(nums)