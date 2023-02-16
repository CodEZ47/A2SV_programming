# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        ctr = 0
        
        while slow and fast and fast.next:
            if fast == slow and ctr != 0:
                return True
            ctr = 1
            slow = slow.next
            fast = fast.next.next
        
        
        return False
            