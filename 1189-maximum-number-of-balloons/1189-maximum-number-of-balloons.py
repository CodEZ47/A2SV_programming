class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # so we need to count how many b a ll oo n for each character
        # condition will be, minimum of (num of b, num of a, num of l/2, num of o/2, num of n/2)
        # hash map of all characters. Another approach is array of 26 and check array since it is small
        # occurance = defaultdict(int)
        # for ch in text:
        #     occurance[ch] += 1
        # numb = occurance['b']
        # numa = occurance['a']
        # numl = occurance['l']//2
        # numo = occurance['o']//2
        # numn = occurance['n']
        # return min(numb, numa, numl, numo, numn)
        occurance = defaultdict(int)
        for ch in 'balon':
            occurance[ch] = 0
        for ch in text:
            if ch in 'balon':
                occurance[ch]+= 1
        occurance['l'] //= 2
        occurance['o'] //= 2
        return min(occurance.values())
            