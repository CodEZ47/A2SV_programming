class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(s,e,nums):
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1
        
        nums.reverse()
        k = k % len(nums)

        rev(0, k-1, nums)
        rev(k, len(nums)-1, nums)
        print(nums)
        