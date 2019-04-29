// var avengers = [
//     {name: "tony"},
//     {name: "captain"},
//     {name: "hulk"},
//     {name: "thor"},
// ];
// var avenger;
//
// for ( var i = 0; i < avengers.length ; i++) {
//     if (avengers[i].name == "tony") {
//         avenger = avengers[i];
//         break
//     }
// }

const avengers = [
    {name: "tony"},
    {name: "captain"},
    {name: "hulk"},
    {name: "thor"},
];

const a = avengers.find(avenger => avenger.name === "hulk" );
console.log(a);