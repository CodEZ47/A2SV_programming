/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let sumr = 1, suml = 1;
    let arrR = [];
    let arrL = [];
    let answer = [];

    for(let i in nums){
        suml = nums[i] * suml;
        arrL.push(suml);
    }
    for(let i = nums.length-1; i >= 0; i--){
        sumr = nums[i] * sumr;
        arrR[i] = sumr;
    }

    for(let i = 0; i < nums.length; i++){

        if(i == 0){
            answer.push(arrR[i+1]);
            continue;
        }
        if(i == nums.length-1){
            answer.push(arrL[i-1]);
            continue;
        }
        answer.push(arrR[i+1] * arrL[i-1]);
    }
    
    return answer;
};
