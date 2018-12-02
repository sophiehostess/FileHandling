#!/usr/bin/python
# -*- coding: utf-8 -*-

fo = open('C:/report.rpt', "r")
str = fo.read(7)
print("string is: ", str)
 
position = fo.tell()
print("current postion is : ", position)

# offset, from
# 如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。
position = fo.seek(1, 0)
str = fo.read(10)
print("read : ", str)

position = fo.tell()
print("current postion is : ", position)

fo.close()