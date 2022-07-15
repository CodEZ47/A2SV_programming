/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
const run = (str = '') => {
   const map=new Map();
   map.set('{','}');
   map.set('(',')');
   map.set('[',']');
   const b=[];
   for(let i=0;i<str.length;i++){
      if(map.has(str.charAt(i))){
         b.push(str.charAt(i));
      } else{
         let pop=b.pop();
         if(map.get(pop)!==str.charAt(i)){
            return false;
         }
      };
   };
   return b.length===0;
};
    
let result = run(s);
return result;
};
