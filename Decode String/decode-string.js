/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    let arr = [];
    let num = [];
    let prev = '';
    let strMul = '';
    let n = '';

    for(let i = 0; i < s.length; i){
        let c = s[i];
        !isNaN(c) ? c = 0: c = c;

        switch(c){
            case (0):
                while(s[i] != '['){
                    n = n.concat(s[i]);
                    i++;
                }
                num.push(parseInt(n));
                n = '';
                console.log(num)
                break;
            case ('['):
                arr.push(strMul);
                strMul = '';
                i++;
                break;
            case (']'):
                prev = arr.pop();
                strMul = prev.concat(strMul.repeat(num.pop()));
                i++;
                break;
            default:
                strMul = strMul.concat(c);
                i++;
                break;
        }
    }

    return strMul;
};
