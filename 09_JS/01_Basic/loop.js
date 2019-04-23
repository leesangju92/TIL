let i = 0;

// while loop
while (i < 10) {
    console.log(i);
    i ++ ;
}

// for loop

for (let j = 0; j < 100; j ++) {
    console.log(j);
}


let sum = 0;

for (const number of [1, 2, 3]) {
    sum += number*12;
}
console.log(sum);


for (const char of "HAPPY") {
    console.log(char)
}