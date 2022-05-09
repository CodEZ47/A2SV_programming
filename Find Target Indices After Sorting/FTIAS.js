/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var targetIndices = function(nums, target) {
    let arr = [];
    let ctrBfr = 0;
    let ctrRpt = 0;
    if(nums.includes(target)){
        for(let i in nums){
            if (nums[i] < target){
                ctrBfr += 1;
            }
            else if(nums[i] == target){
                ctrRpt += 1;
            }
        }
        
        for(let i = ctrBfr; i < ctrBfr+ctrRpt; i++){
            arr.push(i);
        }
    }
    
    return arr;
    
};