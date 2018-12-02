#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os
#获取当前路径
#rootdir = os.getcwd()          
rootdir = "D:/DRIVERS"          
 

x  = u'统计文件大小.csv'
f = open(os.path.join(rootdir,x), "w+")
#获取二级目录所有文件夹与文件
for dirname in os.listdir(rootdir):  
    #路径补齐
    Dir = os.path.join(rootdir, dirname)    
    count = 0
    #判断是否为目录
    if (os.path.isdir(Dir)):
        #遍历目录下所有文件根，目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)[文件夹路径, 文件夹名字, 文件名称]
        for r, ds, files in os.walk(Dir): 
            #遍历所有文件
            for file in files:      
                #获取文件大小
                size = os.path.getsize(os.path.join(r, file)) 
                count += size
        if ((count/1024.0/1024.0) < 1024):
            print(Dir +'\t' + '%.2f'% (count/1024.0/1024.0)+'MB')
            f.write(Dir +','+  '%.2f'% (count/1024.0/1024.0)+'MB' + '\n')
        else:
            print(Dir + '\t' + '%.2f' % (count / 1024.0 / 1024.0/1024.0) + 'GB')
            f.write(Dir + ',' + '%.2f' % (count / 1024.0 / 1024.0/1024.0) + 'GB' + '\n')
    else:
        continue
f.close()