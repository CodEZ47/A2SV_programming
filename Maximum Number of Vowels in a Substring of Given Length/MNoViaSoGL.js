/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */

let isVow = (l) => {
    switch(l){
        case 'a':
            return true;
        case 'e':
            return true;
        case 'i':
            return true;
        case 'o':
            return true;
        case 'u':
            return true;
        default:
            return false;
            
    }
}
var maxVowels = function(s, k) {
    let curr = max = p1 = p2 = 0;
    
    while(p2 < k){
        // console.log(s[p2]);
        if(isVow(s[p2])){
            curr++;
        }
        p2++;
        curr > max? max = curr: max = max;
    }

    while(p2 < s.length){
        if(isVow(s[p1])){
            curr--;
        }
        p1++;

        if(isVow(s[p2])){
            curr++;
        }
        p2++;
        curr > max? max = curr: max = max;      

    }

    return max;

};
