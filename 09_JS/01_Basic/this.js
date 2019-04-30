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

console.log(me.intro());
console.log(you.wait());

// 파이썬 객체 : object 자바스크립트 객체 : dictionary