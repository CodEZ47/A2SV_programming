class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr.reverse()
        ans = []
        
        for i in range(len(arr)):
            if i == 0:
                ans.append(-1)
                maxim = arr[i]
                continue
            
            if arr[i-1] > maxim:
                maxim = arr[i-1]
                ans.append(maxim)
            else:
                ans.append(maxim)
        ans.reverse()
        
        return ans
            