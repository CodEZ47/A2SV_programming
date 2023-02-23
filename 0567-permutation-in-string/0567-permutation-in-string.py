class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        j = len(s2)-k
        dict_comp = defaultdict(int)
        dict_let = Counter(s1)
        
        for i in range(j+1):
            window = s2[i:k+i]
            dict_comp = Counter(window)
            if dict_comp == dict_let:
                return True
        
        return False