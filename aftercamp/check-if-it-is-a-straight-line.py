class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x,y = coordinates[1]
        x2,y2 = coordinates[0]

        if (x-x2) == 0:
            slope = -1000000
        else:
            slope = (y-y2)/(x-x2)

    

        for i in range(1,len(coordinates)):
            x,y = coordinates[i]
            x2,y2 = coordinates[i-1]

            if (x-x2) == 0:
                curr_slope = -1000000
            else:
                curr_slope = (y-y2)/(x-x2)

            if curr_slope != slope:
                return False
        

        return True
