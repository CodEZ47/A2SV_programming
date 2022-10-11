/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let sum = 0;
    let ctr =  0;
    let i = 0;

    if(nums.length == 0){
        return ctr;
    }

    let map = new Map();
    map.set(0,1);

    while(i < nums.length){
        sum += nums[i];
        if(map.has(sum - k)){
            ctr += map.get(sum-k);
        }
        if(map.has(sum)){
            map.set(sum, map.get(sum)+1);
        }else{
            map.set(sum, 1);
        }

        i++;
    }

    return ctr;
};
