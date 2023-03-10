class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        sum_nums = max(nums)
        s = 1
        e = sum_nums


        while s <= e:
            mid = (s+e) >> 1
            comp = sum([ceil(i/mid) for i in nums])

            if comp > threshold:
                s = mid + 1
            elif comp <= threshold:
                e = mid - 1
        
        return s