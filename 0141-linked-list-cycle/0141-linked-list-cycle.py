# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        num = 10001
        
        curr = head
        
        while num and curr:
            curr = curr.next
            num -= 1
        
        if num == 0:
            return True
        
        return False
            