// const logEnd = () => {
//     console.log("end");
// };
//
// console.log("start");
// setTimeout(logEnd, 3000);
// // console.log("end");


// 짧은 시간 내에 확실히 끝낼 수 있는 함수 종류 => blocking 아니면 non-blocking ( back office 로 보내짐)
// back office 에서 신호가 오면 front 에서 call back 함수가 실행된다. 그래서 call back 함수가 필요.
function sleep_3s () {
    console.log("invoke");
    setTimeout(() => console.log("wake up!"), 3000)
}


console.log("start sleep");
sleep_3s();
console.log("end");