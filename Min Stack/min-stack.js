class MinStack{
    constructor(){
        this.stack = [];
        this.minStack = [];
    }

    push(elem){
        if(!this.stack.length || elem < this.minStack[this.minStack.length - 1]){
            this.stack.push(elem);
            this.minStack.push(elem);
        }
        else {
            this.stack.push(elem);
            this.minStack.push(this.minStack[this.minStack.length -1])
        }

    }

    pop(){
        if(!this.stack.length){
            return undefined;
        }
        this.minStack.pop();
        return this.stack.pop();
    }

    top(){
        if(!this.stack.length){
            return undefined;
        }
        return this.stack[this.stack.length - 1];
    }

    getMin(){
        if(!this.minStack.length){
            return undefined;
        }
        return this.minStack[this.minStack.length - 1];
    }
};