class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ends = []
        starts = []

        for i, interval in enumerate(intervals):
            ends.append(interval[1])
            starts.append((interval[0],i))
        
        starts.sort()
        print(ends, starts)

        for i, end in enumerate(ends):

            l = 0
            r = len(ends)

            while l < r:
                mid = (l + r) >> 1

                if starts[mid][0] >= end:
                    r = mid
                else:
                    l = mid + 1

            if l >= len(ends):
                ends[i] = -1
            else:
                ends[i] = starts[l][1] 
        
        return ends