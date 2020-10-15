#!/bin/bash

python $(dirname $0)/config.py | while read DATAPATH BASEURL; do
    while [ -n "$1" ]; do
        NAME=.
        while stat -c "" "$DATAPATH/$NAME" > /dev/null 2>&1; do
            NAME=$(head -c 128 /dev/urandom | sha256sum | cut -d " " -f 1)
        done
        chmod o-rwx $1
        chmod g+w $1
        cp $1 $DATAPATH/$NAME
        shred -u $1
        echo -e "$BASEURL/$NAME\t$1"
        shift
    done
    break
done
