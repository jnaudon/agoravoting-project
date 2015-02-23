#!/bin/bash

BASE="git@github.com:agoravoting"
mkdir -p repos

for i in $(cat repos.txt)
do
    git clone $BASE/$i repos/$i
    cd repos/$i
    git checkout -b next origin/next
    git checkout master
    cd ../..
done
