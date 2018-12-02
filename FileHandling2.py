#!/usr/bin/python
# -*- coding: utf-8 -*-
# Read file, read all lines into a List


f = open("C:/Users/aiwuj_000/OneDrive/Python/FileHandling/FileHandling1.py")
line_list = f.readlines()  # read rows in one-go and pass in a list variable
print(type(line_list))
for line in line_list:
    print(line)
f.close()