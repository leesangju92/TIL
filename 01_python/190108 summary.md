# 190108 summary



## 1. Jupyter 

jupyter notebook



less 파일명 : 보기



touch .bashrc 또는 touch .bash_profile



vim .bashrc

i 후 alias 'jn'='jupyter notebook' 등호사에 띄어쓰기 있으면 안됨 이후 esc

echo 'alias "jn"="jupyter notebook"' >> .bashrc 또는

echo 'alias "jn"="jupyter notebook"'  > .bashrc



## 2. git bash & git setting



bash 라고 하면 껏다 켜짐



leesangju92:~/workspace $ pwd
/home/ubuntu/workspace
leesangju92:~/workspace $ ls
README.md
leesangju92:~/workspace $ rm README.md
leesangju92:~/workspace $ touch prj prj_2 prj_1 prj_final prj_final_1 prj_final_jechool prj_real_final
leesangju92:~/workspace $ rm *
leesangju92:~/workspace $ touch prj_0
leesangju92:~/workspace $ touch prj_0.2 prj_1.0 prj_1.1 prj_1.8
leesangju92:~/workspace $ mkdir prj
leesangju92:~/workspace $ cd prj/
leesangju92:~/workspace/prj $ ls
leesangju92:~/workspace/prj $ ls =a
ls: cannot access =a: No such file or directory
leesangju92:~/workspace/prj $ ls -a
./  ../
leesangju92:~/workspace/prj $ ..
leesangju92:~/workspace $ cd prj
leesangju92:~/workspace/prj $ git init
Initialized empty Git repository in /home/ubuntu/workspace/prj/.git/
leesangju92:~/workspace/prj (master) $ rm -rf .git
leesangju92:~/workspace/prj $ git init
Initialized empty Git repository in /home/ubuntu/workspace/prj/.git/
leesangju92:~/workspace/prj (master) $ which git
/usr/bin/git
leesangju92:~/workspace/prj (master) $ cd ~
leesangju92:~ $ ls
lib/  workspace/
leesangju92:~ $ ls -a
./   .bash_aliases  .bashrc  .cache/   .gem/   .gitconfig  .gnupg/    .hgrc    .npmrc  .profile   .ssh/  workspace/
../  .bash_logout   .c9/     .config/  .gemrc  .gitignore  .hgignore  .local/  .nvm/   .profileE  lib/
leesangju92:~ $ cat .git
.gitconfig  .gitignore  
leesangju92:~ $ cat .gitconfig
[user]
​    name = leesangju
​    email = leesangju92@gmail.com
[core]
​    editor = nano
​    whitespace = off
​    excludesfile = ~/.gitignore
[advice]
​    statusuoption = false
[color]
​    ui = true
[push]
​    default = currentleesangju92:~ $ vim .gitconfig
leesangju92:~ $ cat .gitconfig
[user]
​    name = leesangju
​    email = leesangju92@gmail.com
[core]
​    editor = vim
​    whitespace = off
​    excludesfile = ~/.gitignore
[advice]
​    statusuoption = false
[color]
​    ui = true
[push]
​    default = current
leesangju92:~ $ vim .gitconfig
leesangju92:~ $ ls -a
./   .bash_aliases  .bashrc  .cache/   .gem/   .gitconfig  .gnupg/    .hgrc    .npmrc  .profile   .ssh/     lib/
../  .bash_logout   .c9/     .config/  .gemrc  .gitignore  .hgignore  .local/  .nvm/   .profileE  .viminfo  workspace/
leesangju92:~ $ cd workspace/prj/
leesangju92:~/workspace/prj (master) $ git help
usage: git [--version][--help] [-C <path>][-c name=value]
​           [--exec-path[=<path>]][--html-path] [--man-path][--info-path]
​           [-p | --paginate | --no-pager][--no-replace-objects] [--bare]
​           [--git-dir=<path>][--work-tree=] [--namespace=<name>]
​           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout   Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
leesangju92:~/workspace/prj (master) $ ls -a
./  ../  .git/
leesangju92:~/workspace/prj (master) $ cd .git
leesangju92:~/workspace/prj/.git (GIT_DIR!) $ ls -a
./  ../  HEAD  branches/  config  description  hooks/  info/  objects/  refs/
leesangju92:~/workspace/prj/.git (GIT_DIR!) $ cat config 
[core]
​        repositoryformatversion = 0
​        filemode = true
​        bare = false
​        logallrefupdates = true
leesangju92:~/workspace/prj/.git (GIT_DIR!) $ cd ..
leesangju92:~/workspace/prj (master) $ touch first_file.txt
leesangju92:~/workspace/prj (master) $ rm first_file.txt 
leesangju92:~/workspace/prj (master) $ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
leesangju92:~/workspace/prj (master) $ touch first_file.txt
leesangju92:~/workspace/prj (master) $ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        first_file.txt

