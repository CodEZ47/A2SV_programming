/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var smallerNumbersThanCurrent = function(nums) {
    let arr = [];
    for(let i in nums){
        arr[i] = 0;
    }
    for(let i = 0; i < nums.length; i++){
        for(let j = 0; j < nums.length; j++){
            if(nums[j] < nums[i]){
                arr[i]++;
            }
        }
    }
    
    return arr;
};