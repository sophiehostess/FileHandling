#!/usr/bin/python
# -*- coding: utf-8 -*-
# Read file, read all lines into a String


f = open("C:/Users/aiwuj_000/OneDrive/Python/FileHandling/FileHandling1.py")
s = f.read() # read all lines into a String variable
print(type(s))
for line in s:
    print(line,end=' ')
f.close()