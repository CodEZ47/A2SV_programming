class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pre = [0] * 101


        for log in logs:
            pre[(log[0] - 1950)] += 1
            pre[(log[1] - 1950)] -= 1
        

        for i in range(100):
            pre[i+1] += pre[i]

        maxi = 0
        idx = 0

        for i in range(101):
            if pre[i] > maxi:
                maxi = pre[i]
                idx = i

        return idx + 1950
        