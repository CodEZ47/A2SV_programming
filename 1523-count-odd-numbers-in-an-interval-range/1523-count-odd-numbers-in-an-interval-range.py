class Solution:
    def countOdds(self, low: int, high: int) -> int:
        output = (high-low) // 2
        
        
        output += (high%2 or low%2)
        
        return output