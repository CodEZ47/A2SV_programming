# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        
        h1 = odd
        h2 = even
        # print(next_)
        
        while odd and even:
            odd.next = even.next
            if not even.next:
                break
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        odd.next = h2
        
        return h1
        
        