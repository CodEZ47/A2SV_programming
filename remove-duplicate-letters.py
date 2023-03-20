class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        sdict = Counter(s)
        sset = set()
        stk = []

        for char in s:
          if char not in sset:
            while stk and stk[-1] > char and sdict[stk[-1]] > 0:
                sset.remove(stk.pop())
            stk.append(char)
            sset.add(char)
          sdict[char] -= 1
        
        print(stk)
        return "".join(stk)