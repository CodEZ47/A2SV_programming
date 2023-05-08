class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = Counter(nums)
        arr = list(nums_dict.items())

        def quickSort(start,end,arr):
            if start >= end:
                return

            left,right = start,end
            p = (left+right)//2
            pivot = arr[p][1]

            while left <= right:
                while left <= right and arr[left][1] < pivot:
                    left += 1
                while left <= right and arr[right][1] > pivot:
                    right -= 1
                
                if left <= right:
                    arr[left],arr[right] = arr[right],arr[left]
                    left += 1
                    right -= 1
            
            quickSort(start,right,arr)
            quickSort(left,end,arr)
        
        quickSort(0,len(arr)-1,arr)
        ans = []

        for i in range(k):
            temp = arr.pop()
            ans.append(temp[0])

        return ans