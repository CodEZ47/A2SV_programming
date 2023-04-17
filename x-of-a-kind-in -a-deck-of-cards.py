class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # if len(deck) == 1:
            # return False
        dic = Counter(deck)
        lst = list(dic.values())
        if min(lst) == 1:
            return False
        gcd = 0
        if len(lst) >= 2:
            gcd = math.gcd(lst[0],lst[1])

            for i in range(2,len(lst)):
                gcd = math.gcd(gcd,lst[i])
        
        if gcd == 1:
            return False

        return True