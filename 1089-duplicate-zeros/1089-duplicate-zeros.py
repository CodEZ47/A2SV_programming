class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_ctr = arr.count(0)
        arr_len = len(arr)
        ind = arr_len - 1
        
        
        
        
        while ind > -1:
            if ind + zero_ctr < arr_len:
                arr[ind + zero_ctr] = arr[ind]

            if arr[ind] == 0: 
                zero_ctr -= 1
                if ind + zero_ctr < arr_len:
                    arr[ind + zero_ctr] = 0
                
            ind -= 1
        
        
        
        
        