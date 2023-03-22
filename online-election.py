class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.p = persons
        self.t = times
        self.ans = []
        dic = defaultdict(int)
        maxi = self.p[0]
        dic[maxi] += 1

        for i in range(1,len(self.p)):
            self.ans.append(maxi)
            dic[self.p[i]] += 1

            if dic[self.p[i]] >= dic[maxi]:
                maxi = self.p[i]

        self.ans.append(maxi)
        return



    def q(self, t: int) -> int:
        
        l = 0
        r = len(self.t)

        while l < r:
            mid = (l+r) >> 1

            if self.t[mid] > t:
                r = mid
            elif self.t[mid] < t:
                l = mid + 1
            else:
                return self.ans[mid]
        
        return self.ans[r-1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)