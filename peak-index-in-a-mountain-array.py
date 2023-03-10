class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        s = 0
        e = len(arr) - 1
        
        while s <= e:
            mid = (s+e) >> 1

            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] > arr[mid]:
                e = mid - 1
            else:
                s = mid + 1

        return s+1