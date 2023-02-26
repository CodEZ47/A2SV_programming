class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_ = 0;
        ctr =  0;

        if len(nums) == 0:
            return ctr

        dict_ = dict();
        dict_[0] = 1;

        for i in range(len(nums)):
            sum_ += nums[i]
            if sum_-k in dict_:
                ctr += dict_[sum_-k]
            
            if sum_ in dict_:
                dict_[sum_] += 1
            else:
                dict_[sum_] = 1
            
        
        return ctr