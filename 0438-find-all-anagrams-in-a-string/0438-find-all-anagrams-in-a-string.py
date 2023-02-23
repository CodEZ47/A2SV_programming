class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        let_dict = Counter(p)
        comp_dict = defaultdict(int)
        length = len(p)   
        l = 0
        ans = []
        
        for i in range(len(s)):
            comp_dict[s[i]] += 1
            
            if ((i - l)+1) > length:
                comp_dict[s[l]] -= 1
                if comp_dict[s[l]] == 0:
                    del comp_dict[s[l]]
                l += 1
            if comp_dict == let_dict:
                ans.append(l)
        
        return ans
            