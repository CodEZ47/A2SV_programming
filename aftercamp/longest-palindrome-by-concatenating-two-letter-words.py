class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wordsCtr = Counter(words)
        mid = 0
        tot = 0


        for word in words:
            temp = word[1]+word[0]
            if word[0] == word[1]:
                tot += (wordsCtr[word]//2) * 4
                if wordsCtr[word] % 2 != 0:
                    mid = 2
                wordsCtr[word] = 0
                continue
            tot += min(wordsCtr[word], wordsCtr[temp]) * 4
            wordsCtr[temp] = 0
            wordsCtr[word] = 0

        return tot + mid