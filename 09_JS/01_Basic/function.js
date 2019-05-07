// 1
function add (num1, num2) {
    return num1 + num2;
}
// 2
const sub = function (num1, num2) {
    return num1 - num2;
};
add(1,2 );
sub(10, 3);
// 3 - 1
let multi = function (num1, num2) {
    return num1 * num2;
};
// 1. function 키워드를 없앤다. 2. 괄호와 중괄호 사이에 => 를 넣는다
multi = (num1, num2) => { return num1*num2 };
/*
    step 1 : 인자가 단 하나라면 괄호가 생략가능하다
    step 2 : 함수 블록 안에 코드가 return문 한줄이라면 return 키워드, 중괄호 삭제 가능하다. 중괄호 쓰면 return도 반드시 같이 써야함
 */

// 3 - 2
let square = function (num) {
    return num**2
};
square = num => num**2;
// console.log(square(2));
let noArgs = () => {
    return "nothing"
};

noArgs = () => "nothing";
oneArgs = (a) => "one";
manyArgs = (a,b,c,d,e) => "many";

function sayhello(name) {
    return `hi ${name}`
}

const Say = name => `hi ${name}`;

// console.log(Say("sangju"));
// const Say = (name="ssafy") => `hi ${name}`;
// (name="ssafy") => `hi ${name}`; 익명함수
// (num => num**2)(4); 익명함수 실행방법
console.log(((name="ssafy") => `hi ${name}`)("하이하이"));