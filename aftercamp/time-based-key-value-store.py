class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
    
    def bisectLeft(self,arr,targ,n):  
            l = 0
            r = n-1

            while l <= r:
                mid = (l+r) // 2
                
                if arr[mid][1] <= targ:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return l


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timemap[key]
        n = len(arr)

        if n == 0 or arr[0][1] > timestamp:
            return ""
        idx = self.bisectLeft(arr,timestamp,n)

        if idx >= n:
            return arr[-1][0]
        
        # print(arr,idx)
        if arr[idx][1] <= timestamp:
            return arr[idx][0]
        else:
            return arr[idx-1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = self.TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)