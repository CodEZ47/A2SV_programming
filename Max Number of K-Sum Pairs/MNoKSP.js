/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    let map = new Map;
    let ans = 0;

    for(let i in nums){
        if(map.has(nums[i])){
            map.set(nums[i], map.get(nums[i])+1);
        }else{
            map.set(nums[i], 1);
        }
    }

    for(let i in nums){
        // console.log(map);
        if(map.get(nums[i]) != 0){
            map.set(nums[i], map.get(nums[i])-1);
            if(map.has(k-nums[i]) && map.get(k-nums[i]) != 0){
                map.set(k-nums[i], map.get(k-nums[i]) - 1);
                ans++;
            }
        }
    }

    console.log(ans);
    return ans;
};
