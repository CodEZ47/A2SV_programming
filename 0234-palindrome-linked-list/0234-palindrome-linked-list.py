# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        
        curr = head
        
        while curr:
            lst.append(str(curr.val))
            curr = curr.next
        
        lst2 = "".join(lst)
        lst.reverse()
        lst = "".join(lst)
        
        print(lst, lst2)
        if lst2 == lst:
            return True
        
        return False