nothing added to commit but untracked files present (use "git add" to track)
leesangju92:~/workspace/prj (master) $ 

vim 에서 i 또는 a

esc

콜론, q 또는 w(저장)



leesangju92:~ $ vim .gitconfig
leesangju92:~ $ ls -a
./   .bash_aliases  .bashrc  .cache/   .gem/   .gitconfig  .gnupg/    .hgrc    .npmrc  .profile   .ssh/     lib/
../  .bash_logout   .c9/     .config/  .gemrc  .gitignore  .hgignore  .local/  .nvm/   .profileE  .viminfo  workspace/
leesangju92:~ $ cd workspace/prj/
leesangju92:~/workspace/prj (master) $ git help
usage: git [--version] [--help] [-C <path>] [-c name=value]
​           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
​           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
​           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
​           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout   Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
leesangju92:~/workspace/prj (master) $ ls -a
./  ../  .git/
leesangju92:~/workspace/prj (master) $ cd .git
leesangju92:~/workspace/prj/.git (GIT_DIR!) $ ls -a
./  ../  HEAD  branches/  config  description  hooks/  info/  objects/  refs/
leesangju92:~/workspace/prj/.git (GIT_DIR!) $ cat config 
[core]
​        repositoryformatversion = 0
​        filemode = true
​        bare = false
​        logallrefupdates = true
leesangju92:~/workspace/prj/.git (GIT_DIR!) $ cd ..
leesangju92:~/workspace/prj (master) $ touch first_file.txt
leesangju92:~/workspace/prj (master) $ rm first_file.txt 
leesangju92:~/workspace/prj (master) $ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
leesangju92:~/workspace/prj (master) $ touch first_file.txt
leesangju92:~/workspace/prj (master) $ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        first_file.txt

nothing added to commit but untracked files present (use "git add" to track)
leesangju92:~/workspace/prj (master) $ git add .
leesangju92:~/workspace/prj (master) $ git add first_file.txt 
leesangju92:~/workspace/prj (master) $ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   first_file.txt

leesangju92:~/workspace/prj (master) $ git rm -cached first_file.txt 
error: did you mean `--cached` (with two dashes ?)
leesangju92:~/workspace/prj (master) $ git rm --cached first_file.txt                                                                                                                    
rm 'first_file.txt'
leesangju92:~/workspace/prj (master) $ git add first_file.txt 
leesangju92:~/workspace/prj (master) $ git commit -m "first_commit"
[master (root-commit) 5970fba] first_commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 first_file.txt
leesangju92:~/workspace/prj (master) $ git status
On branch master
nothing to commit, working tree clean
leesangju92:~/workspace/prj (master) $ git log
commit 5970fba3c9a37cdfe4b7497c804625041a1dc055 (HEAD -> master)
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 06:43:46 2019 +0000

    first_commit
leesangju92:~/workspace/prj (master) $ 
leesangju92:~/workspace/prj (master) $ 
leesangju92:~/workspace/prj (master) $ 
leesangju92:~/workspace/prj (master) $ echo '출석부' >> first_file.txt 
leesangju92:~/workspace/prj (master) $ cat first_file.txt 
출석부
leesangju92:~/workspace/prj (master) $ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   first_file.txt

no changes added to commit (use "git add" and/or "git commit -a")
leesangju92:~/workspace/prj (master) $ git add ,
fatal: pathspec ',' did not match any files
leesangju92:~/workspace/prj (master) $ git add .
leesangju92:~/workspace/prj (master) $ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   first_file.txt

leesangju92:~/workspace/prj (master) $ echo '부장' >> first_file.txt                                                                                                                    
leesangju92:~/workspace/prj (master) $ git add first_file.txt 
leesangju92:~/workspace/prj (master) $ git satus
git: 'satus' is not a git command. See 'git --help'.

The most similar command is
​        status
leesangju92:~/workspace/prj (master) $ git status                                                                                                                   
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   first_file.txt

leesangju92:~/workspace/prj (master) $ git commit -m "끝말잇기 2개"
[master 4f431af] 끝말잇기 2개
 1 file changed, 2 insertions(+)
leesangju92:~/workspace/prj (master) $ git log
commit 4f431af6071267dc4d5edf443b5e954b2709b610 (HEAD -> master)
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 06:49:29 2019 +0000

    끝말잇기 2개

commit 5970fba3c9a37cdfe4b7497c804625041a1dc055
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 06:43:46 2019 +0000

    first_commit
leesangju92:~/workspace/prj (master) $ ls -a
./  ../  .git/  first_file.txt
leesangju92:~/workspace/prj (master) $ echo '장구' > first_file.txt 
leesangju92:~/workspace/prj (master) $ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   first_file.txt

