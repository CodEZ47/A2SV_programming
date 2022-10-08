/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
function rev(s,e,nums){
    while(s < e){
        [nums[s], nums[e]] = [nums[e], nums[s]];
        s++;
        e--;
    }
}

var rotate = function(nums, k) {
    nums.reverse();
    k = k % nums.length;

    rev(0, k-1, nums);
    rev(k, nums.length-1, nums);
    console.log(nums);
};
