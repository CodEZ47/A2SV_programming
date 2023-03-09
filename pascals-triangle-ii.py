class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def calc(i):
            if i == 0:
                return [1]
            
            arr = calc(i-1)

            arr2 = [1]*(len(arr)+1)

            for i in range(1,len(arr2)-1):
                arr2[i] = arr[i-1] + arr[i]
            
            return arr2
        
        return calc(rowIndex)