#!/usr/bin/python
# -*- coding: utf-8 -*-



import os
from os.path import join, getsize


def getdirsize(dir)->int:
    size = 0

    # root  : current folder
    # dirs  : sub-folders
    # files : files
    for root, dirs, files in os.walk(dir):
        print(root, dirs, files)
        size += sum([getsize(join(root, name)) for name in files])
    return size


if __name__ == '__main__':
    size = getdirsize(r'C:\DTLFolder')
    print('There are %.3f' % (size / 1024 / 1024), 'Mbytes in C:\\DTLFolder')