mkdir study
cd study
git init githw1

cd githw1
git add README.md
git commit -m 'repo: add a README file'

git branch first_branch
git status
git add README.md
git commit -m 'feat(README): add commands to resolve subtask 1'

git switch master
git add README.md
git commit -m 'feat(README): add commands to resolve subtask 2'
git log --oneline --graph --decorate=short --all
