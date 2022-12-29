class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0;
        nxt = curr + 1;
        temp = 0;
        nums_len = len(nums)

        while nxt < nums_len:
            while curr < nums_len and nums[curr] != 0:
                curr += 1
                nxt = curr+1

            if nxt < nums_len and nums[nxt] != 0:
                temp = nums[nxt]
                nums[nxt] = nums[curr]
                nums[curr] = temp
                curr += 1
                nxt += 1
            else:
                nxt += 1

        return nums;