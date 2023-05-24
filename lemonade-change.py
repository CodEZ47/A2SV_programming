class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)


        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                if change[5] == 0:
                    return False
                change[10] += 1
                change[5] -= 1
            else:
                if change[10] == 0:
                    if change[5] < 3:
                        return False
                    change[5] -= 3
                elif change[5] == 0:
                    return False
                else:
                    change[10] -= 1
                    change[5] -= 1

        return True