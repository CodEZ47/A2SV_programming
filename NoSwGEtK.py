class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ctr = 0

        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i, len(nums)):
                temp = gcd(temp, nums[j])
                
                if temp == k:
                    ctr += 1
        
        return ctr
            