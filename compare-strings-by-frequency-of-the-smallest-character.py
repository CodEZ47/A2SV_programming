class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def f(s):
            for i in range(len(s)):
                tdict = Counter(s[i])
                s[i] = tdict[min(tdict.keys())]
            return s
        queries = f(queries)
        words = f(words)
        words.sort()

        for i, q in enumerate(queries):

            l,r = 0,len(words)
            while l < r:
                mid = (l+r) >> 1

                if words[mid] > q:
                    r = mid
                else:
                    l = mid + 1

            queries[i] = len(words) - l
        
        return queries