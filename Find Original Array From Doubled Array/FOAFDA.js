/**
 * @param {number[]} changed
 * @return {number[]}
 */

var findOriginalArray = function(changed) {
    if(changed.length % 2 != 0) return [];
    let newArr = [];
    changed.sort(function(a, b){return a-b});
    
    const map = new Map();
    
    for(let i = 0; i < changed.length; i++) {
        if(map.has(changed[i])) {
            map.set(changed[i], map.get(changed[i]) + 1)
        } else {
            map.set(changed[i], 1)
        }
    }
    
    for(let i = 0; i < changed.length; i++){
        
        let val = changed[i];
        
        if(map.get(val) === 0)
            continue;
        
        map.set(val, map.get(val)-1);
        
        let doub = val * 2;
        
        if(map.has(doub) && map.get(doub) >= 1){
            newArr.push(val);
            map.set(doub, map.get(doub) -1);
        }
        
    }
    
    console.log(map);
    if(newArr.length === changed.length/2) {
      return newArr;  
    } else {
        return [];
    }
};
