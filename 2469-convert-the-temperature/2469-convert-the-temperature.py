class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = [0,0]
        
        ans[1] = ((celsius*9)/5) + 32
        ans[0] = celsius + 273.15
        
        return ans