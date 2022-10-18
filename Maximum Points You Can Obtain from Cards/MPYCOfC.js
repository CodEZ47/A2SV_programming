/**
 * @param {number[]} cardPoints
 * @param {number} k
 * @return {number}
 */
var maxScore = function(cardPoints, k) {
    let tot = sum = curr = max = p1 = p2 = 0;

    for(let i in cardPoints){
        tot += cardPoints[i];
    }

    while(p2 < cardPoints.length-k){
        sum += cardPoints[p2]
        p2++;
    }

    curr = tot - sum;
    curr > max ? max = curr: curr = curr;

    while(p2 < cardPoints.length){
        sum -= cardPoints[p1];
        p1++;
        sum += cardPoints[p2];
        p2++;

        curr = tot - sum;
        curr > max ? max = curr: curr = curr;
    }

    return max;
};
