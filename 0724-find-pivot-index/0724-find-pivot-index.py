class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
            sumr = 0
            suml = 0
            j = len(nums)
            i = 0

            sumr = sum(nums)
            
            while i < j:
                sumr = sumr - nums[i]
                if suml == sumr:
                    return i
                suml = suml + nums[i]
                i += 1

            return -1;