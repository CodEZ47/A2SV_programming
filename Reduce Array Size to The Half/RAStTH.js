/**
 * @param {number[]} arr
 * @return {number}
 */
var minSetSize = function(arr) {
    let map = new Map;
    let rep = [];
    let len = ans = 0;

    for(let i in arr){
        if(map.has(arr[i])){
            map.set(arr[i], map.get(arr[i])+1);
        }else{
            map.set(arr[i], 1);
        }
    }

    for(let i of map.values()){
        rep.push(i);
    }

    rep.sort((a,b) => a-b);


    while(len < arr.length/2){
        len += rep.pop();
        ans++;

    }
    
    return ans;
};
