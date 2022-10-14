/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function(nums, k) {
    let p1 = 0, p2 = 0;
    let len = 1;
    let maxLen = 1;

    if(!nums.includes(1) && k == 0){
        return 0;
    }

    while(p2 < nums.length){

        if(len > maxLen){
            maxLen = len;
        }

        if(nums[p2] == 1){
            len++;
            p2++;
            // continue;
        }

        if(nums[p2] == 0 && k > 0){
            len++;
            p2++;
            k--;
        }
        if(nums[p2] == 0 && k == 0){
            len--;
            p1++;
            nums[p1-1] == 0? k++ : k = k;
        }
    }
    return maxLen;
}
