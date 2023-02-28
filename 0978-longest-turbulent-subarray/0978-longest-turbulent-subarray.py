class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        inc = 1
        dec = 1
        ans = 1
        
        for i in range(1,len(arr)):
            if arr[i] < arr[i-1]:
                dec = inc + 1
                inc = 1
            elif arr[i] > arr[i-1]:
                inc = dec + 1
                dec = 1
            else:
                inc = 1
                dec = 1
            
            ans = max(ans, max(inc,dec))
        
        return ans