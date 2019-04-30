function waitNSeconds(n) {
    return new Promise( resolve => {
        setTimeout(() => {
                console.log(`${n} second(s) passed`);
                resolve()
        }, n * 1000)
    });
}

// function waitFor10Seconds() {
//     waitNSeconds(1)
//         .then(() => waitNSeconds(2))
//         .then(() => waitNSeconds(3))
//         .then((() => waitNSeconds(4)))
//         .then(() => console.log("total 10 seconds!"));
// }

async function waitFor10Seconds() {
    await waitNSeconds(1);
    await waitNSeconds(2);
    await waitNSeconds(3);
    await waitNSeconds(4);
    console.log("total 10 seconds!");
}

waitFor10Seconds();