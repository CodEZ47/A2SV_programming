/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let sumr = 0;
    let suml = 0;
    let j = nums.length-1;
    let i = 0;

    while(j > i){
        sumr = sumr + nums[j];
        j--;
    }
    while(i < nums.length){
        // console.log('suml:' + suml);
        // console.log('sumr:' + sumr);
        if(suml == sumr){
            return i;
        }
        suml = suml + nums[i];
        i++;
        sumr = sumr - nums[i];
    }
    
    return -1;
    
};
