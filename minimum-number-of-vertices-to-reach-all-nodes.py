class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        return list(set([i for i in range(n)]) - set([r for v, r in edges]))