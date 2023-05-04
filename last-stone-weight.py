class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        def heapifyDown(arr, n, current):
            right = (2*current)+2
            left = (2*current)+1
            maxi = 0
        
            while right < n or left < n:
                if left >= n:
                    maxi = right
                elif right >= n:
                    maxi = left
                elif arr[right] >= arr[left]:
                    maxi = right
                else:
                    maxi = left
                
                if arr[current] < arr[maxi]:
                    arr[current],arr[maxi] = arr[maxi],arr[current]
                    current = maxi
                    right = (2*current)+2
                    left = (2*current)+1
                    continue
                break
        def heapPop(arr):
            if not arr:
                return None
            max_value = arr[0]
            arr[0] = arr[-1]
            arr.pop()
            current = 0
            heapifyDown(arr,len(arr),current)

        def chk(arr,n):
            maxi = 1
            if n >= 3:
                if arr[1] < arr[2]:
                    maxi = 2
            if n == 1:
                return
            elif arr[0] == arr[maxi]:
                heapPop(arr)
                heapPop(arr)
            elif arr[0] > arr[maxi]:
                arr[0] -= arr[maxi]
                arr[maxi] = arr[-1]
                arr.pop()
                buildHeap(arr,len(arr))
            
        def buildHeap(arr,n):
            for i in range(n // 2 - 1, -1, -1):
                heapifyDown(arr,n,i)
        

        buildHeap(stones,len(stones))
        while len(stones) > 1:
            print(stones)
            chk(stones,len(stones))

        if stones:
            return stones[0]
        return 0