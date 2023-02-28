class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        if len(arr) == 2 and arr[0] != arr[1]:
            return 2
        if len(set(arr)) == 1:
            return 1
        
        
        if arr[0] > arr[1]:
            flag = False
        else:
            flag = True
        
        ctr = 1
        maxi = 0
        i= 1
        while i < len(arr)-1:
            if not flag and arr[i] < arr[i+1]:
                ctr += 1
                flag = True
            elif flag and arr[i] > arr[i+1]:
                ctr += 1
                flag = False
            elif arr[i] == arr[i+1]:
                while i < len(arr)-1 and arr[i] == arr[i+1]:
                    i += 1
                    
                if i < len(arr)-1 and arr[i] > arr[i+1]:
                    flag = False
                else:
                    flag = True
                    
                maxi = max(maxi, ctr)
                ctr = 1
            else:
                if i < len(arr)-1 and arr[i] > arr[i+1]:
                    flag = False
                else:
                    flag = True
                    
                maxi = max(maxi, ctr)
                ctr = 1
            i += 1
        
        maxi = max(maxi, ctr) + 1
        
        return maxi