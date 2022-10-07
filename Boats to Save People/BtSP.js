/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function(people, limit) {
    people.sort(function(a, b){return a-b});
    console.log(people);

    let r = people.length-1;
    let l = 0;
    let ctr = 0;

    while(l <= r){
        if(people[l] == limit){
            ctr++;
            l++;
            continue;
        }
        if(people[r] == limit){
            ctr++;
            r--;
            continue;
        }
        if(r == l){
            ctr++;
            l++;
            continue;
        }
        if(people[l] + people[r] <= limit){
            l++;
            r--;
            ctr++;
        }else{
            r--;
            ctr ++;
        }
    }

    return ctr++;
};
