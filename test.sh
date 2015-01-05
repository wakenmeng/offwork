#!/bin/zsh
gp=`which gunicorn`
echo 'meng'
echo $gp
if which gunicorn > /dev/null; then echo 'weikang'; fi

myfile=/Users/meng/code/atest/test.py

exec cat ${myfile}
