class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set()
        
        def gen_par(right,left,arr):
            nonlocal ans
            if right == 0 and left == 0:
                ans.add(''.join(arr))
                return
            
            if right > 0:
                arr.append("(")
                gen_par(right-1,left,arr)
                arr.pop()
            if left > 0 and left > right:
                arr.append(")")
                gen_par(right, left-1, arr)
                arr.pop()
        
        gen_par(n-1,n,["("])

        return ans