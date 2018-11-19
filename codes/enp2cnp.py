#!/usr/bin/env python3

import os
import sys
import subprocess

PUNC_TOBE_REP="!?,.:;“”()"
PUNC_AFBE_REP="！？，。：；\"\"（）"

#print(len(PUNC_TOBE_REP), len(PUNC_AFBE_REP))

def rep(s, RM_NL_FLAG=True):
    if (len(PUNC_TOBE_REP) != len(PUNC_AFBE_REP)):
        raise ValueError(" | What the fuck did you modified...")
    for i in range(len(PUNC_TOBE_REP)):
        s = s.replace(PUNC_TOBE_REP[i], PUNC_AFBE_REP[i])
    if RM_NL_FLAG is True:
        s = s.replace("\n", "")
    print (" | Replace completed...")
    return s

read_clipboard = lambda: subprocess.check_output('pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')
write_clipboard = lambda x: subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, \
                                stdin=subprocess.PIPE).communicate(x.encode('utf-8'))

if __name__ == "__main__":
    string = read_clipboard()
    string = rep(string)
    write_clipboard(string)
