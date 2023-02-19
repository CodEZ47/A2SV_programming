# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        ctr = 0
        
        if right == left:
            return curr
        
        while curr:
            ctr += 1
            curr = curr.next
        
        curr = head
        prev = head
        for i in range(left - 1):
            curr = curr.next
        
        for i in range(right):
            prev = prev.next
                
        cmp = right - left + 1
        
        for i in range(cmp):
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        if left > 1:
            curr = head
            
            for i in range(left-2):
                curr = curr.next
            
            curr.next = prev
        
        if right == ctr and left != 1:
            return head
        if right == ctr or left == 1:
            return prev
            
        return head