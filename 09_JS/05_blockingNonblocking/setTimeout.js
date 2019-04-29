// const logEnd = () => {
//     console.log("end");
// };
//
// console.log("start");
// setTimeout(logEnd, 3000);
// // console.log("end");

function sleep_3s () {
    setTimeout(() => console.log("wake up!"), 3000)
}


console.log("start sleep");
sleep_3s();
console.log("end");