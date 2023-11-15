class Solution:
    def minTimeToType(self, word: str) -> int:
        dic = defaultdict(int)
        for i in range(26):

            dic[chr(ord("a")+i)]= i + 1
        

        tot = 0

        curr = abs(dic["a"] - dic[word[0]])
        tot += min(curr, 26 - curr)+1


        for i in range(1,len(word)):
            curr = abs(dic[word[i-1]] - dic[word[i]])
            tot += min(curr, 26 - curr)+1


        
        return tot
