#!/bin/bash

BASE="git@github.com:agoravoting"
cd repos

for i in $(ls)
do
    cd $i
    git checkout -b next
    git push origin next
    git checkout master
    cd ..
done

cd ..
