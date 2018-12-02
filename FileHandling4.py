#!/usr/bin/python
# -*- coding: utf-8 -*-
# write file, write lines one by one

f = open('C:/Users/aiwuj_000/OneDrive/Python/FileHandling/poet.txt','w',encoding='utf-8')  #open file with over-write mode
f.write('你好，python \n')  #write something, with new line flag
f.write("写入完毕，运行！")
f.close()