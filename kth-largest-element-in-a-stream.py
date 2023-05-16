class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        # for i in range(len(nums)):
        #     self.nums.append(-1*nums[i])
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
    def add(self, val: int) -> int:
        # print(self.nums)
        if len(self.nums) < self.k:
            heapq.heappush(self.nums,val)
        elif val > self.nums[0]:
            heapq.heappushpop(self.nums, val)

        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)