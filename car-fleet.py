class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stk = []
        A = sorted(zip(position,speed))
        A.reverse()
        print(A)

        for d,v in A:
            dist_left = target - d
            time_left = dist_left / v
            if not stk:
                stk.append(time_left)
            elif dist_left / v > stk[-1]:
                stk.append(time_left)
        
        return len(stk)