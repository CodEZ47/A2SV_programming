var chalkReplacer = function(chalk, k) {
    let p = 0;

    while(k > 0){
        if(k < chalk[p]){
            return p;
        }
        k -= chalk[p];
        p == chalk.length - 1 ? p = 0 : p++;
    }
    return p;
};
