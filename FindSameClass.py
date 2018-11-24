# encoding: utf-8
# 脚本的功能：
# 已经有基准的图片库了，可以实现从其他库中提取出相同的图片进入对应的基准图片库
import Function as A                            # 调用Function.py里面定义的函数
import os
import Face_Match as B                          # 调用Face_Match.py里面定义的函数
import random
import time
import shutil

# 定义一些制定路径
base_folder = "E:\\000007work\\base_set"
test_folder = "E:\\000007work\\test_set"
result_folder = "E:\\000007work\\result"


def root_folder():
    # 获取测试目录下文件夹的总和
    SecondPath = A.fileInFolder(base_folder)       # 获取根目录下的文件夹总和 例如：D:\\3_test\\445
    # 统计测试目录下文件夹的数量
    SecondPathFileNum = SecondPath.__len__()
    print ('SecondPathFileNum = ', SecondPathFileNum)
    print ('SecondPath = ', SecondPath)
    for i in range(0, SecondPathFileNum):
        # path 是第二层 文件夹的总和
        # SecondPath[i] 在第二层总和文件夹中表示单个取出来操作
        path = SecondPath[i]                     # 第二层目录单个文件夹路径    例如：path = D:\\3_test\\445
        print ('SecondPath[ ', i, '] = ', SecondPath[i])
        B.DeleteNoneFolder(path)                 # 没有图片的文件夹都被删除了

        second_folder(path)           # 里面的文件夹都有图片
    return


def second_folder(FilePath):
    # ThreePath 表示第三层 文件夹的总和
    ThreePath = A.fileInFolder(FilePath)        # 获取第三层目录下的文件夹总和 例如：D:\\3_test\\445\\49
    # 统计第三层文件夹中有多少个子文件夹
    ThreePathFileNum = ThreePath.__len__()
    print ('ThreePathFileNum = ', ThreePathFileNum)
    # print ('ThreePath = ', ThreePath)
    for i in range(0, ThreePathFileNum):  # 循环遍历基准库
        # print ('ThreePathFileNum = ', ThreePathFileNum)
        # 将文件夹一个一个遍历
        path = ThreePath[i]
        print ('ThreePath[ ', i, '] = ', path)
        # 获得第i个基准库的所有图片
        Photo = A.fileInFolder(path)
        # 获取到文件夹下的图片总和 例如：path =  D:\\3_test\\445\\49\\1534601783,1235657667_align.jpg
        # 统计基准库中图片的数量
        PhotoNum = Photo.__len__()

        # Photo[] 就是选中基准库中的某种图片，道理要随机选取10张，基准库中都是同一个人
        # 在test_set测试库中，某个库中按顺序选中第i张图片，与基准库的这10张进行比较，
        # 若有大于60%，则将测试库中的文件存入基准库中，若有不同，则先保留在测试库中
        # 所谓按顺序，主要是为了，达到终止条件，好跳到下一个测试库中
        # 对每张图片进行遍历

        # 读取测试库中所有文件夹
        test_set = A.fileInFolder(test_folder)
        # 统计测试库中文件夹数量
        test_set_num = test_set.__len__()
        print 'test_set_num =', test_set_num
        # 循环遍历每一个测试库文件夹
        for j in range(0, test_set_num):
            # 提取第j个测试库文件夹
            test_set_j = test_set[j]
            # 读取测试库文件夹中所有图片
            test_set_j_photo = A.fileInFolder(test_set_j)
            # 统计第j个测试库文件夹中图片的数量
            test_set_j_photo_len = test_set_j_photo.__len__()
            # 按顺序循环遍历第j个文件夹中的图片
            for k in range(0, test_set_j_photo_len):
                # test_set_j_photo[k] 表示第j个测试库中第k张图片
                # Photo[x] 表示第i个基准库中第x张图片
                # 初始化 比较情况的 数量
                Same = 0
                Different = 0
                for q in range(0, 6):
                    # PhotoNum 为基准库中图片数量
                    # 随机选取10张其中的图片用作基准图片
                    # 随机选取基准图片的位置为b
                    b = random.randint(0, PhotoNum - 1)
                    # 基准库中的图片与选择的测试库中的图片进行比较
                    goal = A.Face_To_Match(test_set_j_photo[k], Photo[b])
                    time.sleep(0.4)  # 延时0.4s QPS不免费调用接口容易出错
                    # 应该做个异常处理 (必须做)
                    try:
                        # 测试异常
                        result = goal.get('result')
                        # score 是比较得分
                        score = result.get('score')
                    except AttributeError:
                        # 异常处理
                        # result = {}
                        # score = 0
                        print "进行异常处理"
                        print 'Same =', Same
                        print 'Different = ', Different
                        # NewPhotoNum = NewPhotoNum - 1
                        # Different = Different + 1
                    else:
                        # 确定基准库的方法以及阈值
                        # 没有异常
                        # score >= 55 表示图片为同一个人 55 为临界值
                        print 'score =', score
                        if score >= 55:
                            Same = Same + 1
                            # print ('Same = ', Same)
                        elif score < 55:
                            Different = Different + 1
                # 当相同的数目大于不同的数目
                # 则将第j个测试文件夹中第k中图片剪切到第i个基准库中
                print 'Same = ', Same
                print 'Different =', Different
                if Same > Different:
                    shutil.move(test_set_j_photo[k], path)
                # 否则 保留 图片 遍历当前测试库的下一张图片
        # 将分好类的基准库文件存入 结果文件夹
        shutil.move(path, result_folder)
    return

# 程序从这里开始执行


def start():
    if __name__ == "__main__":
        # 程序开始
        start = time.time()
        print ('programming is beginning……')

        # B.MoveChildFolder(BackupFileName, TestFileName, 'copytree')  # 将备份的文件copy到测试文件夹
        B.DeleteNoneFolder(base_folder)                              # 剔除空当前文件夹中空的文件夹
        root_folder()                                                  # 对测试文件夹进行操作
        B.DeleteNoneFolder(base_folder)
        print ('programming is ending……')
        end = time.time()
        print ('spend time = ', end - start, 's')
# 怕出现网络异常，而做的处理

exceptFlag = True
while exceptFlag:
    try:
        print "测试异常"
        start()
        RootPath = A.fileInFolder(base_folder)
        # 如果目标文件夹中没有文件了，直接退出
        RootPathFileNum = RootPath.__len__()
        if RootPathFileNum == 0:
            exceptFlag = False
    except:
        print "处理异常"
        time.sleep(0.1)
        exceptFlag = True
    else:
        print "没有异常"
        # start()
