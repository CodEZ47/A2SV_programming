class Solution:
    def freqAlphabets(self, s: str) -> str:
        temp = ""
        final = ""
        s = list(s)
        
        while(s):
            if(s[-1] != "#"):
                temp += s.pop() 
            else:
                s.pop()
                temp += s.pop() 
                temp += s.pop() 
            
            temp = int(temp [::-1])
            temp = temp + ord("a") - 1
            temp = chr(temp)
            
            final += str(temp)
            temp = ""
        
        final = final [::-1]
        print(final)
        return final