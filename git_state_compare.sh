#!/bin/sh

LOCAL=$(git rev-parse master)
REMOTE=$(git rev-parse origin/master)
BASE=$(git merge-base master origin/master)

if [ $LOCAL = $REMOTE ]; then
    echo "Up-to-date"
elif [ $LOCAL = $BASE ]; then
    echo "Need to pull"
elif [ $REMOTE = $BASE ]; then
    echo "Need to push"
else
    echo "Diverged"
fi
