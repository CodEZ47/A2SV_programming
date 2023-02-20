# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ctr = 0
        
        curr = head
        while curr:
            ctr += 1
            curr = curr.next
            
        n = ctr//2
        lst = []
        
        curr = head
        
        for i in range(n):
            lst.append(curr.val)
            curr = curr.next
        
        for i in range(n-1,-1,-1):
            lst[i] += curr.val
            curr = curr.next
            
        return max(lst)