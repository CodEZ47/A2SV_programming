class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_ctr = Counter(words)

        words = word_ctr.items()
        temp = []
        for word in words:
            heapq.heappush(temp,(word[1]*-1, word[0],))

        print(temp)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(temp)[1])
        
        
        return ans