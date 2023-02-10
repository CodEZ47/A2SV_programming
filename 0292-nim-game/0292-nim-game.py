class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 != 0 or n < 3:
            return True
        else:
            return False