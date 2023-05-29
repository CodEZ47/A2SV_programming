class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        if n < 2:
            return n

        def calc(i,added):
            if added:
                if (2 * i) + 1 <= n and (2 * i) + 1 >= 2:
                    return nums[i] + nums[i+1]
                return 0
            else:
                if (2 * i) <= n and (2 * i) >= 2:
                    return nums[i]
                return 0
        
        nums = [0,1]

        for i in range(1, n):
            # if i % 2 == 0:
            nums.append(calc(i,0))
            # else:
            nums.append(calc(i,1))
        
        print(nums)
                

        
        return max(nums)