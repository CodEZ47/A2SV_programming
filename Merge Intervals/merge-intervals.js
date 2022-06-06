/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
 var merge = function(intervals) {
    let chk = true;
    let ctr = 0;
    let copy = [];
     
    intervals.sort(function (a, b) {
        return a[0] - b[0];
    });
     
    
    while(chk == true){
        ctr = 0;
        copy = [];
        for(let i = 0; i < intervals.length; i++){
            if(i != intervals.length - 1){
                if(intervals[i][1] >= intervals[i+1][0]){
                    copy.push([intervals[i][0], (Math.max(intervals[i][1], intervals[i+1][1]))]);
                    i++;
                    ctr += 1;
            }
                else{
                    copy.push(intervals[i]);
                }
            }
            else{
                copy.push(intervals[i]);
            }
        }
        
        intervals = [...copy];
        ctr == 0? chk = false: chk = true;
    }
     
    return intervals;
};
