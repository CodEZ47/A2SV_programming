class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] %  2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        # print(nums)

        nums_dict = defaultdict(int)
        nums_dict[nums[0]] += 1

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            nums_dict[nums[i]] += 1
        
        ctr = 0

        for num in nums:
            if num == k:
                ctr += 1
            if num - k in nums_dict:
                ctr += nums_dict[num-k]
        
        return ctr