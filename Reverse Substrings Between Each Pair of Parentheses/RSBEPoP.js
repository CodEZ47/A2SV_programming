var reverseParentheses = function(s) {
    let arr = [];
    let strRev = '';
    let prev = '';

    for(let char of s){
        switch(char){
            case '(':
                arr.push(strRev);
                strRev = '';
                break;
            case ')':
                prev = arr.pop();
                strRev = prev.concat(strRev.split('').reverse().join(''));
                break;
            default:
                strRev = strRev.concat(char);
                break;
        }
    }

    return strRev;
};