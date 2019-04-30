// // 비동기 함수 하나 있다면 다 꼬인다. return문이 거의 쓸모 없어짐.
//
// function listUsers() {
//     setTimeout(()=> {
//         const users = [
//         { id : 1, githubID : "Lee Sang Ju" },
//         { id : 2, githubID : "eduYuu" }
//         ]
//     }, 2000);
// }
//
// function getUser(id, callback) {
//     setTimeout(() => {
//         // const user = users.find(user => user.id === id);
//         const users = [
//             { id : 1, githubID : "Lee Sang Ju" },
//             { id : 2, githubID : "eduYuu" }
//         ];
//         const user = users.find(user => user.id === id);
//         console.log("Data Loaded!");
//         console.log(user);
//         callback(user);
//         // return users.find(user => user.id === id)
//         // return user
//     }, 2000)
// }
//
// const getRepos = (user, callback) => {
//     setTimeout(() => {
//         const repos = [
//             "TIL",
//             "Python",
//             "JS",
//         ];
//         callback(repos)
//     }, 2000)
// };
//
//
// console.log("start program");
// getUser(1,  user => {
//     console.log(user);
//     console.log("EOP");
// });
// const user = {id:1, githubID:"eduYu"};
// getRepos(user, (repos) => {
//     console.log(repos)
// });
//
// function getCommits(repo, callback) {
//     const commits = [
//         "Init Repo",
//     "Make index. html"
//     ];
//     setTimeout(() => {
//     console.log("Data Loaded");
//     console.log(commits);
//     callback(repo);
//     }, 2000)
// }

function getUser(id, callback) {
    setTimeout(()=>{
        const users = [
            { id: 1, githubID: 'eduyu' },
            { id: 2, githubID: 'edujohn' },
        ];
        const user = users.find(user => user.id === id);
        console.log('Data Loaded!');
        console.log(user);
        callback(user);
    }, 2000)
}

const getRepos = (user, callback) => {
    setTimeout(()=>{
        const repos = [
            'TIL',
            'Workshop_HW',
            'Python',
            'JS'
        ];
        console.log('Data Loaded');
        console.log(repos);
        callback(repos)
    }, 2000)
};

function getCommits (repo, callback) {
    setTimeout(()=>{
        const commits = [
            'Init repo',
            'Make index.html'
        ];
        console.log('Data Loaded!');
        console.log(commits);
        callback(commits);
    }, 2000)
}

getUser(1, user => {
    getRepos(user, repos => {
        getCommits(repos[0], commits => {
            console.log(`${commits.length} 개 커밋을 했네요!`)
        })
    })
});

// user = getUser(1);
// repos = getRepos(user);
// commits = getCommits(repos[0])
