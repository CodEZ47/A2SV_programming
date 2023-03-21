class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def chk(cap):
          d = 1
          total = 0

          for w in weights:
            total += w
            if total > cap:
              total = w
              d += 1
              if d > days:
                return False
          return True
        

        l = max(weights)
        r = sum(weights)

        while l < r:
          mid = (l+r) >> 1

          if chk(mid):
            r = mid
          else:
            l = mid + 1
        
        return l