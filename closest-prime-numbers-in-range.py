class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(x):
            if x == 1:
                return False
            d = 2
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 1
            return True
        
        primes = []
        mini = 1000000
        curr_primes = [-1,-1]
        for num in range(left,right+1):
            if isPrime(num):
                if primes:
                    if mini > num - primes[-1]:
                        mini = num - primes[-1]
                        curr_primes = [primes[-1], num]
                primes.append(num)

                if mini <= 2:
                    return curr_primes

        
        return curr_primes
        
        