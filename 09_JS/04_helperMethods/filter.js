// var products = [
//     {name: "cucumber", type:"vege",},
//     {name: "banana", type:"fruit",},
//     {name: "carrot", type:"vege",},
//     {name: "tomato", type:"fruit",},
// ];
//
// var fruits = [];
//
// for ( var i = 0; i < products.length; i++) {
//     if (products[i].type === "fruit") {
//         fruits.push(products[i])
//     }
// }
// console.log(fruits);


const products = [
    {name: "cucumber", type:"vegetable",},
    {name: "banana", type:"fruit",},
    {name: "carrot", type:"vegetable",},
    {name: "tomato", type:"fruit",},
];

const delayedPrint = function () {
    setTimeout ( () => {
        setTimeout( () => console.log("bye~"), 1000);
        console.log("hello~")
        }, 1000 )
};

delayedPrint();


console.log(products.filter(product => product.type = "vegetable"));
//
// console.log(products.filter( (product) => {
//     if (product.type === "vegetable") {
//         return product
//     }
// }));
// ​
// console.log(products.filter(product => product.type === "vegetable").map(res => res.name));
// // const veges = map();
// // console.log(veges);
//
// const array1 = [1, 4, 9, 16];
// const map1 = array1.map(x => x * 2);
// console.log(map1);
//
// const users = [
//     { id: 1, admin:true },
//     { id: 2, admin:false },
//     { id: 3, admin:false },
//     { id: 4, admin:true },
//     { id: 5, admin:false },
// ];
//
// const new_users = users.filter( user => user.admin);
// console.log(new_users);
