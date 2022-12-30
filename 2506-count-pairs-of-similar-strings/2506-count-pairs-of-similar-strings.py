class Solution:
    def similarPairs(self, words: List[str]) -> int:
        temp_set1 = ()
        temp_set2 = ()
        temp_set1_len = 0
        set_diff = ()
        words_len = len(words)
        ctr = 0
        
        for i in range(words_len):
            temp_set1 = set(map(str, words[i]))
            temp_set1_len = len(temp_set1)
            
            for j in range(words_len):             
                if i == j:
                    continue
                    
                temp_set2 = set(map(str, words[j]))
                
                if temp_set1_len > len(temp_set2):
                    set_diff = temp_set1.difference(temp_set2)
                else:
                    set_diff = temp_set2.difference(temp_set1)
                    
                # print(temp_set1, temp_set2, set_diff)
                
                if not set_diff:
                    ctr += 1
                    
        return int(ctr/2)