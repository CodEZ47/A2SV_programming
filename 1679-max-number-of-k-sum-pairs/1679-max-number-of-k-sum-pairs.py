class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_dict = defaultdict(int)
        ctr = 0
        
        for num in nums:
            complement = k - num
            if complement in num_dict:
                ctr += 1
                num_dict[complement] -= 1
                if num_dict[complement] == 0:
                    del num_dict[complement]
            else:
                num_dict[num] += 1
        
        return ctr