/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    if(!nums.includes(1)){
        return 0;
    }
    if(!nums.includes(0)){
        return nums.length - 1;
    }

    let p1 = p2 = curr = max = 0;
    let k = 1;
    let lock;

    while(p2 < nums.length){
        if(nums[p2] == 1){
            curr++;
            p2++;
            curr > max ? max = curr: max = max;
            continue;
        }
        if(nums[p2] == 0 && k == 1){
            lock = p2;
            p2++;
            // curr++;
            k--;
            continue;
        }
        if(nums[p2] == 0 && k == 0){
            curr > max ? max = curr: max = max;
            p1 = p2 = lock+1;
            k++;
            curr = 0;
            continue;
        }
    }

    return max;
};
