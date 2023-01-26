class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        inc = False
        dec = False
        summit = False

        for i in range(1, len(arr)):
            # print(arr[i], arr[i-1])
            if arr[i] == arr[i-1]:
                inc = False
                break
            if arr[i] > arr[i-1] and dec == True:
                inc = False
                break
            if arr[i] > arr[i-1]:
                inc = True
                continue
            if arr[i] < arr[i-1] and inc != True:
                inc = False
                break
            if arr[i] < arr[i-1] and inc == True and summit == False:
                summit = True
                dec = True
                continue
            if arr[i] < arr[i-1] and inc == True:
                dec = True

        ans = False
        if inc == True and dec == True and summit == True:
            ans = True
        return ans
