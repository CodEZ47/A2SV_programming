class MyQueue{
    constructor(){
        this.popStack = [];
        this.pushStack = [];
    }

    push(elem){
        this.pushStack.push(elem);
    };

    pop(){
        if(!this.popStack.length){
            while(this.pushStack.length){
                this.popStack.push(this.pushStack.pop());
            }
        }
        return this.popStack.pop();
    }

    peek(){
        if(!this.popStack.length){
            while(this.pushStack.length){
                this.popStack.push(this.pushStack.pop());
            }
        }

        return this.popStack[this.popStack.length -1];
    }

    empty(){
        if(!this.popStack.length && !this.pushStack.length){
            return true;
        }
        return false;
    }
}