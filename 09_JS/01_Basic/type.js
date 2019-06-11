typeof 1; // "number"
typeof (typeof 1); // "string"
typeof (() => {}); // "function"
typeof (function () {});  //"function"
typeof (NaN); // "number"
typeof infinity; // "number"
typeof 100/0; // "NaN" (number)
typeof -100/0; // "NaN" (number)
typeof ("123" + 1);  // "string" "1231"
typeof ("123"-1); // "number" 122
typeof ("123"*2); // "number" 나누기도 같다,
typeof undefined; // "undefined"
typeof null; // "object"
typeof []; // "object"
typeof {}; // "object"


// const exampleObject = {
//     name : " 권성령 ",
//     "favorite foods" : {
//     Korean : "Chicken Feet",
//         Japanese : "Susi",
//         Chinese : "Japchae bap",
// },
// intro : function () {
//     return `안녕~ ${this.name}이라구 해 별명은 또롬이야~ `
// },
// };

const delayedPrint = function () {
    setTimeout ( () => { return "Hello~"} , 1000 )
};
console.log(delayedPrint());