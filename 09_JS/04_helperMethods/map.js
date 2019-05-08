// var numbers =  [1, 2, 3];

const numbers = [1, 2, 3];
function double(n) {
    return n * 2;
}
// var doubleNumbers = [];
// for ( var i = 0; i < numbers.length ; i++) {
//     doubleNumbers.push(numbers[i]*2)
// }
// console.log(doubleNumbers);


// const doubleNumbers = numbers.map(number => number*2);
// console.log(doubleNumbers);
//
// // const doubleNumbers = numbers.map(double);
// const tripleNumbers = numbers.map(number => {
//     return number * 3;
// });

const new_numbers = [];
for (const number of numbers) {
    new_numbers.unshift(number*2)
}
console.log(new_numbers);

// console.log(doubleNumbers);
// console.log(tripleNumbers);

/*
아래의  pluck 함수를 완성하세요
pluck 함수는 배열과 요소 이름을 인자로 받습니다.
 */

function pluck (array, property) {
    let new_array = [];
    array.map(element => {
        if (element[property]) {
            new_array.push(element[property]);
        }
    });
    console.log(new_array);
}

const paints = [
    {color:"red"},
    {color: "blue"},
    {color:"white"},
    {smell:"ughh"},
];

pluck(paints, "color");
pluck(paints, "smell");

