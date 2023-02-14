class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) != len(b):
            max_ = max(len(a), len(b))
            min_ = min(len(a), len(b))
            temp = ""
            
            for i in range(max_ - min_):
                temp += "0"
            
            if len(a) > len(b):
                b = temp + b
            else:
                a = temp + a
        
        p = len(a)-1
        
        ans = []
        carry = "0"
        
        for i in range(p, -1, -1):
            if a[i] == b[i]:
                if a[i] == '0':
                    if carry == '0':
                        ans.append('0')
                    else:
                        ans.append('1')
                        carry = '0'                    
                else:
                    if carry == '0':
                        ans.append('0')
                        carry = '1'
                    else:
                        ans.append('1')
                        carry = '1' 
            else:
                if carry == '1':
                    ans.append('0')
                else:
                    ans.append('1')
                    
        if carry != '0':            
            ans.append(carry)
        ans.reverse()
        
        ans = "".join(ans)
        
        return ans
                