/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    if(!head || !head.next){
        return head;
    }
    let dummy = new ListNode(-Infinity, head);
    let prev = dummy;
    let curr = head;
    let next = curr.next;

    while(curr){
        if(curr && next && curr.val == next.val){
            while(next && curr.val == next.val){
                next = next.next;
            }

            prev.next = next;
            curr = next;
            next = next ? next.next: null;

        } else {
            prev = curr;
            curr = next;
            next = next? next.next: null;
        }
    }
    // console.log('dummy:')
    // console.log(dummy.next);

    return dummy.next;

};
