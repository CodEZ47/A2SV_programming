/**
 * @param {number[]} piles
 * @return {number}
 */
var maxCoins = function(piles) {
    piles.sort((a, b) => a - b);
    let finLen = piles.length/3;
    let sum = 0;
    console.log(piles);

    while(piles.length > finLen){
        piles.pop();
        sum += piles.pop();
    }

    return sum;
};
