#!/bin/bash

./update.sh

cd repos

for i in $(ls)
do
    cd $i
    echo "RELEASING $i"
    git log --oneline master..next | tee $(date +%Y.%m.%d).changelog.txt
    git checkout master
    git merge next
    git push
    git tag $1
    git push --tags
    echo ""
    cd ..
done

cd ..
