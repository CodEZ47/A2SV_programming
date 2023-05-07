# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp = head
        head1 = 0
        head2 = 0
        ptr1 = 0
        ptr2 = 0
        print(temp)
        while temp:
            curr = temp.next
            if temp.val < x and not head1:
                head1 = temp
                head1.next = None
                ptr1 = head1
            elif temp.val >= x and not head2:
                head2 = temp
                head2.next = None
                ptr2 = head2
            elif temp.val < x:
                ptr1.next = temp
                ptr1 = temp
                ptr1.next = None
            elif temp.val >= x:
                ptr2.next = temp
                ptr2 = temp
                ptr2.next = None
            
            temp = curr
            
        if not head1 or not head2:
            return head
        if head2:
            ptr1.next = head2
        return head1