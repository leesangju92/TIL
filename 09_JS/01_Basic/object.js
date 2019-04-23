const my = {
    name : "leesangju",
    "phone number":"01099285830", // 띄어쓰기가 있는 경우, my.["phone number"]로..
    appleproduct : {
        ipad : "none",
        iphone : "6",
        macbook : "nono",
    }
};


my.name; // leesangju

my[name]; // leesangju

my["phone number"]; // 01099285830

my.appleproduct; // 딕셔너리 나옴

my.appleproduct.iphone // 6