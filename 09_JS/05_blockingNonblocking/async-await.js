
function getUser(id, callback) {
    setTimeout(()=>{
        const users = [
            { id: 1, githubID: 'eduyu' },
            { id: 2, githubID: 'edujohn' },
        ];
        const user = users.find(user => user.id === id);
        console.log('Data Loaded!');
        console.log(user);
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

async function main () {
    try {
        const user = await getUser(1, console.log);
        const repos = await getRepos(user);
        const commits = await getCommits(repos[0]);
        console.log(commits.length);
    } catch (e) {
        console.log(e)
    }

}

main();

// user = getUser(1);
// repos = getRepos(user);
// commits = getCommits(repos[0])

