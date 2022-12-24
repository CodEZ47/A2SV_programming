class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict = {}
        for char in s:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        for char in t:
            if char not in dict or dict[char] == 0:
                return char
            if char in dict and dict[char] > 0:
                dict[char] -= 1