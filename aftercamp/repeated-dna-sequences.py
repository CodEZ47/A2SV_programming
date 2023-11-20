class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []

        vis = set()
        repeated = set()
        result = []

        for i in range(n - 9):
            substring = s[i:i + 10]
            if substring in vis:
                repeated.add(substring)
            else:
                vis.add(substring)

        return repeated