class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        val = Counter(arr)

        return len(val.values()) == len(set(val.values()))