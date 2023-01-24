class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = set(numbers)
        l = len(numbers)
        for i in range(l):
            diff = target - numbers[i]
            # print(diff)
            if diff in nums:
                return [i+1, numbers.index(diff, i+1)+1]
        