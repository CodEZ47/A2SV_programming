class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[],[]]
        loss = defaultdict(int)


        for match in matches:
            w, l = match

            loss[w] += 0
            loss[l] += 1
        

        for key, val in loss.items():
            if val == 0:
                ans[0].append(key)
            if val == 1:
                ans[1].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans

