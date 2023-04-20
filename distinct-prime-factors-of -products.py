class Solution(object):
    def distinctPrimeFactors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def prime(n,factorization):
            d = 2

            while d * d <= n:
                while n % d == 0:
                    factorization.add(d)
                    n //= d
                d += 1
            if n > 1:
                factorization.add(n)
            
        factorization = set()
        for num in nums:
            prime(num,factorization)


        return len(factorization)
        # return