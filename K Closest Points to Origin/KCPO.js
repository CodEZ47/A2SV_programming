/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function(points, k) {
    
    let arr = [];
    let arr2 = [];
    
    for(let i in points){
        arr.push(Math.sqrt((Math.pow(points[i][0],2) + Math.pow(points[i][1],2))));
    }

    const max = Math.max(...arr);
    let index = 0;
    let small = arr[0];
    
    for(let i = 0; i < k; i++){
        for (let j = 0; j < arr.length; j++){
            if(arr[j] <= small){
                small = arr[j];
                index = j;
                arr2[i] = points[j];
            }
        };
        arr[index] = max+1;
        small = max;
        index = 0;

    }
    
    return arr2;
};
