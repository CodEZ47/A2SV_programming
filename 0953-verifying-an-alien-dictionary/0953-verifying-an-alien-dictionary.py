class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict = {}
        ctr = 0
        words_lst_len = len(words)
        
        for char in order:
            ctr += 1
            dict[char] = ctr
        # print(dict)
        
        for ind in range(words_lst_len - 1):
            w1 = words[ind]
            w2 = words[ind+1]
            w1_len = len(w1)
            w2_len = len(w2)
            
            for ind in range(w1_len):
                if(ind > w1_len-1 and w2[ind] != ""):
                    break
                if(w1[ind] != "" and ind > w2_len-1):
                    return False
                if(dict.get(w1[ind]) > dict.get(w2[ind])):
                    return False
                if(dict.get(w1[ind]) < dict.get(w2[ind])):
                    break
                if(w1[ind] == w2[ind]):
                    continue
                    
        return True