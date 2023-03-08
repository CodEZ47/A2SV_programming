class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = [0]*(len(nums)+1)
        for s,e in requests:
            arr[s] += 1
            arr[e+1] -= 1
        print(arr, nums)
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
        
        arr.sort(reverse = True)
        nums.sort(reverse = True)

        sum_ = 0

        for i in range(len(nums)):
            sum_ += arr[i] * nums[i]

        return sum_ % ((10**9)+7)