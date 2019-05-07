// function addAll(a, b, c, d, e) {
//     const numbers = [a, b, c ,d ,e];
//     let sum = 0;
//     for (const number of numbers) {
//         sum += number;
//     }
//     return sum;
// }

//rest operator
function addAll(...numbers) {
    let sum = 0;
    for (const number of numbers) {
        sum += number;
    }
    return sum;
}

console.log(addAll(1,2,3,4,5));

const a1 = [1, 2, 3, 4];
const a2 = [5, 6, 7, 8];
// a1+a2 = '1,2,3,45,6,7,8'
// const a3 = [...a1, ...a2]
function combine(numbers1, numbers2) {
    return [...numbers1, ...numbers2]
}

console.log(a1.concat(a2));

console.log(combine(a1, a2)) //
function first0last100(numbers) {
    return [0, ...numbers ,100]
}

console.log(first0last100(a1)) //