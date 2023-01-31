class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        let_dict ={}
        
        for i in range(len(s)):
            if s[i] in let_dict:
                let_dict[s[i]] = i
            else:
                let_dict[s[i]] = i
        
        last_ind = 0
        ctr = 0
        ans = []
        for i in range(len(s)):
            last_ind = max(last_ind, let_dict[s[i]])
            
            if last_ind == i:
                ans.append(ctr+1)
                ctr = 0
                last_ind = 0
            else:
                ctr += 1
        print(ans)
        return ans
                