# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ctr = 0
        curr = head
        
        while curr:
            curr = curr.next
            ctr += 1
        
        if n == ctr:
            head = head.next
            return head
        
        k = ctr - n - 1
        
        curr = head
        
        for i in range(k):
            curr = curr.next
        
        curr.next = curr.next.next
        
        return head