/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} threshold
 * @return {number}
 */
var numOfSubarrays = function(arr, k, threshold) {
    let sum = avg = p1 = p2 = ctr = 0;
    
    while(p2 < k){
        sum += arr[p2]
        p2++;
    }

    avg = sum/k;
    avg >= threshold? ctr++: ctr = ctr;

    while(p2 < arr.length){

        sum -= arr[p1];
        p1++;
        sum += arr[p2];
        p2++;

        avg = sum/k;
        avg >= threshold? ctr++: ctr = ctr;   

    }

    return ctr;

};
