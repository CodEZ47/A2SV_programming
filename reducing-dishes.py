class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()

        temp = 0
        total = 0
        prev_sum = 0

        print(satisfaction)

        while satisfaction and prev_sum >= 0:
            total += prev_sum
            temp = satisfaction.pop()
            prev_sum += temp
        
        if prev_sum >= 0:
            total += prev_sum

            
        

        return total