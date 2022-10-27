/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function(nums) {
    nums.sort((a,b) => a - b);
    let ans = 0;
    let i = temp = 0;
    
    while(i <= nums.length/2){
        temp += nums[i];
        temp += nums[nums.length-1-i];

        if(temp > ans){
            ans = temp;
        }

        temp = 0;
        i++;

    }

    // console.log(nums);
    // console.log(ans);
    return ans;
};
