// function makeArticle (id, title, content) {
//     return {
//         id: id,
//         title: title,
//         content: content,
//         makeOne: function () {
//             return `${this.id} 번 글: ${this.title} => ${this.content}`
//         }
//     }
// }

// arrow function 은 callback 함수 만들때만~
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
