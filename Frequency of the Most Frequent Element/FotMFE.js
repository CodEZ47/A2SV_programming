/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxFrequency = function(nums, k) {
    nums.sort(function(a, b){return b-a});
    
    let n = 0, max = 0, prev = 0;
    let temp = 0;
    // console.log(nums)
    for(let i = 0; i < nums.length; i++){
        
        while(n < nums.length && nums[i] - nums[n] <= k){
            k -= (nums[i] - nums[n]);
            
            max = Math.max(max,n-i+1);
            prev = n;
            n++;
        }
        
        if(i<nums.length-1){
            k += (nums[i]-nums[i+1])*(prev-i);
        }
    }
    
    return max;
};