no changes added to commit (use "git add" and/or "git commit -a")
leesangju92:~/workspace/prj (master) $ git commit -m "??"
On branch master
Changes not staged for commit:
​        modified:   first_file.txt

no changes added to commit
leesangju92:~/workspace/prj (master) $ git log
commit 4f431af6071267dc4d5edf443b5e954b2709b610 (HEAD -> master)
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 06:49:29 2019 +0000

    끝말잇기 2개

commit 5970fba3c9a37cdfe4b7497c804625041a1dc055
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 06:43:46 2019 +0000

    first_commit
leesangju92:~/workspace/prj (master) $ touch second_file.txt
leesangju92:~/workspace/prj (master) $ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   first_file.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        second_file.txt

no changes added to commit (use "git add" and/or "git commit -a")
leesangju92:~/workspace/prj (master) $ git add first_file.txt
leesangju92:~/workspace/prj (master) $ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   first_file.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        second_file.txt

leesangju92:~/workspace/prj (master) $ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   first_file.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        second_file.txt

leesangju92:~/workspace/prj (master) $ git commit -m '끝말잇기 3번째'
[master 199b045] 끝말잇기 3번째
 1 file changed, 1 insertion(+), 2 deletions(-)
leesangju92:~/workspace/prj (master) $ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        second_file.txt

nothing added to commit but untracked files present (use "git add" to track)
leesangju92:~/workspace/prj (master) $ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   first_file.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        second_file.txt

no changes added to commit (use "git add" and/or "git commit -a")
leesangju92:~/workspace/prj (master) $ git add first_file.txt second_file.txt 
leesangju92:~/workspace/prj (master) $ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   first_file.txt
        new file:   second_file.txt

leesangju92:~/workspace/prj (master) $ git commit -m '끝말잇기 4 & second_file 추가'
[master fcdfed5] 끝말잇기 4 & second_file 추가
 2 files changed, 5 insertions(+)
 create mode 100644 second_file.txt
leesangju92:~/workspace/prj (master) $ git log
commit fcdfed55472cdd8886c021f82ee98c23b0573b4c (HEAD -> master)
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 07:19:38 2019 +0000

    끝말잇기 4 & second_file 추가

commit 199b04592774fe41161551a68ecfad22c61e144b
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 07:14:09 2019 +0000

    끝말잇기 3번째

commit 4f431af6071267dc4d5edf443b5e954b2709b610
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 06:49:29 2019 +0000

    끝말잇기 2개

commit 5970fba3c9a37cdfe4b7497c804625041a1dc055
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 06:43:46 2019 +0000

    first_commit
leesangju92:~/workspace/prj (master) $ touch third_file.txt
leesangju92:~/workspace/prj (master) $ echo "졌다" >> third_file.txt 
leesangju92:~/workspace/prj (master) $ echo "졌다" >> first_file.txt                                                                                                                    
leesangju92:~/workspace/prj (master) $ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   first_file.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        third_file.txt

no changes added to commit (use "git add" and/or "git commit -a")
leesangju92:~/workspace/prj (master) $ git add first_file.txt 
leesangju92:~/workspace/prj (master) $ git commit -m "끝말잇기 끝"
[master ae4dec2] 끝말잇기 끝
 1 file changed, 1 insertion(+), 1 deletion(-)
leesangju92:~/workspace/prj (master) $ git add third_file.txt
leesangju92:~/workspace/prj (master) $ git commit -m "important file"
[master 5818f4d] important file
 1 file changed, 1 insertion(+)
 create mode 100644 third_file.txt
leesangju92:~/workspace/prj (master) $ git add .
leesangju92:~/workspace/prj (master) $ git status
On branch master
nothing to commit, working tree clean
leesangju92:~/workspace/prj (master) $ git log
commit 5818f4de5786bb25f1336f83d12e1fc1013a909b (HEAD -> master)
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 07:22:00 2019 +0000

    important file

commit ae4dec24fbc64eb1287e0b9d5ec2722ffa94dfda
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 07:21:43 2019 +0000

    끝말잇기 끝

commit fcdfed55472cdd8886c021f82ee98c23b0573b4c
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 07:19:38 2019 +0000

    끝말잇기 4 & second_file 추가

commit 199b04592774fe41161551a68ecfad22c61e144b
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 07:14:09 2019 +0000

    끝말잇기 3번째

commit 4f431af6071267dc4d5edf443b5e954b2709b610
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 06:49:29 2019 +0000

    끝말잇기 2개

commit 5970fba3c9a37cdfe4b7497c804625041a1dc055
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 06:43:46 2019 +0000

    first_commit
leesangju92:~/workspace/prj (master) $ git stats
git: 'stats' is not a git command. See 'git --help'.

