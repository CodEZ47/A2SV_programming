class Solution:
    def permute(self, n: List[int]) -> List[List[int]]:
        res = []

        if len(n) == 1:
            return [n.copy()]
        
        for num in n:
            temp = n.pop(0)
            vals = self.permute(n)

            for val in vals:
                val.append(temp)
            
            res.extend(vals)
            
            n.append(temp)

        return res