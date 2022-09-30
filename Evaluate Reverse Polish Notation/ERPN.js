let evalRPN = function(tokens){
    const stack = [];

    const operators = {
        '+': (num1, num2) => num1 + num2,
        '-': (num1, num2) => num1 - num2,
        '*': (num1, num2) => num1 * num2,
        '/': (num1, num2) => num1 / num2,
    }

    for(let token in tokens){
        if(operators[token]){
            let num2 = stack.pop();
            let num1 = stack.pop();

            stack.push(operators[token](num1,num2));
        } else{
            stack.push(token);
        }
    }

    return stack.pop()
}