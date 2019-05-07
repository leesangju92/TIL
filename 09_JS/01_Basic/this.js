function hi() {
}

const bus = () => {
};

const me = {
    name : "LSJ",
    phone : "01099275830",
    email : "gmail",
    intro: function () {
        return `Hi my name is ${this.name}`
    }
};

const you = {
    name : "JJY",
    phone : "01099275830",
    email : "gmail",
    // => 는 오류가 발생, 자기 밖을 보려고 한다.
    intro:  () => {
        return `Hi my name is ${this.name}`
    },
    wait: function () {
        setTimeout(() => {
            console.log(this.email)
        }, 1000)
    }
};
//
// console.log(me.intro());
// console.log(you.wait());

// 파이썬 객체 : object 자바스크립트 객체 : dictionary

const myObject = {
    name : "KIM CHUL SOO",
    "favorite foods" : {
        Korean : "bulgogi",
        Japanese : "None",
    },
    intro : () => {
        // 이때 만약 function을 빼먹는다면 this binding이 제대로 작동하지 않는다.
        return `Hi, My name is ${this.name} `
    },
    wait : function (callback) {
        setTimeout ( () => {
            callback();
            // console.log(this["favorite foods"].Korean)
        }, 1000 ) 	// 시간설정에서 단위는 ms이다. 1000ms = 1sec
    },
};

console.log(myObject.intro());