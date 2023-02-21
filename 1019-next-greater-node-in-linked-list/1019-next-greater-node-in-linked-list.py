# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stk = [head]
        
        curr = head.next
        
        
        while curr:
            # print(stk)
            if curr.val <= stk[-1].val:
                stk.append(curr)
            else:
                # print("h")
                while stk and stk[-1].val < curr.val:
                    stk[-1].val = curr.val
                    stk.pop()
                stk.append(curr)
            curr = curr.next
        while stk:
            # print(stk)
            stk[-1].val = 0
            stk.pop()
            
        curr = head
        stk = []
        while curr:
            stk.append(curr.val)
            curr = curr.next
            
        return stk