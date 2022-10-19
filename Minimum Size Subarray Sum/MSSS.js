/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let tot = p1 = p2 = 0;
    let len = 1;
    let sum = nums[0];
    let min = Infinity;

    for(let i in nums){
        tot += nums[i];
    }
    // console.log('total sum: ' + tot);

    if(tot < target){
        return 0;
    }

    while(p2 < nums.length && p1 < nums.length){
        console.log(`p1: ${p1} p2: ${p2} len: ${len} sum: ${sum}`);

        if(p1 == p2 && sum >= target){
            return 1;
        }

        if(sum >= target && p1 < p2){
            len < min? min = len: min = min;
            sum -= nums[p1];
            p1++;
            len--;
            continue;
        }

        len++;
        p2++;
        sum += nums[p2];

    }

    return min;
};
