



function calc(n,m,a){
    let h = 1;
    let w = 1;
    let temp = a;
    if(a < n){
        while(temp < n){
            temp += a;
            w += 1;
        }
    };
    temp = a;
    if(a < m){
        while(temp < m){
            temp += a;
            h += 1;
        }
    };

    console.log(h*w);
    return h*w;
}
