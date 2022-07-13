/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let ctr = 0;
    for(let i = 0; i < nums.length; i++){
        for(let j = i; j < nums.length; j++){
            if(nums[i] == nums[j] && j != i){
                ctr++;
            }
        }
    }
    return ctr++;
    
};
