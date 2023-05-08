class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quickSort(start, end, nums):
            if start >= end:
                return
            
            left, right = start, end
            pivot = nums[(left + right) // 2]
            
            while left <= right:
                while left <= right and nums[left] < pivot:
                    left += 1
                while left <= right and nums[right] > pivot:
                    right -= 1
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1

            quickSort(start, right, nums)
            quickSort(left, end, nums)

        quickSort(0,len(nums)-1,nums)

        
        return nums[(-1*k)]