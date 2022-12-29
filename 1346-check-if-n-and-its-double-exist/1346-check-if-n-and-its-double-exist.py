class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_len = len(arr)
        zer_ctr = 0
        
        for i in range(arr_len):
            curr = arr[i]
            if curr == 0:
                zer_ctr += 1
                
            
            for j in range(arr_len):
                if zer_ctr >= 2:
                    return True
                if curr == arr[j]:
                    continue
                if arr[i] == 2 * arr[j]:
                    # print(arr[i], arr[j])
                    return True
                
        return False