/* 재할당 하는 것과 값이 변화하는 것과는 상관없음 */

const numbers = [1, 2, 3, 4, 5];

let sum = 0;

for (let i = 0; i < numbers.length; i ++ ) {
    sum += numbers[i];
}

console.log(sum);


sum = 0;

for (const number of numbers) {
    sum += number;
}

console.log(sum)

// 할당이면 세미콜론. elseif, for 문에서만 뒤에 세미콜론을 붙이지 않는다.

