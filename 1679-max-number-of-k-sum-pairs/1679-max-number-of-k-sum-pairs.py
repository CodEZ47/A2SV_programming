class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_dict = defaultdict(int)
        
        for num in nums:
            num_dict[num] += 1
        
        ctr = 0
        for num in nums:
            if num == k - num and num_dict[num] == 1:
                num_dict[num] -= 1
                continue
                
            if num_dict[k-num] > 0 and num_dict[num] > 0:
                ctr += 1
                num_dict[k-num] -= 1
                num_dict[num] -= 1
        
        return ctr