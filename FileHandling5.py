#!/usr/bin/python
# -*- coding: utf-8 -*-
# write file, write lines in one go


f = open('C:/Users/aiwuj_000/OneDrive/Python/FileHandling/poet.txt','a+')
print(f.read())
fruits = ['appple\n','banana\n','orange\n','watermelon\n']
f.writelines(fruits)
print('写入成功')
f.close()


# https://www.pythontab.com/html/2018/pythonjichu_0131/1237.html

# mode	文件存在	    文件不存在	读	写	流位置
# r	    读取文件内容	错误	    √	×	begin
# w     清空文件内容	创建	    ×	√	begin
# a	    保留原始内容	创建	    ×	√	begin/end
# r+	读写文件内容	错误	    √	√	begin
# w+	清空文件内容	创建	    √	√	begin
# a+	保留原始内容	创建	    √	√	begin/end
