# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        past = head
        curr = head.next
        
        while curr:
            if past.val == curr.val:
                past.next = None
                curr = curr.next
                continue
            past.next = curr
            past = curr
            curr = curr.next
        
        return head