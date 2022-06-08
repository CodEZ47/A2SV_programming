/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    let swapped = true;
    let temp = 0;
    
    while(swapped == true){
        
        swapped = false;
        for(let i = 1; i < nums.length-1; i++){
            
            if(nums[i] == ((nums[i-1]+nums[i+1])/2)){
                temp = nums[i];
                nums[i] = nums[i+1];
                nums[i+1] = temp;
                
                swapped = true;
            }
        }
    };
    
    return nums;
};
