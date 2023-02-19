# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        comp = head.next
        dummy = ListNode()
        dummy.next = head
        
        
        
        while comp:
            temp = comp
            comp = temp.next
            temp.next = None
            prev.next = comp
            
            curr = dummy
            # print('head', head)
            while curr != comp:
                # print("curr",curr.val)
                if curr == prev:
                    temp.next = prev.next
                    prev.next = temp
                    prev = temp
                    break
                if temp.val <= curr.next.val:
                    temp.next = curr.next
                    curr.next = temp
                    break
                curr = curr.next
        
        head = dummy.next
        
        return head