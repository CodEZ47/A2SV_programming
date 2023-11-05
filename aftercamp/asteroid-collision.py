class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        n = len(asteroids)

        for i in range(n):
            if not stk or stk[-1] < 0 or stk[-1] > 0 and asteroids[i] > 0:
                stk.append(asteroids[i])
            
            else:
                while stk and stk[-1] > 0 and abs(stk[-1]) < abs(asteroids[i]):
                    stk.pop()
                
                
                if stk and stk[-1] > 0:
                    if abs(stk[-1]) > abs(asteroids[i]):
                        continue
                    else:
                        stk.pop()
                else:
                    stk.append(asteroids[i])
        

        return stk
                