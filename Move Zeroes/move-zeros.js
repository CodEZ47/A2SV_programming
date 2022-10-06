/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let curr = 0;
    let next = curr + 1;
    let temp = 0;

    while(next < nums.length){
        while(nums[curr] != 0 && curr < nums.length){
            curr++;
            next = curr+1;
        }

        if(nums[next] != 0 && next < nums.length){
            temp = nums[next];
            nums[next] = nums[curr];
            nums[curr] = temp;

            curr++;
            next++;
        } else{
            next++;
        }
    }

    return nums;
};
