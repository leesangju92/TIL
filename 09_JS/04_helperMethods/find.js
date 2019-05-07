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
    {name: "tony", id:1},
    {name: "captain", id:2},
    {name: "hulk", id:3},
    {name: "hulk", id:4},
];

const a = avengers.find(avenger => avenger.name === "hulk" );
console.log(a.id);