const products = [
    {name: "cucumber", type:"vegetable",},
    {name: "banana", type:"fruit",},
    {name: "carrot", type:"vegetable",},
    {name: "tomato", type:"fruit",},
];

var vegetables = [];
for ( var i = 0; i < products.length; i++) {
    if (products[i].type === "vegetable") {
        vegetables.push(products[i])
    }
}
console.log(vegetables);