/**
 * @param {string} s
 * @return {string}
 */

var sortSentence = function(s) {
    let sentenceArr = [];
    let bool = false;
    let index = 0;
    let i = 0;
    let j = 0;
    
    while(bool == false){

        if (index == s.length+1){
            bool = true;
        }

        if(s[index] <= 9 && s[index] != " " && bool == false){
            i = s[index];
            let str = s.slice(j,(index));
            sentenceArr[i-1] = str;
            j = index+2;

        }
        index += 1;


        
        
    }
    let str = '';
    for(let i in sentenceArr){
        if(i != sentenceArr.length-1){
            sentenceArr[i] = sentenceArr[i]+" ";
        }
        str += sentenceArr[i];
    }
 
    return str;
};
