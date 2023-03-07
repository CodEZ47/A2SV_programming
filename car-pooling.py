class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda trips: trips[1])
        trips_dict = defaultdict(int)

        for trip in trips:
            trips_dict[trip[1]] += trip[0]
            trips_dict[trip[2]] -= trip[0]
        
        arr = sorted(trips_dict.items())

        for i in range(len(arr)):
            arr[i] = arr[i][1]
        
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
            
        for num in arr:
            if num > capacity:
                return False
        
        return True