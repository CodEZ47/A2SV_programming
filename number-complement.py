class Solution:
    def findComplement(self, num: int) -> int:
        if num == 1:
            return 0
        
        comp = (2 ** math.ceil(math.log(num,2))) - 1

        if comp == num - 1:
            return comp

        return num ^ comp