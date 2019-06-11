const numbers = [1, 2, 3, 4];

numbers[0]; // 1
numbers[-1]; // undefined(모르겠는데요)

numbers.length; // 4

/* 원본이 달라지는 method */
numbers.reverse(); // [4, 3, 2, 1]

numbers.push("a"); // [1, 2, 3, 4, "a"]
numbers.pop(); // [1, 2, 3, 4]

numbers.unshift("a"); // ["a", 1, 2, 3, 4]
numbers.shift(); // [1, 2, 3, 4]

/* 복사본을 return 하는 method */


numbers.includes(1); // true
numbers.includes(0); // false

console.log(numbers.push("a", "a"));

numbers.indexOf("a"); // 4 : 가장 앞의 것
console.log(numbers.indexOf("b")); // -1 : 없음

numbers.join(""); // "1234aa"
numbers.join(); // "1,2,3,4,a,a"