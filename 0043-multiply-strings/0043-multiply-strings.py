class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        temp = []
        res = 1
        string = ""
        for ind in num1:
            temp.append(ord(ind) - ord("0"))
            
        temp = sum(d * 10**i for i, d in enumerate(temp[::-1]))
        res *= temp
        temp = []
        
        for ind in num2:
            temp.append(ord(ind) - ord("0"))
            
        temp = sum(d * 10**i for i, d in enumerate(temp[::-1]))
        res *= temp
        
        while True:
            res, remainder = divmod(res, 10)
            string = chr(ord('0') + remainder) + string
            if res == 0:
                break
                
        return string