# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = []
        lst2 = []
        
        curr = l1
        
        while curr:
            lst1.append((str(curr.val)))
            curr = curr.next
            
        curr = l2
        
        while curr:
            lst2.append((str(curr.val)))
            curr = curr.next
            
        lst1.reverse()
        lst2.reverse()
        lst1 = int("".join(lst1))
        lst2 = int("".join(lst2))
        
        ans = lst1 + lst2
        if ans == 0:
            head = ListNode(0)
            return head
        
        head = None
        while ans:
            if not head:
                head = ListNode(ans%10)
                curr = head
                ans = ans // 10
                continue
            curr.next = ListNode(ans%10)
            curr = curr.next
            ans = ans // 10
        
        return head