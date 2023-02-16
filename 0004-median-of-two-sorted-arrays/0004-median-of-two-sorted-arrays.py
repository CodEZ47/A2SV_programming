class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        m_ind = ceil(n / 2)
        
        if n == 1:
            temp = nums1 + nums2
            return temp[0]
        if n == 2:
            temp = nums1 + nums2
            return (temp[0] + temp[1]) / 2
        
        l = 0
        r = 0
        mid = 0
        mid2 = 0
        
        for i in range(m_ind):
            print(mid)
            if l >= len(nums1):
                mid = nums2[r]
                mid2 = nums2[r+1]
                r += 1
                continue
            
            if r >= len(nums2):
                mid = nums1[l]
                mid2 = nums1[l+1]
                l += 1
                continue
                
            if nums1[l] <= nums2[r]:
                mid = nums1[l]
                l += 1
                if l < len(nums1):
                    mid2 = min(nums1[l], nums2[r])
                else:
                    mid2 = nums2[r]
            else:
                mid = nums2[r]
                r += 1
                if r < len(nums2):
                    mid2 = min(nums1[l], nums2[r])
                else:
                    mid2 = nums1[l]
            
        if n % 2 == 0:
            return (mid+mid2)/2
        else:
            return mid
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
            