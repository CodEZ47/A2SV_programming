#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        return arr[i]
    def selectionSort(self, arr,n):
        #code here
        temp = 0

        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if arr[j] <= arr[i]:
                    temp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = temp
                
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
