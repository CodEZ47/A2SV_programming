class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ctr = 0
        str_len = len(strs[0])        
            
        
        for i in range(str_len):
            temp = strs[0][i]
            # print(temp)
            for word in strs:
                # print(word[i])
                if word[i] < temp:
                    ctr += 1
                    break
                temp = word[i]
                
        return ctr