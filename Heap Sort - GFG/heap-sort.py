#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    
    def heapifyUp(self,arr,current):
        parent = (current-1)//2

        while current:
            if arr[current] < arr[parent]:
                arr[current],arr[parent] = arr[parent],arr[current]
                current = parent
                parent = (current-1)//2
            else:
                break
            
    def heapifyDown(self,arr, n, current):
        right = (2*current)+2
        left = (2*current)+1
        min = 0
    
        while right < n or left < n:
            if left >= n:
                min = right
            elif right >= n:
                min = left
            elif arr[right] >= arr[left]:
                min = left
            else:
                min = right
            
            if arr[current] > arr[min]:
                arr[current],arr[min] = arr[min],arr[current]
                current = min
                right = (2*current)+2
                left = (2*current)+1
                continue
            break
        
    def heapPush(self,arr,v):
        arr.append(v)
        current = len(arr) - 1
        self.heapifyUp(arr,current)
        
    def heapPop(self,arr):
        if not arr:
            return None
        min_value = arr[0]
        arr[0] = arr[-1]
        arr.pop()
        current = 0
        self.heapifyDown(arr,len(arr),current)
        return min_value
        
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        newArr = []
        for val in arr:
            self.heapPush(newArr,val)
        return newArr
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.arr = self.buildHeap(arr.copy(),n)
        ans = []
        while self.arr:
            ans.append(self.heapPop(self.arr))
        
        for i in range(n):
            arr[i] = ans[i]
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends