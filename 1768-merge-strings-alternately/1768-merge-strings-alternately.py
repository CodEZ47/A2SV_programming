class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        wrd_merg = ""
        wrd1_len = len(word1)
        wrd2_len = len(word2)
        wrd_len_max = 0
        
        
        
        if (wrd1_len >= wrd2_len):
            wrd_len_max = wrd1_len
        else:
            wrd_len_max = wrd2_len
            
        
        for ind in range(wrd_len_max):
            if wrd1_len > 0 and wrd2_len > 0:
                wrd_merg += word1[ind]
                wrd_merg += word2[ind]
                wrd1_len -= 1
                wrd2_len -= 1
            elif wrd1_len > 0:
                wrd_merg += word1[ind]
                wrd1_len -= 1
            elif wrd2_len > 0:
                wrd_merg += word2[ind]
                wrd2_len -= 1
        
        print(wrd_merg)
        return wrd_merg