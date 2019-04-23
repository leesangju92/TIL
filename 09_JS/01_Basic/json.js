const myobject = {
    coffee: "mochalatte",
    icecream: "shootingstar",


};

const jsondata = JSON.stringify(myobject);

const parseData = JSON.parse(jsondata);

parseData;

parseData.coffee; //'mochalatte'
