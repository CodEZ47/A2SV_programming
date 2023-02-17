class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        lst1 = []
        lst2 = []
        
        dict_arr = Counter(arr1)
        arr2_set = set(arr2)
        
        for num in arr1:
            if num not in arr2_set:
                lst2.append(num)
        
        i = 0
        for num in arr2:
            while dict_arr[num] > 0:
                lst1.append(num)
                dict_arr[num] -= 1
                i += 1
        
        
        
        lst2.sort()
        
        
        return lst1+lst2