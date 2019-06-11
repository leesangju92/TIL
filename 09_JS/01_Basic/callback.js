function myFunc () {
    return n => n+1;
}

const num_101 = myFunc()(100);      // 101을 저장하세요.
console.log(num_101);
console.log("wowbod");

const numbersEachAdd = numbers => {
    let sum = 0;
    for (const number of numbers) {
        sum += number;
    }
    return sum
};
console.log(numbersEachAdd(numbers=[1,2,3,4,5]));

const numbersEachSub = numbers => {
    let acc = 0;
    for (const number of numbers) {
        acc -= number;
    }
    return acc
};
console.log(numbersEachSub(numbers=[1,2,3,4,5]));

// 숫자로 이루어진 배열의 원소들을 각각 {???} 한다. {???}는 알아서.

const numbersEach = (numbers, callback) => {
    let acc; // JS에서는 변수 선언만 가능하다.
    for (const num of numbers) {
        acc = callback(num, acc)
    }
    return acc
};
const adder = (num, sum=0) => sum+num;
const muler = (num, sum=1) => sum*num;
console.log(numbersEach([1,2,3,4,5], muler));

console.log(numbersEach([1,2,3,4,5], (num, sum=0) => sum-num));

