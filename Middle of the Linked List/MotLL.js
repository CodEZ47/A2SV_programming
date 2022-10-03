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
 var middleNode = function(head) {
    let curr = head;
    let ctr = 0;
    while(curr){
        curr = curr.next;
        ctr++;
    };

    if(ctr == 1){
        return head;
    } else if(ctr%2 == 0) {
        ctr = (ctr/2)+1;
    } else{
        ctr = Math.ceil(ctr/2);
    }

    curr = head;

    while(ctr > 1){
        curr = curr.next;
        ctr--;
    }


    return curr;
};
