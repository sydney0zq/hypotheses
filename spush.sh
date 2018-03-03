#! /bin/sh
#
# spush.sh
# Copyright (C) 2018 zhou <zhou@localhost>
#
# Distributed under terms of the MIT license.
#
python3 build.py
git add .
git commit -m"Publish"
git push origin master


