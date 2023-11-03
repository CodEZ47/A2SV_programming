class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        curr = 1

        while l < len(arr) and k > 0:
            if arr[l] == curr:
                l += 1
                curr += 1
            else:
                curr += 1
                k -= 1
        

        if k > 0:
            curr += k
        
        return curr-1