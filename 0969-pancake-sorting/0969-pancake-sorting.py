class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n = len(arr)
        
        for i in range(n):
            max_num = max(arr[:n-i])
            max_ind = arr.index(max_num)+1
            
            arr[:max_ind] = reversed(arr[:max_ind])
            ans.append(max_ind)
            
            arr[:n-i] = reversed(arr[:n-i])
            ans.append(n-i)
            
        return ans