class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        flag = False
        ans = [-1,-1]

        while l <= r:
            mid = (l + r) >> 1

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                flag = True
                l = mid + 1
        
        if not flag:
            return ans
        
        ans[1] = r
        l = 0

        while l <= r:
            mid = (l + r) >> 1

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                flag = True
                r = mid - 1

        ans[0] = l
        
        return ans