The most similar command is
​        status
leesangju92:~/workspace/prj (master) $ git add .
leesangju92:~/workspace/prj (master) $ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   first_file.txt
        modified:   second_file.txt
        modified:   third_file.txt

leesangju92:~/workspace/prj (master) $ git commit -m "consider today's menu"
[master f1f68d0] consider today's menu
 3 files changed, 4 insertions(+), 2 deletions(-)
leesangju92:~/workspace/prj (master) $ git log
commit f1f68d0d3e8ee28696329f38ebb47bd9d03bd8f8 (HEAD -> master)
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 07:25:12 2019 +0000

    consider today's menu

commit 5818f4de5786bb25f1336f83d12e1fc1013a909b
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 07:22:00 2019 +0000

    important file

commit ae4dec24fbc64eb1287e0b9d5ec2722ffa94dfda
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 07:21:43 2019 +0000

    끝말잇기 끝

commit fcdfed55472cdd8886c021f82ee98c23b0573b4c
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 07:19:38 2019 +0000

    끝말잇기 4 & second_file 추가

commit 199b04592774fe41161551a68ecfad22c61e144b
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 07:14:09 2019 +0000

    끝말잇기 3번째

commit 4f431af6071267dc4d5edf443b5e954b2709b610
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 06:49:29 2019 +0000

    끝말잇기 2개

commit 5970fba3c9a37cdfe4b7497c804625041a1dc055
Author: leesangju <leesangju92@gmail.com>
Date:   Tue Jan 8 06:43:46 2019 +0000

    first_commit

leesangju92:~/workspace/prj (master) $ ls
first_file.txt  second_file.txt  third_file.txt
leesangju92:~/workspace/prj (master) $ ls -a
./  ../  .git/  first_file.txt  second_file.txt  third_file.txt
leesangju92:~/workspace/prj (master) $ cd .git
leesangju92:~/workspace/prj/.git (GIT_DIR!) $ ls -a
./  ../  COMMIT_EDITMSG  HEAD  branches/  config  description  hooks/  index  info/  logs/  objects/  refs/
leesangju92:~/workspace/prj/.git (GIT_DIR!) $ ..
leesangju92:~/workspace/prj (master) $ git remote add origin https://github.com/leesangju92/run_git_prj.git
leesangju92:~/workspace/prj (master) $ ls -a
./  ../  .git/  first_file.txt  second_file.txt  third_file.txt
leesangju92:~/workspace/prj (master) $ cd .git
leesangju92:~/workspace/prj/.git (GIT_DIR!) $ ls- a
bash: ls-: command not found
leesangju92:~/workspace/prj/.git (GIT_DIR!) $ ls -a
./  ../  COMMIT_EDITMSG  HEAD  branches/  config  description  hooks/  index  info/  logs/  objects/  refs/
leesangju92:~/workspace/prj/.git (GIT_DIR!) $ ..
leesangju92:~/workspace/prj (master) $ cd /.git/cong
bash: cd: /.git/cong: No such file or directory
leesangju92:~/workspace/prj (master) $ cd /.git/config
bash: cd: /.git/config: No such file or directory
leesangju92:~/workspace/prj (master) $ cd .git/config
bash: cd: .git/config: Not a directory
leesangju92:~/workspace/prj (master) $ ls -a
./  ../  .git/  first_file.txt  second_file.txt  third_file.txt
leesangju92:~/workspace/prj (master) $ cd . git
leesangju92:~/workspace/prj (master) $ cd .git
leesangju92:~/workspace/prj/.git (GIT_DIR!) $ ls -a
./  ../  COMMIT_EDITMSG  HEAD  branches/  config  description  hooks/  index  info/  logs/  objects/  refs/
leesangju92:~/workspace/prj/.git (GIT_DIR!) $ cd config
bash: cd: config: Not a directory
leesangju92:~/workspace/prj/.git (GIT_DIR!) $ cat config 
[core]
​        repositoryformatversion = 0
​        filemode = true
​        bare = false
​        logallrefupdates = true
[remote "origin"]
​        url = https://github.com/leesangju92/run_git_prj.git
​        fetch = +refs/heads/*:refs/remotes/origin/*
leesangju92:~/workspace/prj/.git (GIT_DIR!) $ ..
leesangju92:~/workspace/prj (master) $ git push -u origin master
Username for 'https://github.com': leesangju92
Password for 'https://leesangju92@github.com': 
Counting objects: 24, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (12/12), done.
Writing objects: 100% (24/24), 1.95 KiB | 666.00 KiB/s, done.
Total 24 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/leesangju92/run_git_prj.git

 * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.
    leesangju92:~/workspace/prj (master) $ 

`                                                                                
student@M70319 MINGW64 ~                                                        
$ git clone https://github.com/leesangju92/run_git_prj.git ssafy_git            `