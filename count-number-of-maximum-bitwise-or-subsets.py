class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        length = len(nums)
        ctr = 0
        maxi = 0
        or_dict = defaultdict(int)

        itr = 2 ** length

        for num in range(itr):
            i = length-1
            temp = 0
            while num:
                if num & 1:
                    temp = temp | nums[i]
            
                num = num >> 1
                i -= 1
            
            maxi = max(temp, maxi)
            or_dict[temp] += 1
        
        
        return or_dict[maxi]