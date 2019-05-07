const numbersEach = (numbers, callback) => {
    let acc;
    for (const num of numbers) {
        acc = callback(num, acc)
    }
    return acc
};
const add = (number, sum=0) => sum + number;

console.log(numbersEach([1, 2, 3, 4, 5], add));


function myFunc () {
    return n => n**2
}
const num_100 =  myFunc(10)();

console.log(num_100);

function makeArticle (id, title, content) {
    return {
        id,
        title,
        content,
        makeOne () {
            return `${this.id} 번 글: ${this.title} => ${this.content}`
        },
    }
}

makeArticle("title" = "첫번째글", "content"="안녕하세요. 반갑습니다.", "id"=1 ).makeOne();