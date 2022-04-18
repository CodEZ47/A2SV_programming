/**
 * @param {number} n
 * @return {string[]}
 */
 var fizzBuzz = function(n) {
    let arr = [];
    let num;
    let str = "";
    
    for(let i = 0; i < n; i++){
        
        num = i+1
       
        if (num % 3 == 0 && num % 5 == 0){
            arr[i] = "FizzBuzz";
        }
        else if(num % 5 == 0){
            arr[i] = "Buzz";
        }
        else if (num % 3 == 0){
            arr[i] = "Fizz";
        }
        else {
            str = num.toString();
            arr[i] = str;
        }
    }
    
    return arr;
    
};