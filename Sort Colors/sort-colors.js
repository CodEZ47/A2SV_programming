/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let ctrRed = 0;
    let ctrWhite = 0;
    let ctrBlue = 0;

    for(let i in nums){
        
        nums[i] == 0? ctrRed++: nums[i] == 1? ctrWhite++: ctrBlue++;
    }
    for(let i in nums){
        if(ctrRed != 0){
            nums[i] = 0;
            ctrRed--;
        } 
        else if(ctrWhite != 0){
            nums[i] = 1;
            ctrWhite--;
        }
        else if(ctrBlue != 0){
            nums[i] = 2;
            ctrBlue--;
        };
    }
    console.log(nums);
};
