# encoding:utf-8
import Function as A
import os

# 获取当前路径下所以子文件【可以是文件夹，也可以是文件】
# A.fileInFolder()
PathName = "D:\\3_test"                         # 操作的根目录 D:\\3_test

def RootFilder(FilePath):
    SecondPath = A.fileInFolder(FilePath)       # 获取根目录下的文件夹总和 例如：D:\\3_test\\445
    SecondPathFileNum = SecondPath.__len__()
    # print (SecondPathFileNum)
    # print (SecondPath)
    for i in range(0, SecondPathFileNum - 1):
        path = SecondPath[i]                     # 第二层目录单个文件夹路径    例如：path = D:\\3_test\\445
        SecondFilder(path)
    return

def SecondFilder(FilePath):
    ThreePath = A.fileInFolder(FilePath)        # 获取第三层目录下的文件夹总和 例如：D:\\3_test\\445\\49
    ThreePathFileNum = ThreePath.__len__()
    # print (ThreePathFileNum)
    # print (ThreePath)
    for i in range(0, ThreePathFileNum - 1):
        path = ThreePath[i]
        # print ('ThreePath = ')                 # 第三层目录下的单个文件夹名称 例如：path = D:\\3_test\\445\\49
        # print (path)
        Photo = A.fileInFolder(path)             # 获取到文件夹下的图片总和 例如：path =  D:\\3_test\\445\\49\\1534601783,1235657667_align.jpg
        PhotoNum = Photo.__len__()
        print (PhotoNum)
        for i in range(0, PhotoNum - 1):
            SignalPhoto = Photo[i]              # 获得单张图片
            print ('SignalPhoto')
            print (SignalPhoto)


    return


# 程序开始
DeleteFile = A.fileInFolder(PathName)

# 删除空的文件夹
for path in DeleteFile:
    Test_File = A.fileInFolder(path)
    lenght = Test_File.__len__()  # 检测文件夹中文件的数量
    print (lenght)
    if lenght == 0:
        os.rmdir(path)

RootFilder(PathName)
