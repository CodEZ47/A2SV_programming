class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def calc(a, b):
            num1 = a + b
            num2 = b + a
            if num1 > num2:
                return -1
            return 1
        
        nums = [str(i) for i in nums]
        nums.sort(key = cmp_to_key(calc))
        ans = "".join(nums)
        ans = int(ans)
        
        print(ans)
        return str(ans)
            