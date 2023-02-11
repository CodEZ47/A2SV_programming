# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        ctr = 0
        while curr:
            ctr += 1
            curr = curr.next
        cmp = ctr
        if ctr == 0:
            return
        if ctr == 1:
            return head
        
        while ctr-2 >= 0:
            curr = head
            for i in range(ctr-2):
                curr = curr.next
            temp = curr.next
            temp.next = curr
            curr.next = None
            
            if cmp == ctr:
                head1 = temp
            ctr -= 1
        
        
        
        return head1
            