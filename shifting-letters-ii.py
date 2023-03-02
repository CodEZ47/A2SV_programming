class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        p_sum = [0]*(n+1)


        # since adding 1 to all nums in [0,0,0] is the same as the prefix sum of [1,0,0]
        for start,end,direction in shifts:
            if direction == 1:
                p_sum[start] += 1
                p_sum[end+1] -= 1
            else:
                p_sum[start] -= 1
                p_sum[end + 1] += 1
            

        #calculate prefix sum

        for i in range(1,n):
            p_sum[i] += p_sum[i-1]
        
        ord_A = ord("a") #base for further calculations
        ans = []

        for i,c in enumerate(s):
            curr = (ord(c) - ord_A + p_sum[i]) % 26 #just incase the input is larger than the 26 range
            ans.append(chr(curr + ord_A))
        
        return "".join(ans)