class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        prod = 1
        prod_without_zero = 1
        ctr = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                ctr += 1
                continue
            prod *= nums[i]
        
        for i in range(len(nums)):
            if ctr > 1:
                return [0]*len(nums)
            if nums[i] != 0 and ctr == 0:
                answer.append(prod//nums[i])
            if ctr == 1:
                if nums[i] != 0:
                    answer.append(0)
                else:
                    answer.append(prod)



        return answer