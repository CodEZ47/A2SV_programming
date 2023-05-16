class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        num_ctr = Counter(nums)
        ends = defaultdict(int)


        for num in nums:
            if num_ctr[num]:
                if ends[num-1]:
                    ends[num-1] -= 1
                    ends[num] += 1
                    num_ctr[num] -= 1
                elif num_ctr[num+1] and num_ctr[num+2]:
                    num_ctr[num+1] -= 1
                    num_ctr[num+2] -= 1
                    ends[num+2] += 1
                    num_ctr[num] -= 1
                else:
                    return False
        
        return True