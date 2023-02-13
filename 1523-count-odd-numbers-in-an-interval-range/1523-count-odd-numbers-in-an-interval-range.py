class Solution:
    def countOdds(self, low: int, high: int) -> int:
        output = 0
        
        if low % 2 != 0:
            output += 1
            
        if high % 2 != 0:
            output += 1
            
        diff = high - low - 1
        
        if output == 1:
            output += int(diff/2)
            return output
        if output == 0:
            output += ceil(diff/2)
            return output
        if output == 2:
            output += diff//2
            return output