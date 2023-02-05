class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int(''.join(map(str, digits))) 
        n += 1
        
        lst = []
        while n > 0:
            lst.append(n % 10)
            n = n // 10
        
        lst.reverse()
        
        return lst