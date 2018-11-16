# encoding:utf-8
import Function as A   #将相关不变的函数进行打包引用
import os
import shutil
import time

time_start=time.time() # 程序运行开始计时
fileName = "D:\\2_test"

A.Root_Choose(fileName)
ProcessFile = os.path.join(fileName,'Two')
A.PreocessTwoFloder(ProcessFile)   # 输入你要操作的文件夹 （相当于第一层文件夹）
                                       # Two文件夹下面有n个需要判断的文件夹，n个文件夹下面有两个文件夹需要处理

DeleteFile = A.fileInFolder(fileName)

# 删除空的文件夹
for path in DeleteFile:
    Test_File = A.fileInFolder(path)
    lenght = Test_File.__len__()  # 检测文件夹中文件的数量
    #print (lenght)
    if lenght == 0:
        os.rmdir(path)

time_end=time.time()  # 程序结束
print('time cost = ',time_end-time_start,'s')


