class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        w1 = list(word1)
        w2 = list(word2)
        temp = []
        
        output = ""
        
        while len(w1) > 0 and len(w2) > 0:
            if w1 > w2:
                output += w1[0]
                w1 = w1[1:]
            else:
                output += w2[0]
                w2 = w2[1:]
        
        output += "".join(w1) + "".join(w2)
        
                
        return output