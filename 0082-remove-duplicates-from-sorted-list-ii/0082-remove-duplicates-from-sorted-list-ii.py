# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        curr = head
        past = dummy
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                temp = curr.val
                while curr and curr.val == temp:
                    curr = curr.next
                past.next = curr
                continue
            past = past.next
            curr = curr.next
        
        
        
        return dummy.next