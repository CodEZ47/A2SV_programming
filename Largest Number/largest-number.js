/**
 * @param {number[]} nums
 * @return {string}
 */

var largestNumber = function(nums) {
    
    let str = "";

    nums.sort();
    // console.log(nums);
    further_sort(nums);
    // console.log(nums);
    nums.reverse();
    // console.log(nums);
    if(nums.every(chkZeros)){
        str = "0";
    }
    else{
        for(let i =0; i < nums.length; i++){
    
            str += (nums[i].toString());
        }
    }
    // console.log(str);
    return str;

    
};

function further_sort(nums){
    let temp = 0;
    let str, str2 = "";
    let ctr = 1;
    while(ctr > 0){

        ctr = 0;
        for(let i = 0; i < nums.length - 1; i++){
            str = nums[i].toString();
            str2 = nums[i+1].toString();
            if (str.concat(str2) > str2.concat(str)){
                temp = nums[i];
                nums[i] = nums[i+1];
                nums[i+1] = temp;
                ctr++
            }
        }
    };
    // console.log("number of 0s is " + ctr);
};

function chkZeros(num) {
    return num == 0;
};
