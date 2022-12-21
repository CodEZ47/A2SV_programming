class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = []
        fin = []
        s = strs[0]
        
        for char in s:
            pre.append(char)
            
        for word in strs:
            if len(pre) > len(word):
                while(len(pre) > len(word)):
                    pre.pop()
            for i in range(len(pre)):
                # print(i, pre[i])
                if(pre[i] == word[i]):
                    fin.append(pre[i]) 
                else:
                    break
            pre = fin
            fin = []
        
        pre = "".join(pre)
        
        return pre
