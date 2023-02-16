# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ctr = 0 
        curr = head
        
        while curr:
            ctr += 1
            curr = curr.next
            
        if ctr == 1:
            return head
        
        ctr = ctr//2
        curr = head
        
        for i in range(ctr):
            curr = curr.next
            
        return curr