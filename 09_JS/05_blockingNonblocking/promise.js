const getUser = id => {
    const users = [
        { id:1, githubID: "dddddd"},
        { id:2, githubID: "eeeeee"}
    ];
    console.log(id);
    return new Promise( (resolve, reject) => {
        setTimeout(() => {
            const user = users.find(user => user.id === id);
            if (user) resolve(user);
             else reject(new Error(`cant find user ${id}`));
        }, 2000)
    })
};

const getRepos = user => {
    const repos = ["TIL", "Workshop", "Python", "JS"];
    console.log(user);
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (repos) resolve(repos);
            else reject(new Error("No REPOS"))
        }, 1000);
    })
};

const getCommits = repo => {
    const commits = [ "init repo", "Make index.html", "hoyhoy" ];
    console.log(repo);
    return new Promise((resolve, reject) => {
        setTimeout( () => {
            if (commits) {
                resolve(commits);
            } else {
                reject(new Error ("errrrrrrr"))
            }
        }, 2000)
    })
};

getUser(1)
    .then(user => getRepos(user))
    .then(repos => getCommits(repos))
    .then(commits => console.log(commits.length))
    .catch(err => console.log(err));

