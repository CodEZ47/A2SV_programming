class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n_str = str(n)
        sum_ = 0
        for i in range(len(n_str)):
            if i % 2 == 0:
                sum_ += int(n_str[i])
            else:
                sum_ -= int(n_str[i])
        
        return sum_