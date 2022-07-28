var kthLargestNumber = function(nums, k) {
     k = nums.length-k;
     nums.sort((a,b)=>{
         var n1 = BigInt(a);
         var n2 = BigInt(b);
         if(n1>n2)
         {
            return 1;
         }
         else if(n1<n2)
         {
            return -1;
         }
         return 0;
     });
    return nums[k];
};
