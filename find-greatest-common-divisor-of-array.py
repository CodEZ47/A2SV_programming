class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        mini = nums[0]
        maxi = nums[-1]
        def gcd(mini, maxi):
            if not maxi:
                return mini
            return gcd(maxi, mini % maxi)
        
        return gcd(mini,maxi)