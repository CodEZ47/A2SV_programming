class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []
        ans = [-1]*len(nums)

        for i in range(len(nums)):
            if not stk:
                stk.append((nums[i],i))
            else:
                if stk[-1][0] > nums[i]:
                    stk.append((nums[i],i))
                else:
                    while stk and stk[-1][0] < nums[i]:
                        ans[stk[-1][1]] = nums[i]
                        stk.pop()
                    stk.append((nums[i],i))
        l = 0
        while stk:
            val = stk.pop()
            while val[0] >= nums[l] and l < val[1]:
                l += 1
            if l == val[1]:
                break
            ans[val[1]] = nums[l]

        return ans