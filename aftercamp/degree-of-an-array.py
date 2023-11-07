class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        val = Counter(nums)

        curr = max(val.values())
        maxis = [x for x in val.keys() if val[x] == curr]

        def findMin(maxi):
            l = 0
            r = len(nums) - 1
            while l <= r:
                if nums[l] == maxi and nums[r] == maxi:
                    return (r - l) + 1
                
                if nums[l] != maxi:
                    l += 1
                if nums[r] != maxi:
                    r -= 1
            
            return 1
        
        mini = 50001

        for maxi in maxis:
            mini = min(mini, findMin(maxi))

        return mini

    